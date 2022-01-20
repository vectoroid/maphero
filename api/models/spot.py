"""
"""
import enum
import ..models.base as base_models
import ..api.types


valid_geojson = api.types.ValidGeojsonTypes

class GeoProperties(base_models.MetaDetaBaseModel):
    """
    Represents the `properties` attribute from the GeoJSON specification
    -  i.e. `properties` attributes of models are where features/data not 
    pertaining to the GeoJSON spec
    -  e.g. Perhaps you save a spot and want to recall (later) its:
        -  name
        -  description/reason why this Spot is important to you, etc.
        
    @todo:  create a class, called "Notes," with which you can save 
            (multiple) notes about a particular Spot(s).
            -  this will necessitate creating a new database in Deta Base? No?
    """
    name: str
    description: str
    notes: str
    created_at: datetime.datetime

class Point(base_models.MetaDetaBaseModel, api.types.GeoBase):
    """
    Point() 
    
    A class respresenting the GeoJSON "Point" object. 
    
    -  coordinates: proper order => (longitude, latitude)
    """
    type: str = valid_geojson.Point
    coordinates: geojson_types.Position 
    
    
class Feature(base_models.MetaDetaBaseModel, api.types.GeoBase):
    """
    Feature()
    
    A class respresenting the GeoJSON "Feature" object. 
    
    -  coordinates: proper order => (longitude, latitude)
    """
    type: str = valid_geojson.Feature
    geometry: Point
    properties: GeoProperties
    
    
class FeatureCollection(base_models.MetaDetaBaseModel, api.types.GeoBase):
    type: str = valid_geojson.FeatureCollection
    geometry: Point
    properties: GeoProperties
    

class GeometryCollection(base_models.MetaDetaBaseModel, api.types.GeoBase):
    """
    GeometryCollection()
    
    A class respresenting the GeoJSON "GeometryCollection" object. 
    
    -  coordinates: proper order => (longitude, latitude)
    """
    type: valid_geojson.GeometryCollection
    geometries: list[typing.Union[Point, Feature]]
    properties: GeoProperties