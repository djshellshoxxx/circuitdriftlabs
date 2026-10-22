# Shared Noncustodial Payment Components — Circuit Drift Labs

Status: Architecture proposal | 2026-10-22

## Vision
Create a reusable, modular, open-source, local-first payments toolkit that powers multiple independent Circuit Drift Labs applications without requiring CDL to custody user funds. Components should work in mobile browsers and static-site deployments when possible, while making external blockchain RPC, wallet and smart-contract dependencies explicit. Separate common primitives from product-specific rules; avoid a mandatory central platform.

## Problems solved
Each new payment product otherwise reinvents invoice schemas, wallet connectors, QR generation, address validation, chain selection, transaction verification, reconciliation, security controls and tests. Duplicated logic introduces inconsistencies, security defects and high maintenance costs. A shared foundation reduces engineering effort and makes updates propagate safely.

## Target products
- GhostInvoice: signed/encrypted invoices and payment requests.
- NullCart: embeddable static-site checkout.
- SovereignShop: exportable static storefronts.
- BlockReceipt: independently verifiable transaction receipts.
- StealthTip and GhostDonate/FreedomFund: creator tipping and fundraising.
- PaySplit: audited contract-based payment distributions.
- GhostPayroll: batch payout preparation and reconciliation.
- OffRampQuote and SwapReceipt: quote preparation and settlement evidence.
- GhostPay: existing candidate modules; p2p-offramp: potential future integration after repository audit.

## Package design
1. **identity-and-keys**: public-key identity, signature verification, key rotation guidance, hardware-wallet capability checks; never send private keys to a server.
2. **address-safety**: strict chain-aware parsing, checksum and lookalike warnings, allowlisted token metadata, recipient confirmation.
3. **wallet-connectors**: standardized connect, disconnect, sign, simulate and send interfaces, explicit network selection.
4. **invoice-schema**: canonical versioned JSON invoices, validation, serialization, expiry, signatures and optional encrypted envelopes.
5. **qr-and-links**: QR codes, deep links and safely encoded payment requests.
6. **chain-adapters**: read-only RPC, confirmations, event decoding, reorg detection, chain/token registry, configurable endpoints.
7. **tx-review**: human-readable transaction and typed-data preview before wallet signing.
8. **receipt-verification**: chain-backed receipt evidence, signed local exports and replay-resistant reconciliation.
9. **payment-routing**: optional independently audited, fee-transparent noncustodial contracts; never claim a frontend can enforce protocol fees alone.
10. **storage-and-export**: IndexedDB drafts, encrypted backup, portable JSON, deterministic import/export.
11. **ui-components**: accessible mobile checkout, invoice, wallet status, payment progress, QR and error screens.
12. **test-fixtures**: vectors, mocked RPC failures, wallet edge cases, property tests and reproducible builds.

## Technical design
TypeScript monorepo with independently versioned packages, strict interfaces, tree-shakable ESM builds and example Vite PWAs. Use decimal-safe integer minor units or BigInt, no floating-point money arithmetic. Keep network, token and protocol registries signed/versioned. The shared toolkit must not become a single point of failure: allow user-selected RPC endpoints, exportable state and self-hosted builds.

## Integration with existing work
Review djshellshoxxx/GhostPay modules: core-crypto, invoice-schema, chain-adapters, tx-review, address-safety and BTC Silent Payments. The GhostPay README reports no production deployment, no independent third-party audit and disabled mainnet payments. Extract only after API review, tests, licensing checks and security gates. Inspect p2p-offramp implementation before committing to module reuse. Avoid circular dependencies; applications consume the shared packages, not each other.

## Monetization
Open-source core SDK with commercial support and integration licenses; $19–$99 premium templates, $29–$199 developer kits, and optional hosted services on commercial-compatible infrastructure. An audited on-chain router may collect a clearly disclosed protocol fee where appropriate. Example: 20 developer kit purchases × $49 = $980 gross in a month, before costs. Never depend on obscured fees or unverifiable frontend subscription gates.

## Implementation game plan
**Phase 0 — inventory:** audit existing GhostPay and p2p-offramp packages, dependency licenses, duplication, interface boundaries, current tests and security findings. Produce a migration matrix and dependency graph.

**Phase 1 — core MVP:** implement shared address-safety, invoice-schema, QR, chain-adapters and receipt-verification packages. Add documented TypeScript interfaces and test vectors. Demonstrate a complete testnet invoice → wallet payment → verified receipt flow.

**Phase 2 — first products:** integrate GhostInvoice, NullCart and BlockReceipt; then use the same checkout in SovereignShop. Publish one example static site and a copy-paste integration guide.

**Phase 3 — revenue:** release premium templates and developer kits, collect feedback from five merchants, test willingness to pay and measure support costs. Deploy commercial checkout on a static host whose terms permit ecommerce.

**Phase 4 — advanced modules:** introduce audited split-payment routing, batch payout preparation, stealth-payment options and off-ramp integrations only after security review and relevant testnet validation.

## Release and security acceptance criteria
Unit, property, integration and browser tests; signature and invoice tamper tests; wrong chain/token/address; RPC disagreement and outages; chain reorgs; decimal precision; wallet cancellation; malicious QR and links; secret leakage; replay; reproducible builds; dependency/license scans. Any contract handling real funds requires independent security review and real-wallet/testnet trials. Maintain explicit limitations about pseudonymity, blockchain visibility and third-party dependencies.

## Key success metrics
Time to integrate SDK in a new app, number of duplicate code paths removed, test coverage of payment invariants, testnet payment completion rate, verified merchant pilots, paid kit conversion, support hours and cost per active integration.
