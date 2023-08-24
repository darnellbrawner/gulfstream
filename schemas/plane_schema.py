from .schema import *

class PlaneBaseSchema(MyBaseModel):
    id: Optional[int]
    name: str
    max_range_unit:  str
    high_speed_cruise: float
    long_range_cruise: float
    cruising_unit: str
    living_areas_max:  float
    window_count:  int
    window_id:  int
    total_interior_length:  int
    interior_length_unit:  str
    avionic_id:  int
    engine_id:  int
    engine_count:  int
    delivered:  bool = False
    # createdAt: datetime | None = None
    # updatedAt: datetime | None = None


class ListPlaneResponse(MyBaseModel):
    status: str
    results: int
    planes: List[PlaneBaseSchema]

