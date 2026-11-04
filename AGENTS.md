# Hotplug website

This public repository owns hotplug.dev website content and operations only. Product code remains separate and private. Never copy credentials, product source or private diagnostic payloads here.

Use English; brand spelling is Hotplug. Describe software as in development until genuine release/compatibility evidence exists. No invented downloads, testimonials, subscriptions, universal support, performance superiority or permanent price/license promises.

Static files live in site/. There is no client JavaScript or production dependency. Run npm ci, npm test and npm run test:browser before changing deployment claims. Publish only site/ through GitHub Pages; never upload repository root. Keep Actions pinned to full SHA. Use a PR with passing checks; single maintainer requires zero approving reviews. Preserve DNSSEC, mail-deny TXT and rollback evidence for DNS changes. Update docs/ops/LAUNCH.md at material lifecycle boundaries; source commit is distinct from live acceptance.
