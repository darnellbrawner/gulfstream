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

#UPDATE 
@app.patch('/{id_}')
def update_engine(id_: int,  payload: EngineBaseSchema,  db: Session = Depends(get_db)):
    engine_query = db.query(Engine).filter(Engine.id == id_)
    db_engine = engine_query.first()
    if not db_engine:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f'No engine with this id: {id_} found')
    
    update_data = payload.model_dump(exclude_unset=True)
    engine_query.filter(Engine.id == id_).update(update_data,synchronize_session=False)
    db.commit()
    db.refresh(db_engine)
    return {"status": "success", "engine": db_engine}

#CREATE
@app.post("/", status_code=status.HTTP_201_CREATED)
def create_engine(payload: EngineBaseSchema, db: Session = Depends(get_db)):
    new_engine = Engine(**payload.model_dump())
    db.add(new_engine)
    db.commit()
    db.refresh(new_engine)
    return {"status": "success", "engine": new_engine}

#DELETE
@app.delete("/{id_}")
def delete_engine(id_: int, db: Session = Depends(get_db)):
    engine_query = db.query(Engine).filter(Engine.id == id_)
    engine = engine_query.first()
    if not engine:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f'No engine with this id: {id_} found')
    engine_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)