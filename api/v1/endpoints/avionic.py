from .endpoints import *
app = APIRouter()

@app.get("/{id_}")
async def plane(id_: int, request: Request, db: Session = Depends(get_db)):
    avionics = db.query(Avionic
                       ).options(joinedload(Avionic.planes)
                                 ).filter(Avionic.id == id_).all()
    
    if len(avionics) == 0:
        raise HTTPException(status_code=404, detail="avionics not found")
    return avionics

@app.get("/")
async def avionics(request: Request, db: Session = Depends(get_db)):
    avionics = db.query(Avionic).options(joinedload(Avionic.planes)).all()
    return avionics
