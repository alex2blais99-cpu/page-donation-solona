# ⚙️ Paramètres - Guide d'Utilisation

## Vue d'ensemble

L'onglet Paramètres permet de gérer toutes les configurations de l'application, notamment les adresses des wallets, les noms des projets, et la suppression de projets.

## Fonctionnalités

### 1. Modifier un Projet

Permet de changer le nom et l'adresse du wallet d'un projet.

**Comment utiliser:**
1. Accédez à l'onglet "⚙️ Paramètres"
2. Trouvez le projet à modifier
3. Cliquez sur le bouton "✏️ Modifier"
4. Dans le dialogue:
   - Modifiez le **Nom du projet**
   - Modifiez l'**Adresse Wallet**
5. Cliquez sur "OK" pour sauvegarder

**Validation:**
- ✅ Le nom ne peut pas être vide
- ⚠️ L'adresse Solana est validée (format base58, 32-44 caractères)
- ⚠️ Une confirmation est demandée si l'adresse semble invalide

### 2. Supprimer un Projet

Permet de retirer complètement un projet de l'application.

**Comment utiliser:**
1. Trouvez le projet à supprimer
2. Cliquez sur le bouton "🗑️ Supprimer"
3. Confirmez la suppression dans le dialogue

**⚠️ Attention:**
- La suppression est **définitive**
- Toutes les données du projet sont perdues
- La liquidité associée sera perdue

### 3. Actualiser la Liste

Le bouton "🔄 Actualiser" permet de recharger la liste des projets depuis le fichier de configuration.

## Interface

```
┌─────────────────────────────────────────────────────────────┐
│ ⚙️ Paramètres de l'Application                             │
│ Modifier les adresses des wallets, renommer les projets    │
├─────────────────────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ ID │ Projet  │ Adresse Wallet        │ Actions │ Supp. │ │
│ ├────┼─────────┼───────────────────────┼─────────┼───────┤ │
│ │ 1  │ Proj 1  │ 11111111111111111111  │[✏️]     │[🗑️]  │ │
│ │ 2  │ Proj 2  │ 22222222222222222222  │[✏️]     │[🗑️]  │ │
│ │ 3  │ Proj 3  │ 33333333333333333333  │[✏️]     │[🗑️]  │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
│ [🔄 Actualiser]                                             │
└─────────────────────────────────────────────────────────────┘
```

## Dialogue de Modification

```
┌─────────────────────────────────────────┐
│ Modifier Projet #1                      │
├─────────────────────────────────────────┤
│ Nom du projet:                          │
│ [Projet 1 - Production          ]      │
│                                         │
│ Adresse Wallet:                         │
│ [Dm8rWW4PwVv7qLgZDNs2W9sBh...]        │
│                                         │
│          [Annuler]      [OK]            │
└─────────────────────────────────────────┘
```

## Format des Adresses Solana

### Adresse Valide
Une adresse Solana valide doit:
- Être encodée en base58
- Contenir entre 32 et 44 caractères
- Utiliser uniquement les caractères: `1-9A-HJ-NP-Za-km-z`
- Ne **PAS** contenir: `0`, `O`, `I`, `l` (pour éviter confusion)

### Exemples d'Adresses Valides
```
Dm8rWW4PwVv7qLgZDNs2W9sBhnrQGTZY3PJ3qvCwKCp7
7EYnhQoR9YM3N7UoaKRoA44Uy8JeaZV3qyouSsXx
EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
```

### Validation Interactive
- ✅ Si l'adresse est valide: acceptée directement
- ⚠️ Si l'adresse semble invalide: demande de confirmation
- ❌ Si le champ est vide: accepté (peut être modifié plus tard)

## Bonnes Pratiques

### 1. Nommage des Projets
```
✅ Bon:
- "Projet Production"
- "Wallet Principal"
- "Reserve - Team"
- "Marketing Q1"

❌ À éviter:
- "" (vide)
- "Projet" (trop générique)
- "asdfgh" (non descriptif)
```

### 2. Gestion des Adresses
- ✅ **Vérifiez** toujours l'adresse avant de la sauvegarder
- ✅ **Copiez-collez** depuis votre wallet (évite les erreurs)
- ✅ **Testez** avec un petit montant d'abord
- ⚠️ **Ne partagez jamais** vos clés privées

### 3. Avant de Supprimer
- ⚠️ Vérifiez qu'il n'y a pas de liquidité active
- ⚠️ Notez l'adresse du wallet ailleurs si nécessaire
- ⚠️ Assurez-vous que ce n'est pas une erreur

## Fichier de Configuration

Les modifications sont sauvegardées dans `wallets.json`:

```json
{
  "projects": [
    {
      "id": 1,
      "name": "Projet Production",
      "wallet": "Dm8rWW4PwVv7qLgZDNs2W9sBhnrQGTZY3PJ3qvCwKCp7",
      "enabled": true
    }
  ]
}
```

### Sauvegarde Automatique
- ✅ Chaque modification est **sauvegardée immédiatement**
- ✅ Le fichier `wallets.json` est **mis à jour automatiquement**
- ✅ Les autres onglets se **synchronisent** au prochain refresh

## Cas d'Usage

### Cas 1: Renommer un Projet
```
Avant: "Projet 1"
Action: Modifier → "Wallet Principal"
Après: "Wallet Principal"
Usage: Meilleure organisation et clarté
```

### Cas 2: Changer l'Adresse
```
Situation: Nouveau wallet créé
Action: 
  1. Modifier le projet
  2. Remplacer l'ancienne adresse
  3. Vérifier dans Distribution
Résultat: Les futures distributions iront au nouveau wallet
```

### Cas 3: Nettoyer les Projets
```
Situation: Trop de projets test
Action:
  1. Identifier les projets inutiles
  2. Supprimer un par un
  3. Actualiser la liste
Résultat: Interface plus propre
```

## Raccourcis et Astuces

1. **Double-vérification**: Toujours vérifier l'adresse après modification
2. **Sauvegarde externe**: Gardez une copie de vos adresses ailleurs
3. **Noms descriptifs**: Utilisez des noms qui expliquent le but du wallet
4. **Ordre logique**: Organisez vos projets de manière logique (production, test, reserve)

## Messages d'Erreur

### "Le nom du projet ne peut pas être vide"
- **Cause**: Vous avez effacé le nom
- **Solution**: Entrez un nom valide

### "L'adresse Solana semble invalide"
- **Cause**: Format d'adresse incorrect
- **Solution**: Vérifiez l'adresse ou cliquez "Oui" pour forcer

### "Confirmer la suppression"
- **Cause**: Mesure de sécurité
- **Action**: Cliquez "Yes" pour confirmer, "No" pour annuler

## Synchronisation

Les modifications dans Paramètres affectent:
- 📊 **Dashboard**: Met à jour les noms de projets
- 💰 **Distribution**: Utilise les nouvelles adresses
- 💼 **Wallets**: Reflète les changements

**Note**: Certains onglets ont un auto-refresh, d'autres nécessitent un changement d'onglet pour voir les modifications.

## Support

Pour toute question:
1. Vérifiez que votre adresse Solana est valide sur un explorateur
2. Assurez-vous que le fichier `wallets.json` n'est pas corrompu
3. Redémarrez l'application si nécessaire
