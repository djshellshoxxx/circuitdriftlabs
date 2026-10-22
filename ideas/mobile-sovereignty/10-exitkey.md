# ExitKey — Portable Cryptographic Reputation

Status: Concept and implementation plan | Date: 2026-10-22 | Owner: Circuit Drift Labs

## Executive concept
A mobile-first, privacy-respecting service designed to reduce dependence on centralized intermediaries. Start with a narrow, testable MVP and validate paying demand before adding advanced decentralization.

## Problem and target users
Reviews and transaction histories are locked inside platforms, making it difficult to switch services without losing earned trust.

## How the product works
Users hold keys and export signed attestations from counterparties; relying services validate issuer signatures and inspect issuer credibility. Offer optional W3C VC 2.0 compatibility and revocation/status. Show provenance rather than a universal trust score. Signed statements do not establish truth; prevent Sybil gaming with contextual transaction evidence and reputation weighting.

## Disruptive mechanism
Portable user data, optional pseudonymity, direct participant relationships and transparent pricing reduce intermediary lock-in. The degree of decentralization depends on implementation: a hosted MVP is not automatically censorship-resistant or anonymous.

## Monetization and example economics
Individuals issue/store credentials for free; merchants $9/month for issuance; marketplaces $29/month for verification console; metered verification API and hosted white-label integrations. Example 100 marketplaces at $29 = $2,900/month gross.

Gross revenue scenarios are hypothetical; deduct processing fees, refunds, hosting, acquisition, support, taxes and other operating costs. Validate conversion before forecasting profit.

## Technical architecture and why the MVP is manageable
TypeScript PWA, WebCrypto/maintained Ed25519 library, JSON credentials, issuer registry, Postgres and API. Separate private keys from server; device backup/recovery and key rotation are essential.

A mobile PWA avoids maintaining separate native apps. Reuse mature cryptographic, billing, QR and storage libraries; avoid inventing primitives. The feature-limited MVP is relatively simple, but security, fraud resistance and dependable operations require additional time.

## Build, launch and customer-acquisition plan
Phase 1: define credential schema, key lifecycle, signatures, verification and exports. Phase 2: issue credentials after verified test transactions, revocation/status, merchant console and API. Phase 3: pilot with two small marketplaces; track credential issuance, third-party verification and false-claim reports. Later add standards interoperability.

## Security, quality assurance and acceptance criteria
Test tampering, signature substitution, replay, issuer spoofing, expiry, revoked credentials, key rotation, lost devices, malicious attestations and privacy correlation. Reference: https://www.w3.org/TR/vc-data-model-2.0/ .

Release gate: critical paths covered by automated tests, successful staging end-to-end walkthrough, documented backups/recovery, abuse controls, accessibility/mobile usability review, and no known critical security defects.

## Post-launch roadmap
1. Interview early users and measure activation, repeat use, support burden and payment conversion.
2. Improve reliability and automation before adding speculative features.
3. Add exportability, optional self-hosting/federation and advanced privacy in response to actual demand.
4. Publish a transparent pricing and data-retention policy; review local financial, consumer and privacy obligations where applicable.
