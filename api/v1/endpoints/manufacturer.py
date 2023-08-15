from .endpoints import *

app = APIRouter()

@app.get("/{id_}")
async def manufacturers(id_: int, db: Session = Depends(get_db)):
    manufacturers = db.query(Manufacturer).filter(Manufacturer.id == id_).all()
    return manufacturers

@app.get("/")
async def manufacturers( db: Session = Depends(get_db)):
    manufacturers = db.query(Manufacturer).all()
    return manufacturers

#UPDATE 
@app.patch('/{id_}')
def update_manufacturer(id_: int,  payload: ManufacturerBaseSchema,  db: Session = Depends(get_db)):
    manufacturer_query = db.query(Manufacturer).filter(Manufacturer.id == id_)
    db_manufacturer = manufacturer_query.first()
    if not db_manufacturer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f'No manufacturer with this id: {id_} found')
    
    update_data = payload.model_dump(exclude_unset=True)
    manufacturer_query.filter(Manufacturer.id == id_).update(update_data,synchronize_session=False)
    db.commit()
    db.refresh(db_manufacturer)
    return {"status": "success", "manufacturer": db_manufacturer}

#CREATE
@app.post("/", status_code=status.HTTP_201_CREATED)
def create_manufacturer(payload: ManufacturerBaseSchema, db: Session = Depends(get_db)):
    new_manufacturer = Manufacturer(**payload.model_dump())
    db.add(new_manufacturer)
    db.commit()
    db.refresh(new_manufacturer)
    return {"status": "success", "manufacturer": new_manufacturer}

#DELETE
@app.delete("/{id_}")
def delete_manufacturer(id_: int, db: Session = Depends(get_db)):
    manufacturer_query = db.query(Manufacturer).filter(Manufacturer.id == id_)
    manufacturer = manufacturer_query.first()
    if not manufacturer:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f'No manufacturer with this id: {id_} found')
    manufacturer_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
   