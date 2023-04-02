from django.db import models


STATUS_CHOICES = [
    ('TO_DO', 'To do'),
    ('IN_PROGRESS', 'In progress'),
    ('CANCELLED', 'Cancelled'),
    ('COMPLETED', 'Completed'),
]

class WorkItem (models.Model):
    title = models.CharField(max_length=50)
    estimated_duration = models.IntegerField(default = 0, blank= True,  null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TO_DO')
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

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




