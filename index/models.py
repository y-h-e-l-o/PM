from django.db import models

# Create your models here.
class Alerte(models.Model):
	name = "Alerte en cours; À supprimer pour faire disparaître"
	contenu = models.TextField()
	def __str__(self): 
		return self.name


class Paragraphe(models.Model):

	titre = models.CharField(max_length=200)
	MENU = [
		('oui','oui'),
		('non','non')
	]
	titre_affiché_dans_le_menu = models.CharField(max_length=4,choices=MENU,default='Oui')
	contenu = models.TextField()
	ordre_dans_l_admin = models.DecimalField(default=0,max_digits=1, decimal_places=0)

	POSITIONS = [
		('Gauche', 'Gauche'),
		('Milieu', 'Milieu'),
		('Droite', 'Droite'),
	]
	LIGNES = [
		('Une', 'Une'),
		('Deux', 'Deux'),
		('Trois', 'Trois'),
		('Quatre', 'Quatre'),
		('Cinq', 'Cinq'),
		('Six', 'Six'),
		('Sept', 'Sept'),
		('Huit', 'Huit'),
		('Neuf', 'Neuf'),
		('Dix', 'Dix'),
	]
	COULEURS = [
		('Rose','Rose'),
		('Jaune','Jaune'),
		('Vert','Vert'),
		('Blanc','Blanc'),
		('vertCanard','Vert canard'),
		('Transparent','Transparent')
	]
	TAILLES = [
		('Classique','Classique'),
		('Large','Large'),
		('Xlarge','Extra Large')
	]


	position = models.CharField(max_length=6,choices=POSITIONS,default='Gauche')
	ordre_d_affichage = models.CharField(max_length=6,choices=LIGNES,default='Une')
	largeur = models.CharField(max_length=11,choices=TAILLES,default='Classique')
	fond = models.CharField(max_length=11,choices=COULEURS,default='Blanc')

	def __str__(self): 
		return self.titre
	class Meta : 
		ordering = ["ordre_dans_l_admin"]

class Horaire(models.Model):
	name= "Horaire"
	contenu = models.TextField()
	def __str__(self): 
		return self.name	


class Contact(models.Model):
	name = "Contacts"
	contenu = models.TextField()
	def __str__(self): 
		return self.name