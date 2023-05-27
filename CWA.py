##name = input("Enter your name>>")
##print(f"Hi {name}!")
##howdy= input("How are you doing?")
#this code makes use of nested lists
no_of_subjects = int(input("How many courses do your offer>>"))
marks_andcredit_hours =[]
totalmarksandcredithours = 0
total_cred = 0
cred_hrs = []
for i in range(0, no_of_subjects-1): 
    marks = int(input("Enter your marks>>"))
    credit_hours = int(input("Enter the corresponding credit hours>>"))
    marks_andcredit_hours.append([marks, credit_hours])  # appends input to a list   
    cred_hrs.append(credit_hours)    
#print(marks_andcredit_hours)
/*this part of the code calculates the totaol credit hour of user and saves in to a new variable called totalcredit hours*/
for j in marks_andcredit_hours:
    result = j[0]*j[1]
    totalmarksandcredithours+=result
print(totalmarksandcredithours)

for m in cred_hrs:
    total_cred+=m
    m+=1
print(total_cred)

/*the next section of code grades the user according to his cwa score*/
CWA_SCORE =round(totalmarksandcredithours/total_cred)
if  70 <= CWA_SCORE <= 100:
    print(f"Your CWA is {CWA_SCORE}")
    print("Your are in the first class") 
elif 65.999 <= CWA_SCORE <= 69.999:
    print(f"Your CWA is {CWA_SCORE}")
    print("You are in 2nd Class Upper") 
elif 60 <= CWA_SCORE <= 65:
    print(f"Your CWA is {CWA_SCORE}")
    print("You are a 2nd class lower student")
else:
    print("You have passed")
