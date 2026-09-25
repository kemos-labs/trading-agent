# Chapter 8 — Blockchain and Cryptocurrency Analysis

## Core idea
Blockchain as a new financial infrastructure: the decentralized ledger,
consensus mechanisms, smart contracts, DeFi, and how to analyze
cryptocurrency markets (technical/fundamental/sentiment).

## Blockchain basics
- **Distributed ledger**: a shared, decentralized database — every node
  holds a copy; no single point of failure.
- **Blocks**: transactions grouped into blocks, each linked to the previous
  via a cryptographic hash — immutability (altering one block requires
  rewriting all subsequent blocks).
- **Consensus**: Proof of Work (PoW) vs Proof of Stake (PoS) validate
  transactions and agree on ledger state.
- **Origins**: Bitcoin (2009, Satoshi Nakamoto) as peer-to-peer electronic
  cash; **Ethereum** added a Turing-complete scripting language for smart
  contracts and DApps.

## Finance applications
- **Smart contracts**: self-executing contracts with terms in code —
  automate and enforce agreements without intermediaries.
- **Tokenization**: real-world assets represented digitally — liquidity and
  access.
- **DeFi**: decentralized exchanges (DEXs), lending, yield farming — open
  access, no traditional institutions.
- Benefits: transparency, security, efficiency (fewer intermediaries, faster
  settlement), traceability.
- Challenges: scalability, PoW energy consumption, regulatory uncertainty,
  smart-contract vulnerabilities (irreversible transactions).

## Analyzing cryptocurrency markets
- **Technical**: price charts and volumes — patterns and trends.
- **Fundamental**: technology, team, ecosystem development.
- **Sentiment**: social media and news mood — a natural fit for NLP/ML
  (ch7).
- Crypto markets are notably volatile — high opportunity and high risk.

## Python angle
- Libraries: Web3.py (Ethereum interaction), PyTezos (Tezos);
  data/backtesting tools for crypto prices (CCXT-class APIs).

## Pitfalls
- Irreversibility: a mistake on-chain cannot be undone.
- Smart-contract bugs = lost funds; audit code.
- Regulatory frameworks still evolving; classification (security vs
  commodity) shifts.

## Bottom line
The frontier-topic chapter: blockchain mechanics and the three-part crypto
analysis approach (technical/fundamental/sentiment). The sentiment angle
reuses the NLP material from ch7; the volatility/risk discussion echoes
ch6.
