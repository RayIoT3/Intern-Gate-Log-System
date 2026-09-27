from datetime import datetime

class GateService:
    def __init__(self):
        # A simple list to keep track of who is inside for now
        self.inside_list = []

    def check_in(self, intern_id: str):
        """Checks an intern into the facility."""
        if intern_id in self.inside_list:
            return f"Error: Intern {intern_id} is already inside!"
        
        self.inside_list.append(intern_id)
        return f"Success: Intern {intern_id} checked in at {datetime.now().strftime('%H:%M:%S')}."

    def check_out(self, intern_id: str):
        """Checks an intern out of the facility."""
        if intern_id not in self.inside_list:
            return f"Error: Intern {intern_id} is not currently inside."
        
        self.inside_list.remove(intern_id)
        return f"Success: Intern {intern_id} checked out."

    def get_inside_interns(self):
        """Returns everyone currently inside."""
        return self.inside_list
