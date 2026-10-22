# NullCart: Embeddable noncustodial crypto checkout for static websites

Status: Concept / not implemented | Date: 2026-10-22 | Circuit Drift Labs

## Executive overview
Embeddable noncustodial crypto checkout for static websites. A mobile-first, local-first project that favors portable data, direct payment relationships, transparent fees and optional pseudonymity.

## Problem and target users
Merchants need a minimal payment UI without registering with a centralized checkout provider.

## How it works (user journey)
Merchant embeds a JS widget and declarative product configuration. Cart constructs invoice/payment request and checks payment status through external blockchain RPC or compatible wallet protocol. Show network, token, address and fee before approval. Payment confirmation does not by itself trigger trustworthy digital delivery from a static site.

## Disruptive value proposition
Unbundles checkout from hosted ecommerce accounts and enables portable, independently hosted payment pages.

## Revenue model and economics
Open-source basic widget; $29 premium merchant configuration kit; $99 multi-storefront integration license; optional audited fee router after demand. Browser code alone cannot securely enforce per-transaction fees.

These are illustrative gross revenue scenarios, not forecasts. Subtract processing costs, chain fees, refunds, support, acquisition and taxes. Test willingness to pay before investing in sophisticated protocol fees.

## Why the initial build is relatively small / technical architecture
Framework-agnostic TypeScript library plus web component, Vite demo, chain adapters, QR generation, signed config and test vectors. Reuse GhostPay invoice-schema, chain-adapters and address-safety; do not expose secrets in browser bundles.

Scope the first release to a browser-only PWA or static exporter. A browser cannot keep server secrets or privately validate subscription entitlements. Smart contracts, public RPC nodes, hosted APIs and wallet providers are external dependencies, even when the frontend is static.

## Step-by-step development and launch game plan
MVP: embed script, cart UI, invoice generation, copy/QR, chain selection, transaction reference verification and local receipts. Next: accessibility, plugin API, testnet integration, downloadable docs, paid themes. Only then evaluate audited protocol fee routing.

## QA, security and release gates
Test fake confirmations, malicious merchant configuration, RPC outage, chain ID mismatch, token decimal precision, reorgs, wallet rejection, CORS failures, XSS and browser storage. Payments require on-chain confirmation or trustworthy external evidence.

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
