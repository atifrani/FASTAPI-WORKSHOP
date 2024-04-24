from fastapi import FastAPI, APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import Base, get_db
from sqlalchemy import Column, Integer, String, ForeignKey
import schemas, models


route = APIRouter()


# Add new book

# Retrieve a list of all books:

# Retrieve details for a specific book:

# Update an existing book:

# delete an existing book: