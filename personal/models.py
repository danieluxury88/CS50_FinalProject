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
    end_time = models.DateTimeField(blank=True, null=True)

    def duration(self):
        if self.end_time is None:
            return "Not Finished"
        else:
            duration = self.end_time - self.start_time
            hours, remainder = divmod(duration.seconds, 3600)
            minutes, _ = divmod(remainder, 60)
            return f"{hours}h {minutes}m"

    def __str__(self):
        start_time_str = self.start_time.strftime('%B %d %H:%M')
        if self.end_time is None:
            return f"{start_time_str} - Not Finished"
        else:
            end_time_str = self.end_time.strftime('%B %d %H:%M')
            duration_str = self.duration()
            return f"{start_time_str} - {end_time_str} (Duration: {duration_str})"





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
    


class DayRegister (models.Model):
    date = models.DateField()
    note = models.IntegerField(blank=True, null=True)
    comment = models.TextField(max_length=1000)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f" {self.date.strftime('%B %d')}"

