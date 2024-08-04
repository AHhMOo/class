class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
car1 = Vehicle(reg_num="ABC123", type="Sedan", owner="John Doe")
car2 = Vehicle(reg_num="XYZ789", type="SUV", owner="Jane Smith")

print("Before updating owner:")
print(f"Vehicle 1 - Registration Number: {car1.registration_number}, Type: {car1.type}, Owner: {car1.owner}")
print(f"Vehicle 2 - Registration Number: {car2.registration_number}, Type: {car2.type}, Owner: {car2.owner}")

car1.update_owner("Alice Johnson")
car2.update_owner("Bob Brown")

print("\nAfter updating owner:")
print(f"Vehicle 1 - Registration Number: {car1.registration_number}, Type: {car1.type}, Owner: {car1.owner}")
print(f"Vehicle 2 - Registration Number: {car2.registration_number}, Type: {car2.type}, Owner: {car2.owner}")
