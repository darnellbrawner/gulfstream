from .endpoints import *
app = APIRouter()

@app.get("/{id_}")
async def plane(id_: int, db: Session = Depends(get_db)):
    planes = db.query(Plane).options(joinedload(Plane.window)
                        ).options(joinedload(Plane.avionic)
                        ).options(joinedload(Plane.engine)).filter(Plane.id == id_).all()
    
    if len(planes) == 0:
        raise HTTPException(status_code=404, detail="plane not found")
    return planes

@app.get("/")
async def planes(db: Session = Depends(get_db)):
    planes = db.query(Plane
                      ).options(joinedload(Plane.window)
                        ).options(joinedload(Plane.avionic)
                        ).options(joinedload(Plane.engine)).all()
    if len(planes) == 0:
        raise HTTPException(status_code=404, detail="planes not found")
    return planes