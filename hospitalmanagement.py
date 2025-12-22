# Name: Elvis Ochieng
# Admission Number: ABMI/00955/2023
# Project: BBIT Python Project - Hospital Management System

class Service:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_total(self, discount_rate=0):
        # Polymorphism
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

class HospitalSystem:
    def __init__(self):
        # Data Structure: List to store patient records
        self.patients = []
        # Products/Services offered
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
        # Control structures: Input and validation
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = input("Enter Age: ")
        record = {"id": patient_id, "name": name, "age": age}
        self.patients.append(record)
        print("Record added successfully.")

    def view_records(self):
        if not self.patients:
            print("No records found.")
            return
        for p in self.patients:
            print(f"ID: {p['id']} | Name: {p['name']} | Age: {p['age']}")

    def search_record(self):
        search_id = input("Enter Patient ID to search: ")
        for p in self.patients:
            if p['id'] == search_id:
                print(f"Found: {p['name']}, Age: {p['age']}")
                return
        print("Record not found.")

    def update_record(self):
        search_id = input("Enter Patient ID to update: ")
        for p in self.patients:
            if p['id'] == search_id:
               print(f"Current Name: {p['name']}")
               print(f"Current Age: {p['age']}")

            p['name'] = input("Enter new name: ")
            p['age'] = input("Enter new age: ")

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
            
            # Applying discount: 5% for any service above KES 2500
            discount = 0
            if selected_service.price > 2500:
                discount = 5 
            
            total = selected_service.calculate_total(discount)
            
            print(f"\nService: {selected_service.name}")
            print(f"Original Price: KES {selected_service.price}")
            print(f"Discount: {discount}%")
            print(f"Total Cost: KES {total}")
            
            while True:
                print("\nPayment Methods:")
                print("1. Mpesa")
                print("2. Credit/Debit Card")

                pay_method = input("Select payment method: ")

                if pay_method == '1':
                   print("Payment processed successfully via Mpesa. Receipt generated.")
                   break
                elif pay_method == '2':
                   print("Payment processed successfully via Card. Receipt generated.")
                   break
                else:
                   print("Invalid payment method. Please try again.")

        else:
            print("Invalid selection.")

if __name__ == "__main__":
    system = HospitalSystem()
    system.main_menu()