from django.db import models
import re
import bcrypt
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
contact_number = re.compile(r'^[0-9][0-9]\*\\.?[0-9]*')

class UserManager(models.Manager): # Validates the regitration form is complete and the email and phone are not in use
    def reg_validator(self, postData):
        errors = {}
        if len(postData['first_name']) == 0:
            errors['first_name'] = "First Name is Required"
        if len(postData['first_name']) < 2 or postData['first_name'].isalpha() != True:
            errors['first_name'] = "First Name must be at least 2 characters long"
        if len(postData['last_name']) == 0:
            errors['last_name'] = "Last Name is Required"
        if len(postData['last_name']) < 2 or postData['last_name'].isalpha() != True:
            errors['last_name'] = "Last Name must be at least 2 characters long"
        if len(postData['mail']) == 0:
            errors['mail'] = "Email is Required"
        existing_user = User.objects.filter(mail=postData['mail'])
        if len(existing_user) > 0:
            errors['mail'] = "Email already in use"
        elif not email_regex.match(postData['mail']):
            errors['mail'] = "Invalid Email Format"
        if len(postData['contact_no']) == 0:
            errors['contact_no'] = "Phone Number is Required"
        elif len(postData['contact_no']) < 10:
            errors['contact_no'] = "Phone Number must be at least 10 digits long"
        existing_contact = User.objects.filter(contact_no=postData['contact_no'])
        if len(existing_contact) > 0:
            errors['contact_no'] = "Phone Number already in use"
        elif not contact_number.match(postData['contact_no']):
            errors['contact_no'] = "Invalid Phone Number Format"
        if len(postData['password']) == 0:
            errors['password'] = "Password is Required"
        elif len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 Characters"
        elif postData['password'] != postData['comfirm_password']:
            errors['password'] = "Password and Confirm Password must match!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    mail = models.CharField(max_length=60)
    contact_no = models.IntegerField(max_length=10)
    password = models.CharField(max_length=40)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = UserManager()





 
        


