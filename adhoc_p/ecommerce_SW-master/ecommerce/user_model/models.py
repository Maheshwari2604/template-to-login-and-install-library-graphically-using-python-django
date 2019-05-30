# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from django.core.urlresolvers import reverse
from django.db import models
import hashlib
# Create your models here.


class register_model(models.Model):
    username = models.CharField(max_length=250, help_text='Required')
    email = models.EmailField(max_length=250, help_text='Required')
    password = models.CharField(max_length=100)
    #address = models.ForeignKey('address')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    email_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['firstname', 'lastname']

    '''def get_absolute_url(self):
        return reverse('details', kwargs={'pk':self.pk})'''

    def __str__(self):
        return str(self.id)


class add_student(models.Model):
    first_name = models.CharField(max_length=250, help_text='Required')
    last_name = models.CharField(max_length=250, null=True)
    contact_number = models.PositiveIntegerField(help_text='Required')
    email = models.EmailField(max_length=250, help_text='Required')
    college = models.CharField(max_length=250, help_text='Required')
    branch = models.CharField(max_length=250, help_text='Required')
    Cource = models.CharField(max_length=250, help_text='Required')
    Cource_fee = models.PositiveIntegerField(help_text='Required')
    father_name = models.CharField(max_length=250, help_text='Required')
    father_contact_no = models.PositiveIntegerField(help_text='Required')
    Addmission_type = models.CharField(max_length=250, help_text='Required')
    training_type = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    Fee_paid = models.PositiveIntegerField(help_text='Required')
    #address = models.ForeignKey('address')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['firstname', 'lastname']

    '''def get_absolute_url(self):
        return reverse('details', kwargs={'pk':self.pk})'''

    def __str__(self):
        return str(self.id)


#winter, regular, summers, walkin
#off9, on9