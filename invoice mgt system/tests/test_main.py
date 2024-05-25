import pytest
from httpx import AsyncClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.model import Base
from app.db import get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.mark.asyncio
async def test_create_invoice():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/invoices/", json={"number": "INV001", "amount": 1500, "status": "Paid", "date": "2023-01-01T00:00:00"})
    assert response.status_code == 200
    assert response.json()["number"] == "INV001"

@pytest.mark.asyncio
async def test_read_invoices():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/invoices/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_read_invoice():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/invoices/", json={"number": "INV002", "amount": 2000, "status": "Pending", "date": "2023-02-01T00:00:00"})
        invoice_id = response.json()["id"]
        response = await ac.get(f"/invoices/{invoice_id}")
    assert response.status_code == 200
    assert response.json()["number"] == "INV002"

@pytest.mark.asyncio
async def test_update_invoice():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/invoices/", json={"number": "INV003", "amount": 2500, "status": "Paid", "date": "2023-03-01T00:00:00"})
        invoice_id = response.json()["id"]
        response = await ac.put(f"/invoices/{invoice_id}", json={"number": "INV003", "amount": 2600, "status": "Paid", "date": "2023-03-01T00:00:00"})
    assert response.status_code == 200
    assert response.json()["amount"] == 2600

@pytest.mark.asyncio
async def test_delete_invoice():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/invoices/", json={"number": "INV004", "amount": 3000, "status": "Pending", "date": "2023-04-01T00:00:00"})
        invoice_id = response.json()["id"]
        response = await ac.delete(f"/invoices/{invoice_id}")
    assert response.status_code == 200
    response = await ac.get(f"/invoices/{invoice_id}")
    assert response.status_code == 404
