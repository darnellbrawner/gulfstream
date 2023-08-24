from .schema import *

class ManufacturerBaseSchema(MyBaseModel):
    id: Optional[int]
    name: str
    # content: str
    # category: str | None = None
    # published: bool = False
    # createdAt: datetime | None = None
    # updatedAt: datetime | None = None



class ListManufacturerResponse(MyBaseModel):
    status: str
    results: int
    manufacturers: List[ManufacturerBaseSchema]

