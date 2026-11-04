# Hotplug.dev launch — 2026-11-04

## Mission

- Objective: a useful, accessible English Hotplug project website, actually hosted on GitHub Pages at https://hotplug.dev, with practical GitHub operations.
- Owner: Codex launch chat on MINI, delegated by coordinator 01a1a5ab-6748-7a13-8179-4924c1e826f5.
- Authority: create a separate public website repo, publish and deploy; reversible .dev DNS/config changes under KDEV-150 standing authorization (Juan, 2026-10-22). No spending, private product code publication, credentials, unrelated repos or secondary-domain cutovers.
- Deliverable: site, workflows, public participation routes, verified deployment and reproducible rollback.
- Closure: exact source deployed by successful Pages run; HTTPS apex serves new content; www canonical preserves path/query; desktop/mobile/keyboard and automated accessibility/link checks pass; DNSSEC/TLS intact; remote configuration read back.
- State: active. Next: implement, verify and deploy. Codex owns the remainder; coordinator owns compact continuity.
- Cadence: meaningful milestones immediately; maximum three minutes during active work.

## Ownership and preservation

The Hotplug directory was empty and not a Git repository at admission. gh identity: muriente. Website repository: muriente/hotplug.dev (public). No private product source is copied. Existing .dev DNS owner reported idle; this mission owns website cutover. No host-wide agent/runtime configuration changes. Preflight: MINI, KDEV checkout /Users/muriente/Developer/Projects/killer-dev-environment. AGENTS.md/CANON.md provide backup/verification/standing authorization rules; docs/AGENT-OWNERSHIP.md checked. No active competing owner for this new site. Existing unrelated KDEV dirty state preserved.

## Acceptance risks and discriminating checks

1. DNS/routing mismatch: predict old parking content or wrong IPs. Probe authoritative and public resolvers, edge content and origin with SNI. Falsified by new source-specific content through both paths.
2. Deployment/artifact mismatch: predict successful workflow but stale/missing pages. Probe exact SHA, artifact manifest and live hashes. Falsified by content/hash agreement and successful Pages deployment.
3. TLS/edge mismatch: predict origin certificate pending or edge 525/526. Probe GitHub certificate state, direct origin HTTPS and edge HTTPS; preserve Full(strict), never use Flexible.
4. Product-claim/UX mismatch: predict visitors infer an available universal product. Inspect copy, real links and rendered first-setup/development notices; no placeholder forms/downloads.

Evidence is recorded below as it is observed. A completed turn or source commit is not launch acceptance.

## Pre-publication checks

HTML validation, local asset/fragment checks and size budgets passed. npm audit: zero vulnerabilities. Desktop/mobile axe WCAG checks and keyboard navigation passed. Independent read-only review caught enlarged-text overflow (412px at 320px viewport with 200% root text); corrected intrinsic grid minimums and wrapping rather than hiding overflow. All 12 browser tests subsequently passed. Review found no further important copy/publishing defects. Domain hotplug.dev was successfully verified under GitHub account muriente through the authenticated Pages UI; permanent challenge TXT added, with existing DNSSEC untouched. Secret scanning/push protection, private reporting, Dependabot alerts and automated security fixes enabled with API readback.

## Deployment and remote controls

Initial source 82b42c3f76e4d6cfc47b58457451f76c6cac3031 deployed successfully by https://github.com/muriente/hotplug.dev/actions/runs/41858126030. Direct origin HTTP `/version.json` matched that source. DNS four A records changed to 185.199.{108,109,110,111}.153; www CNAME muriente.github.io. Both temporarily DNS-only TTL300 for certificate issuance. TLS was not accepted while certificate was pending; strict edge validation stayed enabled. Public 1.1.1.1 and authoritative cody agreed on A records; parent DS remained 2371/13/2 with original digest.

Ruleset 26542972 active on default branch, no bypass: PR with zero required approvals, GitHub Actions app-bound Site checks, up-to-date branch requirement, resolved review threads, linear history, no force pushes/deletion. github-pages environment permits only main. Workflow default contents read, no Actions approval of PRs. Public repo homepage/topics, Discussions, issue form, private reporting, secret scanning/push protection, vulnerability alerts/security fixes all read back. Weekly Dependabot successfully created its first Actions update PRs; current release pins consolidated into the launch verification PR to avoid five serial stale-branch merges. All eight external website links returned200.
