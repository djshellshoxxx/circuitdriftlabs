# PaySplit: Noncustodial on-chain royalty and revenue splitting

Status: Concept / not implemented | Date: 2026-10-22 | Circuit Drift Labs

## Executive overview
Noncustodial on-chain royalty and revenue splitting. A mobile-first, local-first project that favors portable data, direct payment relationships, transparent fees and optional pseudonymity.

## Problem and target users
Creators and collaborators rely on agencies or centralized payment administrators to divide shared earnings.

## How it works (user journey)
Creator configures recipient addresses and basis-point allocations summing to 10,000. A static frontend displays and deploys an audited, immutable splitter contract; payers send funds and recipients withdraw or receive shares according to contract semantics. Provide transparent fee previews and public audit history.

## Disruptive value proposition
Automates revenue distribution without a platform custody account and makes allocations publicly inspectable.

## Revenue model and economics
One-time deployment/configuration fee, or explicitly disclosed contract fee where justified. Example $100,000/month routed at 0.25% = $250 gross before gas and support; no guaranteed volume.

These are illustrative gross revenue scenarios, not forecasts. Subtract processing costs, chain fees, refunds, support, acquisition and taxes. Test willingness to pay before investing in sophisticated protocol fees.

## Why the initial build is relatively small / technical architecture
Vite/React, wallet connector, viem, audited payment-splitter contracts, optional block explorer links. Never ship bespoke custody logic without specialist review. Distinct from GhostPay stealth routing; explore optional privacy-aware payouts without assuming unlinkability.

Scope the first release to a browser-only PWA or static exporter. A browser cannot keep server secrets or privately validate subscription entitlements. Smart contracts, public RPC nodes, hosted APIs and wallet providers are external dependencies, even when the frontend is static.

## Step-by-step development and launch game plan
Phase 1: review existing splitter contracts, licenses, audits and chain support. Phase 2: testnet deploy UI, share validation, gas estimation and signed config exports. Phase 3: contract tests/fuzzing, failure scenarios, testnet creator pilot. Phase 4: independent audit and explicit mainnet approval.

## QA, security and release gates
Invariants: shares exactly 100%, no overwithdrawal, no unauthorized recipient mutation, conservation of funds, dust accounting, ERC20 quirks, reentrancy, fee accounting, unsupported tokens, chain switching and lost-key recovery. Avoid promising privacy on public ledgers.

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
