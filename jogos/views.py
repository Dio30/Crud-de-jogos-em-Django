from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Jogos
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class JogosList(LoginRequiredMixin, ListView):
    model = Jogos
    queryset = Jogos.objects.order_by('nome_do_jogo').all()
    login_url = reverse_lazy('login')
    paginate_by = 3
    
    def get_queryset(self):
        self.object_list = Jogos.objects.filter(usuario=self.request.user)
        return self.object_list
    
    def get(self, request, *args, **kwargs):
        search = self.request.GET.get('nome_do_jogo')
        if search:
            self.object_list = self.get_queryset().filter(nome_do_jogo__icontains=search)
        else:
            self.object_list = self.get_queryset()
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)

class JogosNew(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Jogos
    fields = ['nome_do_jogo', 'tipo_de_jogo', 'valor_do_jogo', 'descrição_do_jogo']
    success_url = reverse_lazy('lista')
    success_message = 'Jogo foi criado com sucesso'
    login_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Jogos"
        return context
    
class JogosUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Jogos
    fields = ['nome_do_jogo', 'tipo_de_jogo', 'valor_do_jogo', 'descrição_do_jogo']
    success_url = reverse_lazy('lista')
    success_message = 'Jogo foi atualizado com sucesso'
    login_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Jogos, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Jogos"
        return context
    
class JogosDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    queryset = Jogos.objects.all()
    success_url = reverse_lazy('lista')
    success_message = 'Jogo foi deletado com sucesso'
    login_url = reverse_lazy('login')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Jogos, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object