# Snirium - Commande et Surveillance d'un Robot

## Table des Matières
- Aperçu du Projet
- Fonctionnalités
- Structure du Projet
- Prérequis
- Installation
- Utilisation
- Licence

---

## Aperçu du Projet

Snirium est un projet qui permet de contrôler et de surveiller un robot en temps réel via une application mobile. Ce projet est conçu pour envoyer des commandes au robot et recevoir des informations sur son état. Il est divisé en deux parties :
- **Application mobile** développée avec React Native pour envoyer des commandes au robot.
- **Programme robotique** en Python pour gérer les capteurs, moteurs et la communication réseau.

## Fonctionnalités

- **Contrôle du robot en temps réel** : Envoi de commandes pour diriger le robot (avancer, reculer, tourner, etc.).
- **Affichage de l’état du robot** : L'application affiche les informations provenant des capteurs (distance, angle, etc.).
- **Serveur TCP** pour la communication entre l'application mobile et le robot.

## Structure du Projet

- `code_source/mobile` : Contient le code de l'application mobile React Native.
- `code_source/robot` : Contient le code Python pour la gestion des capteurs et moteurs du robot.

## Prérequis

- **Node.js** et **React Native** pour exécuter l'application mobile.
- **Python 3.x** pour le programme robotique.
- Modules Python requis : `socket`, `json`, etc. (Installez-les en utilisant `pip install <nom_module>` si nécessaire)

## Installation

### Cloner le Dépôt
```bash
git clone https://github.com/RimMaths/Snirium.git
cd Snirium

### Partie Mobile

Accédez au dossier de l'application mobile :
cd code_source/mobile

Installez les dépendances avec npm :
npm install
Partie Robot

Accédez au dossier du programme robotique :
cd code_source/robot

Installez les modules Python requis (si nécessaire) :
pip install -r requirements.txt  # Créez ce fichier si nécessaire avec les dépendances

###  Utilisation
Démarrer l'Application Mobile
Dans le dossier code_source/mobile, lancez l'application avec :
npm start
Suivez les instructions pour exécuter l'application sur un émulateur ou un appareil physique.

###  Démarrer le Programme du Robot
Dans le dossier code_source/robot, exécutez le programme principal en Python :
python main.py
Contrôle du Robot
Utilisez l'application mobile pour envoyer des commandes de mouvement au robot. Les informations du robot (par exemple, distance mesurée, angle) s'affichent dans l'interface.

Licence
Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.
