class Employee:
    def work(self):
        print("work is being done.")
class Manager(Employee):
    def manage(self):
        print("manage is being done.")
mana=Manager()
mana.work()
mana.manage()
