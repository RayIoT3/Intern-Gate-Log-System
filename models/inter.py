class Intern:
    def __init__(self, intern_id, name, programme, department, status="OUTSIDE"):
        self.intern_id = intern_id
        self.name = name
        self.programme = programme
        self.department = department
        self.status = status  # "OUTSIDE" or "INSIDE"

    def to_dict(self):
        """Converts the intern object into a dictionary for JSON saving."""
        return {
            "intern_id": self.intern_id,
            "name": self.name,
            "programme": self.programme,
            "department": self.department,
            "status": self.status
        }
