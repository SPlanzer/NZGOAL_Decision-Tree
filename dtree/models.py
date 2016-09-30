from __future__ import unicode_literals
from django.db import models
#from django.core.urlresolvers import reverse

class DataSet(models.Model):
    dataSetName = models.CharField(max_length=200)
    dmName = models.CharField(max_length=200)
    treeComplete = models.BooleanField(default=False) 
    ldsId = models.CharField(max_length=10 ,null=True, blank = True)
    #add login derived data owner
 
    def __str__(self):
        return self.dataSetName
 
class Question(models.Model):
    qid = models.CharField(max_length=2)
    question = models.CharField(max_length=1500)
    y = models.CharField(max_length=2) 
    n = models.CharField(max_length=2)
    isquestion = models.BooleanField(default=True) 
        
    def __str__(self):
        return 'Q'+self.qid+': '+self.question

class Answer(models.Model):
    dataSet = models.ForeignKey(DataSet, on_delete=models.CASCADE)
    question = models.ForeignKey(Question)
    date = models.DateTimeField(auto_now=True)
    answer = models.CharField(max_length=3, null=True, blank=True)
