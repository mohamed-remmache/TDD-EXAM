# Mars Rover Simulation

Ce projet est une simulation de la navigation de robots sur une grille rectangulaire représentant un plateau martien. Les robots suivent des commandes simples pour se déplacer et tourner dans différentes directions, tout en respectant les limites de la grille.

---

## Table des matières

- [Description](#description)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Fonctionnalités](#fonctionnalités)
- [Tests](#tests)
- [Structure du projet](#structure-du-projet)

---

## Description

Ce projet implémente un système permettant à un rover de :
- Se déplacer sur une grille.
- Tourner à gauche ou à droite.
- Respecter les limites de la grille.
- Signaler les commandes invalides.

Les rovers suivent des commandes fournies sous forme de chaînes de caractères (`L`, `R`, `M`), où :
- `L` : Tourner à gauche.
- `R` : Tourner à droite.
- `M` : Avancer d'une unité dans la direction actuelle.

---

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/mohamed-remmache/TDD-EXAM
   cd TDD-EXAM
