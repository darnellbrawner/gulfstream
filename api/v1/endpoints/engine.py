from .endpoints import *
app = APIRouter()

@app.get("/{id_}")
async def plane(id_: int, db: Session = Depends(get_db)):
    engines = db.query(Engine).options(joinedload(Engine.planes)
                                 ).filter(Engine.id == id_).all()
    
    if len(engines) == 0:
        raise HTTPException(status_code=404, detail="engine not found")
    return engines

@app.get("/")
async def engines( db: Session = Depends(get_db)):
    engines = db.query(Engine).options(joinedload(Engine.planes)).all()
    return engines
