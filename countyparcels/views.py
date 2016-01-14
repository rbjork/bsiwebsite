from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
#from django.core.files.uploadedfile import UploadedFile
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.core.mail import send_mail, BadHeaderError, EmailMessage
import traceback
from django.contrib.sessions.models import Session
from django import forms
from django import template
from django.template.defaultfilters import stringfilter
import psycopg2
from .forms import UploadFileForm



from django.views.decorators.csrf import csrf_exempt

from .models import Counties
import csv
import json
from itertools import groupby
from forms import RequestForQuoteForm,ShoppingCartForm,BuyForm
from django_project import settings
from django.forms.formsets import formset_factory
register = template.Library()
# Create your views here.

STATIC_URL = '/static/'
SHOPPING_CART = 'shoppingcart'

states = []

@register.filter
@stringfilter
def trim(value):
    return value.strip()

def fk(item):
    return item.state

def sendmail():
    try:
        #send_mail('Subject here', 'Here is the message.', 'from@example.com',['to@example.com'], fail_silently=False)
        #send_mail(subject, message, sender,recepients, fail_silently=False)
        print "sendemail"
        send_mail('Todays work', 'Here is the work.', 'rgbbiz10@gmail.com',['rgbbiz10@gmail.com'], fail_silently=False)
    except Exception as e:
        print e.message


def index(request):
    if request.path != '/countyparcels/':
        return HttpResponseRedirect('/countyparcels/')

    latest_countyparcels_list = Counties.objects.all().order_by('state')

    mediaroot = settings.MEDIA_ROOT
    currentpath = settings.CURRENT_PATH
   # latest_countyparcels_list.sort(key=lambda x: x[1])
    stateCounties = {}
    stateCountyCount = []
    states = []
    counties = []
    #latest_countyparcels_list = sorted(latest_countyparcels_list, key=fk)
    for k, g in groupby(latest_countyparcels_list, fk):
        listg = list(g)
        stateCountyCount.append(len(listg))
        stateCounties[k] = listg   # Store group iterator as a list
        counties.append((k,listg))
        states.append(k)
       # print k,listg[1].fip
    '''
    for k,v in counties:
        print k,type(v)
        for c in v:
            print c.county
    '''

    stateNumber =  len(states)
    states.sort()
    request.session['states'] = states
    #jsontable = json.dumps(latest_countyparcels_list)
    rownum = len(latest_countyparcels_list)
    colnum = 13
    print len(states)

    #for state in stateCounties:
       # print state,type(stateCounties[state])
        #for cnty in stateCounties[state]:
            #print cnty.county

    # render_template('ordergeneratorgrouped.html',states=states,statenumber=statenumber,statecounties=stateCounties,statecountycounts=stateCountyCount,itemdata=csvtable,colcnt=colnum)

    template = loader.get_template('countyparcels/ordergeneratorgrouped.html')
    context = RequestContext(request, {
        'states': states,
        'statenumber': range(stateNumber),
        'statecounties': counties,
        'statecountycounts': stateCountyCount,
        'itemdata': latest_countyparcels_list,
        'colcnt': colnum,
        'latest_countyparcels_list': latest_countyparcels_list
    })
    return HttpResponse(template.render(context))



def getSelectSpecial(request,misc):
    minpercent = request.GET["minpercent"]
    attributemin = request.GET["attribute"]
    print minpercent,attributemin

    if attributemin == "owner":
        latest_countyparcels_list = Counties.objects.filter(ownpercent__gte = minpercent).order_by('state')
    elif attributemin == "use":
        latest_countyparcels_list = Counties.objects.filter(usepercent__gte = minpercent).order_by('state')
    elif attributemin == "apn":
        latest_countyparcels_list = Counties.objects.filter(apnpercent__gte = minpercent).order_by('state')
    elif attributemin == "val":
        latest_countyparcels_list = Counties.objects.filter(valpercent__gte = minpercent).order_by('state')
    elif attributemin == "flr":
        latest_countyparcels_list = Counties.objects.filter(flrpercent__gte = minpercent).order_by('state')
    elif attributemin == "unt":
        latest_countyparcels_list = Counties.objects.filter(untpercent__gte = minpercent).order_by('state')
    elif attributemin == "yrb":
        latest_countyparcels_list = Counties.objects.filter(yrbpercent__gte = minpercent).order_by('state')
    elif attributemin == "sit":
        latest_countyparcels_list = Counties.objects.filter(sitpercent__gte = minpercent).order_by('state')
    else:
        latest_countyparcels_list = Counties.objects.filter(comp__gte = minpercent).order_by('state')

    stateCounties = {}
    stateCountyCount = []
    states = []

    counties = []
    #latest_countyparcels_list = sorted(latest_countyparcels_list, key=fk)
    for k, g in groupby(latest_countyparcels_list, fk):
        listg = list(g)
        stateCountyCount.append(len(listg))
        stateCounties[k] = listg   # Store group iterator as a list
        counties.append((k,listg))
        states.append(k)

    stateNumber =  len(states)
    states.sort()
    #jsontable = json.dumps(latest_countyparcels_list)
    rownum = len(latest_countyparcels_list)

    template = loader.get_template('countyparcels/ordergeneratorgrouped.html')

    colnum = 13
    context = RequestContext(request, {
        'minpercent':minpercent,
        'attributemin':attributemin,
        'states': states,
        'statenumber': range(stateNumber),
        'statecounties': counties,
        'statecountycounts': stateCountyCount,
        'itemdata': latest_countyparcels_list,
        'colcnt': colnum,
        'latest_countyparcels_list': latest_countyparcels_list
    })
    return HttpResponse(template.render(context))


@csrf_exempt
def save2shoppingcart(request,misc):
    try:
        response_data = {}
        if request.method == 'POST':
            request.session['shappingcart'] = request.POST.copy()
            print "save2shoppingcart"
            response_data['values'] = "good"
        return HttpResponse(json.dumps(response_data),content_type="application/json")
    except Exception as e:
        raise Http404("Failed to save")
        return HttpResponse('False')

def request4purchase(request,misc):
    try:
        request.session[SHOPPING_CART] = json.loads(request.POST['counties'])
    except Exception as e:
        print e.message
        request.session[SHOPPING_CART] = {}
    return HttpResponse("True",content_type="text/plain")

def showMapView(request,misc):
    print "showmapview"
    latest_countyparcels_list = Counties.objects.all().order_by('state')
    template = loader.get_template('countyparcels/qgis2web/usa.html')
    states = request.session['states']
    try:
        counties = request.session[SHOPPING_CART]
    except Exception as e:
        print e.message
        counties = None
    context = RequestContext(request, {
        'states': states,
        'counties':counties
    })
    return HttpResponse(template.render(context))

def buyform(request,misc):
    template = loader.get_template('countyparcels/buyform.html')
    try:
        counties = request.session[SHOPPING_CART]
    except Exception as e:
        print e.message
        counties = None
    context = RequestContext(request, {
        'counties':counties
    })
    return HttpResponse(template.render(context))

def request4quote(request,misc):
    try:
        request.session[SHOPPING_CART] = json.loads(request.POST['counties'])
    except Exception as e:
        request.session[SHOPPING_CART] = {}
    return HttpResponse("True",content_type="text/plain")

def quoteform(request,misc):
    template = loader.get_template('countyparcels/requestforquote.html')
    try:
        counties = request.session[SHOPPING_CART]
    except Exception as e:
        print e.message
        counties = None
    context = RequestContext(request, {
        'counties':counties
    })
    return HttpResponse(template.render(context))

def sendrequest4quote(request,misc):
    form = RequestForQuoteForm(request=request,label_suffix='')
    if form.is_valid():
        print "form is valid"
    else:
        print "form is not valid"
    subject = "Request for Quote" #form.cleaned_data['subject']
    try:
        message = "Name: " + request.POST['FirstName'] + " " + request.POST['LastName'] + "  ORG:" + request.POST['Org'] + "  Contact Preference:" + request.POST['Contact'] \
                  + "  Email:" + request.POST['Email'] +  "  Phone:" + request.POST['Phone'] + "\n Comments:" + request.POST['Comments'] + "\n  Order:" +  request.POST['fipsorder']
        sender = request.POST['Email']
    except Exception as e:
        print e.message
        return HttpResponse('Invalid Form data.')

    recipients = ['ronaldbjork@sbcglobal.net','dklein@boundarysolutions.com']
    try:
        send_mail(subject, message, sender, recipients)
    except BadHeaderError as e:
        print e.message
        return HttpResponse('Invalid header found.')
    return HttpResponse("<br><center><h2>Thanks for your interest. You'll be contacted within 2 business days</h2></center>")
    #else:
       # print "Invalid Form"
        #return HttpResponse("<br><center><h2>Sorry. There was a problem with your order.</h2></center>")
'''
def sendrequest4quote(request,misc):
    form = RequestForQuoteForm(request.POST)
    if form.is_valid():
        message = form.cleaned_data['FirstName'] + " " + form.cleaned_data['LastName'] + "  " +  form.cleaned_data['fipsorder']
        sender = request.POST['Email']
        return HttpResponse("<br><center><h2>Thanks for your interest. You'll be contacted within 2 business days.</h2></center>")
    else:
        print "Invalid Form"
        return HttpResponse("<br><center><h2>Sorry. There was a problem with your order.</h2></center>")
'''

def loaderview(request,misc):

    path = "./orderpage.csv"
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Counties.objects.get_or_create(
                fip=row[0],
                state=row[1],
                countyname=row[2],
                version=row[3],
                comp=row[4],
                percentapn=row[5],
                percentown=row[6],
                uuse=row[7],
                flr=row[8],
                unit=row[9],
                yrbuilt=row[10]
                )

def upload_csv(request,misc):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            process_csv(request.FILES['orderpage'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render_to_response('countyparcels/upload.html', {'form': form})

def process_csv(f):
    #uploadfile = UploadedFile(request.FILES)
    #uploadfile.file
    with open('./orderpage.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    with psycopg2.connect("dbname=django user=django") as conn:
        path = "./orderpage.csv"
        cur = conn.cursor()
        with open(path) as f:
            cur.copy_from(f, 'counties', columns=("FIP", "STATE", "COUNTY", "VERSION", "COMP", "APNPercent", "SITPercent", "OWNPercent", "USEPercent", "VALPercent", "FLRPercent", "UNTPercent", "YRBPercent"))
