from fastapi import APIRouter
from api.v1.endpoints import (
    manufacturer,
    plane,
    #window,
    engine,
    avionic
    )

api_router = APIRouter()
api_router.include_router(manufacturer.app, prefix="/manufacturers", tags=["Manufacturers"])
api_router.include_router(plane.app, prefix="/planes", tags=["Planes"])
#api_router.include_router(window.app, prefix="/window", tags=["window"])
api_router.include_router(engine.app, prefix="/engines", tags=["Engines"])
api_router.include_router(avionic.app, prefix="/avionics", tags=["Avionics"])


