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
async def register(player: sch.PlayerRegister) -> sch.PlayerRegisterResult:
    tourn_id = player.tournament_id
    if tourn_id is None:
        raise HTTPException(status_code = )


    return sch.PlayerRegisterResult(
        id = 1105,
        full_name = player.full_name,
        email = player.email,
    )
    
#:

#####################################################################

def main():
    import uvicorn
    from docopt import docopt
    help_doc = """
A Web accessible FastAPI server that allow players to register/enroll
for tournaments.

Usage:
  app.py [-c | -c -d] [-r] [-p PORT] [-h HOST_IP]

Options:
  -p PORT, --port=PORT          Listen on this port [default: 8000]
  -c, --create-ddl              Crea    te datamodel in the database
  -d, --populate-db             Populate the DB with dummy for testing purposes
  -h HOST_IP, --host=HOST_IP    Listen on this IP address [default: 127.0.0.1]
  -r --reload,                  Reload
"""    
    
    args = docopt(help_doc)
    create_ddl = args['--create-ddl']
    populate_db = args['--populate-db']
    if create_ddl:
        print("Will create ddl")
        if populate_db:
            print("Will also populate the DB")
        #:
    #:

    # print(args)

    
    uvicorn.run(
                'app:app', 
                port = int(args['--port']),
                host = args['--host'],
                reload = args['--reload']
    )
#:
 
if __name__ == '__main__':
    main()
#:


