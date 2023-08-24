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

#UPDATE 
@app.patch('/{id_}')
def update_plane(id_: int,  payload: PlaneBaseSchema,  db: Session = Depends(get_db)):
    plane_query = db.query(Plane).filter(Plane.id == id_)
    db_plane = plane_query.first()
    if not db_plane:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f'No plane with this id: {id_} found')
    
    update_data = payload.model_dump(exclude_unset=True)
    plane_query.filter(Plane.id == id_).update(update_data,synchronize_session=False)
    db.commit()
    db.refresh(db_plane)
    return {"status": "success", "plane": db_plane}

#CREATE
@app.post("/", status_code=status.HTTP_201_CREATED)
def create_plane(payload: PlaneBaseSchema, db: Session = Depends(get_db)):
    new_plane = Plane(**payload.model_dump())
    db.add(new_plane)
    db.commit()
    db.refresh(new_plane)
    return {"status": "success", "plane": new_plane}

#DELETE
@app.delete("/{id_}")
def delete_plane(id_: int, db: Session = Depends(get_db)):
    plane_query = db.query(Plane).filter(Plane.id == id_)
    plane = plane_query.first()
    if not plane:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f'No plane with this id: {id_} found')
    plane_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
   