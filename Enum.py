# Python version of C++ bit-field and enum example
from enum import Enum

# -------------------------
# Define Enums (like C++ enum)
# -------------------------
class Gender(Enum):
    FEMALE = 0
    MALE = 1

class ID(Enum):
    ONE = 0
    TWO = 1

class Status(Enum):
    SINGLE = 0
    MARRIED = 1
    COMMITTED = 2

class Efficient(Enum):
    YES = 0
    NO = 1

# -------------------------
# Simulate a struct with "bit-fields"
# -------------------------
class Employee:
    def __init__(self, gender, emp_id, status, efficient):
        # In C++, bit-fields restrict the number of bits
        # In Python, we just store integers (0 or 1, etc.)
        self.gender = gender.value       # 1 bit
        self.emp_id = emp_id.value       # 4 bits (can store up to 15)
        self.status = status.value       # 3 bits (can store up to 7)
        self.efficient = efficient.value # 2 bits (can store up to 3)

# -------------------------
# Main logic
# -------------------------
if __name__ == "__main__":
    # Assign enum values
    gg = Gender.FEMALE
    gi = ID.ONE
    gs = Status.COMMITTED
    ge = Efficient.YES

    # Create an employee object
    e = Employee(gg, gi, gs, ge)

    # Print stored values
    print("Gender:", e.gender)      # 0 = FEMALE
    print("ID:", e.emp_id)          # 0 = ONE
    print("Status:", e.status)      # 2 = COMMITTED
    print("Efficient:", e.efficient) # 0 = YES
