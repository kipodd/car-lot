from file_handler import FileHandler
from user import User
from logger import Logger
from car_lot import CarLot

data = {'id': '4', 'name': 'Josh Smith',
        'password': '12345678', 'position': 'teacher', 'salary': '10', 'role': 'teacher'}

# Users = FileHandler("users.csv")
# Users.load_csv("users.csv")
# print(Users.get_csv_data())
# print(Users.append_to_csv(data))
# print(Users.remove_from_csv("1"))
# print(Users.update_csv(data))
# print(Users.sort_by_key("id", "desc"))

my_car_lot = CarLot()
# my_car_lot.update_salary_by_name("Josh Smith", "15")
# print(my_car_lot.add_to_fleet("vehicles.csv"))
# print(my_car_lot.get_all_cars_by_brand("subaru"))
# print(my_car_lot.get_fleet())
print(my_car_lot.get_fleet_size())

# my_logger = Logger()
# my_logger.add_to_log("Hi")


# john = User()
# print(john.user_auth("Jane Doe", "12345678", "users.csv"))
# print(john.user_auth("Jane Doe", "12345678", "bla.csv"))
