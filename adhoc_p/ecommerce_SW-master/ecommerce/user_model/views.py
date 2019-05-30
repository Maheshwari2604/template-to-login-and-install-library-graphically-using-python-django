# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import register_model, add_student
from django.shortcuts import render, HttpResponseRedirect, reverse
import hashlib
from django.contrib import auth
from django.contrib.auth import authenticate, login
# authenticate is for to autnticate username and paswd and login is for session_id
from django.shortcuts import render, redirect
#from django.views.generic import TemplateView
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
#from .tokens import account_activation_token
#from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
#from django.core.context_processors import csrf
from django.template import RequestContext
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
import hashlib
from django.contrib.auth.hashers import make_password , check_password



# Create your views here.
def user_login(request):
    #context = {}
    #csrfContext = RequestContext(request)
    try:
        if request.method == 'POST':
            #con = {}
            username = request.POST['username']
            password = request.POST['password']
            #print username
            #print password
            #return HttpResponse(password)
            #user = register.objects.get(username=username)
            #return HttpResponse(user.password)
            try:
                passw = register_model.objects.get(username=username)
                #print passw
                passwordd = passw.password
                #print (passw.password)
            
            except:
                print "error"

                
            passwd = check_password(password, passwordd)
            #print (passwd)
            #user = authenticate(username = username, password = password)
            if passwd:
                user = register_model.objects.get(username=username , password = passwordd)
                #print user
                #print "user"
            #    print "error"
            #return HttpResponse(user)
            #return HttpResponse(user.username)
            if user:
                #print(user)
                #return HttpResponse(user.id)
                #request.session['signupp_id'] = user
                #print (user.id)
                request.session['user_id'] = user.id
                new_id = user.id
                user.save()
                #print new_id
                #print "new_id"
                #print (request.session['user_id'])
                #return render(request,'S_W/error.html',{'username':username})
                #login(request, user)
                #uu = request.session['signupp_id']
                #return HttpResponse(uu)
                #request.session['email_confirmed'] = True 

                return HttpResponseRedirect(reverse('user_home'))
            #else:
                #context['error'] = "Error in Connection"
                #return render(request, 'S_W/error.html', context)
        else:
            #context[error] = "ERROR"
            #return HttpResponse("eeeoooorrrrooror")
            return render(request, 'user_model/login.html')
    except:
        #print "error3"
        context = {
            "message": "You are a new user, please register your account"
        }
        return render(request, 'user_model/login.html', context)

def password_reset(request):
    #print "hey"
    if request.method == 'POST':
     #   print "problem"
        email = request.POST['email']
        try:
            users = register_model.objects.get(email=email)
        except:
            users = None

      #  print email

        if users is not None:
       #     print "password reset process"
            context = {
                "message" : "you are registered user"
            }
            user = users
            user.save()
        #    print user
            current_site = get_current_site(request)
            subject = 'rest password of your account.'
            message = render_to_string('user_model/password_reset_confirm.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            })
            to_email = email
            Email = EmailMessage(subject,message,to=[to_email])
            Email.send()
            request.session['user_id'] = user.id
            new_id = user.id
         #   print "session is"
          #  print new_id
            #return HttpResponse("Activation link is sent to an email, Please activate your account")
            #return render(request, 'S_W/confirmaton.html')
            context = {
                    "message": "Activation link is sent to an email, Please activate your account"
                }
            return render(request, 'user_model/password_reset.html', context)

        else:
           # print "Something wents wrong"
            #print "please try again with different ID"
            context = {
                "message" : "you are not registered user"
            }

    else:
        context = {
            "message" : "Please Enter your Email......"
        }
        #print "Sorry"

    return render(request, 'user_model/password_reset.html', context)


def password_reset_new(request):

        new_id = request.session['user_id']
        #print new_id
        if new_id is not None:
         #   print new_id
            if request.method == 'POST':
                try:
                    user = register_model.objects.get(id = new_id)
           #         print "User is"
          #          print user
                except:
                    user = None
                if user is not None:           
            #        print new_id
                    old_password = request.POST['old_password']
                    new_password = request.POST['new_password']
             #       print old_password
              #      print user.password
                    confirm_password = make_password(old_password)
                    #print password

                    if (old_password == new_password):
               #         print "passwords are same"
                        user.password = confirm_password
                #        print user.password
                        user.is_active = True
                        user.email_confirmed = True
                        user.save()
                        
                        context = {
                            "message": "your password is changed successfully",
                            "conn": True
                        }
                        

                        # now redirect a page on user_login and set a sleep time of 5 sec to redirect it automaticaly
                        # ye dekhna hai apan ko kal kii kesse
                        # ki back jaaane pr session expire ho jaaaye
                        # fir wapas login page pr redirect ho and new sessions bane
                        # 

                    else:
                 #       print "passswords are not same"
                        
                        context = {
                            "message": "your password is not changed, both passwords are not same",
                        }

                    
                
                else:
                  #  print "user is none"
                # print user
                # print user.firstname
                # print user.password
                # user.password = make_password(password)
                # user.save()
            
                # print user.password

                # print "hey"

                    context = {
                        "message": "your password is changed successfully"
                    }

            else:
            #    print "you are on secand path"

                context = {
                        "message": "you are on wrong path"
                    }

        else:
            context = {
                "message" : "Please reset your password"
            }

        return render(request, 'user_model/reset_pass.html', context)


def activate_password(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = register_model.objects.get(pk = uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        #return HttpResponse("heyyyyyyyyyyyyy")
        #user.is_active = True
        user.save()
        #login(request, user)
        return HttpResponseRedirect(reverse('password_reset_new'))

        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')

    else:
        return HttpResponse('Activation link is invalid!')




def user_home(request):
    request.session.set_expiry(300)
    try:
        #context = {}
        #if request.session.get('email_confirmed'):
        try:
            new_id = request.session['user_id']
            #print (new_id)
            #print("user id is")
        except:
            new_id = None
            HttpResponse("Error")


        try:
            if new_id is not None:
                #print ("in New_id")
                #print (new_id)
                #hello = request.session['user_id']
                USER = register_model.objects.get(id = new_id)  
                #print (hello)
                #print ("user is below")
                #print (USER)
                context = {'user':USER}

                return render(request, 'install/index.html')
                #return render(request,'user_model/error.html',context)
                #user = request.user
                #return render(request,'S_W/error.html',context)
            else:
                context={
                    "message": "please login your account"
                }

                return render(request, 'user_model/add_student.html', context)
                #return HttpResponseRedirect(reverse('home'))
                #return render(request,'user_model/error.html', context)
        except:
            print "except1"
            #return HttpResponseRedirect(reverse('home'))

    except:
        context = {
            "message" : "please login your account"
        }
        #print "except2"
        #return HttpResponseRedirect(reverse('home'))  



def logout(request):
   try:
      del request.session['user_id']
      
   except:
      pass
   return HttpResponse("<strong>You are logged out.</strong>")



# def profile(request):
    
#     #the_id = request.session['cart_id']
#     try:
#         if the_id:
#             print "hey profile"
#             register_mod = register_model.objects.get(id = the_id)
#             print register_mod
#             context = {
#                 'register_mod' : register_mod
#             }
#             return render(request, 'profilee/profile.html', context)
#         else:
#             print 'no profile'
#     except:
#         print 'no the_id'  
