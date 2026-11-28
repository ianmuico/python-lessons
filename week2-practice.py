"""
The Challenge: Bug Report Cost Estimator

Inputs (ask the user for):
    - Project name, bug ID, and bug description
    - Bug severity score (1-5)
    - Estimated hours required to fix the bug
    - Developer's hourly rate
    - Whether the bug is reproducible (yes/no)

Calculations:
    - Fixing cost
    - Testing time (25% of fixing hours)
    - Total development time and cost, including testing

Checks (use comparison operators):
    - Critical: severity >= 4
    - Long fix: fixing takes more than 8 hours
    - Expensive: total estimated cost exceeds $1,000
    - Urgent: bug is critical AND reproducible

Output:
    - A formatted bug report using f-strings
"""


class Bug:
    def __init__(self, project_name, bug_id, description, severity,
                 fix_hours, hourly_rate, reproducible):
        self.project_name = project_name
        self.bug_id = bug_id
        self.description = description
        self.severity = severity
        self.fix_hours = fix_hours
        self.hourly_rate = hourly_rate
        self.reproducible = reproducible

    # Calculations

    def fixing_cost(self):
        return self.fix_hours * self.hourly_rate

    def testing_hours(self):
        return self.fix_hours * 0.25

    def total_hours(self):
        return self.fix_hours + self.testing_hours()

    def total_cost(self):
        return self.total_hours() * self.hourly_rate

    # Checks (each one returns True or False)

    def is_critical(self):
        return self.severity >= 4

    def is_long_fix(self):
        return self.fix_hours > 8

    def is_expensive(self):
        return self.total_cost() > 1000

    def is_urgent(self):
        return self.is_critical() and self.reproducible

    # Output

    def display_report(self):
        # One f-string in triple quotes prints exactly as it looks.
        # The lines start at the left edge so no extra spaces are printed.
        print(f"""
========== BUG REPORT ==========
Project:        {self.project_name}
Bug ID:         {self.bug_id}
Description:    {self.description}
Severity:       {self.severity}
Reproducible:   {self.reproducible}
--------------------------------
Fixing hours:   {self.fix_hours:.2f}
Testing hours:  {self.testing_hours():.2f}
Total hours:    {self.total_hours():.2f}
Hourly rate:    ${self.hourly_rate:,.2f}
Fixing cost:    ${self.fixing_cost():,.2f}
Total cost:     ${self.total_cost():,.2f}
--------------------------------
Critical:       {self.is_critical()}
Over 8 hours:   {self.is_long_fix()}
Over $1,000:    {self.is_expensive()}
Urgent:         {self.is_urgent()}
================================""")


def main():
    project_name = input("Project name: ")
    bug_id = input("Bug ID: ")
    description = input("Bug description: ")
    severity = int(input("Severity (1-5): "))
    fix_hours = float(input("Estimated hours to fix: "))
    hourly_rate = float(input("Developer's hourly rate: "))
    reproducible = input("Reproducible? (yes/no): ").strip().lower() == "yes"

    bug = Bug(project_name, bug_id, description, severity,
              fix_hours, hourly_rate, reproducible)
    bug.display_report()


main()