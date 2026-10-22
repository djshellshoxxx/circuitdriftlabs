# BlockReceipt: Portable, independently verifiable blockchain payment receipts

Status: Concept / not implemented | Date: 2026-10-22 | Circuit Drift Labs

## Executive overview
Portable, independently verifiable blockchain payment receipts. A mobile-first, local-first project that favors portable data, direct payment relationships, transparent fees and optional pseudonymity.

## Problem and target users
Payment screenshots can be fabricated; merchants need portable proof of settlement without granting a payment processor control of records.

## How it works (user journey)
Payer enters chain, transaction hash, intended recipient and amount. Browser queries a user-selectable RPC, verifies chain ID, confirmation status, asset contract, recipient, amount and log semantics, and generates a signed, downloadable JSON/PDF receipt. A verifier independently rechecks the chain; no claim of real-world delivery is implied.

## Disruptive value proposition
Direct payment receipts challenge proprietary processor dashboards and platform-controlled transaction histories.

## Revenue model and economics
Free local verification; $9 downloadable merchant receipt pack; $19/month reconciliation/export service on an appropriate commercial host; paid branded receipt templates. Example 100 pack sales × $9 = $900 gross, not recurring.

These are illustrative gross revenue scenarios, not forecasts. Subtract processing costs, chain fees, refunds, support, acquisition and taxes. Test willingness to pay before investing in sophisticated protocol fees.

## Why the initial build is relatively small / technical architecture
PWA TypeScript/Vite, viem or ethers, chain allowlist, QR generator, WebCrypto, local PDF export. Reuse GhostPay chain adapters, tx-review and address-safety after independent tests; no custody.

Scope the first release to a browser-only PWA or static exporter. A browser cannot keep server secrets or privately validate subscription entitlements. Smart contracts, public RPC nodes, hosted APIs and wallet providers are external dependencies, even when the frontend is static.

## Step-by-step development and launch game plan
Milestone 1: Ethereum Sepolia ERC20/native verification and receipt schema. Milestone 2: multi-RPC agreement, finality handling, downloadable signed receipts. Milestone 3: merchant batch reconciliation, testnets, user trials and paid templates.

## QA, security and release gates
Tests: reorgs, wrong chain, wrong token, event spoofing, transaction reverted, ERC20 transfer variants, wrong payee, confirmations, RPC disagreement, replay and malicious QR. Never present an unconfirmed transaction as final.

Require testnet end-to-end testing, repeatable builds, mobile accessibility, documented trust assumptions, and no known critical security findings before real-value usage.

## Connections to existing Circuit Drift Labs work
GhostPay (djshellshoxxx/GhostPay) has candidate invoice-schema, chain-adapters, core-crypto, tx-review and address-safety packages. Its README states that mainnet is disabled, contracts are not deployed and no independent audit has occurred. Treat these as experimental components, not trusted production dependencies. P2P-offramp may share future noncustodial payment and settlement primitives, but integration requires a code-level review of its current state.

## Hosting and operational model
GitHub Pages is suitable for noncommercial demonstrations and project documentation, but GitHub's terms disallow using it primarily for ecommerce/SaaS. Use an alternative static host that permits commercial activity for paid deployment. No private keys, secrets or merchant credentials should be committed to static bundles.

## Future roadmap
1. Ship narrow MVP and gather five real user trials.
2. Add payment verification and robust error recovery.
3. Validate first paid transaction or template purchase.
4. Improve privacy, portability, auditing and optional decentralized publishing.
5. Add cross-product integrations only after explicit security review.
