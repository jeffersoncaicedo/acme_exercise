import unittest
from EmployeesCoincidence import organize_data, calculate_coincidence, print_results


class Coincidence(unittest.TestCase):

    def test_data_valid(self):
        data = ['MARCO=TU18:00-20:00\n', 'GRACE=MO12:00-14:00']
        expected_res = [{'TU_entry': '18:00', 'TU_departure': '20:00', 'employee': 'MARCO'}, {'MO_entry': '12:00',
                                                                                              'MO_departure': '14:00',
                                                                                              'employee': 'GRACE'}]
        self.assertEqual(organize_data(sets_of_data=data), expected_res)

    def test_data_invalid(self):
        data = ['MARCO=TU25:00-30:00\n', 'GRACE=MO12:00s-14:00']
        with self.assertRaises(ValueError):
            organize_data(sets_of_data=data)

    def test_coincidence_false(self):
        data = [{'TU_entry': '18:00', 'TU_departure': '20:00', 'employee': 'MARCO'}, {'MO_entry': '12:00',
                                                                                      'MO_departure': '14:00',
                                                                                      'employee': 'GRACE'}]
        expected_res = 0
        self.assertEqual(calculate_coincidence(data), expected_res)

    def test_coincidence_true(self):
        data = [{'MO_entry': '18:00', 'MO_departure': '20:00', 'employee': 'MARCO'}, {'MO_entry': '19:00',
                                                                                      'MO_departure': '21:00',
                                                                                      'employee': 'GRACE'}]
        expected_res = 1
        self.assertEqual(calculate_coincidence(data), expected_res)

    def test_result_false(self):
        employee1 = {'employee': 'MARCO'}
        employee2 = {'employee': 'GRACE'}
        count = 0
        expected_res = "No employee coincides in the work schedule"
        self.assertEqual(print_results(employee1=employee1, employee2=employee2, count=count), expected_res)

    def test_result_true(self):
        employee1 = {'employee': 'MARCO'}
        employee2 = {'employee': 'GRACE'}
        count = 3
        expected_res = "MARCO-GRACE:3"
        self.assertEqual(print_results(employee1=employee1, employee2=employee2, count=count), expected_res)


if __name__ == '__main__':
    unittest.main()
