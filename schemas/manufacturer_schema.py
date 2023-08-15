from .schema import *

class ManufacturerBaseSchema(BaseModel):
    id: Optional[int]
    name: str
    # content: str
    # category: str | None = None
    # published: bool = False
    # createdAt: datetime | None = None
    # updatedAt: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListManufacturerResponse(BaseModel):
    status: str
    results: int
    manufacturers: List[ManufacturerBaseSchema]

