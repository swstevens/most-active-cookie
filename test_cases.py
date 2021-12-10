from os import error
import most_active_cookie
import unittest

class TestMultiple(unittest.TestCase):
    def test_multiple(self):
        print("testing for two results")
        assert most_active_cookie.find_most_active(['.\\most_active_cookie.py', '.\\test_multiple.csv', '-d', '2018-12-09']) == ['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA']
        print()
    def test_multiple_2(self):
        print("testing for three results")
        assert most_active_cookie.find_most_active(['.\\most_active_cookie.py', '.\\cookie_log.csv', '-d', '2018-12-08']) == ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG']
        print()


class TestEdgeCases(unittest.TestCase):
    def test_empty(self):
        print("tesing empty csv")
        assert most_active_cookie.find_most_active(['.\\most_active_cookie.py', '.\\test_empty.csv', '-d', '2018-12-09']) == []
        print()
    def test_wrong_date(self):
        print("testing single entry csv with incorrect date")
        assert most_active_cookie.find_most_active(['.\\most_active_cookie.py', '.\\test_empty.csv', '-d', '2018-12-09']) == []
        print()
    def test_single_entry(self):
        print("testing single entry csv with correct date")
        assert most_active_cookie.find_most_active(['.\\most_active_cookie.py', '.\\test_one.csv', '-d', '2018-12-09']) == ['AtY0laUfhglK3lC7']
        print()

class IncorrectUsage(unittest.TestCase):
    def test_incorrect_format(self):
        print("testing incorrect datetime")
        with self.assertRaises(error):
            most_active_cookie.find_most_active(['.\\most_active_cookie.py', '.\\test_incorrect.csv', '-d', '2018-12-09'])
        print()
    def test_incorrect_arguments(self):
        print("testing incorrect number of arguments")
        with self.assertRaises(error):
            most_active_cookie.find_most_active(['.\\most_active_cookie.py', '.\\test_one.csv', '-d'])
        print()
    def test_no_d_flag(self):
        print("testing usage without flag")
        assert most_active_cookie.find_most_active(['.\\most_active_cookie.py', '.\\test_one.csv']) == []
        print()


        
if __name__ == "__main__":
    unittest.main()
    
