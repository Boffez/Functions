# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import keyboard 


first_name = keyboard.input_string('Enter first name: ')
last_name = keyboard.input_string('Enter last name: ')
age = keyboard.input_integer('Enter age: ')
salary = keyboard.input_real('Enter salary: ')
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n): ')

print('DATA RECORD')
print('===========')
print('Name:', first_name, last_name)
print('Age:', age)
if is_salary_hidden:
    print('Salary: Hidden')
else:
    print('Salary:', salary)