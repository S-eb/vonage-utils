# script-replay-vonage

Script simple permettant de realiser un appel téléphonique d'un numéro "from" vers un numéro "to".
Une fois l'appel décroché un message vocal répète trois fois "Hello World"

## Pour installer

Ce script utilise poetry pour gérer les dépendances.
Le script nécessite les package suivant:
- ```vonage```
- ```python-dotenv```

Installation avec poetry 

```

poetry install

```


## configuration

ajouter un fichier .env avec les variables suivantes:

```

VONAGE_APPLICATION_ID ='app-key-of-vonage-app'.  # cle de l'application vonage
VONAGE_APPLICATION_PRIVATE_KEY_PATH ='./private.key'            # chemin vers la clé privée 

```


## executer le script

Example pour appeler une sip Uri et répéter trois fois "hello John"

```
poetry run python make-call.py -m "hello John" -l 3 -s True -f "33612345678" -t "sip:mysipaccount@sipdomain.com"

```
