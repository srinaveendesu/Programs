
class Employer:
    Bonus = 0

    def __init__(self, firstname, pay):
        self.firstname = firstname
        self.pay = pay

    @classmethod
    def increment(cls, bonus):
        cls.Bonus = cls.Bonus + (bonus * 0.01)


    def payment(self):
        return round(self.pay * (1 + self.Bonus))

    @staticmethod
    def email(name):
        return f'{name}@domain.com'
    
class Manager(Employer):
    def __init__(self, name, pay):
        super().__init__(name, pay)
        

class Engineer(Employer):
    def __init__(self, name, pay):
        super().__init__(name, pay)

E1 = Employer('srinav', 50000)
E2 = Employer('jackryan', 60000)

print(f'Employer payment with bonus {E1.Bonus}: ', E1.payment())
print(f'Employer payment with bonus {E2.Bonus}:', E2.payment())

Employer.increment(5)

print(f'Employer payment after increment with bonus {E2.Bonus}:', E1.payment())
print(f'Employer payment after increment with bonus {E2.Bonus}:', E2.payment())

M = Manager('manager', 100000)

print(f'Manager payment with bonus {M.Bonus}: ', M.payment())

Manager.increment(5)

print(f'Manager payment after increment with bonus {M.Bonus}: ', M.payment())


En = Engineer('engineer', 80000)

print(f'Engineer payment with bonus {En.Bonus}: ', En.payment())

Engineer.increment(2)

print(f'Engineer payment after increment with bonus {En.Bonus} : ', En.payment())

print(M.email(M.firstname))


# Employer payment with bonus 0:  50000
# Employer payment with bonus 0: 60000
# Employer payment after increment with bonus 0.05: 52500
# Employer payment after increment with bonus 0.05: 63000
# Manager payment with bonus 0.05:  105000
# Manager payment after increment with bonus 0.1:  110000
# Engineer payment with bonus 0.05:  84000
# Engineer payment after increment with bonus 0.07 :  85600
# manager@domain.com