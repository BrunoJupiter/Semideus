from django.http import HttpResponse
from .temp_data import livro_data
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Livro
from .forms import LivroForm
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import Livro, Review, List
from .forms import LivroForm, ReviewForm


def list_livros(request):
    livro_list = Livro.objects.all()
    context = {'livro_list': livro_list}
    return render(request, 'livros/index.html', context)

def detail_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    context = {'livro': livro}
    return render(request, 'livros/detail.html', context)



def create_livro(request):
    if request.method == 'POST':
        livro_name = request.POST['name']
        livro_release_year = request.POST['release_year']
        livro_poster_url = request.POST['poster_url']
        livro = Livro(name=livro_name,
                      release_year=livro_release_year,
                      poster_url=livro_poster_url)
        livro.save()
        return HttpResponseRedirect(
            reverse('livros:detail', args=(livro.id, )))
    else:
        return render(request, 'livros/create.html', {})

def update_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)

    if request.method == "POST":
        livro.name = request.POST['name']
        livro.release_year = request.POST['release_year']
        livro.poster_url = request.POST['poster_url']
        livro.save()
        return HttpResponseRedirect(
            reverse('livros:detail', args=(livro.id, )))

    context = {'livro': livro}
    return render(request, 'livros/update.html', context)


def delete_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)

    if request.method == "POST":
        livro.delete()
        return HttpResponseRedirect(reverse('livros:index'))

    context = {'livro': livro}
    return render(request, 'livros/delete.html', context)

def create_review(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_author = form.cleaned_data['author']
            review_text = form.cleaned_data['text']
            review = Review(author=review_author,
                            text=review_text,
                            livro=livro)
            review.save()
            return HttpResponseRedirect(
                reverse('livros:detail', args=(livro_id, )))
    else:
        form = ReviewForm()
    context = {'form': form, 'livro': livro}
    return render(request, 'livros/review.html', context)

class ListListView(generic.ListView):
    model = List
    template_name = 'livros/lists.html'


class ListCreateView(generic.CreateView):
    model = List
    template_name = 'livros/create_list.html'
    fields = ['name', 'author', 'livros']
    success_url = reverse_lazy('livros:lists')