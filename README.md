Module Gestion des Autorisations - Odoo 17

Ce projet est un module Odoo 17 pour gérer les autorisations des utilisateurs sur les différents modules de l’ERP. Il permet d’attribuer des niveaux d’accès spécifiques (lecture, écriture, administration) et de centraliser la gestion des droits de manière sécurisée et simple.

Fonctionnalités principales

Gestion des droits par utilisateur et module : lecture, écriture, administration.

Vues intuitives : formulaire pour chaque autorisation, liste pour filtrer et trier les droits.

Sécurité : contrôle d’accès basé sur les mécanismes natifs d’Odoo.

Historique : suivi des modifications sur les autorisations.

Déploiement Docker : conteneurs Odoo et PostgreSQL avec volumes pour la persistance des données.

Architecture technique

Backend : Python/Odoo ORM pour les modèles et règles métiers.

Frontend : XML pour les vues (formulaire, liste).

Base de données : PostgreSQL pour la persistance des informations utilisateurs et permissions.

Objectifs

Centraliser et automatiser la gestion des autorisations.

Faciliter l’administration et le suivi des droits.

Garantir la sécurité et l’intégrité des données.

Permettre l’extension du module sans impacter le système existant.
