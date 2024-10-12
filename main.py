# Class to represent an Employee
class Employee:
    def __init__(self, emp_id, name, base_salary, bonus=0, deductions=0):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary
        self.bonus = bonus
        self.deductions = deductions

    # Method to calculate total salary
    def calculate_total_salary(self):
        return self.base_salary + self.bonus - self.deductions


# Payroll System class
class PayrollSystem:
    def __init__(self):
        self.employees = {}  # Dictionary to store employee details

    # Function to add a new employee
    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        if emp_id in self.employees:
            print("Employee with this ID already exists.")
            return

        name = input("Enter Employee Name: ")
        base_salary = float(input("Enter Base Salary: "))
        bonus = float(input("Enter Bonus (default is 0): ") or 0)
        deductions = float(input("Enter Deductions (default is 0): ") or 0)

        # Create an Employee object and add it to the system
        employee = Employee(emp_id, name, base_salary, bonus, deductions)
        self.employees[emp_id] = employee
        print(f"Employee {name} added successfully!")

    # Function to view employee details and total salary
    def view_employee(self):
        emp_id = input("Enter Employee ID to view details: ")
        if emp_id in self.employees:
            employee = self.employees[emp_id]
            total_salary = employee.calculate_total_salary()
            print(f"\nEmployee ID: {employee.emp_id}")
            print(f"Name: {employee.name}")
            print(f"Base Salary: {employee.base_salary}")
            print(f"Bonus: {employee.bonus}")
            print(f"Deductions: {employee.deductions}")
            print(f"Total Salary: {total_salary:.2f}")
        else:
            print("Employee not found.")

    # Function to update employee details
    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ")
        if emp_id in self.employees:
            employee = self.employees[emp_id]
            print("Current details:")
            print(f"Base Salary: {employee.base_salary}")
            print(f"Bonus: {employee.bonus}")
            print(f"Deductions: {employee.deductions}")

            # Update details
            employee.base_salary = float(input("Enter new Base Salary: "))
            employee.bonus = float(input("Enter new Bonus (default is 0): ") or 0)
            employee.deductions = float(input("Enter new Deductions (default is 0): ") or 0)

            print(f"Employee {employee.name}'s details updated successfully!")
        else:
            print("Employee not found.")

    # Function to remove an employee
    def remove_employee(self):
        emp_id = input("Enter Employee ID to remove: ")
        if emp_id in self.employees:
            del self.employees[emp_id]
            print("Employee removed successfully!")
        else:
            print("Employee not found.")

    # Function to view all employees
    def view_all_employees(self):
        if not self.employees:
            print("No employees found.")
        else:
            print("\n--- Employee List ---")
            for emp_id, employee in self.employees.items():
                total_salary = employee.calculate_total_salary()
                print(f"ID: {emp_id}, Name: {employee.name}, Total Salary: {total_salary:.2f}")
            print("---------------------")

    # Main menu for the system
    def menu(self):
        while True:
            print("\nPayroll Management System")
            print("1. Add Employee")
            print("2. View Employee")
            print("3. Update Employee")
            print("4. Remove Employee")
            print("5. View All Employees")
            print("6. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.view_employee()
            elif choice == '3':
                self.update_employee()
            elif choice == '4':
                self.remove_employee()
            elif choice == '5':
                self.view_all_employees()
            elif choice == '6':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice! Please try again.")


# Main function to run the system
if __name__ == "__main__":
    payroll_system = PayrollSystem()
    payroll_system.menu()
