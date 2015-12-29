from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message

class AuthorForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField()


# Assignment Part
#=================================================

from django import forms
from mysite.models import Teacher, Student, Course


class teacherform(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    office = forms.Field()
    phone = forms.IntegerField()
    email = forms.EmailField()

    def save_teacher(self):
        Form = Teacher(first_name=self.cleaned_data["first_name"],
                     last_name=self.cleaned_data["last_name"],
                     email=self.cleaned_data["email"],
                     office=self.cleaned_data['office'],
                     phone=self.cleaned_data['phone'])

        Form.save()


class studentform(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

    def save_student(self):
        Form = Student(first_name=self.cleaned_data["first_name"],
                     last_name=self.cleaned_data["last_name"],
                     email=self.cleaned_data["email"],
                     )
        Form.save()
        for item in self.cleaned_data['courses']:
            Form.course.add(item)


class courseform(forms.Form):
    course_name = forms.CharField(max_length=50)
    code = forms.CharField(max_length=30)
    classroom = forms.CharField(max_length=30)
    time = forms.TimeField()
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())

    def save_course(self):
        Form = Course(course_name=self.cleaned_data["course_name"],
                     code=self.cleaned_data["code"],
                     classroom=self.cleaned_data["classroom"],
                     time=self.cleaned_data['time'],teacher=self.cleaned_data['teacher'])

        Form.save()

#====================================================