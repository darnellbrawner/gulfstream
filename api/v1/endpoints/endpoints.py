from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, Request, Form, status, HTTPException, Response, APIRouter

from starlette.responses import RedirectResponse
#from starlette.templating import Jinja2Templates

from sqlalchemy.orm import Session
from sqlalchemy import event

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from models.database import get_db


#import models
#import schemas
from models import *
from schemas import *

from models.database import SessionLocal #, engine

