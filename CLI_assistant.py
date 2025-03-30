from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return str(self.value)
    
class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)
        
class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must contain 10 digits")
        super().__init__(value)
        
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        return f"Phone {phone} added to contact {self.name}"
    
    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return f"Phone {phone} removed from contact {self.name}"
        raise ValueError(f"Phone {phone} not found for contact {self.name}")
        
    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return f"Phone {old_phone} changed to {new_phone} for contact {self.name}"
        raise ValueError(f"Phone {old_phone} not found for contact {self.name}")
        
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record 
        return f"Contact {record.name.value} added to address book"
    
    def find(self, name):
        if name in self.data:
            return self.data[name]
        raise KeyError(f"Contact {name} not found")
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"Contact {name} deleted from address book"
        raise KeyError(f"Contact {name} not found")
    
if __name__ == "__main__":
    book = AddressBook()
    
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)
    
    for name, record in book.data.items():
        print(record)
        
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print(john)
    
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")
    
    book.delete("Jane")
        