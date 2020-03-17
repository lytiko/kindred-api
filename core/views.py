import json
from django.http import JsonResponse
from .forms import UserForm, LoginForm

def signup(request):
    """Processes a signup request."""

    if request.method == "POST":
        data = json.loads(request.body.decode())
        form = UserForm(data)
        if form.is_valid():
            user = form.save()
            return JsonResponse({"message": user.create_jwt()})
        return JsonResponse({"error": dict(form.errors)}, status=422)
    return JsonResponse({"error": "Method not allowed"}, status=405)


def login(request):
    """Processes a login request."""

    if request.method == "POST":
        data = json.loads(request.body.decode())
        print(data)
        form = LoginForm(data)
        user = form.validate_credentials()
        print(user)
        if user:
            r = JsonResponse({"message": user.create_jwt()})
            print(r)
            return r
        else:
            print("Returning", dict(form.errors))
            r =  JsonResponse({"error": dict(form.errors)}, status=422)
            print(r)
            return r
    return JsonResponse({"error": "Method not allowed"}, status=405)