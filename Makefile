# Variables
PYTHON=python3
MANAGE=$(PYTHON) manage.py
VENV=.venv
PIP=$(VENV)/bin/pip
PY=$(VENV)/bin/python

# Par défaut
.DEFAULT_GOAL := help

## ======================
## 📦 Environnement
## ======================

venv: ## Crée l'environnement virtuel
	$(PYTHON) -m venv $(VENV)

## Commande pour lancer le venv:
## source .venv/bin/activate

install: ## Installe les dépendances
	$(PIP) install -r requirements.txt

freeze: ## Met à jour requirements.txt
	$(PIP) freeze > requirements.txt

## ======================
## 🚀 Django
## ======================

run: ## Lance le serveur Django
	$(PY) manage.py runserver

migrate: ## Applique les migrations
	$(PY) manage.py migrate

migration: ## Crée les migrations
	$(PY) manage.py makemigrations

user: ## Crée un super utilisateur
	$(PY) manage.py createsuperuser

shell: ## Ouvre le shell Django
	$(PY) manage.py shell

test: ## Lance les tests
	$(PY) manage.py test

## ======================
## 🧹 Qualité & nettoyage
## ======================

lint: ## Lint du projet (flake8)
	$(VENV)/bin/flake8

format: ## Formatage avec black
	$(VENV)/bin/black .

clean: ## Nettoie les fichiers temporaires
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

## ======================
## 📚 Aide
## ======================

help: ## Affiche l'aide
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "👉 %-20s %s\n", $$1, $$2}'
