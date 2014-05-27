import unittest

from employee import Employee
import utils

class Employee_test(unittest.TestCase):
    def setUp(self):
        self.employee = Employee()

    def set_values_tests(self):
        values = {'id' : 10,
                  'name' : 'John',
                  'age' : 30}
        self.employee.set_values(values)
        assert self.employee.id == values['id']
        assert self.employee.name == values['name']
        assert self.employee.age == values['age']
        
        values2 = self.employee.to_dict()
        for key in values.keys():
            assert values[key] == values2[key]

    def add_working_seconds_test(self):
        hours = 5
        seconds = hours * 60 * 60
        self.employee.add_working_seconds(seconds)
        self.employee.add_working_seconds(seconds)
        assert self.employee.get_working_hours(utils.current_month()) == hours * 2
        assert self.employee.get_working_hours('01 1999') == 0
        
