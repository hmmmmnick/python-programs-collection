"""
Structure-to-Dictionary Conversion in Python
Demonstrates converting structured objects / classes into Python dictionaries.
"""
from dataclasses import dataclass, asdict


@dataclass
class StudentRecord:
    student_id: str
    name: str
    university: str
    specialization: str
    cgpa: float
    is_active: bool

    def to_dict(self) -> dict:
        """Converts the dataclass instance to a standard Python dictionary."""
        return asdict(self)


if __name__ == "__main__":
    student = StudentRecord(
        student_id="JU-2023-CS01",
        name="Ambesh Mishra",
        university="JECRC University",
        specialization="Artificial Intelligence & Machine Learning",
        cgpa=8.8,
        is_active=True
    )

    student_dict = student.to_dict()
    print("Converted Structure to Dictionary:")
    print(student_dict)
    print(f"Dictionary Type: {type(student_dict)}")