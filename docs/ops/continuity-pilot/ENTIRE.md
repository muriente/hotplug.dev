# Entire evaluation — 2026-11-06

## Provenance and installed version

- Official source: https://github.com/entireio/cli (MIT).
- Pinned release: https://github.com/entireio/cli/releases/tag/v0.12.2
- Tag resolved through GitHub API to `c4f103d8dfed1f1549db9b2c793f2d7e10f65eb8`.
- Asset: `entire_darwin_arm64.tar.gz`, downloaded with `gh release download`.
- SHA-256: `ec8f8a325e0f8f0b0c17781906273b5e21bc125b0bb6cfbc0c61cad8dfccba4f`.
- Compared to the release's `checksums.txt`; this checks consistency with the
  publisher's release, not an independent signature or source-build audit.
- Executed binary reports Entire CLI 0.12.2, darwin/arm64.

## Observed surfaces and compatibility boundary

Claude Code CLI 2.1.318 is present, but `claude auth status` reported logged out.
A minimal non-tool probe with only project settings and no MCP servers returned
`Not logged in · Please run /login`. No inference from that failure is made about
Claude's separately hosted web/cloud sessions, which were not available here.

Codex CLI 0.166.0-alpha.6 reported ChatGPT login. Entire installed project hook
definitions but its status reported seven Codex hooks requiring approval via
`/hooks`. Trust was not bypassed. The current desktop/delegated session started
outside this clone, so it is not evidence that those new project hooks ran.

Official Codex integration documentation describes `.codex/hooks.json` and reading
rollout files under `CODEX_HOME` or `~/.codex`. Ephemeral runs may lack the transcript
path. That contract alone proves neither capture in a cloud agent nor transfer of
a Claude conversation into Codex. A branch handoff record can be shared even when
native session resume remains agent-specific.

## Data destinations and safeguards actually used

Entire documents checkpoints containing prompts, transcripts and touched files,
normally uploaded as `refs/entire/checkpoints/...` alongside Git pushes. Public
repository checkpoints are publicly readable. Secret redaction is best effort.
Separate private checkpoint destinations are supported, but none was configured
or created in this experiment. No GitHub App, Entire login, repository mirror,
Entire cloud hosting, brain/search plugin or paid service was enabled.

This clone used `--local --skip-push-sessions --telemetry=false`; readback confirmed
`push_sessions: false`, telemetry false and Git-refs backend. Entire still identified
origin as its read destination, which is not proof of upload. Capture was disabled
after the unauthenticated probe. No existing session history was imported. Session
storage and generated agent settings remain local and excluded from publication.
All ref names and the outgoing explicit branch refspec are inspected before push.
Only authored, non-sensitive pilot artifacts go to the existing public GitHub repo.
The Claude probe could not submit model work because authentication was absent.

Installation warned that `~/.cache/entire` could not be created in this sandbox and
proceeded without its hook-installation lock. The clone was independent and had no
other writer. This is a limitation of the scoped install, not a successful normal
host installation. No permission boundary was bypassed to create that cache.

## Repeating the unperformed acceptance test

On an authorized, authenticated Claude Code surface, enable this pinned binary in
an isolated clone with uploads and telemetry off. Put the binary on that process's
PATH so project agent hooks can find it. Approve only the inspected Codex hooks
through the supported `/hooks` interface if that surface is used. Start fresh
synthetic sessions; do not import existing private history. Have Claude make a tiny
pilot-only artifact, commit, inspect the checkpoint, interrupt, and have Codex read
the shared mission and artifact. Record the actual receiving acknowledgment and
time. Validate native checkpoint recovery separately from Git recovery.

Before publishing any checkpoint, inspect its complete contents and destination
recipients; for a public repo prefer keeping transcripts local or using a separately
authorized private destination. Do not enable automatic uploads as a test shortcut.

Sources: official [README](https://github.com/entireio/cli),
[Codex integration](https://docs.entire.com/agents/codex), release-linked source and
the installed commands' `--help`. The documented design is broader than the
verified local behavior above. No purchase or global adoption is recommended from
this partial experiment.
