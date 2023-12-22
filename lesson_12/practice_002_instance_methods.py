"""
* Create a Printer class that has two functions:
   notify_low_ink()
   notify_out_of_paper()
* notify_low_ink() should print a message saying ink is low.
* notify_out_of_paper() should print a message saying printer is out of paper.
* Create an instance of the printer, then call each of the instance methods
  to test the messages.
"""
class Printer:
    def notify_low_ink(self):
        print("Ink is low")

    def notify_out_of_paper(self):
        print("Printer is out of paper")

Printer1 = Printer()
Printer1.notify_out_of_paper()
Printer1.notify_low_ink()
