from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Profile,Link
from django.urls import reverse_lazy


# Create your views here.
# Class based view
class LinkListView(ListView):
    # query for all links Link.abjects.all()
    model = Link


class LinkCreateView(CreateView):
    model = Link
    fields = "__all__"
    success_url = reverse_lazy('home')
    # template model_form -> link_form
    
class LinkUpdateView(UpdateView):
    model = Link
    fields = ['text','url']
    success_url  =reverse_lazy('home')
    # no need to create templates shares same template as Createview
    
class LinkDeleteView(DeleteView):
    model = Link
    success_url=reverse_lazy('home')
    #form to submit to delete the item
    # expect a template name model_confirm_delete.html
    #link_confirm_delete.html

def profile_view(request,profile_slug):
    profile = get_object_or_404(Profile,slug=profile_slug)
    print(profile)
    links = profile.links.all()
    context = {
        'profile': profile,
        'links':links
    }
    return render(request,'link_plant/profile.html',context)