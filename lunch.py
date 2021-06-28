import random

WEEKS = 16
GROUP_SIZE = 4

employees = []
group = []
def read_file(filename):
    '''takes each line and makes a list'''
    file = open(filename, "r")
    employees.clear()
    for line in file:
        employees.append(line.strip('\n'))
    


def assign_groups():

    old_group = group.copy()
    group.clear()

    #temporarily remove employees from last group from employee pool.
    for element in old_group:
        if element in employees:
            employees.remove(element)

    #add employees to group
    for _ in range(GROUP_SIZE):
        if len(employees) == 0:
            break
        next_employee = random.choice(employees)
        employees.remove(next_employee)
        group.append(next_employee)

        #might not be the best idea to have this here instead of in the main function, but performance would be better to just do it here
        output.write(next_employee + "\n")
    
    #add previous group back in
    for element in old_group:
        employees.append(element)

    print(group)
   
if __name__ == "__main__":
    #clear old group file if it exists
    open("groups.txt", "w").close()
    output = open("groups.txt", "a")

    for _ in range(WEEKS):
        output.write("\n")
        read_file("employees.txt")

        assign_groups()

    output.close()