import pytest
import emp

def test_first_name():
    assert emp.is_valid_first_name('Sus') == True
    assert emp.is_valid_first_name('sushant') == False
    assert emp.is_valid_first_name('Sushant') == True
    assert emp.is_valid_first_name('Su') == False
    assert emp.is_valid_first_name('8ushant') == False
    assert emp.is_valid_first_name('Sus8') == False

def test_last_name():
    assert emp.is_valid_last_name('Kumar') == True
    assert emp.is_valid_last_name('Das') == True
    assert emp.is_valid_last_name('Da') == False
    assert emp.is_valid_last_name('da') == False
    assert emp.is_valid_last_name('7as') == False
    assert emp.is_valid_last_name('Sus8') == False

def test_valid_email():
    assert emp.is_valid_email('abc@yahoo.com') == True
    assert emp.is_valid_email('abc111@abc.com') == True
    assert emp.is_valid_email('abc+100@gmail.com') == True
    assert emp.is_valid_email('abc@1.com') == True
    assert emp.is_valid_email('sushant.das@gmail.com') == True
    assert emp.is_valid_email('abc') == False
    assert emp.is_valid_email('abc123@gmail.a') == False
    assert emp.is_valid_email('abc123@.com') == False
    assert emp.is_valid_email('abc..2002@gmail.com') == False
    assert emp.is_valid_email('abc@gmail.com.aa.au') == False

def test_phone_num():
    assert emp.is_valid_phone_no('91 6923440589') == True
    assert emp.is_valid_phone_no('91 7923440589') == True
    assert emp.is_valid_phone_no('91 8923440589') == True
    assert emp.is_valid_phone_no('91 9923440589') == True
    assert emp.is_valid_phone_no('91 69234') == False
    assert emp.is_valid_phone_no('6923440589') == False
    assert emp.is_valid_phone_no('11 6923440589') == False
    assert emp.is_valid_phone_no('116923440589') == False

def test_password():
    assert emp.validate_password('Su7@hyegegegge') == True
    assert emp.validate_password('Su@hyegegegge') == False
    assert emp.validate_password('Su7hyegegegge') == False
    assert emp.validate_password('Su7') == False
    assert emp.validate_password('676754458') == False
    assert emp.validate_password('Su@@egegegge') == False