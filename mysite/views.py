# coding=utf-8
from django.template.loader import get_template
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import Context
from django.shortcuts import render
from mysite.forms import AuthorForm, ContactForm
from mysite.models import Book, Author
import datetime

# Assignamnet [3] Importing Part
from mysite.forms import teacherform, studentform, courseform
from mysite.models import Teacher, Course, Student


def hello(request):
    print(request.META)
    if 'q' in request.GET:
        print(request.GET['q'])
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
    return render(request, 'current_datetime.html', locals())

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
    return render(request, 'hours_ahead.html', locals())




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
    html = t.render({'item_list': d.items(), 'index': 'Histogram'})
    # html = t.render({'d':d.items(), 'k':k, 'v':v })
    return HttpResponse(html)


def display_meta(request):
    values = request.META.items()
    values = sorted(values)
    html = []
    for k, v in values:
        html.append('<tr><td> %s </td><td> %s </td></tr>'% (k,v))
    return HttpResponse('<table> %s </table>' % '\n'.join(html))

def search_form(request):
    return render(request, "search form.html")


def search(request):
    if 'q' in request.GET and request.GET['q'] != '':
        message = 'You searched for: %r' % request.GET['q']
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'search results.html', {'books':books, 'query':q})
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)


def addauthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            a = Author(first_name=form.cleaned_data["first_name"],
                       last_name=form.cleaned_data["last_name"],
                       email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/all-authors/')
    else:
        form = AuthorForm()
    return render(request, 'addauthor.html', {'form': form})

def all_authors(request):
    return render(request, 'all_authors.html', {'author_list': Author.objects.all()})


def latest_books(request):
    book_list = Book.objects.order_by('-publication_date')[:10]
    return render(request, 'latest_books.html', {'book_list': book_list})


def contact_form(request):
    return render(request, 'contact_form.html')

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
            return HttpResponseRedirect('/contact/thanks/', {})
    return render(request, 'contact_form.html', {'errors': errors})


def contact_formsframework(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form2.html', {'form': form})


# Assignamnet [3] Part
#========================================================
# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from mysite.forms import teacherform, studentform, courseform
# from mysite.models import Teacher, Course, Student


def addteacher(request):
    if request.method == 'POST':
        form = teacherform(request.POST)
        if form.is_valid():
            form.save_teacher()
            return HttpResponseRedirect('/teachersuccess')
    else:
        form = teacherform()
    return render(request, 'TForm.html', {'form': form})

def addstudent(request):
    if request.method == 'POST':
        form = studentform(request.POST)
        if form.is_valid():
            form.save_student()
            return HttpResponseRedirect('/studentssuccess')
    else:
        form = studentform()
    return render(request, 'SForm.html', {'form': form})

def addcourse(request):
    if request.method == 'POST':
        form = courseform(request.POST)
        if form.is_valid():
            form.save_course()
            return HttpResponseRedirect('/coursesuccess')
    else:
        form = courseform()
    return render(request, 'CForm.html', {'form': form})


def succesteacher(request):
    Form = Teacher.objects.all()
    return render(request, 'TSForm.html',{'teacher':Form})
    #Queryset object from the database table containing its keys, and its values are inside the TSForm.html

def home(request):
    return render(request, 'Home.html')

def succescourse(request):
    Form = Course.objects.all()
    return render(request, 'CSForm.html',{'course':Form.values()})

def successtudent(request):
    Form = Student.objects.all()
    return render(request, 'SSForm.html',{'student':Form})

#========================================================