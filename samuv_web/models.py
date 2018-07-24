import os
from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    idUsuario= models.AutoField('auth.User', primary_key=True, blank=False, null=False)
    nomeUsuario = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=50, unique=True, blank=False,)
    senha = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class Profissional(models.Model):
    usuario = models.ForeignKey(Usuario)
    idProfissional = models.AutoField(primary_key=True, blank=False, null=False)
    
    def __str__(self):
        return self.usuario.nomeUsuario

		
class Paciente(models.Model):
    # Paciente é um usuario??? = models.ForeignKey(Usuario)
    idPaciente = models.AutoField(primary_key=True, blank=False, null=False)
    
    def __str__(self):
        return self.usuario.nomeUsuario
		
		
class Doenca(models.Model):
    idDoenca = models.AutoField(primary_key=True, blank=False, null=False)
    idPaciente = models.ForeignKey(Paciente)
	

class Evolucao(models.Model):
    idEvolucao = models.AutoField(primary_key=True, blank=False, null=False)
    idDoenca = models.ForeignKey(Doenca)
	
	
class Ferida(models.Model):
    idFerida = models.AutoField(primary_key=True, blank=False, null=False)
    idDoenca = models.ForeignKey(Doenca)
	
	
class Caracteristica_da_ferida(models.Model):
    idCaracteristica = models.AutoField(primary_key=True, blank=False, null=False)
    idFerida = models.ForeignKey(Ferida)
	
	
class Imagem(models.Model):
    idImagem = models.AutoField(primary_key=True, blank=False, null=False)
    idAtendimento = models.ForeignKey(Atendimento)
	foto = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	
	def get_image_path(instance, filename):
		return os.path.join('repository', str(instance.id), filename)

	def __str__(self):
        return self.get_image_path
	
class Tecnica(models.Model):
    idTecnica = models.AutoField(primary_key=True, blank=False, null=False)
    nomeTecnica = models.CharField(max_length=250, blank=True, null=True)
	
	def __str__(self):
        return self.nomeTecnica
	
class Atendimento(models.Model):
	idAtendimento = models.AutoField(primary_key=True, blank=False, null=False)
    idTecnica = models.ForeignKey(Tecnica)
	idProfissional = models.ForeignKey(Profissional)
	idEvolucao = models.ForeignKey(Evolucao)
    idCaracteristica = models.ForeignKey(Caracteristica_da_ferida)
	