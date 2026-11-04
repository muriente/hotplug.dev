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

Quality checks run on MINI. Commit and push a task branch, open a PR, then run `python3 scripts/check-local.py` on the clean exact PR head. It runs the checks locally and publishes `MINI / site checks` to GitHub. The protected PR requires this status, resolved conversations and zero second-person approvals.

After squash merge, fast-forward local main, run `python3 scripts/check-local.py` again for the merged SHA, then `python3 scripts/publish.py`. The local publisher copies only site/ plus a source manifest to the gh-pages branch, preserving its history. GitHub's managed Pages service publishes that branch with .nojekyll. GitHub hosts the site; Cloudflare provides DNS/edge.

No configurable hosted build/test/lint/audit jobs, self-hosted runner or new service is required. The former workflows and settings are archived as rollback evidence. GitHub's native Pages publishing run is the hosting service, not our quality-compute route. Weekly Dependabot npm update PRs remain, with validation performed locally. Run live health commands explicitly on MINI; no unattended monitor is claimed. See [local publication](docs/ops/LOCAL-PUBLICATION.md) for the exact change/validation/publish/rollback procedure and trust boundary.

## Roll back

For website content, revert the faulty merge through a PR, pass checks and merge. Run the local publisher and confirm the resulting managed Pages run and `/version.json`; do not equate source revert with live recovery. Use a verified known-good content revert; never force-push or delete history.

For DNS, restore the five changed records from `docs/ops/dns-before.json` through Cloudflare's DNS API, preserving unrelated later records. Return each original content/proxy/TTL value by record ID. Do not alter DNSSEC/DS, nameservers, mail-deny TXT, `_domainconnect`, or future domain verification TXT. The prior origin is parking; a DNS rollback restores parking, not an older Hotplug website. Keep Full(strict); never use Flexible as a certificate workaround. See [launch evidence](docs/ops/LAUNCH.md) and [decisions](docs/research/DECISIONS.md).

## Operations

CODEOWNERS, contribution guidance, issue form, private reporting, secret scanning/push protection, dependency alerts/security updates, branch protections and explicit local checks are configured and recorded with readback in the launch record. No release workflow/binary badge is present because there are no product artifacts here. Security reports: [SECURITY.md](SECURITY.md).
