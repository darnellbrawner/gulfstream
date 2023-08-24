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

#UPDATE 
@app.patch('/{id_}')
def update_avionic(id_: int,  payload: AvionicBaseSchema,  db: Session = Depends(get_db)):
    avionic_query = db.query(Avionic).filter(Avionic.id == id_)
    db_avionic = avionic_query.first()
    if not db_avionic:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f'No avionic with this id: {id_} found')
    
    update_data = payload.model_dump(exclude_unset=True)
    avionic_query.filter(Avionic.id == id_).update(update_data,synchronize_session=False)
    db.commit()
    db.refresh(db_avionic)
    return {"status": "success", "avionic": db_avionic}

#CREATE
@app.post("/", status_code=status.HTTP_201_CREATED)
def create_avionic(payload: AvionicBaseSchema, db: Session = Depends(get_db)):
    new_avionic = Avionic(**payload.model_dump())
    db.add(new_avionic)
    db.commit()
    db.refresh(new_avionic)
    return {"status": "success", "avionic": new_avionic}

#DELETE
@app.delete("/{id_}")
def delete_avionic(id_: int, db: Session = Depends(get_db)):
    avionic_query = db.query(Avionic).filter(Avionic.id == id_)
    avionic = avionic_query.first()
    if not avionic:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f'No avionic with this id: {id_} found')
    avionic_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)