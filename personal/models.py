from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.db.models import Q

from tasks.models import Task
from django.db.models import Count

#Cycle
class Cycle (models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @staticmethod
    def get_current_cycle():
        current_time = timezone.now()
        existing_cycle = Cycle.objects.filter( start_time__lte=current_time, end_time__gte=current_time).first()
        return existing_cycle
    
    def get_completed_tasks(self):
        completed_tasks = Task.objects.filter(status='COMPLETED', end_time__gte=self.start_time, end_time__lte=self.end_time).select_related('milestone')
        completed_tasks = completed_tasks.annotate(num_tasks=Count('milestone')).order_by('milestone')
        return completed_tasks
    

    def __str__(self):
        start_time_str = self.start_time.strftime('%B %d %H:%M')
        end_time_str = self.end_time.strftime('%B %d %H:%M')
        return f"{start_time_str} - {end_time_str}"
    
    def end_time_formatted(self):
        return self.end_time.strftime('%Y-%m-%dT%H:%M:%S%z')
    

    def to_dict(self):
        return {
            "start_time": self.start_time.strftime('%Y-%m-%dT%H:%M:%S%z'),
            "end_time": self.end_time.strftime('%Y-%m-%dT%H:%M:%S%z'),
            "end_time_formatted": self.end_time_formatted(),
            "str_representation": str(self),
        }


#Events
class EventType(models.Model):
    title = models.CharField(max_length=100)
    is_regular = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    
    
class Event(models.Model):
    event_type = models.ForeignKey(EventType, on_delete=models.SET_NULL, blank=True, null=True, related_name='events')
    title = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField()
    extra_info_1 = models.CharField(max_length=200, blank=True, null=True)
    extra_info_2 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return f" {self.date.strftime('%B %d')} -  {self.title}"
    
    @staticmethod
    def get_events_within_cycle(cycle):
        return Event.objects.filter(date__gte=cycle.start_time.date(), date__lte=cycle.end_time.date())
    


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
        

    @staticmethod
    def get_today_work_sessions(day):
        next_day = day + timezone.timedelta(days=1)

        return WorkSession.objects.filter(
            start_time__range=(day, next_day - timezone.timedelta(seconds=1)),
            end_time__range=(day, next_day - timezone.timedelta(seconds=1)),
        )
    

    @classmethod
    def get_todays_work_sessions_duration(cls, day):
        next_day = day + timezone.timedelta(days=1)
        work_sessions = cls.objects.filter(
            start_time__range=(day, next_day - timezone.timedelta(seconds=1)),
            end_time__range=(day, next_day - timezone.timedelta(seconds=1)),
        )

        total_duration = timedelta()
        for session in work_sessions:
            if session.end_time is not None:
                total_duration += session.end_time - session.start_time

        hours, remainder = divmod(total_duration.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        return f"{hours}h {minutes}m"
    

    @staticmethod
    def get_current_work_session():
        current_time = timezone.now()
        work_session = WorkSession.objects.filter(start_time__lte=current_time, end_time__isnull=True).first()
        return work_session
    
    @staticmethod
    def get_sessions_within_cycle(cycle):
        return WorkSession.objects.filter(
            Q(start_time__gte=cycle.start_time, start_time__lt=cycle.end_time) | 
            Q(end_time__gt=cycle.start_time, end_time__lte=cycle.end_time) |
            Q(start_time__lt=cycle.start_time, end_time__gt=cycle.end_time)
        )