# ReceiptRebel — Crowdsourced Verified Price Intelligence

Status: Concept and implementation plan | Date: 2026-10-22 | Owner: Circuit Drift Labs

## Executive concept
A mobile-first, privacy-respecting service designed to reduce dependence on centralized intermediaries. Start with a narrow, testable MVP and validate paying demand before adding advanced decentralization.

## Problem and target users
Retailers know actual checkout prices while consumers lack comparable transaction-level evidence; hidden fees, shrinkflation and local price differences are difficult to detect.

## How the product works
Phone captures receipt; local redaction removes card fragments, names, loyalty IDs and other sensitive details; OCR extracts merchant/date/line items/taxes/fees. Normalize units, GTINs and promotions, deduplicate and score evidence quality. Publish aggregated price comparisons and historical trends rather than raw personal receipts.

## Disruptive mechanism
Portable user data, optional pseudonymity, direct participant relationships and transparent pricing reduce intermediary lock-in. The degree of decentralization depends on implementation: a hosted MVP is not automatically censorship-resistant or anonymous.

## Monetization and example economics
Free contributions and basic lookup; $3/month alerts; $5/month consumer history; $19/month researcher API; $99/month business API with aggregation thresholds. Example 50 business API accounts × $99 = $4,950/month gross only after meaningful coverage.

Gross revenue scenarios are hypothetical; deduct processing fees, refunds, hosting, acquisition, support, taxes and other operating costs. Validate conversion before forecasting profit.

## Technical architecture and why the MVP is manageable
PWA camera capture, Tesseract.js or OCR provider, Python normalization service, Postgres, item/merchant taxonomy, job queue and price API. Raw images should have short retention and explicit opt-in.

A mobile PWA avoids maintaining separate native apps. Reuse mature cryptographic, billing, QR and storage libraries; avoid inventing primitives. The feature-limited MVP is relatively simple, but security, fraud resistance and dependable operations require additional time.

## Build, launch and customer-acquisition plan
Week 1: receipt ingestion, redaction preview, OCR correction UI, merchant and item schema. Week 2: unit-price normalization, deduplication, aggregate comparisons, search and price charts. Pilot one region and product category; obtain hundreds of diverse receipts, measure extraction accuracy and retention. Add paid alerts and API after coverage thresholds.

## Security, quality assurance and acceptance criteria
Test OCR misreads, duplicate receipts, forged submissions, tax-included vs excluded prices, unit conversions, coupons, returns, personal-data redaction and reidentification through sparse aggregates. Establish provenance and minimum sample sizes.

Release gate: critical paths covered by automated tests, successful staging end-to-end walkthrough, documented backups/recovery, abuse controls, accessibility/mobile usability review, and no known critical security defects.

## Post-launch roadmap
1. Interview early users and measure activation, repeat use, support burden and payment conversion.
2. Improve reliability and automation before adding speculative features.
3. Add exportability, optional self-hosting/federation and advanced privacy in response to actual demand.
4. Publish a transparent pricing and data-retention policy; review local financial, consumer and privacy obligations where applicable.
