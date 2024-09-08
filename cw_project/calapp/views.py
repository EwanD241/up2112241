from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Entries
from django.utils import timezone
import datetime


#Forms the calendar using the event data
def calendar(request):
    all_entries = Entries.objects.all()
    context = {"entries":all_entries}
    return render(request,'calendar.html',context)

#Retrieves the events from the calendar
def all_entries(request):                                                                                                 
    all_entries = Entries.objects.filter(user=request.user)                                                                                    
    out = []                                                                                                             
    for entry in all_entries:                                                                                             
        out.append({'title': entry.title, 'id': entry.id, 'start': entry.start.isoformat(), 'end': entry.end.isoformat(), 'allDay': True})                                                                                                                                                                                                                                                                                                            
    return JsonResponse(out, safe=False)  

#Adds an event to the calendar
def new_entry(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    start = timezone.datetime.strptime(start, "%Y-%m-%d").date()
    end = timezone.datetime.strptime(end, "%Y-%m-%d").date()
    entry = Entries(title=str(title), start=start, end=end, user=request.user)
    entry.save()
    data = {}
    return JsonResponse(data)

#Updates the event
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    entry = Entries.objects.get(id=id)
    entry.start = start
    entry.end = end
    entry.title = title
    entry.save()
    data = {}
    return JsonResponse(data)

#Deletes the event
def remove(request):
    id = request.GET.get("id", None)
    entry = Entries.objects.get(id=id)
    entry.delete()
    data = {}
    return JsonResponse(data)