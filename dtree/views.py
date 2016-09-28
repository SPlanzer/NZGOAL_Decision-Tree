from django.http import Http404
from django.shortcuts import render
from django.template import loader
from .models import Question, Answer, DataSet
from django.views import generic
from django.views.generic.edit import CreateView
from django import forms
from .forms import DataSetForm, AddLdsIdForm

# --------------------------
# Views
# --------------------------

def datasets(request):
    allDataSets = DataSet.objects.order_by('dataSetName').all()
    return render(request, 'dtree/datasets.html', {'allDataSets':allDataSets}) 

def index(request):
    allDataSets = DataSet.objects.all()
    return render(request, 'dtree/index.html', {'allDataSets':allDataSets}) 

def detail(request, dataSet_id):
    # add 404 handling
    answers = getAnswers(dataSet_id)
    dataset = getDataSet(dataSet_id)
    #except DataSetDs.DoesNotExist:
    #    raise Http404('Data Set Does Not Exist')
    return render(request, 'dtree/detail.html', {'answers': answers, 'dataset':dataset})

def addLdsId(request, dataSet_id):
    
    form = AddLdsIdForm(request.POST or None)
    if form.is_valid():
        form.cleaned_data['ldsId']
        DataSet = getDataSet(dataSet_id) 
        DataSet.ldsId = form.cleaned_data['ldsId']
        DataSet.save()
        return datasets(request)
    context = {
        "form": form,
    }
    return render(request, 'dtree/addldsid.html', context)
        
def createDataSet(request):
    """
    Get form input (new data set name), create 
    new dataset as well as first question
    """
    
    #need to add error handling
    form = DataSetForm(request.POST or None)
    if form.is_valid():
        dataSet = form.save(commit=False)
        dataSet.dataSetName
        dataSet.save()
        nextQuestion(dataSet)
        answers = Answer.objects.filter(dataSet__id=dataSet.pk)
        return render(request, 'dtree/detail.html', {'answers': answers, 'dataset':dataSet})    
    context = {
        "form": form,
    }
    return render(request, 'dtree/create_dataset.html', context)

# --------------------------
# Functions to support views
# --------------------------

def getAnswers(id):
    """ 
    Returns all answers associated with a dataset 
    """
    
    return Answer.objects.order_by('question').filter(dataSet__id=id)

def getDataSet(id):
    """
    Returns a Dataset Object as related to a 
    dataset pk 
    """
    
    return DataSet.objects.get(pk=id)

def setTreeComplete(dataSet):
    """
    Indicate tdetail(request, dataSet_id):hat the decision process has ended
    """
    print 'COMPLETE'
    dataSet.treeComplete = True
    dataSet.save()

def nextQuestion(dataSet, ca = None, decision = None):
    """
    Create Answer DB entry with null answer.
    This is the new Question the user must answer
    """
    
    if not decision:
        nextQ = '01'
    elif decision == 'no':
        nextQ = ca.question.n
    else:
        nextQ = ca.question.y
    q = Question.objects.get(qid__exact=nextQ)
    print q
    a = Answer(dataSet=dataSet, question=q)
    print nextQ
    a.save()
    if nextQ in ('04', '08','10', '17', '22', '24', '30'): #these q's are the end of the line
        print 'complete'
        setTreeComplete(dataSet)
 

def currentAnswer(dataSet_id):
    """
    Return The last created question for a dataset
    """
    
    return Answer.objects.order_by('-question').filter(dataSet__id=dataSet_id)[0]

def setAnswer(ca, ans):
    """
    Set an answer to a question 
    Either, 'yes', 'no' ,'ok'
    """
    
    ca.answer = ans
    ca.save()

def uDecision(request): 
    """
    Set the user decision (yes, no , ok)
    against an answer/question    
    """
    
    r = request.POST.values()
    if 'yes' in r:
        decision = 'yes'
    elif 'no'in r:
        decision = 'no'
    elif 'ok' in r:
        decision = 'ok'
    #error handelng in case the above fails
    datasetid = request.POST.keys()[request.POST.values().index(decision)]
    dataSet = getDataSet(datasetid)
    ca = currentAnswer(datasetid)
    setAnswer(ca, decision)
    nextQuestion(dataSet, ca, decision)
    answers = getAnswers(dataSet.pk)
    return render(request, 'dtree/detail.html', {'answers': answers, 'dataset':dataSet})

def removeDataSet(request, dataSet_id):
    dataSet = getDataSet(dataSet_id)
    print dataSet
    dataSet.delete()
    return datasets(request)
    











