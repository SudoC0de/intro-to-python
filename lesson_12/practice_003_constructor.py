"""
Now that you can use a constructor, modify your Printer class so you can
pass the brand, model and paper capacity. Create an instance for each
of the following models:

   Brand       Model       Capacity
   HP          7955e       125 sheets
   Brother     HL-L2310D   250 sheets
   Canon       G4270       100 sheets

Add a print_document() instance method that receives a string and prints
it out. The printout should include the brand and model of the printer.
"""
class Printer:
    def __init__(self, brand, model, capacity):
        self.brand = brand
        self.model = model
        self.capacity = capacity

    def print_document(self, print_document):
        print(print_document)

    def notify_low_ink(self):
        print("Ink is low")

    def notify_out_of_paper(self):
        print("Printer is out of paper")

hp = Printer("HP","7955e",125)
brother = Printer("Brother","HL-L2310D",250)
canon = Printer("Canon","G4270",100)

hp.print_document(f"Printer Brand: {hp.brand}, Model: {hp.model}, Capacity: {hp.capacity}")
brother.print_document(f"Printer Brand: {brother.brand}, Model: {brother.model}, Capacity: {brother.capacity}")
canon.print_document(f"Printer Brand: {canon.brand}, Model: {canon.model}, Capacity: {canon.capacity}")
