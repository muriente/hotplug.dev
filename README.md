# Hotplug website

Public website for **Hotplug**, an in-development project for sharing Android phone internet over USB with supported computers or routers.

**Live:** https://hotplug.dev · **Hosting:** GitHub Pages · **Community:** [Discussions](https://github.com/muriente/hotplug.dev/discussions)

This repository publishes website source only. It does not contain or license the separate Hotplug software, announce product downloads, or promise device compatibility, pricing, or source availability. Website code/assets use the [MIT license](LICENSE); no trademark rights are granted.

## Edit and verify

Requires Node 24+ and Python 3. Static pages are in `site/`; no production dependencies, client JavaScript, tracking or third-party fonts. Only `site/` is uploaded.

```sh
npm ci --ignore-scripts
npx playwright install chromium
npm test
npm run test:browser
npm run preview
```

Open http://localhost:4173. Change HTML/CSS directly. `npm run test:links` checks external participation/privacy links; `python3 scripts/live.py` verifies public deployment content and www redirection. Tests cover all pages at desktop/mobile sizes, automated WCAG checks, keyboard skip link/disclosures, 320px reflow with enlarged text, local links, metadata and file budgets. Automated checks do not replace assistive-technology user testing.

## Publish

Use a PR targeting `main`. `Site checks` must pass; no second-person approval is required. Squash merge triggers the Website workflow: checks → package only static files → deploy to the `github-pages` environment using GitHub OIDC. No deployment secrets or Cloudflare token are stored in Actions. Actions are pinned to full commit SHAs; weekly Dependabot PRs update Actions and development dependencies.

The `github-pages` environment is limited to main. GitHub Pages serves the site with custom domain `hotplug.dev`. `site/version.json` is generated during deployment with the exact source SHA and repository. Cloudflare owns DNS/edge, not hosting. The weekly Live site health workflow checks actual content, canonical redirect and external links; failures use GitHub's normal workflow notifications.

## Roll back

For website content, revert the faulty merge through a PR, pass checks and merge. Confirm the resulting Pages run and `/version.json`; do not equate source revert with live recovery. An urgent maintainer can dispatch Website on a known-good main revision after reverting; never force-push or delete history.

For DNS, restore the five changed records from `docs/ops/dns-before.json` through Cloudflare's DNS API, preserving unrelated later records. Return each original content/proxy/TTL value by record ID. Do not alter DNSSEC/DS, nameservers, mail-deny TXT, `_domainconnect`, or future domain verification TXT. The prior origin is parking; a DNS rollback restores parking, not an older Hotplug website. Keep Full(strict); never use Flexible as a certificate workaround. See [launch evidence](docs/ops/LAUNCH.md) and [decisions](docs/research/DECISIONS.md).

## Operations

CODEOWNERS, contribution guidance, issue form, private reporting, secret scanning/push protection, dependency alerts/security updates, branch protections, least-privilege Actions and weekly health checks are configured and recorded with readback in the launch record. No release workflow/binary badge is present because there are no product artifacts here. Security reports: [SECURITY.md](SECURITY.md).
