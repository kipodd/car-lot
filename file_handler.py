import csv


class FileHandler:
    def __init__(self, file_name):
        self.load_csv(file_name)

    def load_csv(self, file_name):  # can change loaded csv
        self.file_name = file_name
        # TODO check if CSV is empty
        try:
            with open(file_name) as f:
                reader = csv.DictReader(f)
                self.csv_data = []
                for row in reader:
                    self.csv_data.append(row)
        except FileNotFoundError:
            print(f"{file_name} doesn't exist.")
            exit(1)

        self.csv_fieldnames = list(self.csv_data[0])

    # appends if row with that ID doesn't exist already
    def append_to_csv(self, row_to_insert):
        # TODO check if arg is dict
        if self.csv_fieldnames != list(row_to_insert):
            print(
                "Field names aren't equal. Please give data with"
                "these field names as argument:\n",
                self.csv_fieldnames,
            )
            return False

        for row in self.csv_data:
            if row["id"] == row_to_insert["id"]:
                print(
                    f"A row with ID {row['id']} already exists. "
                    "Please give data with unique ID as argument."
                )
                return False

        try:
            with open(self.file_name, "a", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=self.csv_fieldnames)
                writer.writerow(row_to_insert)
        except FileNotFoundError:
            print(f"{self.file_name} doesn't exist.")
            exit(1)
        self.load_csv(self.file_name)  # reload csv
        return True

    def remove_from_csv(self, id):
        if not self.is_number(id):
            print("ID is not a number. Please give a number as argument.")
            return False

        for row in self.csv_data:
            if row["id"] == str(id):
                self.csv_data.remove(row)
                try:
                    with open(self.file_name, "w", newline="") as f:
                        writer = csv.DictWriter(f, fieldnames=self.csv_fieldnames)
                        writer.writeheader()
                        writer.writerows(self.csv_data)
                except FileNotFoundError:
                    print(f"{self.file_name} doesn't exist.")
                    exit(1)

                self.load_csv(self.file_name)  # reload csv
                return True
        return False

    def update_csv(self, new_row):
        for row in self.csv_data:
            if row["id"] == new_row["id"]:
                self.remove_from_csv(row["id"])
                self.append_to_csv(new_row)
                return True

        return False

    def is_number(self, var):
        try:
            int(var)
            return True
        except ValueError:
            return False

    def get_csv_data(self):
        return self.csv_data

    def sort_by_key(self, key, direction="asc"):
        if direction == "asc":
            return sorted(self.csv_data, key=lambda row: row[key])
        elif direction == "desc":
            return sorted(self.csv_data, key=lambda row: row[key], reverse=True)
        else:
            print(
                "Invalid direction. Please give a valid direction as "
                "argument or use the default <asc> argument."
            )
            return False
