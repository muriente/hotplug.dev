# Local quality checks, GitHub Pages publication

Effective 2026-11-04 after Juan's new AGENTS.md preflight item7 (KDEV-162). Quality compute belongs on MINI. GitHub remains review, reconciliation and the explicitly requested website host. No self-hosted Actions runner, new service, paid resource or standing cloud test job is required.

The earlier Website/Live site health Actions configurations are preserved under `pre-local-compute/` as rollback evidence, not executable workflow files. Those two repository workflows were disabled. Earlier hosted runs are retained as historical evidence and must not be described as user-requested compute. The explicit human request was GitHub hosting and operations; the initial hosted quality job was an implementation choice superseded by the new constraint.

## Normal change path

1. Edit a task branch, commit and push it, then open a PR.
2. On MINI run `python3 scripts/check-local.py` at that exact clean PR head. It runs npm ci, HTML/link/budget checks, 12 desktop/mobile/keyboard/axe tests, and dependency audit. It publishes the `MINI / site checks` commit status using existing gh authentication. Failure/interruption publishes failure; dirty/concurrently changed source cannot receive success.
3. Read the PR's final head, checks, review threads and issue effects, then squash merge. No second-person approval is required, but conversations must be resolved and the local status must pass. A new commit needs fresh checks.
4. Update local main with a fast-forward pull. Run `python3 scripts/check-local.py` for the exact merged main SHA, then `python3 scripts/publish.py`.
5. The publisher checks clean main, remote SHA and successful maintainer local status, creates a disposable isolated checkout, copies only site/, adds source version.json, and fast-forward pushes gh-pages. A concurrent changed main stops publication. Nothing force-pushes or rewrites history.
6. GitHub's managed Pages publishing service serves the root of gh-pages; .nojekyll bypasses Jekyll. GitHub may display this required hosting/publication service as a managed Pages build/deploy run. It is distinct from our own configurable Actions build/test/lint/audit jobs, which no longer run.
7. Verify native Pages deployment success, `/version.json` equals main, public pages, canonical redirect and `SITE_URL=https://hotplug.dev npm run test:browser`. Run `python3 scripts/live.py` and `npm run test:links` explicitly on MINI for live health; there is no unattended health-monitor promise.

The local status is a maintainer attestation via existing GitHub auth, not a cryptographic proof or hosted check. Repository write access remains a trust boundary. Do not store an account token in this repository. Dependabot's native dependency-update service remains useful; review its npm PRs and run quality checks locally before merge.

## Rollback

Revert content through a validated PR, merge, validate the resulting main and run the local publisher. Keep gh-pages history; no force push. To restore the prior publication mode only if authorized by a later compute-policy change, restore archived workflows via PR, re-enable them, set Pages build_type workflow, and restore captured ruleset JSON. Do not restore hosted compute under the current local default.

DNS rollback remains in README.md and dns-before.json. DNSSEC, mail records and verified-domain TXT are preserved. Native branch publication retains the same custom domain and enforced HTTPS.
