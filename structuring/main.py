from models import Antibiotic, Vitamin, Vaccine

def show_medicine_info(medicines):
    for med in medicines:
        print(med.info())

if __name__ == "__main__":
    inventory = [
        Antibiotic("Amoxicillin", 10, 5.5),
        Vitamin("Vitamin C", 20, 0.8),
        Vaccine("FluVax", 5, 12.0),
    ]

    show_medicine_info(inventory)