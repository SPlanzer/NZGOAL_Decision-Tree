from django.http import Http404
from django.shortcuts import render
from django.template import loader
from .models import Question, Answer, DataSet
from django.views import generic
from django.views.generic.edit import CreateView
from .forms import DataSetForm

# --------------------------
# Views
# --------------------------

def datasets(request):
    allDataSets = DataSet.objects.all()
    template = loader.get_template('dtree/datasets.html')
    return render(request, 'dtree/datasets.html', {'allDataSets':allDataSets}) 

def index(request):
    allDataSets = DataSet.objects.all()
    template = loader.get_template('dtree/index.html')
    return render(request, 'dtree/index.html', {'allDataSets':allDataSets}) 

def detail(request, dataSet_id):
    # add 404 handling
    answers = getAnswers(dataSet_id)
    dataset = getDataSet(dataSet_id)
    #except DataSetDs.DoesNotExist:
    #    raise Http404('Data Set Does Not Exist')
    return render(request, 'dtree/detail.html', {'answers': answers, 'dataset':dataset})

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
    Indicate that the decision process has ended
    """
    print 'COMPLETE'
    dataSet.treeComplete = True
    dataSet.save()

def nextQuestion(dataSet, ca = None, decision = None):
    """
    Create Answer DB entry with null answer.
    This is the new Question the user msut answer
    """
    
    if not decision:
        nextQ = '01'
    elif decision == 'no':
        nextQ = ca.question.n
    else:
        nextQ = ca.question.y
    print nextQ
    print '^^^^'
    q = Question.objects.get(qid__exact=nextQ)
    a = Answer(dataSet=dataSet, question=q)
    a.save()
    if nextQ in ('04', '08','10', '17'): #these q's are the end of the line
        setTreeComplete(dataSet)
 
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

qs = {
      1:'Does the material which the agency proposes to release constitute or contain copyright?',
      2:'Does the agency own the copyright in the work or otherwise have sufficient rights to licence the work?' ,
      3:'Work should be licenced with Creative Common BY licence unless restriction applies?' ,
      4:'Either obtain the relevant rights and proceed or do not release for -reuse' ,
      5:'Are there any restrictions on release and re-use?' ,
      6:'Can the restriction(s) be addressed by amendment or anonymisation of the material?' ,
      7:'Does the restriction prevent all form of release?' ,
      8:'Do not publish' ,
      9:'Consider licensing work with the other CC licence (taking Creativity, Authenticity and Non-Discrimination Principles into account) or restrictive lincence as appropriate ' , 
      10:'If appropriate, prepare restricted licence and release to restricted audience',
      11:'Apply Chosen CC licence markings to work and/or prepare to apply them at point of release. For all online releases, include the CC-generated code/metadata',
      12:"Does the author of the work's right to be identified as an author arise and, if so, has the author asserted the right to be identified?"  ,
      13:'Identify the author when publishing the work or an adaptation of it commercially, performing it in the public or communicating it to the public ',
      14:'Does the agency know the format(s) in which people would likw the material to be released?',
      15:'To the extent practicable, prepare the material for release in those format(s). Where material is released in proprietary format, endeavor to release in open, non-proprietary format(s) as well.',
      16: 'Either seek public feedback on desired format(S) before release or prepare the material for release in 1 or more standards-compliant formats with a view to asking recipients, after release, whether they are satisfied with those format(s). Where material is released in proprietary format,endeavor to release in open, non-proprietary format(s) as well.',
      17: "Select appropriate channels for release, whether government and/or third party operated, but including where possible the agency's own website and outgoing Atom or RSS feed and for datasets, an announcment/listing on data.govt.nz. COnsider using press releases and/or social media to publicise release and maximise uptake. RELEASE"}














