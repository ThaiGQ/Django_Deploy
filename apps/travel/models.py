from __future__ import unicode_literals

from django.db import models
from ..login.models import User
import datetime
from dateutil.parser import *

# Create your models here.
class tripManager(models.Manager):
    def trip_validator(self, submitted_data):

        errors = []
        flag = True

        today = datetime.datetime.now()
        try:
            begin_date = parse(str(submitted_data["trip_begin"]))
            if begin_date.date() < today.date():
                errors.append("Start date cannot be before today!")
                flag = False
        except Exception as e:
            errors.append("Start date cannot be empty!")
            flag = False

        try:
            end_date = parse(str(submitted_data["trip_end"]))
            try:
                if end_date.date() < begin_date.date():
                    errors.append("Trip cannot end before it begins!")
                    flag = False
            except:
                pass
        except Exception as e:
            errors.append("End date cannot be empty!")
            flag = False

        if len(submitted_data["trip_name"]) < 1:
            errors.append("Trip name cannot be empty!")
            flag = False
        if len(submitted_data["trip_destination"]) < 1:
            errors.append("Destination cannot be empty!")
            flag = False
        if len(submitted_data["trip_description"]) < 1:
            errors.append("Description cannot be empty!")
            flag = False

        # if begin_date.date() < today.date():
        #     errors.append("Start date cannot be before today!")
        #     flag = False
        # if end_date.date() < begin_date.date():
        #     errors.append("Trip cannot end before it begins!")
        #     flag = False

        if flag:
            trip = Trip.objects.create(
                trip_name = submitted_data["trip_name"],
                trip_destination = submitted_data["trip_destination"],
                trip_description = submitted_data["trip_description"],
                trip_begin = submitted_data["trip_begin"],
                trip_end = submitted_data["trip_end"],
                created_by = User.objects.get(id = submitted_data["created_by"]),
                )
            return (flag, trip)
        return (flag, errors)

class Trip(models.Model):
    trip_name = models.CharField(max_length = 255)
    trip_destination = models.CharField(max_length = 100)
    trip_description = models.TextField(max_length = 1000)
    trip_begin = models.DateTimeField()
    trip_end = models.DateTimeField()
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = tripManager()

class Travel_Companions(models.Model):
    trip = models.ForeignKey(Trip)
    companion = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
