from django.shortcuts import render
from .models import Faculty
from django.db.models import Q
import json

def blog1(request):
    return render(request, 'faculty/blog1.html')

def search(request):
    query = request.GET.get('query', None)

    All_Faculties = Faculty.objects.all()

    if query:
        Faculties = (Faculty.objects.filter(Q(college__icontains=query)) | Faculty.objects.filter(Q(name__icontains=query)) | Faculty.objects.filter(Q(department__icontains=query)) | Faculty.objects.filter(Q(research_areas__icontains=query))) 
    else:
        Faculties = All_Faculties

    all_research_areas = set()
    for faculty in All_Faculties:
        research_areas_list = getattr(faculty, 'research_areas')
        for area in research_areas_list:
            all_research_areas.add(area)

    all_colleges = set()
    for faculty in All_Faculties:
        college = getattr(faculty, 'college')
        all_colleges.add(college)

    sorted_research_areas = sorted(all_research_areas)
    sorted_colleges = sorted(all_colleges)

    context = {
        'Faculties': Faculties,
        'research_areas': sorted_research_areas,
        'colleges': sorted_colleges,
    }

    return render(request, 'faculty/search.html', context)

def professor(request, professor_name):
    id = request.GET.get('id', None)
    professor = Faculty.objects.get(id = id)

    context = {
        'professor': professor,
    }

    return render(request, 'faculty/professor.html', context)

def home(request):
    Faculties = Faculty.objects.all()

    all_research_areas = set()
    for faculty in Faculties:
        research_areas_list = getattr(faculty, 'research_areas')
        for area in research_areas_list:
            all_research_areas.add(area)

    all_colleges = set()
    for faculty in Faculties:
        college = getattr(faculty, 'college')
        all_colleges.add(college)

    sorted_research_areas = sorted(all_research_areas)
    sorted_colleges = sorted(all_colleges)

    context = {
        'Faculties': Faculties[:3],
        'research_areas': sorted_research_areas,
        'colleges': sorted_colleges,
    }

    return render(request, 'faculty/home.html', context)
