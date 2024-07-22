import csv
from mongoengine import Document, StringField

class BaseModel(Document):
    """
    Base class that provides the save_to_csv and get_from_csv functionality.
    """
    save_to_csv = False

    def save_to_csv(self):
        """
        Saves the current instance to a CSV file with the same name as the class.
        """
        if self.save_to_csv:
            csv_filename = f"{self.__class__.__name__}.csv"
            
            try:
                with open(csv_filename, 'r') as file:
                    reader = csv.reader(file)
                    header = next(reader)
            except FileNotFoundError:
                header = [field.name for field in self._fields.values()]
                
                with open(csv_filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
            
            with open(csv_filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([getattr(self, field.name) for field in self._fields.values()])

    @classmethod
    def get_from_csv(cls):
        """
        Retrieves all the data from the CSV file and returns a list of dictionaries.
        """
        csv_filename = f"{cls.__name__}.csv"
        data = []

        try:
            with open(csv_filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            pass

        return data

class StaffTable(BaseModel):
    name = StringField(required=True)
    save_to_csv = True

class CustomerTable(BaseModel):
    name = StringField(required=True)
    email = StringField(required=True)
    save_to_csv = True

# Usage
staff = StaffTable(name="Mark")
staff.save()
staff.save_to_csv()

customer = CustomerTable(name="John", email="john@example.com")
customer.save()
customer.save_to_csv()

staff_data = StaffTable.get_from_csv()
print(staff_data)
# Output: [{'name': 'Mark'}]

customer_data = CustomerTable.get_from_csv()
print(customer_data)
# Output: [{'name': 'John', 'email': 'john@example.com'}]