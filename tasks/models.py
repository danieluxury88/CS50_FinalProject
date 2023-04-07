from django.db import models
from django.urls import reverse


STATUS_CHOICES = [
    ('TO_DO', 'To do'),
    ('IN_PROGRESS', 'In progress'),
    ('CANCELLED', 'Cancelled'),
    ('COMPLETED', 'Completed'),
    ('OUT_OF_SCOPE', 'Out Of Scope'),
]

class WorkItem (models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=300, blank= True,  null=True)
    priority = models.IntegerField(default=9)
    title = models.CharField(max_length=300)
    estimated_duration = models.IntegerField(default = 0, blank= True,  null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TO_DO')
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    start_time = models.DateTimeField(blank=True, null = True)
    end_time = models.DateTimeField(blank=True, null = True)
    due_tomorrow = models.BooleanField(default=False)

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

class Task(WorkItem):
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    def __str__(self):
        if self.milestone != None:
            return f' {self.milestone.project.title} {self.milestone.title} {self.title}'
        return self.title
    
    def get_absolute_url(self):
        # return reverse('tasks:task_detail', args=[str(self.id)])
        return reverse('tasks:task_list')



