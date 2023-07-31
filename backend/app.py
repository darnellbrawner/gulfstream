
# Database initial data
INITIAL_DATA = {
    
    'manufacturers': [
        {
            'id': 1,
            'name': 'Gulf Stream'
        },
        {
            'id': 2,
            'name': 'Windows Plus'
        },
        {
            'id': 3,
            'name': 'Rolls-Royce'
        },
        {
            'id': 4,
            'name': 'Pratt & Whitney'
        },
        {
            'id': 5,
            'name': 'Honeywell'
        }
    ],
    'windows': [
            {
                  'id': 1,
                  'size': '',
                  'shape': 'Oval',
                  'panoramic': True,
                  'manufacturer_id': 1
            },
            {
                  'id': 2,
                  'size': 'large',
                  'shape': 'oval',
                  'panoramic': True,
                  'manufacturer_id': 1
            } 
     ],
    'avionics': [
            {
                  'id': 1,
                  'name': 'Gulfstream Symmetry Flight Desk',
                  'manufacturer_id':  1
            },
             {
                  'id': 2,
                  'name': 'Gulfstream PlaneView II',
                  'manufacturer_id': 1
            },
             {
                  'id': 3,
                  'name': 'Gulfstream PlaneView280',
                  'manufacturer_id': 1
            },
     ],
    'engines': [
            {
                  'id': 1,
                  'manufacturer_id': 3,
                  'make': 'Rolls-Royce',
                  'model': 'Pearl 700',
            },
            {
                  'id': 2,
                  'manufacturer_id': 3,
                  'make': 'Rolls-Royce',
                  'model': 'BR725',
            }, 
            {
                  'id': 3,
                  'manufacturer_id': 4,
                  'make': 'Pratt & Whitney',
                  'model': 'PW815GA'
            },
            {
                  'id': 4,
                  'manufacturer_id': 4,
                  'make': 'Pratt & Whitney',
                  'model': 'PW814GA'
            },
            {
                  'id': 5,
                  'manufacturer_id': 4,
                  'make': 'Pratt & Whitney',
                  'model': 'PW812GA'
            },
            {
                  'id': 6,
                  'manufacturer_id': 5,
                  'make': 'Honeywell',
                  'model': 'HTF7250G'
            }
     ],
    'planes': [
            {
                  'name': 'G800',
                  'max_range': 8000,
                  'max_range_unit': 'nm',
                  'high_speed_cruise': 0.90,
                  'long_range_cruise': 0.85,
                  'cruising_unit': 'mach',
                  'living_areas_max': 4.0,
                  'window_count': 16,
                  'window_id': 1,
                  'total_interior_length': 1633,
                  'interior_length_unit': 'cm',
                  'avionic_id': 1,
                  'engine_id': 1,
                  'engine_count': 2,
                  'delivered': False
            },
            {
                  'name': 'G700',
                  'max_range': 7500,
                  'max_range_unit': 'nm',
                  'high_speed_cruise': 0.90,
                  'long_range_cruise': 0.85,
                  'cruising_unit': 'mach',
                  'living_areas_max': 5.0,
                  'window_count': 20,
                  'window_id': 1,
                  'total_interior_length': 1940,
                  'interior_length_unit':'cm',
                  'avionic_id': 1,
                  'engine_id': 1,
                  'engine_count': 2,
                  'delivered': False
            },
            {
                  'name': 'G65ER',
                  'max_range': 7500,
                  'max_range_unit': 'nm',
                  'high_speed_cruise': 0.90,
                  'long_range_cruise': 0.85,
                  'cruising_unit': 'mach',
                  'living_areas_max': 4.0,
                  'window_count': 16,
                  'window_id': 1,
                  'total_interior_length': 1633,
                  'interior_length_unit':'cm',
                  'avionic_id': 2,
                  'engine_id': 2,
                  'engine_count': 2,
                  'delivered': False
            },
            {
                  'name': 'G650',
                  'max_range': 7000,
                  'max_range_unit': 'nm',
                  'high_speed_cruise': 0.90,
                  'long_range_cruise': 0.85,
                  'cruising_unit': 'mach',
                  'living_areas_max': 4.0,
                  'window_count': 16,
                  'window_id': 1,
                  'total_interior_length': 1633,
                  'interior_length_unit':'cm',
                  'avionic_id': 2,
                  'engine_id': 2,
                  'engine_count': 2,
                  'delivered': True
            },
            {
                  'name': 'G600',
                  'max_range': 6600,
                  'max_range_unit': 'nm',
                  'high_speed_cruise': 0.90,
                  'long_range_cruise': 0.85,
                  'cruising_unit': 'mach',
                  'living_areas_max': 4.0,
                  'window_count': 14,
                  'window_id': 1,
                  'total_interior_length': 1562,
                  'interior_length_unit':'cm',
                  'avionic_id': 1,
                  'engine_id': 3,
                  'engine_count': 2,
                  'delivered': True
            },
            {
                  'name': 'G500',
                  'max_range': 5300,
                  'max_range_unit': 'nm',
                  'high_speed_cruise': 0.90,
                  'long_range_cruise': 0.85,
                  'cruising_unit': 'mach',
                  'living_areas_max': 3.0,
                  'window_count': 14,
                  'window_id': 1,
                  'total_interior_length': 1450,
                  'interior_length_unit':'cm',
                  'avionic_id': 1,
                  'engine_id': 4,
                  'engine_count': 2,
                  'delivered': True
            },
            {
                  'name': 'G400',
                  'max_range': 4200,
                  'max_range_unit': 'nm',
                  'high_speed_cruise': 0.88,
                  'long_range_cruise': 0.85,
                  'cruising_unit': 'mach',
                  'living_areas_max': 2.5,
                  'window_count': 10,
                  'window_id': 1,
                  'total_interior_length': 1293,
                  'interior_length_unit':'cm',
                  'avionic_id': 1,
                  'engine_id': 5,
                  'engine_count': 2,
                  'delivered': True
            },
            {
                  'name': 'G280',
                  'max_range': 3600,
                  'max_range_unit': 'nm',
                  'high_speed_cruise': 0.84,
                  'long_range_cruise': 0.80,
                  'cruising_unit': 'mach',
                  'living_areas_max': 2.0,
                  'window_count': 19,
                  'window_id': 2,
                  'total_interior_length': 983,
                  'interior_length_unit':'cm',
                  'avionic_id': 3,
                  'engine_id': 6,
                  'engine_count': 2,
                  'delivered': True
            }
      ]
}

from fastapi.middleware.cors import CORSMiddleware
import random
from fastapi import FastAPI, Depends, Request, Form, status, HTTPException

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from sqlalchemy.orm import Session
from sqlalchemy import event

from sqlalchemy import select
from sqlalchemy.orm import joinedload


import logging
logger = logging.getLogger(__name__)

import uvicorn

import models
#import seeding
from database import SessionLocal, engine


from models import Plane, Avionic, Engine, Manufacturer, Window

templates = Jinja2Templates(directory="templates")
app = FastAPI()

origins = [
     "http://localhost:5173"
 ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# This method receives a table, a connection and inserts data to that table.
def initialize_table(target, connection, **kw):
    tablename = str(target)
    if tablename in INITIAL_DATA and len(INITIAL_DATA[tablename]) > 0:
        connection.execute(target.insert(), INITIAL_DATA[tablename])

# I set up this event before table creation
event.listen(Manufacturer.__table__, 'after_create', initialize_table)
event.listen(Window.__table__, 'after_create', initialize_table)
event.listen(Avionic.__table__, 'after_create', initialize_table)
event.listen(Engine.__table__, 'after_create', initialize_table)
event.listen(Plane.__table__, 'after_create', initialize_table)

# This will create the DB schema and trigger the "after_create" event
@app.on_event("startup")
def configure():
     models.Base.metadata.create_all(bind=engine)

if __name__ == "__app__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/rand")
async def hello():
   return random.randint(0, 100)

@app.get("/planes")
async def planes(request: Request, db: Session = Depends(get_db)):
    planes = db.query(models.Plane
                      ).options(joinedload(models.Plane.window)
                        ).options(joinedload(models.Plane.avionic)
                        ).options(joinedload(models.Plane.engine)).all()
    return planes


@app.get("/engines")
async def engines(request: Request, db: Session = Depends(get_db)):
    engines = db.query(models.Engine).options(joinedload(models.Engine.planes)).all()
    return engines

@app.get("/avionics")
async def avionics(request: Request, db: Session = Depends(get_db)):
    avionics = db.query(models.Avionic).options(joinedload(models.Avionic.planes)).all()
    return avionics

@app.get("/manufacturers")
async def manufacturers(request: Request, db: Session = Depends(get_db)):
    manufacturer = db.query(models.Manufacturer).all()
    return manufacturer

@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    planes = db.query(models.Plane).all()
    return templates.TemplateResponse("base.html",
                                      {"request": request, "plane_list": planes})

@app.post("/add")
def add(request: Request, title: str = Form(...), db: Session = Depends(get_db)):
    new_plane = models.Plane(title=title)
    db.add(new_plane)
    db.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

@app.get("/update/{plane_id}")
def update(request: Request, plane_id: int, db: Session = Depends(get_db)):
    plane = db.query(models.Plane).filter(models.Plane.id == plane_id).first()
    plane.complete = not plane.complete
    db.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)


@app.get("/delete/{plane_id}")
def delete(request: Request, plane_id: int, db: Session = Depends(get_db)):
    plane = db.query(models.Plane).filter(models.Plane.id == plane_id).first()
    db.delete(plane)
    db.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)



#planes = [int, Plane] = {}
# @app.get("/todos/")
# async def create_plane(request: Request, db: Session = Depends(get_db)):
#       todos = db.query(models.Todo).all()
#       return templates.TemplateResponse("todos.html", {"request": request, "todo_list": todos})

#     id_ = max(planes.keys(), default=0) + 1
#     planes[id_] = plane
#     return {"id": id_, "plane": plane}

# @app.get("/todo/{id_}", response_model=Plane)
# async def read_plane(id_: int):
#     if id_ not in planes:
#         raise HTTPException(status_code=404, detail="plane not found")
#     return planes[id_]

# @app.put("/plane/{id_}", response_model=Plane)
# async def update_plane(id_: int, plane: Plane):
#     if id_ not in planes:
#         raise HTTPException(status_code=404, detail="plane not found")
#     planes[id_] = plane
#     return plane

# @app.delete("/plane/{id_}")
# async def delete_plane(id_: int):
#     if id_ not in planes:
#         raise HTTPException(status_code=404, detail="plane not found")
#     del planes[id_]
#     return {"detail": "plane has been deleted"}

# @app.get("/planes/")
# async def read_all_planes():
#     return planes
