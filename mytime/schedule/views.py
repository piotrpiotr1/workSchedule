from django.shortcuts import render

def department(request,departments_id):
    return HttpResponse("You're looking at department %s." % department_id)