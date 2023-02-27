"""
In this version we use both Pydantic and SQLAlchemy:

    1. Pydantic: For defining, parsing and validating data exposed by the
    Web API

    2. SQLAlchemy: To define and use the SQL data model.

In the next version we'll use SQLModel to bridge the gap between Pydantic
and SQLAlchemy.

We'll also use the common layering and file structure recommend for FastAPI
and Flask apps:

    - schemas.py: Pydantic models/schemas
    - models.py: SQLAlchemy models (the data model)
    - database_crud.py: SQLAlchemy database access operations
    - database.py: SQLAlchemy connection and session definitions

Links:
    https://fastapi.tiangolo.com/tutorial/sql-databases/
    https://docs.sqlalchemy.org/en/14/orm/quickstart.html
    https://docs.sqlalchemy.org/en/14/orm/
"""

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

import database as db
import database_crud as crud
import schemas as sch
import models
from schemas import ErrorCode


app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5501",
    "http://127.0.0.1:8080",
]

# https://fastapi.tiangolo.com/tutorial/cors/
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# def get_db_session():
#     db_session = db.SessionLocal()
#     try:
#         yield db_session
#     finally:
#         db_session.close()
# #:

@app.post('/register')
async def register(player: str):
    pass "XPTO"

#:

#####################################################################

def main():
    import uvicorn

    uvicorn.run('app:app', reload=True)
#:

if __name__ == '__main__':
    main()
#:


