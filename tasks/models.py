from django.db import models
from django.urls import reverse
from django.utils import timezone
from enum import Enum, unique


@unique
class DueDateChoice(Enum):
    DUE_TODAY = 1
    DUE_TOMORROW = 2
    DUE_THIS_CYCLE = 3
    DUE_NEXT_CYCLE = 4
    UNPLANNED = 5
    COMPLETED = 6

@unique
class Status(Enum):
    IN_PROGRESS = 1
    TO_DO = 2
    COMPLETED = 3 
    BACKLOG = 4
    OUT_OF_SCOPE = 5
    CANCELLED = 6


class WorkItem (models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=300, blank= True,  null=True)
    priority = models.IntegerField(default=9)
    title = models.CharField(max_length=300)
    estimated_duration = models.IntegerField(default = 0, blank= True,  null=True)
    status = models.IntegerField(choices=[(tag.value, tag.name.replace('_', ' ')) for tag in Status], default=Status.TO_DO.value)
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    start_time = models.DateTimeField(blank=True, null = True)
    end_time = models.DateTimeField(blank=True, null = True)
    due_date = models.IntegerField(choices=[(tag.value, tag.name.replace('_', ' ')) for tag in DueDateChoice], default=DueDateChoice.UNPLANNED.value)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"{self.__class__.__name__}(title='{self.title}', estimated_duration={self.estimated_duration}, status='{self.status}')"


class Project(WorkItem):
    pass

class Milestone(WorkItem):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='milestones')

    def save(self, *args, **kwargs):
        # Check if the status has been updated to 'IN_PROGRESS'
        if self.status == Status.IN_PROGRESS.value:
            self.start_time = timezone.now()
            self.end_time = None

        # Check if the status has been updated to 'COMPLETED'
        if self.status == Status.COMPLETED.value:
            self.end_time = timezone.now()
            self.due_date = DueDateChoice.COMPLETED.value

        if self.due_date == DueDateChoice.COMPLETED.value:
            self.end_time = timezone.now()
            self.status = Status.COMPLETED.value

        super(WorkItem, self).save(*args, **kwargs)

class Task(WorkItem):
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    def __str__(self):
        if self.milestone != None:
            return f' {self.milestone.project.title} {self.milestone.title} {self.title}'
        return self.title
    
    def get_absolute_url(self):
        # return reverse('tasks:task_detail', args=[str(self.id)])
        return reverse('tasks:task_list')
    

    def save(self, *args, **kwargs):
        # Check if the status has been updated to 'IN_PROGRESS'
        if self.status == Status.IN_PROGRESS.value:
            self.start_time = timezone.now()
            self.end_time = None

        # Check if the status has been updated to 'COMPLETED'
        if self.status == Status.COMPLETED.value:
            self.end_time = timezone.now()
            self.due_date = DueDateChoice.COMPLETED.value

        if self.due_date == DueDateChoice.COMPLETED.value:
            self.end_time = timezone.now()
            self.status = Status.COMPLETED.value

        super(WorkItem, self).save(*args, **kwargs)



