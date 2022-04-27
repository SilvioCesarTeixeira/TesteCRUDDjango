from django.shortcuts import render, redirect
from appcrud.forms import ReservasForm
from appcrud.models import Reservas
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Reservas.objects.filter(Sala_nro__icontains=search)
    else:
        qry_data = Reservas.objects.get_queryset().order_by('id')  # Garante que o DB fornece um registro de cada vez, ordenado por Id
        paginator = Paginator(qry_data, 4)  # Exibe 4 registros do DB por página
        pages = request.GET.get('page')  # Captura qual é a página (page) selecionada no index.html pelo usuário
        data['db'] = paginator.get_page(pages)
    # data['db'] = Reservas.objects.all() ## Buscar todos os registros do DB ## Linha para requests sem paginação
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = ReservasForm()
    return render(request, 'form.html', data)


def create(request):
    form = ReservasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Reservas.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Reservas.objects.get(pk=pk)
    data['form'] = ReservasForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Reservas.objects.get(pk=pk)
    form = ReservasForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Reservas.objects.get(pk=pk)
    db.delete()
    return redirect('home')