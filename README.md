# 🚀 AutoTrading Bot - Solana Donation Tracker

Application de trading automatisé avec suivi des donations Solana et gestion de liquidité.

## 📦 Structure du Projet

```
page-donation-solona/
├── core/                      # Modules principaux
│   ├── wallet_manager.py      # Gestion des wallets et projets
│   ├── wallet_balance.py      # Gestion des balances
│   ├── liquidity_tracker.py   # Suivi de liquidité (nouveau)
│   ├── injection_engine.py    # Injection de liquidité
│   ├── price_feed.py          # Flux de prix SOL/CAD
│   ├── risk_controller.py     # Contrôle des risques
│   └── solana_validator.py    # Validation d'adresses Solana
│
├── ui/                        # Interface utilisateur
│   ├── ui_qt.py              # Interface principale
│   ├── ui_dashboard.py       # Onglet Dashboard (nouveau)
│   ├── ui_wallets.py         # Onglet Wallets
│   └── styles.css            # Styles CSS
│
├── trading/                   # Modules de trading
│   ├── main.py               # Bot de trading principal
│   ├── config.py             # Configuration
│   ├── data_feed.py          # Flux de données marché
│   ├── strategy.py           # Stratégies de trading
│   ├── broker.py             # Exécution des trades
│   └── risk.py               # Gestion des risques
│
├── launcher.py               # Point d'entrée principal
├── debug_checks.py           # Tests de vérification
├── install.py                # Installation des dépendances
├── requirements.txt          # Dépendances Python
└── wallets.json             # Configuration des 12 projets
```

## 🎯 Fonctionnalités

### 📊 Dashboard
- Affiche les **12 projets** configurés
- Liquidité en temps réel (SOL)
- Valeur en CAD
- Statut activé/désactivé
- Rafraîchissement automatique

### 💼 Wallets
- Gestion des projets
- Ajout/modification de projets
- Activation/désactivation
- Gestion des adresses Solana

### 📈 Trading
- Bots de trading automatisés
- Stratégies multiples (scalping, trend following, mean reversion)
- Gestion des risques
- Suivi des positions

## 🔧 Installation

1. **Installer les dépendances:**
```bash
python install.py
```

2. **Vérifier l'installation:**
```bash
python debug_checks.py
```

3. **Lancer l'application:**
```bash
python launcher.py
```

## 📝 Configuration

### wallets.json
Fichier de configuration des 12 projets avec:
- ID unique
- Nom du projet
- Adresse wallet Solana
- Statut (enabled/disabled)

### Exemple:
```json
{
  "projects": [
    {
      "id": 1,
      "name": "Projet 1",
      "wallet": "11111111111111111111111111111111",
      "enabled": true
    }
  ]
}
```

## 🎨 Interface Utilisateur

L'interface comprend 3 onglets:
1. **📊 Dashboard** - Vue d'ensemble des projets et liquidités
2. **💼 Wallets** - Gestion des wallets et projets
3. **📈 Trading** - Contrôle des bots de trading

## ✅ Imports Corrigés

Tous les imports ont été restructurés pour suivre la nouvelle architecture:

### UI Modules → Core
```python
from core.wallet_manager import WalletManager
from core.liquidity_tracker import LiquidityTracker
from core.price_feed import PriceFeed
```

### UI Modules → Trading
```python
from trading.main import TradingBot
from trading.config import BOTS
```

### Trading Modules (relative imports)
```python
from .config import START_PRICE
from .data_feed import MarketDataFeed
```

### Core Modules (relative imports)
```python
from .wallet_manager import WalletManager
```

## 🧪 Tests

Exécuter les vérifications:
```bash
python debug_checks.py
```

Le script vérifie:
- ✅ Tous les modules core
- ✅ Tous les modules trading
- ✅ Modules UI (si environnement graphique disponible)
- ✅ Chargement des 12 projets
- ✅ Initialisation des liquidités à 0.0 SOL
- ✅ Prix SOL/CAD
- ✅ Validation Solana
- ✅ Configuration des bots

## 🔜 Prochaines Étapes

- [ ] Graphique par projet
- [ ] Historique des injections
- [ ] Synchronisation injection → dashboard
- [ ] Mode réel Solana
- [ ] Export CSV

## 📄 Licence

MIT
