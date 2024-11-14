from app.backend.db import LocalSession


async def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
