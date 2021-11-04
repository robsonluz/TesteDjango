from django.db import models

# Create your models here.
class TodoItem(models.Model):
  content = models.TextField()
  title = models.TextField()
  
  def __str__(self):
      return self.content

class Ator(models.Model):
  nome = models.CharField("Nome", max_length=100)
  def __str__(self):
      return self.nome
  class Meta:
      verbose_name = "Ator"
      verbose_name_plural = "Atores"


class Filme(models.Model):
  titulo = models.CharField("Título", max_length=100)
  sinopse = models.CharField("Sinopse", max_length=100)
  duracao = models.IntegerField("Duração")
  atores = models.ManyToManyField("Ator", verbose_name="Atores")
  
  def __str__(self):
      return self.titulo
  class Meta:
      verbose_name = "Filme"
      verbose_name_plural = "Filmes"


class Sessao(models.Model):
  data = models.DateTimeField("Data")
  sala = models.ForeignKey('Sala', on_delete=models.PROTECT, verbose_name="Sala")
  filme = models.ForeignKey('Filme', on_delete=models.PROTECT, verbose_name="Filme")
  def __str__(self):
      return f"{self.data} - {self.filme} - sala: {self.sala}"
  class Meta:
      verbose_name = "Sessão"
      verbose_name_plural = "Sessões"


class Sala(models.Model):
  numero = models.CharField("Número", max_length=50)
  capacidade = models.IntegerField("Capacidade")
  def __str__(self):
      return str(self.numero)
  class Meta:
      verbose_name = "Sala"
      verbose_name_plural = "Salas"


class Duvida(models.Model):
  pergunta = models.TextField("Pergunta")
  resposta = models.TextField("Resposta")
  def __str__(self):
      return str(self.pergunta)
  class Meta:
      verbose_name = "Dúvida frequente"
      verbose_name_plural = "Dúvidas frequentes"

class Cidade(models.Model):
  nome = models.CharField("Nome", max_length=255)
  
  def __str__(self):
      return self.nome
  class Meta:
      verbose_name = "Cidade"
      verbose_name_plural = "Cidades"  

class Usuario(models.Model):
  nome = models.CharField("Nome", max_length=255)
  email = models.CharField("E-mail", max_length=100)
  telefone = models.CharField("Telefone", max_length=100)
  senha = models.CharField("Senha", max_length=100)
  cidade = models.ForeignKey('Cidade', on_delete=models.PROTECT, verbose_name="Cidade", null=True)
  
  def __str__(self):
      return self.nome
  class Meta:
      verbose_name = "Usuário"
      verbose_name_plural = "Usuários"      