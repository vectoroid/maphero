"""
Application-specific (bespoke) types
-  e.g. for GeoJSON
"""
import enum
from msilib.schema import Feature
import pydantic
import typing


# NumType:
# because coordinates are typically given as either
# an integer or floating point value, depending on
# the standard in use.
NumType = typing.Union[float, int]

# Most fundamental Geometry type 
# -  comprises the Coordinates class
Position = typing.Union[
    # Position in 2D coordinates
    # -   for geographic coordinates, the order is: (Longitude, Latitude)
    typing.Tuple[NumType, NumType], 
    # Position in 3D coordinates
    # -   for geographic coordinates, the order is: (Longitude, Latitude, Altitude)
    typing.Tuple[NumType, NumType, NumType]
]

class GeoBase(pydantic.BaseModel):
    type: str = pydantic.Field(...)
    coordinates: Position = pydantic.Field(...)
    
class ValidGeojsonTypes(enum.Enum):
    """
    Valid types according to the GeoJSON specification
    """
    Point: str = 'Point'
    LineString: str = 'LineString'
    Polygon: str = 'Polygon'
    MultiPoint: str = 'MultiPoint'
    MultiLineString: str = 'MultiLineString'
    MultiPolygon: str = 'MultiPolygon'
    Feature: str = 'Feature'
    FeatureCollection: str = 'FeatureCollection'
    GeometryCollection: str = 'GeometryCollection'
    