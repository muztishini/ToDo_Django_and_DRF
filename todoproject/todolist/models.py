from django.db import models


class Status(models.Model):
    name_status = models.CharField(max_length=20)

    def __str__(self):
        return self.name_status


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE, default="open")

    def __str__(self):
        return self.name
