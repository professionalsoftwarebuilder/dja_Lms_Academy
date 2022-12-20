from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json
import datetime
from registrar.models import Teacher, Module, LearningUnit
from registrar.models import Student
from registrar.models import Course
from registrar.models import Lecture
from teacher.forms import LectureForm, ModuleForm


@login_required(login_url='/landpage')
def lectures_page(request, course_id):
    course = Course.objects.get(id=course_id)
    teacher = Teacher.objects.get(user=request.user)
    return render(request, 'teacher/lecture/view.html',{
        'teacher' : teacher,
        'course' : course,
        'NO_VIDEO_PLAYER': settings.NO_VIDEO_PLAYER,
        'YOUTUBE_VIDEO_PLAYER': settings.YOUTUBE_VIDEO_PLAYER,
        'VIMEO_VIDEO_PLAYER': settings.VIMEO_VIDEO_PLAYER,
        'BLIPTV_VIDEO_PLAYER': settings.BLIPTV_VIDEO_PLAYER,
        'user' : request.user,
        'tab' : 'lectures',
        'HAS_ADVERTISMENT': settings.APPLICATION_HAS_ADVERTISMENT,
        'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })


@login_required(login_url='/landpage')
def lectures_table(request, course_id):
    course = Course.objects.get(id=course_id)
    teacher = Teacher.objects.get(user=request.user)
    
    try:
        lectures = Lecture.objects.filter(course=course).order_by('-week_num', '-lecture_num')
    except Lecture.DoesNotExist:
        lectures = None
    return render(request, 'teacher/lecture/table.html',{
        'teacher' : teacher,
        'course' : course,
        'lectures' : lectures,
        'NO_VIDEO_PLAYER': settings.NO_VIDEO_PLAYER,
        'YOUTUBE_VIDEO_PLAYER': settings.YOUTUBE_VIDEO_PLAYER,
        'VIMEO_VIDEO_PLAYER': settings.VIMEO_VIDEO_PLAYER,
        'BLIPTV_VIDEO_PLAYER': settings.BLIPTV_VIDEO_PLAYER,
        'user' : request.user,
    })


@login_required(login_url='/landpage')
def lecture_modal(request, course_id):
    if request.method == u'POST':
        # Get the lecture_id of post and either create a brand new form
        # for the user, or load up existing one based on the database
        # data for the particular lecture.
        lecture_id = int(request.POST['lecture_id'])
        form = None
        if lecture_id > 0:
            lecture = Lecture.objects.get(lecture_id=lecture_id)
            form = LectureForm(instance=lecture)
        else:
            form = LectureForm()
        return render(request, 'teacher/lecture/modal.html',{
            'form' : form,
        })


@login_required(login_url='/landpage')
def save_lecture(request, course_id):
    response_data = {'status' : 'failed', 'message' : 'unknown error with saving'}
    if request.is_ajax():
        if request.method == 'POST':
            course = Course.objects.get(id=course_id)
            lecture_id = int(request.POST['lecture_id'])
            form = None

            # If lecture already exists, then lets update only, else insert.
            if lecture_id > 0:
                lecture = Lecture.objects.get(lecture_id=lecture_id)
                form = LectureForm(instance=lecture, data=request.POST)
            else:
                form = LectureForm(request.POST, request.FILES)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.course = course
                instance.save()
                response_data = {'status' : 'success', 'message' : 'saved'}
            else:
                response_data = {'status' : 'failed', 'message' : json.dumps(form.errors)}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


@login_required(login_url='/landpage')
def delete_lecture(request, course_id):
    response_data = {'status' : 'failed', 'message' : 'unknown error with deleting'}
    if request.is_ajax():
        if request.method == 'POST':
            lecture_id = int(request.POST['lecture_id'])
            teacher = Teacher.objects.get(user=request.user)
            try:
                lecture = Lecture.objects.get(lecture_id=lecture_id)
                if lecture.course.teacher == teacher:
                    lecture.delete()
                    response_data = {'status' : 'success', 'message' : 'deleted'}
                else:
                    response_data = {'status' : 'failed', 'message' : 'unauthorized deletion'}
            except Lecture.DoesNotExist:
                response_data = {'status' : 'failed', 'message' : 'record not found'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


@login_required(login_url='/landpage')
def modules_page(request, course_id):
    course = Course.objects.get(id=course_id)
    try:
        modules = Module.objects.filter(module_courses__course_id=course_id).order_by('module_courses__volgnr')
    except Module.DoesNotExist:
        modules = None
    return render(request, 'teacher/module/table.html',{
        'course' : course,
        'modules' : modules,
        'user' : request.user,
        'tab' : 'modules',
        'HAS_ADVERTISMENT': settings.APPLICATION_HAS_ADVERTISMENT,
        'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })


@login_required(login_url='/landpage')
def module(request, module_id, course_id, unit_id, ):
    if unit_id == None:
        #unit_id =
        pass

    course = Course.objects.get(id=course_id)

    #print('in get, ' + str(module_id))
    try:
        module = Module.objects.get(pk=module_id)
        #units = module.module_units.filter(module=module_id)
        units = module.learningunits.all().order_by('unit_modules__serialnr')

        if request.method == 'GET':
            if unit_id == '0':
                activeunit = units.first()
            else:
                activeunit = LearningUnit.objects.get(id=unit_id)
        else:
            cont = request.POST.get('editor1', '')
            #print(cont)
            activeunit = LearningUnit.objects.get(id=unit_id)
            activeunit.content = cont
            activeunit.save()


        print(units.count)
        # Hier first omdat je twee keer dezelfde module aan een cursus kunt hangen wat niet de bedoeling is
        moduleinfo = module.module_courses.filter(course=course_id).first()

    except Module.DoesNotExist:
        module = None
    return render(request, 'teacher/module/details.html',{
        'course': course,
        'module': module,
        'units': units,
        'activeunit': activeunit,
        'user': request.user,
        'moduleinfo': moduleinfo,
        'HAS_ADVERTISMENT': settings.APPLICATION_HAS_ADVERTISMENT,
        'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })


@login_required(login_url='/landpage')
def module_modal(request, course_id):
    #if request.method == u'POST':
    # Get the lecture_id of post and either create a brand new form
    # for the user, or load up existing one based on the database
    # data for the particular lecture.
    module_id = int(request.POST.get('module_id', 0))
    form = None
    if module_id > 0:
        theModule = Module.objects.get(module_id=module_id)
        form = ModuleForm(instance=theModule)
    else:
        form = ModuleForm()

    return render(request, 'teacher/module/modal.html', {'form': form, })


