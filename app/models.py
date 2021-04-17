from django.db import models

# Create your models her
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.topic_name

class cinema(models.Model):
    topic_name=models.ForeignKey(Topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    url=models.URLField(max_length=100)

    def __str__(self):
        return self.name
    
class acc_record(models.Model):
    name=models.ForeignKey(cinema, on_delete=models.CASCADE)
    date=models.DateField()

    




