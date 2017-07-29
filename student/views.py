# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from .models import Detail

# Create your views here.
def list_student(request):
	s = Detail.objects.exclude()

	context = {
		'student' : s,
	}
	return render(request, "index.html", context)

class CourseList(View):
	def get(self, request):
		courses = Course.objects.all()

		context = {
		'courses': courses,
		}
		return render(request, "course.html", context)