from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
import json

# Update an existing inciVdent
@require_http_methods(["POST"])
def incident_update(request, incident_id):
    return HttpResponse(json.dumps('OK')) #XXX: actually do something

# Create a new incident
@require_http_methods(["POST"])
def incident_create(request):
    return HttpResponse(json.dumps('OK')) #XXX: actually do something

# Gets an incident
@require_http_methods(["GET"])
def incident_get(request, incident_id):
    return HttpResponse(json.dumps({'incident_id' : incident_id}))

# Gets an incidents tags
@require_http_methods(["GET"])
def incident_gettags(request, incident_id):
    return HttpResponse(json.dumps({'incident_id' : incident_id}))

# Gets an incidents updates
@require_http_methods(["GET"])
def incident_getupdates(request, incident_id):
    return HttpResponse(json.dumps({'incident_id' : incident_id}))

# Gets an incidents owner
@require_http_methods(["GET"])
def incident_getowner(request, incident_id):
    return HttpResponse(json.dumps({'incident_id' : incident_id}))

# Gets an incidents affected services
@require_http_methods(["GET"])
def incident_getservice(request):
    return HttpResponse(json.dumps({'incident_id' : incident_id}))

# Gets by default a bunch of tags
# XXX: this should probably do something awesome like paginate all tags
# XXX: maybe sort by something
# XXX: maybe be limitable to some types or something
# XXX: good for use as a tag cloud or searching list of tags
@require_http_methods(["GET"])
def tags_get(request):
    return HttpResponse(json.dumps({'tags' : incident_id}))

# Gets a tag by its id
@require_http_methods(["GET"])
def tags_get_by_id(request, tag_id):
    return HttpResponse(json.dumps({'tags' : incident_id}))


# Gets a tag by its id
@require_http_methods(["GET"])
def tags_get_by_name(request, tag_name):
    return HttpResponse(json.dumps({'tags' : incident_id}))


# Gets a tag by its id
@require_http_methods(["GET"])
def tags_get_by_name_fuzzy(request, tag_name):
    return HttpResponse(json.dumps({'tags' : incident_id}))

# Creates a new tag and adds it to an incident
# 1 of 2 ways to add a tag to an incident
@require_http_methods(["POST"])
def tag_create(request, incident_id):
    return HttpResponse(json.dumps({'tags' : incident_id}))

# Updates a tag, this should probably not really be exposed
# Or maybe only admins can have it
# it could be very tricky to handle
@require_http_methods(["POST"])
def tag_update(request, tag_id):
    return HttpResponse(json.dumps({'tags' : incident_id}))

# Creates a new owner
@require_http_methods(["POST"])
def owner_create(request):
    return HttpResponse(json.dumps({'tags' : incident_id}))

# Creates a new service
@require_http_methods(["POST"])
def service_create(request):
    return HttpResponse(json.dumps({'tags' : incident_id}))
