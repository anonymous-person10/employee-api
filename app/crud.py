from typing import List, Optional
from .schemas import Employee, EmployeeCreate, EmployeeUpdate


class EmployeeDB:
    def __init__(self):
        self._data: List[Employee] = []
        self._next = 1

    def list(self) -> List[Employee]:
        return self._data

    def get(self, emp_id: int) -> Optional[Employee]:
        for e in self._data:
            if e.id == emp_id:
                return e
        return None

    def create(self, emp_in: EmployeeCreate) -> Employee:
        emp = Employee(id=self._next, **emp_in.dict())
        self._next += 1
        self._data.append(emp)
        return emp

    def update(self, emp_id: int, upd: EmployeeUpdate) -> Optional[Employee]:
        emp = self.get(emp_id)
        if not emp:
            return None
        updated = emp.copy(update=upd.dict(exclude_unset=True))
        idx = self._data.index(emp)
        self._data[idx] = updated
        return updated

    def delete(self, emp_id: int) -> bool:
        emp = self.get(emp_id)
        if not emp:
            return False
        self._data.remove(emp)
        return True
