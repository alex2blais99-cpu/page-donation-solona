# 📊 Dashboard UI Preview

## Interface Layout

The AutoTrading Bot UI has 3 main tabs:

### 1. 📊 Dashboard Tab (Main View)

```
┌─────────────────────────────────────────────────────────────────┐
│  🚀 AutoTrading Bot - Solana                                    │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  [📊 Dashboard]  [💼 Wallets]  [📈 Trading]                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  📊 Dashboard — Projets & Liquidité                            │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ ID  │ Projet     │ Actif │ Liquidité (SOL) │ Valeur (CAD)│ │
│  ├─────┼────────────┼───────┼─────────────────┼─────────────┤ │
│  │  1  │ Projet 1   │  ✅   │     0.0000      │   0.00 $   │ │
│  │  2  │ Projet 2   │  ✅   │     0.0000      │   0.00 $   │ │
│  │  3  │ Projet 3   │  ✅   │     0.0000      │   0.00 $   │ │
│  │  4  │ Projet 4   │  ✅   │     0.0000      │   0.00 $   │ │
│  │  5  │ Projet 5   │  ✅   │     0.0000      │   0.00 $   │ │
│  │  6  │ Projet 6   │  ✅   │     0.0000      │   0.00 $   │ │
│  │  7  │ Projet 7   │  ✅   │     0.0000      │   0.00 $   │ │
│  │  8  │ Projet 8   │  ✅   │     0.0000      │   0.00 $   │ │
│  │  9  │ Projet 9   │  ✅   │     0.0000      │   0.00 $   │ │
│  │ 10  │ Projet 10  │  ✅   │     0.0000      │   0.00 $   │ │
│  │ 11  │ Projet 11  │  ✅   │     0.0000      │   0.00 $   │ │
│  │ 12  │ Projet 12  │  ✅   │     0.0000      │   0.00 $   │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  Auto-refresh: ⟳ Every 1 second                                │
└─────────────────────────────────────────────────────────────────┘
```

**Features:**
- ✅ Displays all 12 projects
- ✅ Real-time liquidity in SOL
- ✅ CAD value conversion
- ✅ Active/Inactive status with checkmark
- ✅ Auto-refreshes every second
- ✅ Clean table layout

### 2. 💼 Wallets Tab

```
┌─────────────────────────────────────────────────────────────────┐
│  💼 Gestion des Wallets                                         │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ ID  │ Projet     │ Wallet                             │ ☑ │ │
│  ├─────┼────────────┼────────────────────────────────────┼───┤ │
│  │  1  │ Projet 1   │ 11111111111111111111111111111111  │ ✓ │ │
│  │  2  │ Projet 2   │ 22222222222222222222222222222222  │ ✓ │ │
│  │ ... │ ...        │ ...                                │...│ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  [Project Name Input]  [Ajouter Projet]                        │
└─────────────────────────────────────────────────────────────────┘
```

**Features:**
- ✅ Project management
- ✅ Enable/disable checkboxes
- ✅ Wallet address display
- ✅ Add new projects
- ✅ Auto-refreshes

### 3. 📈 Trading Tab

```
┌─────────────────────────────────────────────────────────────────┐
│  📈 Trading Bots                                                │
│                                                                 │
│  Bot: Bot Scalper (scalping)                                   │
│  [Start Bot]                                                    │
│                                                                 │
│  Bot: Bot Trend (trend_following)                              │
│  [Start Bot]                                                    │
│                                                                 │
│  Bot: Bot Mean Reversion (mean_reversion)                      │
│  [Bot Disabled]                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Features:**
- ✅ Multiple trading bots
- ✅ Strategy display
- ✅ Start/Stop controls
- ✅ Enabled/Disabled status

## Color Scheme (from styles.css)

- **Background:** Dark theme (#1e1e1e)
- **Text:** White (#ffffff)
- **Buttons:** Blue (#0066cc)
- **Tables:** Dark gray (#2d2d2d)
- **Borders:** Medium gray (#444444)
- **Selected items:** Blue highlight (#0066cc)

## Key Dashboard Features

1. **Real-time Updates:** Dashboard refreshes every second
2. **Zero Initial State:** All projects start at 0.0000 SOL
3. **Dynamic Pricing:** SOL/CAD conversion updates automatically
4. **Project Status:** Visual indicators (✅/❌) for enabled projects
5. **Scalable:** Ready to handle liquidity injection when implemented

## Data Flow

```
wallets.json
    ↓
WalletManager.load()
    ↓
LiquidityTracker(projects)  ←→  PriceFeed
    ↓                                ↓
Dashboard Display (Table)    →  SOL → CAD conversion
    ↓
Auto-refresh (1s timer)
```

## Future Enhancements

- 📈 Charts for liquidity trends
- 🧾 Transaction history
- 🔄 Real-time Solana blockchain sync
- 📊 Analytics and reporting
- 🪙 Multi-token support
- 📦 CSV export functionality
