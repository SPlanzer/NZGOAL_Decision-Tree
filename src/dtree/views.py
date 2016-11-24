from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Question, Answer, DataSet
from django import forms

import threading

from .forms import DataSetForm, AddLdsIdForm, AuditForm
from .audit import auditLds


# --------------------------
# Views
# --------------------------

def datasets(request):
    allDataSets = DataSet.objects.order_by('dataSetName').all()
    return render(request, 'dtree/datasets.html', {'allDataSets':allDataSets}) 

def about(request):
    allDataSets = DataSet.objects.all()
    return render(request, 'dtree/about.html', {'allDataSets':allDataSets}) 

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
    return get_object_or_404(DataSet, pk=id)

def setTreeComplete(dataSet):
    """
    Indicate tdetail(request, dataSet_id):hat the decision process has ended
    """

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
    a = Answer(dataSet=dataSet, question=q)
    a.save()
    if nextQ in ('04', '08','10', '17', '22', '24', '30'): #these q's are the end of the line
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

def rollBackDecision(dataSet_id):
    a = currentAnswer(dataSet_id)
    a.delete()
    
def uDecision(request): 
    """
    Set the user decision (yes, no , ok)
    against an answer/question    
    """
    r = request.POST.values()
    if 'Yes' in r:
        decision = 'Yes'
    elif 'No'in r:
        decision = 'No'
    elif 'Ok' in r:
        decision = 'Ok'
    elif '^' in r:
        decision = '^'
    #error handelng in case the above fails
    datasetid = request.POST.keys()[request.POST.values().index(decision)]
    dataSet = getDataSet(datasetid)
    ca = currentAnswer(datasetid)
    if decision != '^':
        setAnswer(ca, decision)
        nextQuestion(dataSet, ca, decision)
    #user request a roll back i.e last question
    else:
        rollBackDecision(datasetid)
    answers = getAnswers(dataSet.pk)
    return render(request, 'dtree/detail.html', {'answers': answers, 'dataset':dataSet})

def removeDataSet(request, dataSet_id):
    dataSet = getDataSet(dataSet_id)
    dataSet.delete()
    return datasets(request)

def audit(request):
    if request.method == 'POST':
        form = AuditForm(request.POST)
        if form.is_valid():
            date_from = form.cleaned_data['date_from']
            date_to = form.cleaned_data['date_to']
            email = form.cleaned_data['email']
            lds_ids = DataSet.objects.filter(treeComplete=True).values_list('ldsId', flat=True)
            t = threading.Thread(target=auditLds,args=(lds_ids, date_from, date_to, email))
            t.start()
            return render(request, 'dtree/audit_standby.html', {'email': email})
    else:
        form = AuditForm()
    return render(request, 'dtree/audit.html', {'form': form})







