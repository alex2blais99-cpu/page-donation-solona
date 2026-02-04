# 💰 Distribution Professionnelle - Guide d'Utilisation

## Vue d'ensemble

Le système de distribution professionnelle permet de distribuer des montants de SOL entre plusieurs wallets de manière équitable ou selon des pourcentages personnalisés.

## Fonctionnalités

### 1. Distribution Équitable

Distribue un montant total de manière égale entre tous les wallets sélectionnés.

**Exemple:**
- Montant: 100 SOL
- Wallets sélectionnés: 3
- Résultat: 33.3333 SOL par wallet (+ reste au premier wallet)

**Comment utiliser:**
1. Sélectionnez "Distribution Équitable"
2. Entrez le montant total à distribuer
3. Cochez les wallets à inclure
4. Cliquez sur "Calculer Distribution" pour voir l'aperçu
5. Cliquez sur "Exécuter Distribution" pour finaliser

### 2. Distribution par Pourcentage

Distribue un montant selon des pourcentages spécifiques pour chaque wallet.

**Exemple:**
- Montant: 1000 SOL
- Wallet 1: 50% = 500 SOL
- Wallet 2: 30% = 300 SOL
- Wallet 3: 20% = 200 SOL

**Comment utiliser:**
1. Sélectionnez "Distribution par Pourcentage"
2. Entrez le montant total
3. Cochez les wallets à inclure
4. Ajustez les pourcentages (doivent totaliser 100%)
5. Cliquez sur "Calculer Distribution" pour voir l'aperçu
6. Cliquez sur "Exécuter Distribution" pour finaliser

**Note:** Lorsque vous passez en mode pourcentage, les pourcentages sont automatiquement calculés de manière équitable comme point de départ.

### 3. Sélection Multiple

**Boutons pratiques:**
- **✓ Tout Sélectionner**: Sélectionne tous les wallets actifs
- **✗ Tout Désélectionner**: Désélectionne tous les wallets

### 4. Aperçu en Temps Réel

Le tableau d'aperçu se met à jour automatiquement et affiche:
- Nom du projet
- Adresse du wallet
- Montant qui sera distribué (SOL)
- Pourcentage du total

## Interface

```
┌─────────────────────────────────────────────────────────────┐
│ 💰 Distribution Professionnelle                            │
├─────────────────────────────────────────────────────────────┤
│ [Montant total (SOL): 100.0000 SOL]                       │
│                                                             │
│ Mode de Distribution:                                       │
│  ⦿ Distribution Équitable (égale entre tous)               │
│  ○ Distribution par Pourcentage (%)                        │
│                                                             │
│ Sélection des Wallets:                                     │
│  [✓ Tout Sélectionner] [✗ Tout Désélectionner]           │
│  ☑ Projet 1 (#1)        [ 33.33 %]                        │
│  ☑ Projet 2 (#2)        [ 33.33 %]                        │
│  ☑ Projet 3 (#3)        [ 33.34 %]                        │
│                                                             │
│ Aperçu de la Distribution:                                 │
│  ┌────────────────────────────────────────────────────┐   │
│  │ Projet | Wallet | Montant (SOL) | Pourcentage (%) │   │
│  ├────────────────────────────────────────────────────┤   │
│  │ Proj 1 │ 111... │    33.3334    │     33.33       │   │
│  │ Proj 2 │ 222... │    33.3333    │     33.33       │   │
│  │ Proj 3 │ 333... │    33.3333    │     33.33       │   │
│  └────────────────────────────────────────────────────┘   │
│  Total: 100.0000 SOL                                       │
│                                                             │
│  [📊 Calculer Distribution] [✅ Exécuter Distribution]     │
└─────────────────────────────────────────────────────────────┘
```

## Validation

### Distribution Équitable
- ✅ Vérifie qu'au moins 1 wallet est sélectionné
- ✅ Vérifie que le montant est > 0
- ✅ Gère les restes d'arrondi (ajoutés au premier wallet)

### Distribution par Pourcentage
- ✅ Vérifie que les pourcentages totalisent 100%
- ✅ Vérifie qu'aucun pourcentage n'est négatif
- ✅ Vérifie qu'aucun pourcentage ne dépasse 100%
- ✅ Gère les arrondis automatiquement

## Exemples d'Utilisation

### Cas 1: Distribution Simple
```
Montant: 1000 SOL
Wallets: 5 sélectionnés
Mode: Équitable
Résultat: 200 SOL par wallet
```

### Cas 2: Distribution Pondérée
```
Montant: 10000 SOL
Mode: Pourcentage
- Wallet Principal: 60% = 6000 SOL
- Wallet Secondaire: 25% = 2500 SOL
- Wallet Reserve: 15% = 1500 SOL
```

### Cas 3: Distribution Partielle
```
Montant: 500 SOL
Total wallets: 12
Wallets sélectionnés: 3 (seulement les actifs)
Mode: Équitable
Résultat: 166.6667 SOL par wallet sélectionné
```

## Conseils

1. **Prévisualisez toujours** avant d'exécuter pour vérifier les montants
2. **Utilisez le mode équitable** pour une distribution rapide et juste
3. **Utilisez le mode pourcentage** quand vous avez des besoins spécifiques
4. **Vérifiez les adresses** dans l'onglet Paramètres avant distribution
5. **Le total est conservé** - aucune perte de SOL dans les arrondis

## Formules

**Distribution Équitable:**
```
Montant par wallet = Montant total ÷ Nombre de wallets
Reste = Montant total - (Montant par wallet × Nombre de wallets)
Premier wallet reçoit = Montant par wallet + Reste
```

**Distribution par Pourcentage:**
```
Montant pour wallet X = Montant total × (Pourcentage X ÷ 100)
```

## Sécurité

- ✅ Confirmation requise avant exécution
- ✅ Aperçu détaillé avant validation
- ✅ Validation des montants et pourcentages
- ✅ Historique dans le Dashboard (mise à jour de la liquidité)

## Support

Pour toute question sur la distribution:
1. Vérifiez que les wallets sont correctement configurés (⚙️ Paramètres)
2. Assurez-vous que les wallets sont activés (💼 Wallets)
3. Consultez le Dashboard (📊) pour voir les montants distribués
