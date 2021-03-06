# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Detail, Course, Subject


# Register your models here.
#@admin.register(Detail)

class StudentAdmin(admin.ModelAdmin):
	fieldset = [("Student Details",{"fields":["first_name","last_name"]})]

	def student_course(self, obj):
		return obj.list_course()

	list_display = ("first_name","last_name",)

admin.site.register(Detail)
admin.site.register(Course)
admin.site.register(Subject)