# Template – Tester une application avec SonarQube (BTS SIO SLAM)
Bloc 3 – Cybersécurité des services informatiques / Qualité de code

Ce dépôt est un **template repository** prêt à l’emploi (local ou GitHub Codespaces) pour :
- lancer **SonarQube** via Docker Compose
- analyser une application (ici : une mini app Python) avec **SonarScanner**
- interpréter : **Bugs**, **Vulnérabilités**, **Security Hotspots**, **Code Smells**

---

## Contexte pro (étude de cas)
Vous êtes développeur dans une ESN. Votre équipe doit livrer une application.
Avant la livraison, le responsable qualité / sécurité impose un contrôle automatique :
> “Pas de livraison si le code contient des vulnérabilités ou des mauvaises pratiques graves.”

Vous devez donc mettre en place un **contrôle SonarQube** et produire une **remédiation**.

---

## Objectif
Ce projet permet de lancer **SonarQube** dans un environnement **GitHub Codespaces** afin d’analyser la qualité du code avec Docker.

Les étudiants doivent **exécuter les commandes dans le terminal Codespaces** pour démarrer correctement SonarQube.

---

# Ouvrir le projet dans GitHub Codespaces

1. Aller sur le dépôt GitHub.
2. Cliquer sur :

Code → Codespaces → Create codespace on main

3. Attendre que l’environnement se lance.

Un terminal Linux est automatiquement ouvert.

---

# Vérifier que Docker fonctionne

Dans le terminal, taper :

```bash
docker --version
docker compose version
---

# Corriger la configuration Elasticsearch

SonarQube nécessite un paramètre spécifique du noyau Linux.

Dans le terminal Codespaces, taper :

```bash
sudo sysctl -w vm.max_map_count=262144
```





Vérifier que la valeur est correcte :

```bash
cat /proc/sys/vm/max_map_count
```

La valeur doit être :

262144

# Lancer SonarQube avec Docker

Dans le terminal :

```bash
docker compose up -d
```

# Vérifier que les conteneurs fonctionnent

```bash
docker compose ps
```

Résultat attendu :

sonarqube   Up
db          Up

# Vérifier que SonarQube répond

Dans le terminal :

curl -I http://127.0.0.1:9000

Vous devez obtenir :

HTTP/1.1 200

# Ouvrir SonarQube dans le navigateur

Dans Codespaces :

Ouvrir l’onglet Ports

Repérer le port 9000

Cliquer sur Open in Browser

Ou utiliser l’URL fournie par Codespaces :

https://<nom-du-codespace>-9000.app.github.dev

---

## Première connexion SonarQube
- URL : port 9000
- Login : **admin**
- Password : **admin**
- SonarQube vous demandera de changer le mot de passe (faites-le).

---

## Créer un projet + Token
Dans SonarQube :
1. **Create Project** → *Manually*
2. Project key : `bts-sio-slam-demo`
3. Display name : `BTS SIO SLAM Demo`
4. Choisir **Locally**
5. Générer un **Token** (copiez-le)

Ensuite, dans le terminal :

```bash
export SONAR_TOKEN="COLLEZ_VOTRE_TOKEN_ICI"
```

### IMPORTANT (Codespaces)
L’URL SonarQube n’est pas `localhost` depuis l’extérieur.
Dans Codespaces, copiez l’URL du port 9000 (ex: `https://xxxx-9000.app.github.dev`)
et tapez la commande suivante dans la fenêtre de terminal :

```bash
export SONAR_HOST_URL="https://XXXX-9000.app.github.dev"
```














---

## 6) Lancer l’analyse (SonarScanner via Docker)
Ce template fournit un script :

```bash
bash scripts/scan.sh
```

---

## 7) Travail demandé (questions)
### Partie A — Compréhension
1. À quoi sert SonarQube ?
2. Différence entre : Bug / Code Smell / Vulnerability / Security Hotspot
3. Pourquoi SonarQube est utile en DevSecOps ?

### Partie B — Analyse
Après scan, relevez :
1. Nombre de **Bugs**
2. Nombre de **Vulnerabilities**
3. Nombre de **Security Hotspots**
4. Donnez 2 exemples de problèmes et expliquez le risque.

### Partie C — Remédiation
1. Corrigez au moins **2 problèmes** détectés
2. Relancez le scan
3. Montrez l’amélioration (avant/après)

---

## 8) Livrables attendus
- `REPONSES.md` (réponses + captures/URL + avant/après)
- Le dépôt avec vos corrections (commits)

---

## 9) Barème (/20)
- Mise en route SonarQube + scan OK : 6 pts
- Analyse et réponses : 6 pts
- Remédiation + scan avant/après : 6 pts
- Qualité du rendu : 2 pts

---

## Dépannage rapide
- Démarrage : `docker compose logs -f sonarqube`
- Scan échoue : vérifiez `SONAR_TOKEN` et `SONAR_HOST_URL`
