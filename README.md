# USV Drone Control Dashboard 🌊⚓

Une interface web moderne et complète pour le contrôle et la surveillance de drones de surface autonomes (USV), développée avec **Flask** et **Tailwind CSS**.

## ✨ Fonctionnalités

- **Authentification complète** : Inscription, Connexion, Déconnexion.
- **Dashboard temps réel** : Interface inspirée du style "Crextio" avec coins arrondis et design épuré.
- **Télémétrie complète** :
    - État général (Online/Offline, Mode, Uptime)
    - Navigation (Vitesse, Cap, GPS, Carte interactive simulée)
    - Énergie (Batterie, Tension, Température interne)
    - Environnement (Qualité de l'eau, Météo)
    - Bathymétrie (Profondeur instantanée)
    - Caméra (Flux vidéo simulé et détection)
- **Gestion des missions** : Liste des tâches en cours et historique.
- **Alertes** : Système de notifications pour les événements critiques.

## 🛠️ Installation et Lancement

### Prérequis
- Python 3.8+
- pip (gestionnaire de paquets Python)

### Étapes rapides
1. **Extraire les fichiers** du projet.
2. **Lancer le script d'installation** (Linux/macOS) :
   ```bash
   ./run.sh
   ```
   *Ou manuellement :*
   ```bash
   pip install -r requirements.txt
   python app.py
   ```
3. **Accéder à l'application** : Ouvrez votre navigateur sur [http://localhost:5000](http://localhost:5000)

### Identifiants par défaut
- **Utilisateur** : `admin`
- **Mot de passe** : `admin123`

## 📂 Structure du Projet

- `app.py` : Point d'entrée principal, routes et simulation de données.
- `models.py` : Définition des modèles de base de données (Utilisateurs, Télémétrie).
- `auth.py` : Logique d'authentification.
- `templates/` : Fichiers HTML (Jinja2).
- `static/` : Assets (CSS, JS, Images).

---
Développé avec ❤️ pour la surveillance marine.
