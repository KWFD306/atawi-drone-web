#!/bin/bash
echo "🚀 Installation des dépendances..."
pip install -r requirements.txt

echo "🗄️ Initialisation de la base de données..."
python3 -c "from app import app, init_db; init_db()"

echo "✅ Prêt ! Lancement de l'application sur http://localhost:5000"
echo "🔑 Compte admin par défaut : admin / admin123"
python3 app.py
