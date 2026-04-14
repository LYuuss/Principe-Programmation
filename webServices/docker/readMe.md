# Docker

## Introduction : le cloud

Avant de définir Docker, il est utile d’introduire la notion de **cloud computing**.

Le cloud désigne un ensemble de **serveurs distants accessibles via Internet**, permettant de stocker des données et d’exécuter des applications sans dépendre directement de la machine locale.

---

## Qu’est-ce que Docker ?

Docker est une **plateforme logicielle** qui permet de créer, déployer et exécuter des applications dans des **conteneurs**.

Contrairement à une machine virtuelle, Docker est **léger** et **rapide**, car il partage le noyau du système hôte.

---

## Les conteneurs

Un **conteneur** est un environnement isolé qui contient :

- le code de l’application  
- ses dépendances  
- ses configurations  

Cela permet d’exécuter une application **de manière identique** sur n’importe quelle machine.

Par défaut, un conteneur est **éphémère** :  
si le conteneur est supprimé, ses données internes sont perdues.

---

##Les volumes Docker

Pour éviter la perte de données, Docker propose des **volumes**.

Un volume permet de **stocker les données en dehors du conteneur**, sur la machine hôte.

Ainsi :
- supprimer un conteneur n’efface pas les données  
- recréer un conteneur récupère les données  

---

## Types de stockage avec Docker

### Bind mounts

- Lie un dossier de la machine hôte à un dossier dans le conteneur  
- Accès direct aux fichiers en temps réel  
- Très pratique en développement  

⚠️ Inconvénients :
- dépend du système hôte  
- risques de sécurité si mal configuré  

---

### Volumes Docker (recommandé)

- Gérés directement par Docker  
- Stockés généralement dans `/var/lib/docker/volumes/`  
- Indépendants de l’arborescence utilisateur  
- Plus sécurisés et facilement sauvegardables  

À privilégier en production  

---

### TMPFS

- Stockage temporaire en mémoire (RAM)  
- Très rapide  
- Aucune écriture sur disque  

⚠️ Inconvénient :  
les données sont **perdues au redémarrage**

---

## Networking avec docker

## Dockerfile

Un dockerfile sert à automatiser la création d'images Docker
Sans Dockerfile:
tu dois configurer ton conteneur à la main
Avec Dockerfile:
Docker fait tout ça automatiquement

### Structure générale d'un Dockerfile

- FROM : choisir l'image de base
- RUN : Executer une commande dans l'image
- COPY : copie un fichier ou dossier locale dans l'image
- WORKDIR : definir le dossier de travail
- EXPOSE : documenter le port exposé 
- CMD / ENTRYPOINT : commande lancé au demarrage du conteneur

## Docker Compose

Docker Compose permet de **gérer plusieurs conteneurs en même temps** à l’aide d’un seul fichier de configuration.

👉 Au lieu de lancer plusieurs commandes `docker run`, on décrit toute l’architecture dans un fichier `docker-compose.yml`.

---

### Pourquoi utiliser Docker Compose ?

- Lancer plusieurs services facilement  
- Centraliser la configuration  
- Gérer automatiquement les réseaux  
- Simplifier le développement et le déploiement  

---

## Résumé

Docker permet de :

- isoler les applications avec des conteneurs  
- garantir la portabilité  
- gérer facilement les dépendances  
- persister les données grâce aux volumes  

---

## Exemple : MySQL avec Docker

```bash
docker volume create mysql_data

docker run -d \
  --name mysql \
  -e MYSQL_ROOT_PASSWORD=pass \
  -v mysql_data:/var/lib/mysql \
  -p 3306:3306 \
  mysql:8  
```


## Exemple de fichier `docker-compose.yml`

```yaml
version: "3.9"

services:
  mysql:
    image: mysql:8
    container_name: mysql
    environment:
      MYSQL_ROOT_PASSWORD: pass
    volumes:
      - mysql_data:/var/lib/mysql
    ports:
      - "3306:3306"

  site:
    image: nginx
    container_name: site
    ports:
      - "8080:80"
    depends_on:
      - mysql

volumes:
  mysql_data:  
``````