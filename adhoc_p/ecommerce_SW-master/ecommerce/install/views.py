from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from django.template import RequestContext
import os
# Create your views here.

def installation(request):
    try:
        #print "in try"
        #csrfContext = RequestContext(request)
#       print ("hey")
        #print request.POST.get("installation")
        #return HttpResponse (request.POST.get("installation"))
        if request.method == 'POST':
            #print "register in postt"
            #form = SignupForm(request.POST or None)
            #if form.is_valid():
            #password = form.cleaned_data['password']
            installation = request.POST['installation']
            #print installation
            #print password
            if (installation == 'Docker'):
                os.system('yum install docker')
                return HttpResponse (request.POST.get("installation"))
            elif (installation == 'spark'):
                os.system('mkdir sparkk')
                return HttpResponse (request.POST.get("installation"))
            else:
                print "error"
        else:
            print "error"
    except:
        print("error")       
            
            
        #return render(request, 'user_model/register.html')
   
        
