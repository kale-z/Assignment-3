# coding=utf-8
from django.template.loader import get_template, render_to_string
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.shortcuts import render_to_response
from mysite.forms import AuthorForm, ContactForm
from django.template import RequestContext
from django.core.mail import send_mail
from models import Book, Author
import datetime
import re




def hello(request):
    print request.META
    if 'q' in request.GET:
        print request.GET['q']
    return HttpResponse("Hello World")

'''
def current_datetime(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It's {{ current_date }}.</body></html>")
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
'''
'''
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>lt is %s</body></html>" % now
    return HttpResponse(html)
'''


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())

'''
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '<html><body>In %s hour(s), it’ll be %s.</body></html>' % (offset, dt)
    return HttpResponse(html)
'''


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html', locals())




def freQ(request):
    l = "Netflix use information about the things people buy or rent to determine which people or items are similar to one another, and then make recommendations based on purchase history. Other sites like Pandora and Last.fm use your ratings of different bands and songs to create custom radio stations"
    d = {}
    for item in l.split():
        if item in d:
            d[item] = d.get(item)+1
        else:
            d[item] = 1
    post = ""
    t = get_template('index.html')
    for k, v in d.items():
        post += "<p> %s : %s </p>" % (k , v)
    html = t.render(Context({'d':d.items(), 'k':k, 'v':v }))
    return HttpResponse(html)


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td> %s </td><td> %s </td></tr>'% (k,v))
    return HttpResponse('<table> %s </table>' % '\n'.join(html))

def search_form(request):
    return render_to_response("search form.html")


def search(request):
    if 'q' in request.GET and request.GET['q'] != '':
        message = 'You searched for: %r' % request.GET['q']
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search results.html', {'books':books, 'query':q})
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)


def addauthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            a = Author(first_name=form.cleaned_data["first_name"],
                       last_name=form.cleaned_data["Last_name"],
                       email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/all-authors/')
    else:
        form = AuthorForm()
    return render_to_response('addauthor.html', {'form': form}, RequestContext(request))

def all_authors(request):
    return render_to_response('all_authors.html', {'author_list': Author.objects.all()})


def latest_books(request):
    book_list = Book.objects.order_by('-pub_date')[:10]
    return render_to_response('latest_books.html', {'book_list': book_list})


def contact_form(request):
    return render_to_response('contact_form.html', RequestContext(request))

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            # send_mail(
            #      request.POST['subject'],
            #      request.POST['message'],
            #      request.POST['email'],
            #      ['ahmetbulut@gmail.com']
            # )
            return HttpResponseRedirect('/contact/thanks/', {}, RequestContext(request))
    return render_to_response('contact_form.html', {'errors': errors})


def contact_formsframework(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print cd
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact_form2.html', {'form': form}, RequestContext(request))


# Assignamnet [3] Part
#========================================================
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from mysite.forms import teacherform, studentform, courseform
from mysite.models import Teacher, Course, Student


def addteacher(request):
    if request.method == 'POST':
        form = teacherform(request.POST)
        if form.is_valid():
            form.save_teacher()
            return HttpResponseRedirect('/teachersuccess')
    else:
        form = teacherform()
    return render_to_response('TForm.html', {'form': form},
                                      RequestContext(request))

def addstudent(request):
    if request.method == 'POST':
        form = studentform(request.POST)
        if form.is_valid():
            form.save_student()
            return HttpResponseRedirect('/studentssuccess')
    else:
        form = studentform()
    return render_to_response('SForm.html', {'form': form,},
                                      RequestContext(request))

def addcourse(request):
    if request.method == 'POST':
        form = courseform(request.POST)
        if form.is_valid():
            form.save_course()
            return HttpResponseRedirect('/coursesuccess')
    else:
        form = courseform()
    return render_to_response('CForm.html', {'form': form},
                                      RequestContext(request))


def succesteacher(request):
    Form = Teacher.objects.all()
    return render_to_response('TSForm.html',{'teacher':Form},RequestContext(request))

def home(request):
    return render_to_response('Home.html',RequestContext(request))

def succescourse(request):
    Form = Course.objects.all()
    return render_to_response('CSForm.html',{'course':Form},RequestContext(request))

def successtudent(request):
    Form = Student.objects.all()
    return render_to_response('SSForm.html',{'student':Form},RequestContext(request))

#========================================================