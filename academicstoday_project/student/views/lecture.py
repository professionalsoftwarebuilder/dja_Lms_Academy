from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from registrar.models import Course, Module, TstCourseModule, LearningUnit
from registrar.models import Lecture
import json
import datetime

# Developer Notes:
# (1) Templates
# https://docs.djangoproject.com/en/1.7/ref/templates
#
# (2) JSON
# https://docs.djangoproject.com/en/1.7/topics/serialization/


@login_required(login_url='/landpage')
def lectures_page(request, course_id):
    course = Course.objects.get(id=course_id)
    try:
        lectures = Lecture.objects.filter(course_id=course_id).order_by('week_num', 'lecture_num')
    except Lecture.DoesNotExist:
        lectures = None
    return render(request, 'course/lecture/view.html',{
        'course' : course,
        'lectures' : lectures,
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
def modules_page(request, course_id):
    course = Course.objects.get(id=course_id)
    try:
        modules = Module.objects.filter(module_courses__course_id=course_id).order_by('module_courses__volgnr')
    except Module.DoesNotExist:
        modules = None
    return render(request, 'course/module/table.html',{
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

    if request.method == 'GET':
        #print('in get, ' + str(module_id))
        try:
            module = Module.objects.get(pk=module_id)
            #units = module.module_units.filter(module=module_id)
            units = module.learningunits.all().order_by('unit_modules__serialnr')

            if unit_id == '0':
                activeunit = units.first()
            else:
                activeunit = LearningUnit.objects.get(id=unit_id)

            print(units.count)
            # Hier first omdat je twee keer dezelfde module aan een cursus kunt hangen wat niet de bedoeling is
            moduleinfo = module.module_courses.filter(course=course_id).first()

        except Module.DoesNotExist:
            module = None
        return render(request, 'course/module/details.html',{
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
def lecture(request, course_id):
    response_data = {}
    if request.is_ajax():
         if request.method == 'POST':
             # Check to see if any fields where missing from the form.
             if request.POST['lecture_id'] != '':
                 try:
                     lecture_id = int(request.POST['lecture_id'])
                     lecture = Lecture.objects.get(lecture_id=lecture_id)
                 except Lecture.DoesNotExist:
                     lecture = None
                 return render(request, 'course/lecture/details.html',{
                    'lecture' : lecture,
                    'NO_VIDEO_PLAYER': settings.NO_VIDEO_PLAYER,
                    'YOUTUBE_VIDEO_PLAYER': settings.YOUTUBE_VIDEO_PLAYER,
                    'VIMEO_VIDEO_PLAYER': settings.VIMEO_VIDEO_PLAYER,
                    'BLIPTV_VIDEO_PLAYER': settings.BLIPTV_VIDEO_PLAYER,
                    'user' : request.user,
                    'HAS_ADVERTISMENT': settings.APPLICATION_HAS_ADVERTISMENT,
                    'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
                    'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS,
                 })
