from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Produto

# Create your views here.
def homepage(request):
    return render(request, 'LojaMariFe/homepage.html', context=None)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            context = {'form':form,}
            return render(request, 'Auth/register.html', context)
    else:
        form = CustomUserCreationForm()
        context = {'form':form,}
        return render(request, 'Auth/register.html', context)


@login_required
def carrinho(request):
    return render(request, 'LojaMariFe/carrinho.html', context=None)


def camisa(request):
    camisas = Produto.objects.filter(categoria = 'Camisa')
    imagens = []
    for camisa in camisas:
        camisa.imagem = str(camisa.imagem)[22:]

    context = {
        'camisas':camisas,
    }

    return render(request, 'LojaMariFe/camisa.html', context=context)


def calca(request):
    calcas = Produto.objects.filter(categoria = 'Calça')
    context = {'calcas':calcas,}
    return render(request, 'LojaMariFe/calca.html', context=context)

def sapato(request):
    sapatos = Produto.objects.filter(categoria = 'Sapato')
    context = {'sapatos':sapatos,}
    return render(request, 'LojaMariFe/sapato.html', context=context)

def vestido(request):
    vestidos = Produto.objects.filter(categoria = 'Vestido')
    context = {'vestidos':vestidos,}
    return render(request, 'LojaMariFe/vestido.html', context=context)
