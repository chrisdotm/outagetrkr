from django.http import HttpResponse, HttpResponseBadRequest
import json


#you can add or update an incident there is no delete
def incident_readupdate(request, incident_id):
    if request.method == 'GET':
        return HttpResponse(json.dumps({'incident_id' : incident_id}))
    elif request.method == 'POST':
        return addIncident(request.POST)
    else:
        return HttpResponse.HttpResponseBadRequest

def incident_create(request):
    if request.method == 'POST':
        return HttpResponse(json.dumps('incident created'))
    else:
        return HttpResponseBadRequest()
