from django.shortcuts import render

# Create your views here.
def introduce_view(request, username):
    # username = request.GET.get('username')
    context = {
        'username':username ,
    }
    return render(request, 'my_app/introduce.html', context)
