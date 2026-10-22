# SplitFree — Noncustodial Group Expense Settlement

Status: Concept and implementation plan | Date: 2026-10-22 | Owner: Circuit Drift Labs

## Executive concept
A mobile-first, privacy-respecting service designed to reduce dependence on centralized intermediaries. Start with a narrow, testable MVP and validate paying demand before adding advanced decentralization.

## Problem and target users
Shared bills are difficult to audit, expense platforms collect social/financial metadata, and people are pushed toward one payment provider.

## How the product works
Mobile groups created via invite QR; members record payments in integer minor currency units; deterministic per-member balances and a debt-minimization settlement plan; generate external Lightning/crypto payment requests or cash instructions. Payment status is verified from wallet callbacks where available, otherwise marked manually and explicitly unverified.

## Disruptive mechanism
Portable user data, optional pseudonymity, direct participant relationships and transparent pricing reduce intermediary lock-in. The degree of decentralization depends on implementation: a hosted MVP is not automatically censorship-resistant or anonymous.

## Monetization and example economics
Free unlimited small groups; $2/month recurring expense schedules; $10/month clubs with export, permissions and audit trail; $29/month white-label deployment. Example 100 clubs at $10 = $1,000 monthly gross, not profit.

Gross revenue scenarios are hypothetical; deduct processing fees, refunds, hosting, acquisition, support, taxes and other operating costs. Validate conversion before forecasting profit.

## Technical architecture and why the MVP is manageable
PWA React/TypeScript; FastAPI or Node; SQLite/Postgres; QR generation; optional wallet integrations. Tables groups, members, expenses, allocations, settlements, payment_evidence, subscriptions. No custodial balances.

A mobile PWA avoids maintaining separate native apps. Reuse mature cryptographic, billing, QR and storage libraries; avoid inventing primitives. The feature-limited MVP is relatively simple, but security, fraud resistance and dependable operations require additional time.

## Build, launch and customer-acquisition plan
Week 1: validate splits, currencies, partial shares, rounding and refund edge cases; implement group invitation, expense entry and immutable change log. Week 2: settlement minimization, QR and exports, recurring templates, billing and deployment. Pilot 5 shared households and 3 clubs; measure monthly retention and paid conversion.

## Security, quality assurance and acceptance criteria
Unit/property tests for sum-zero invariant, rounding, negative/zero expenses, repeated imports, idempotent updates, authorization, concurrency and backups. Never claim an external transfer settled without independent evidence.

Release gate: critical paths covered by automated tests, successful staging end-to-end walkthrough, documented backups/recovery, abuse controls, accessibility/mobile usability review, and no known critical security defects.

## Post-launch roadmap
1. Interview early users and measure activation, repeat use, support burden and payment conversion.
2. Improve reliability and automation before adding speculative features.
3. Add exportability, optional self-hosting/federation and advanced privacy in response to actual demand.
4. Publish a transparent pricing and data-retention policy; review local financial, consumer and privacy obligations where applicable.
