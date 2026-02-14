import random


def emploee_salary():
    salary = [10000, 25000, 600, 400, 890, 33333]
    random_salary = random.sample(salary,1)
    random_salary_int = random_salary[0]
    bonus = [True, False]
    bonus2  = random.choices(bonus,k=1)
    bonus_boolean = bonus2[0]
    bonus_value = random.randrange(1,500)
    if bonus_boolean is True:
        total_salary = '$' + str(random_salary_int + bonus_value)
    else:
        total_salary = '$' + str(random_salary_int)
    print(f"{random_salary_int}, {bonus2[0]} - '{total_salary}'")


emploee_salary()
emploee_salary()
emploee_salary()
