from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden


def index(request, id): 
    people = ["Tom", "Jerry", "Jack", "Bill", "Bob", "John", "Paul", "George", "Ringo", "Pete", "Steve"]
    if id in range(0, len(people)):
        return HttpResponse(people[id])
    else:
        return HttpResponseNotFound("Person not found")
def access(request, age):
    if age not in range(1, 111):
        return HttpResponseBadRequest("Age must be between 1 and 110")
    if(age < 18):
        return HttpResponseForbidden("You are not allowed to access this page")
    else:
        return HttpResponse("You are allowed to access this page")

