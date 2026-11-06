# Continuity pilot — one mission, one branch

This is a bounded experiment on the existing Hotplug website repository. It does
not resume the website launch, change the product or publish the site. The private
`muriente/hotplug` repository was empty when inspected. The saved Hotplug project
and its existing source point to `muriente/hotplug.dev`.

The experiment uses ordinary Git commits and a draft PR. No new service, account,
required hook, hosted workflow, subscription or global agent instruction is added.

## Working agreement for this experiment

The agent owns the record and the bookkeeping; the human keeps talking normally.
An instruction remains active until completed, changed or cancelled. A later
clarification does not silently cancel it. Resuming does not require renewed
authorization for the same scope.

Execute on any authorized surface that can do the work. Delegation may start
immediately; recording its link can follow asynchronously. A GitHub outage,
unavailable computer or missing capture integration must not hold up useful work.
State the unsynchronized remainder honestly and reconcile when available.

At a meaningful decision, valuable work boundary or handoff, update `mission.json`
with the outcome, actual state, evidence, next action and responsible agent. Commit
only reviewed, non-sensitive work. Save a patch or artifact for valuable uncommitted
work if necessary; a record without that artifact does not preserve the edits.
Avoid routine per-message or per-tool records. Transcripts are optional evidence,
never the only source of the mission's next action.

The receiving agent reads the record and linked evidence, then acknowledges what
it actually recovered. Until that happens, mark the handoff as pending. A turn
ending does not complete the human outcome. This experiment establishes no global
policy and creates no new approval prerequisite.

## Reproduce recovery

Clone the actual repository at the pilot branch, without using the first checkout:

```sh
git clone --single-branch --branch pilot/continuity-20261106 \
  https://github.com/muriente/hotplug.dev.git hotplug-recovery
cd hotplug-recovery
python3 scripts/continuity-pilot.py
```

The command reads a compact record, checks the checkpoint's committed artifact
against its SHA-256, and prints the next action and pending boundaries. It does
not fetch private transcripts, change ownership, execute the next action, or
declare the pilot complete. A missing or altered checkpoint fails explicitly.

## Entire experiment and rollback

Entire was evaluated separately in an independent clone, not a shared worktree:
Git worktrees share hooks, which could have affected active work. Only the official
v0.12.2 macOS ARM64 release was downloaded into the task folder, verified against
its release checksum. No installer script, Homebrew or host-wide installation ran.
Project hooks were installed with local-only settings, telemetry disabled and
`push_sessions: false`. No historical session import was requested.

The local Claude Code CLI was unauthenticated; its minimal probe returned
`Not logged in`. Codex CLI was authenticated but Entire reported seven hooks
requiring approval. They were not approved or bypassed. No actual cross-agent
capture, resume or cloud-to-local recovery is claimed. Entire was disabled locally
after inspection. Hook/config files remain excluded from this branch; no transcripts
or Entire checkpoint refs are included in the PR.

Rollback: close the draft PR and stop using this branch; nothing has been merged
or deployed. The original checkout is unchanged. Entire is already disabled in the
isolated clone; its documented `entire disable --uninstall` removes that clone's
integration if desired. Keep evidence until the evaluation is reconciled. The
downloaded binary is outside all host PATH directories and has no service.

See `ENTIRE.md` for provenance, destinations and the remaining acceptance test,
and `RESULTS.md` for measured results. Adopt or reject based on recovered work and
friction, not on successful installation alone.
