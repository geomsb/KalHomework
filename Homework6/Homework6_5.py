import random

rank = ["assistant", "associate", "full"]

lines = ""
for i in range(0,1001):
    name = ("FirstName") + str(i + 1) + " " + ("LastName") + str(i + 1)
    rangeProfessor = random.choice(rank)
    salary = 0
    if rangeProfessor == "assistant":
        assistantSalary = format(random.uniform(50000.00, 80000.00),"5.2f")
        salary = assistantSalary
    if rangeProfessor == "associate":
        associateSalary = format(random.uniform(60000.00, 110000.00),"5.2f")
        salary = associateSalary
    if rangeProfessor == "full":
        fullSalary = format(random.uniform(75000.00, 130000.00),"6.2f")
        salary = fullSalary
    line = name + " " + rangeProfessor + " " + salary + "\n"
    lines += line
    print(line)

createAfile = open("Salary.txt", "x")
createAfile.write(lines) 
createAfile.close()

