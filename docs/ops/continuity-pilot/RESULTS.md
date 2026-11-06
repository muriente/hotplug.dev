# Result: adjust; do not adopt Entire globally yet

The GitHub-first portion works for the narrow tested case. A fresh GitHub clone
recovered the mission, decision, pending handoff, next action and byte-identical
synthetic artifact. This supports keeping a compact project-owned record alongside
valuable work. It does not establish automatic capture or genuine agent handoff.

## Verified evidence

Target: existing public `muriente/hotplug.dev`, branch
`pilot/continuity-20261106`, based on unchanged main
`fb6c90f32e4e56ae724b0ff29a401c00d9981b81`. Repository CODEOWNERS names
`@muriente`; both candidate repos had no open pull requests in the preflight.
The only original worktree was main, with a preserved untracked restart checkpoint.
Its recorded launch ownership and explicit pause were left unchanged. The private
`muriente/hotplug` had no default branch/content. No substitute repository was made.

Checkpoint commit `122cb14f5b89bfaa2087aa981e4d3ddbe2ef9ebe` was pushed with
an explicit branch refspec. `git ls-remote` confirmed that exact remote SHA. A
fresh clone from GitHub, without the producer's working directory or agent state,
recovered SHA-256 `72422489637bfde7e42b9b8896daacef4daba0060a9c4371c29837e62485efc4`.

| Check | Observed result | Meaning / limit |
| --- | --- | --- |
| Normal scoped work | Authored record and synthetic artifact committed | No product runtime or branding edits |
| GitHub recovery | Clone 0.9035 s; verifier process 0.0485 s | Single warm-machine run, not human comprehension time |
| Synthetic process interruption | Producer exited 23; new verifier recovered in 0.0395 s | Checkpoint already durable; not an actual agent crash |
| Altered / missing artifact | Both rejected with nonzero exit | No silent success on those incomplete recovery cases |
| Pending handoff | Preserved as pending | No fabricated acknowledgment |
| Entire installation | Release verified, hooks generated, status read back | Not proof that capture works |
| Entire capture/recovery | Not verified | No checkpoint produced by a successfully authenticated agent session |
| Real Claude→Codex / cloud→local | Blocked / not exercised | Claude CLI logged out; Codex hooks await approval; hosted Claude surface unavailable |

Raw non-sensitive measurements are in `measurements.json`. Run
`python3 scripts/test-continuity-pilot.py` for the disposable process-interruption,
fresh-process and corruption fixtures. It clones the actual current repository
locally and never changes the original checkout or contacts a model provider.
The remote test commands are in README.md. Later SHA readback verifies publication
of this evidence; the measured checkpoint above remains independently reproducible.

## Friction and coverage

The recovery command is one step after cloning and adds no approval/delegation
gate. However, this experiment's record was authored by an agent manually: no
automatic checkpoint/event bridge has been demonstrated. No before/after baseline,
human effort measurement, sustained workload or genuine context-comprehension test
was performed. The millisecond timings must not be advertised as end-to-end task
resumption. The test does not preserve uncommitted edits or absent cloud output.

Entire added a downloaded binary, PATH consideration for agent hooks, local
configuration, sandbox cache warning, authentication dependency and hook-trust
step. That is enough observed friction to reject immediate global rollout. It is
not evidence to discard the product: authenticated local capture could still help.

## Exact open boundaries

1. Claude Code session probe in the isolated clone returned `Not logged in`.
   No Claude task executed; no authentication bypass or credential transfer ran.
2. Entire status reported seven Codex hooks needing approval in `/hooks`.
   No approval was granted or inferred; no hook-trust bypass ran.
3. No callable hosted Claude execution connector was exposed here. Installed local
   CLIs do not prove access to Claude's cloud sessions. No cloud coverage is claimed.
4. The real handoff acknowledgment and Entire checkpoint interruption/recovery
   remain open. Native resume may restore an agent-specific session rather than
   translate it between providers. Verify that behavior separately.

These are observed access/acceptance boundaries, not an automatic approval-review
denial. GitHub branch publication succeeded. Entire has been disabled locally, and
its settings/transcripts/hooks were not published. No checkpoint refs were present
locally or advertised remotely in the inspected Entire namespace. Nothing was
merged, deployed, bought, globally enabled or applied to another repository.

Recommendation: retain this draft experiment and portable record pattern; adjust
the capture integration only after a genuine authenticated cross-agent test.
Keep delegation independent of record synchronization. The overall pilot remains
partial until its stated closure condition is met or the user changes the scope.
