from fastapi import FastAPI, HTTPException
import asyncpg
import os

app = FastAPI()

# Database connection settings
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")

# Create a global variable for the database connection pool
db_pool = None

@app.on_event("startup")
async def startup():
    global db_pool
    db_pool = await asyncpg.create_pool(DATABASE_URL)

@app.on_event("shutdown")
async def shutdown():
    global db_pool
    await db_pool.close()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the API"}

@app.get("/staff/{staff_id}")
async def get_staff(staff_id: int):
    global db_pool
    async with db_pool.acquire() as connection:
        staff = await connection.fetchrow("SELECT * FROM staff WHERE id = $1", staff_id)
        if staff:
            return dict(staff)
        raise HTTPException(status_code=404, detail="Staff not found")

@app.get("/staff")
async def get_all_staff():
    global db_pool
    async with db_pool.acquire() as connection:
        staff_list = await connection.fetch("SELECT * FROM staff")
        return [dict(staff) for staff in staff_list]
