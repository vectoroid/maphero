"""
MetaDeta

This file contains the base model class, which defines the interface to which all derived
models should adhere.
"""
import aiohttp
import api
import fastapi
import math
import pydantic
import typing
import uuid


class MetaDetaBaseModel(pydantic.BaseModel):
    """
    MetaDetaBaseModel < pydantic.BaseModel: 
    Base model class, derived from pydantic.BaseModel
    """
    key: uuid.UUID = pydantic.Field(default_factory=uuid.uuid4)
    version: int = 1
    db_name: typing.ClassVar
    
    def dict(self, *args, **kwargs) -> dict:
        return {**super().dict(*args, **kwargs), "key": str(self.key)}
    
    async def save(self) -> None:
        async with api.db.async_detabase(self.db_name) as db:
            self.version += 1
            await db.insert(fastapi.encoders.jsonable_encoder(self))
            
    async def update(self, **kwargs) -> None:
        async with api.db.async_detabase(self.db_name) as db:
            new_version = self.version + 1
            new_instance = self.__class__({**self.dict(), **kwargs, "version": new_version})
            await db.put(fastapi.encoders.jsonable_encoder(new_instance))
            
            self.__dict__.update(new_instance.__dict__)
            
    async def delete(self) -> None:
        async with api.db.async_detabase(self.db_name) as db:
            await db.delete(str(self.key))
        return True
    
    @classmethod
    async def find(cls, _key: typing.Union[uuid.UUID, str], exception=api.exceptions.NotFoundHTTPException()):
        async with api.db.async_detabase(cls.db_name) as db:
            instance = await db.get(str(_key))
            
            if instance is None and exception:
                raise exception
            elif instance:
                return cls(**instance)
            else:
                return None
            
    @classmethod
    async def fetch(cls, query, limit_upper_bound: int=math.inf) -> list:
        async with api.db.async_detabase(cls.db_name) as db:
            documents_limit = min(limit_upper_bound, api.config.ApiSettings.documents_limit)
            query = fastapi.encoders.jsonable_encoder(query)
            
            results = await db.fetch(query, limit=documents_limit)
            retrieved_docs = results.items
            
            while len(retrieved_docs) <= documents_limit and results.last:
                results = await db.fetch(query, last=results.last)
                retrieved_docs += results.items
                
            return [cls(**instance) for instance in retrieved_docs]

            