
def get_user_input():
    marks_and_credit_hours = []
    while True:
        try:
            no_of_students = int(input("How manu courses do you offer>>"))
        except ValueError:
            print('Invalid Argument\nTry again')
        else:
            for i in range(no_of_students):
                marks = int(input("Enter your marks>>"))
                credit_hours = int(input("Enter the corresponding credit hours>>"))
                marks_and_credit_hours.append((marks, credit_hours))
            return marks_and_credit_hours


def cal_CWA(marks_and_credit_hours):
    total = sum([marks * credit_hours for marks, credit_hours in marks_and_credit_hours])
    total_cred = sum([credit_hours for marks, credit_hours in marks_and_credit_hours])
    cwa = total / total_cred
    print(cwa)
    return cwa


""" total = 0
    total_cred = 0
    for marks, credit_hours in marks_and_credit_hours:
        result = marks * credit_hours
        total += result
        total_cred += credit_hours
    cwa = total / total_cred
    print(cwa)
    return cwa
"""


def show_grade(cwa):
    if 70 <= cwa <= 100:
        print("Your are in the first class")
    elif 65.999 <= cwa <= 69.999:
        print("You are in 2nd Class Upper")
    elif 60 <= cwa <= 65:
        print("You are a 2nd class lower student")
    else:
        print("You have passed")


if __name__ == '__main__':
    User = get_user_input()
    Cwa = cal_CWA(User)
    show_grade(Cwa)
