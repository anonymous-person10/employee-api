from fastapi import FastAPI, HTTPException
from .schemas import EmployeeCreate, EmployeeUpdate
from .crud import EmployeeDB

app = FastAPI(title="Employee API")

db = EmployeeDB()


@app.get("/employees")
def list_employees():
    return db.list()


@app.post("/employees", status_code=201)
def create_employee(emp: EmployeeCreate):
    return db.create(emp)


@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    emp = db.get(emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp


@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, upd: EmployeeUpdate):
    emp = db.update(emp_id, upd)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp


@app.delete("/employees/{emp_id}", status_code=204)
def delete_employee(emp_id: int):
    ok = db.delete(emp_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Employee not found")
    return None
