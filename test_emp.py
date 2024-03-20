import unittest
import emp

class TestEmp(unittest.TestCase):

    def test_first_name(self):
        self.assertEqual(emp.is_valid_first_name('Sushant'), True)
        self.assertEqual(emp.is_valid_first_name('sushant'), False)
        self.assertEqual(emp.is_valid_first_name('Su'), False)
        self.assertEqual(emp.is_valid_first_name('8ushant'), False)
        self.assertEqual(emp.is_valid_first_name('Sus'), True)
        self.assertEqual(emp.is_valid_first_name('Sus8'), False)
    
    def test_last_name(self):
        self.assertEqual(emp.is_valid_last_name('Kumar'), True)
        self.assertEqual(emp.is_valid_last_name('Da'), False)
        self.assertEqual(emp.is_valid_last_name('da'), False)
        self.assertEqual(emp.is_valid_last_name('7as'), False)
        self.assertEqual(emp.is_valid_first_name('Das'), True)
        self.assertEqual(emp.is_valid_last_name('Sus8'), False)
    
    def test_email(self):
        self.assertEqual(emp.is_valid_email('abc@yahoo.com'), True)
        self.assertEqual(emp.is_valid_email('abc111@abc.com'), True)
        self.assertEqual(emp.is_valid_email('abc+100@gmail.com'), True)
        self.assertEqual(emp.is_valid_email('abc@1.com'), True)
        self.assertEqual(emp.is_valid_email('sushant.das@gmail.com'), True)
        self.assertEqual(emp.is_valid_email('abc'), False)
        self.assertEqual(emp.is_valid_email('abc123@gmail.a'), False)
        self.assertEqual(emp.is_valid_email('abc123@.com'), False)
        self.assertEqual(emp.is_valid_email('abc..2002@gmail.com'), False)
        self.assertEqual(emp.is_valid_email('abc@gmail.com.aa.au'), False)
    
    def test_phone_num(self):
        self.assertEqual(emp.is_valid_phone_no('91 6923440589'), True)
        self.assertEqual(emp.is_valid_phone_no('91 7923440589'), True)
        self.assertEqual(emp.is_valid_phone_no('91 8923440589'), True)
        self.assertEqual(emp.is_valid_phone_no('91 9923440589'), True)
        self.assertEqual(emp.is_valid_phone_no('91 69234'), False)
        self.assertEqual(emp.is_valid_phone_no('6923440589'), False)
        self.assertEqual(emp.is_valid_phone_no('11 6923440589'), False)
        self.assertEqual(emp.is_valid_phone_no('116923440589'), False)
        
    def test_password(self):
         self.assertEqual(emp.validate_password('Su7@hyegegegge'), True)
         self.assertEqual(emp.validate_password('Su@hyegegegge'), False)
         self.assertEqual(emp.validate_password('Su7hyegegegge'), False)
         self.assertEqual(emp.validate_password('Su7'), False)
         self.assertEqual(emp.validate_password('676754458'), False)
         self.assertEqual(emp.validate_password('Su@@egegegge'), False)



if __name__ == "__main__":
    unittest.main()