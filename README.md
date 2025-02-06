# Payload Generator

Un générateur de payloads configurable pour les commandes WCS, avec validation et génération de lots.

## État du Projet

### Complété ✅
- Structure de base du repository
- Implémentation des Data Classes (Payload models)
- Schémas de validation
- Configuration des codes INSEE

### En Cours 🚧
- Mise en place des tests unitaires (TDD)
- Implémentation de la génération basique de payloads

## Fonctionnalités Prévues

- [ ] **Validation des Payloads**
  - Validation via schémas
  - Vérification des codes INSEE
  - Validation des types de données
  - Messages d'erreur détaillés

- [ ] **Génération de Payloads**
  - Génération unitaire
  - Génération par lots
  - Support des templates

- [ ] **Formats de Sortie**
  - JSON (format raw)
  - Liste de dictionnaires Python
  - Fichiers exportables
  - Format compatible Postman

## Roadmap

### Phase 1: Fondations & Tests
- [x] Structure du projet
- [x] Data Classes & Validators
- [ ] Tests unitaires (objectif: 70% coverage)
- [ ] Tests d'intégration basiques
- [ ] Documentation des tests

### Phase 2: Génération & Validation
- [ ] Implémentation de la génération basique
- [ ] Validation des payloads
- [ ] Gestion des erreurs
- [ ] Tests des validateurs

### Phase 3: Fonctionnalités Avancées
- [ ] Génération par lots
- [ ] Templates configurables
- [ ] Export multi-formats
- [ ] CLI basique

### Phase 4: Optimisations
- [ ] Interface CLI avancée
- [ ] Amélioration de la performance
- [ ] Documentation complète
- [ ] Exemples d'utilisation

## Installation

```bash
# Prochainement
```

## Utilisation

```python
# Exemples à venir
```

## Tests

```bash
# Lancement des tests
pytest

# Avec coverage
pytest --cov=payload_generator
```

## Contribution

Les contributions sont les bienvenues ! Consultez le fichier CONTRIBUTING.md (à venir) pour plus de détails.