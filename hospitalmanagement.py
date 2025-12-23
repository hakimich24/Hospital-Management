# Name: Elvis Ochieng
# Admission Number: ABMI/00955/2023
# Project: BBIT Python Project - Hospital Management System


# Classes and Inheritance
class Service:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_total(self, discount_rate=0):
        # Polymorphism: can be overridden in subclasses
        discount = self.price * (discount_rate / 100)
        return self.price - discount


class Consultation(Service):
    def __init__(self, name, price, doctor_type):
        super().__init__(name, price)
        self.doctor_type = doctor_type


class LabTest(Service):
    def __init__(self, name, price, urgent=False):
        super().__init__(name, price)
        self.urgent = urgent

    # Polymorphism: override calculate_total
    def calculate_total(self, discount_rate=0):
        total = super().calculate_total(discount_rate)
        if self.urgent:
            total += 500  
        return total


# Patient class 
class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age

    def summary(self):
        return f"ID: {self.patient_id} | Name: {self.name} | Age: {self.age}"



# Hospital System
class HospitalSystem:
    def __init__(self):
        # Data Structure: List of Patient objects
        self.patients = []
        # Services offered
        self.services = {
            "1": Consultation("General Consultation", 1500, "General"),
            "2": LabTest("Full Blood Count", 2500),
            "3": LabTest("Malaria Test", 800),
            "4": Service("Pharmacy/Medicine", 3000),
            "5": Service("X-Ray Scan", 4000)
        }

    def main_menu(self):
        while True:
            print("\n--- HOSPITAL MANAGEMENT SYSTEM ---")
            print("1. Add New Patient Record")
            print("2. View All Patient Records")
            print("3. Search Patient by ID")
            print("4. Update Patient Record")
            print("5. Select Service & Make Payment")
            print("6. Exit")

            choice = input("Select an option: ")

            if choice == '1':
                self.add_record()
            elif choice == '2':
                self.view_records()
            elif choice == '3':
                self.search_record()
            elif choice == '4':
                self.update_record()
            elif choice == '5':
                self.process_payment()
            elif choice == '6':
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

    def add_record(self):
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = int(input("Enter Age: "))
        patient = Patient(patient_id, name, age)
        self.patients.append(patient)
        print("Record added successfully.")

    def view_records(self):
        if not self.patients:
            print("No records found.")
            return
        for p in self.patients:
            print(p.summary())

    def search_record(self):
        search_id = input("Enter Patient ID to search: ")
        for p in self.patients:
            if p.patient_id == search_id:
                print("Found:", p.summary())
                return
        print("Record not found.")

    def update_record(self):
        search_id = input("Enter Patient ID to update: ")
        for p in self.patients:
            if p.patient_id == search_id:
                print(f"Current Name: {p.name}")
                print(f"Current Age: {p.age}")
                new_name = input("Enter new name (leave blank to keep current): ")
                new_age = input("Enter new age (leave blank to keep current): ")

                if new_name:
                    p.name = new_name
                if new_age:
                    p.age = new_age

                print("Record updated successfully.")
                return
        print("Record not found.")

    def process_payment(self):
        print("\nAvailable Services:")
        for key, service in self.services.items():
            print(f"{key}. {service.name} - KES {service.price}")

        choice = input("Select service: ")
        if choice in self.services:
            selected_service = self.services[choice]

            # Discount policy: 5% for services above KES 2500
            discount = 5 if selected_service.price > 2500 else 0
            total = selected_service.calculate_total(discount)

            print(f"\nService: {selected_service.name}")
            print(f"Original Price: KES {selected_service.price}")
            print(f"Discount: {discount}%")
            print(f"Total Cost: KES {total}")

            while True:
                print("\nPayment Methods:")
                print("1. M-pesa")
                print("2. Credit/Debit Card")

                pay_method = input("Select payment method: ")

                if pay_method == '1':
                    print("Payment processed successfully via M-pesa. Receipt generated.")
                    break
                elif pay_method == '2':
                    print("Payment processed successfully via Card. Receipt generated.")
                    break
                else:
                    print("Invalid payment method. Please try again.")
        else:
            print("Invalid selection.")



# Run Program
if __name__ == "__main__":
    system = HospitalSystem()
    system.main_menu()