# Website and operations decisions

Research checked 2026-11-04. Requirements: GitHub hosting, a preliminary technical project site, no fabricated availability or product claims, no spending.

## Approach comparison

| Approach | Benefits | Cost / fit | Decision |
|---|---|---|---|
| Plain HTML/CSS, GitHub Actions Pages | No runtime dependencies, no hydration, easy rollback, full control of semantics | Some repeated page chrome | Adopt for three small pages |
| Astro static output, GitHub Pages | Reusable components and content collections | Build dependencies for very little content | Revisit when documentation grows |
| Jekyll / GitHub native branch build | Mature Markdown publishing | Themes/Ruby pipeline unnecessary for this visual site | Skip |
| Cloudflare Pages | Useful static hosting | Fails explicit GitHub-hosting requirement | Skip; Cloudflare remains DNS/edge |

## Primary sources

- [Custom workflows for Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages): artifact build and deploy dependency, github-pages environment, Pages and OIDC permissions only on deploy job.
- [Custom domain configuration](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site): claim custom domain before DNS; four documented IPv4 addresses; www CNAME to muriente.github.io; no wildcard DNS.
- [HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https): wait for certificate and enforce HTTPS, avoid conflicting records.
- [Domain verification](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages): account-level DNS challenge prevents domain takeover. Keep challenge TXT permanently once verified.
- [Actions security](https://docs.github.com/en/actions/reference/security/secure-use): pin full commit SHAs; contents read default; no secrets in PR execution; no pull_request_target execution of contributed code.
- [Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets): available for public Free repos. Require passing checks and PRs, zero required approvals for a single maintainer, prevent force pushes and deletion.
- [web.dev performance](https://web.dev/learn/performance): reduce critical resources. System fonts, local SVG, no client scripts/trackers, no third-party font requests.
- GoogleChrome modern-web-guidance CLI: searched accessible responsive static site; retrieved accessibility, html, responsive-design. Native landmarks/details, focus-visible outlines, fluid rem+viewport type, reserved image dimensions, no custom keyboard widget.

## Empirical community evidence (context, not authority)

[HN: GitHub Pages for static sites](https://news.ycombinator.com/item?id=41677027) contains firsthand adoption reports; [HN custom Actions discussion](https://news.ycombinator.com/item?id=43422066) cautions that static HTML alone does not need an elaborate build; [Reddit static HTML hosting discussion](https://www.reddit.com/r/learnprogramming/comments/1s3a41l/is_it_okay_to_host_a_static_htmlcssjs_website_on/) describes the deploy/custom-domain workflow. These are qualitative anecdotes, not uptime or performance proof. The decision follows project constraints and our measured acceptance, rather than community popularity.

## Operations and content

Separate website MIT license; no license claim about Hotplug software, branding/trademark grant or private source. Product remains in development. Android + client installation and first accessory/background permissions are described as intended setup, not verified universal compatibility. Mac/OpenWrt are development targets, not a compatibility matrix. No binary download until genuine artifacts exist.

Actions are pinned to freshly resolved official tag commits. Dependabot updates Actions and development dependencies weekly; updates require checks. Browser/axe dependencies are development-only. Static validation and browser accessibility checks gate deployment; weekly external link/live checks surface rot without creating ongoing third-party telemetry. CodeQL would add no useful application-language coverage to a no-JS HTML/CSS site; no empty scanning workflow. Secret scanning/push protection and private reporting are configured where public free repository capabilities permit. No release attestation workflow until release artifacts exist; Pages deployment provenance ties source SHA to a GitHub deployment.

Fresh release metadata and the first Dependabot run identified newer official Actions majors than the documentation examples. Updated to checkout v7.0.1, setup-node v7.1.0, configure-pages v6.0.0, upload-pages-artifact v5.0.0, deploy-pages v5.0.1 at full release commit SHAs; The PR checks validate checkout/setup-node and site quality; package/deploy validation remains pending until the merged main workflow executes successfully.

## Superseding local-compute decision

Juan's replacement AGENTS.md preflight7 now governs: all quality checks run locally on MINI, reported as an exact-SHA maintainer commit status. Local publishing produces a dedicated gh-pages branch; native GitHub Pages publishing is retained because GitHub hosting is explicitly requested. Earlier custom Actions design and pinned-release research above are historical, with archived workflows retained for rollback; no hosted quality job or scheduled health job remains active. See docs/ops/LOCAL-PUBLICATION.md.
