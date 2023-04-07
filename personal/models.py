from django.db import models
from datetime import timedelta


#Cycle duration
class Cycle (models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.DurationField(default=timedelta(hours=99, minutes =59, seconds =99))


#Challenges & Events
class Challenge (Cycle):
    title = models.CharField(max_length=100)
    comment = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.title


class EventType(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    
    
class Event(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.SET_NULL, blank=True, null=True)
    event_type = models.ForeignKey(EventType, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField()
    extra_info_1 = models.CharField(max_length=200, blank=True, null=True)
    extra_info_2 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return f" {self.date.strftime('%B %d')} -  {self.title}"
    


#Work Session
class WorkSession(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField( blank=True, null=True)



#Dates/Calendar
class DateType (models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type
    
class Date (models.Model):
    title = models.CharField(max_length=100)
    type = models.ForeignKey(DateType, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f" {self.date.strftime('%B %d')} -  {self.title}"
    


