from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    birth_date = models.DateField(blank=True, null=True, verbose_name="Data de Nascimento")
    street = models.CharField(max_length=100, blank=True, null=True, verbose_name="Rua")
    house_number = models.CharField(max_length=10, blank=True, null=True, verbose_name="Número da Casa")
    neighborhood = models.CharField(max_length=100, blank=True, null=True, verbose_name="Bairro")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cidade")
    state = models.CharField(max_length=50, blank=True, null=True, verbose_name="Estado")
    cep = models.CharField(max_length=10, blank=True, null=True, verbose_name="CEP")
    interests = models.TextField(blank=True, null=True, verbose_name="Interesses e Hobbies (ex: novelas, filmes, culinária, yoga, leitura, musculação, esportes, viagens, etc.)")
    services_offered = models.TextField(blank=True, null=True, verbose_name="Serviços Oferecidos (O que você gostaria de compartilhar nesta rede? ex: dar aulas de yoga, cuidar de crianças, oferecer caronas, etc.)")
    services_needed = models.TextField(blank=True, null=True, verbose_name="Serviços Procurados (O que você busca nas conexões desta comunidade? ex: troca de experiências, apoio para o cuidado dos filhos, receber caronas, alguém que possa dar aulas de reforço para seus filhos, etc.)")
    number_of_children = models.IntegerField(blank=True, null=True, verbose_name="Quantos filhos você tem? (Use somente números)")
    children_age_groups = models.JSONField(default=list, verbose_name="Escolha a faixa etária dos seus filhos (pode marcar mais de uma faixa etária)")

    def __str__(self):
        return self.username