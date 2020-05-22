import ctypes
import os
from file_handler import FileHandler
from logger import Logger


class CarLot:
    def __init__(self):
        self.fleet = []
        self.log = Logger()

    def update_salary_by_name(self, name, new_salary):
        if not self.is_admin():
            print(
                "User is not administrator. "
                "Please try to run the function as adminstrator."
            )
            return False

        employees_csv = FileHandler("users.csv")
        employees = employees_csv.get_csv_data()
        same_name_employees = []

        for employee in employees:
            if employee["name"] == name:
                employee["salary"] = new_salary
                same_name_employees.append(employee)

        if not same_name_employees:
            print("No employees with that name. Please enter a valid employee name.")
            return False

        for employee in same_name_employees:
            employees_csv.update_csv(employee)

        print("Updated salaries successfully.")
        return True

    def is_admin(self):
        try:
            is_admin = os.getuid() == 0
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        return is_admin

    def add_to_fleet(self, csv_file):
        headers = ["id", "brand", "owner", "last_test", "color", "door_count"]
        fleet = FileHandler(csv_file)
        fleet_data = fleet.get_csv_data()

        if list(fleet_data[0]) == headers:
            self.fleet.extend(fleet_data)
            return True
        else:
            print(
                "Invalid columns." "Please give a CSV file with these columns:\n",
                headers,
            )
            return False

    def get_fleet(self):
        return self.fleet

    def get_fleet_size(self):
        if self.fleet:
            return len(self.fleet)
        else:
            self.log.add_to_log(
                "No cars added to fleet. "
                "Use the add_to_fleet() function to add cars."
            )
            return False

    def get_all_cars_by_brand(self, brand):
        count = 0
        for car in self.fleet:
            if car["brand"] == brand:
                count += 1
        return count
