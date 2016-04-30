from django.shortcuts import render
from .models import Usuario

import oauth2 as oauth
import json
import urllib

CONSUMER_KEY = "SOAqTFAbsqvJkwrFL3ik5U5vl"
CONSUMER_SECRET = "4hLvb1jXXL4hCpznJanOsjtwY9bsMB8H4EjMIixvEt9EdPvDDA"
ACCESS_KEY = "719890253696352256-hBVmR9KvbsVTKSAUS1AelcGLjwqGfmy"
ACCESS_SECRET = "DFQxMhXV78Gp1LaWzN3xLE3EVYhVVxOwiovC8vRmsmrgF"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)


#Auxiliar: analiza que dispositivo usa el usuario
def DispositivoUsuario(seguidor):
        linea = seguidor['status']['source']
        tokens = linea.split()
        #print seguidor['status']['source']
        if tokens[4]=='iPhone</a>' :
                return 1
        else :
                if tokens[4]=='Android</a>' :
	                return 2
                else :
	                return 3 


#Entrada: login twitter
#Salida: lista de seguidores en formato Ids
def IdsSeguidores(usuario):
        params = {'screen_name': usuario, 'user_id' : usuario}
        twurl = "https://api.twitter.com/1.1/followers/ids.json?"+urllib.urlencode(params)       
        response, data = client.request(twurl)
        statuses = json.loads(data)
        try:
                ids = statuses['ids']
                return ids
        except:
                ids = "Usuario privado, peticion no autorizada"
                return ids


#Entrada: lista de Ids
#Salida: guarda en la base de datos info sobre las Ids                     
def ResumenUsuarios(ids):
        if type(ids)!=str:
                for i in ids:  
                        params = {'user_id' : i}
                        twurl = "https://api.twitter.com/1.1/users/show.json?"+urllib.urlencode(params)   
                        response, data = client.request(twurl)
                        seguidor = json.loads(data) 
                        id = seguidor['id']
                        print seguidor['id']
                        nombre = seguidor['name']
                        print seguidor['name']
                        login = seguidor['screen_name']
                        print seguidor['screen_name']
                        descripcion = seguidor['description']
                        print seguidor['description']
                        localidad = seguidor['location']
                        print seguidor['location']
                        namigos = seguidor['friends_count']
                        print seguidor['friends_count']                        
                        nseguidores = seguidor['followers_count']
                        print seguidor['followers_count']
                        ntweetsp = seguidor['statuses_count']
                        print seguidor['statuses_count']
                        nfavoritos = seguidor['favourites_count']
                        print seguidor['favourites_count']
                        try:
                                device = DispositivoUsuario(seguidor)
                        except:
                                device = 0
                        print device
                        #Creamos usuario en base de datos
                        Usuario.objects.create(id = id, nombre = nombre, login = login, localidad = localidad, coordenadas = 0, descripcion = descripcion, dispositivom = device, nseguidores = nseguidores, namigos = namigos, ntweetsp = ntweetsp, nfavoritos = nfavoritos)


#ACCION DEL INDEX.HTML
def index(request):
        idseguidores = IdsSeguidores('rubenznho')
        ResumenUsuarios(idseguidores)
	usuarios = Usuario.objects.all()
	return render(request, 'usertwitter/index.html', {'usuarios': usuarios})

