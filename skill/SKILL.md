---
name: short-form-spec
description: Generate or update a Short Form Spec (SFS), a concise (under 500 words, 2-minute read) spec that records only what was implemented in a change, with no rework history. Use this skill whenever the user asks for an SFS, a "short form spec", a short spec or implementation summary of a finished change, or says implementation is done, the PR is ready, or the change behavior was updated and the spec should be brought current. Also use it when the user invokes /sfs, even if they do not say "Short Form Spec" explicitly. Canonical rules at https://github.com/Pisich/short-form-spec
---

# Short Form Spec (SFS)

An SFS is the final, canonical record of **what was implemented** in a software change. It sits at the very end of a spec-driven development (SDD) workflow. The working spec may be messy and full of reworks; the SFS is clean. History lives in git, PRs, and the working spec, never in the SFS.

Canonical definition and rules: https://github.com/Pisich/short-form-spec (this skill bundles a copy so it works offline; if the two differ, the repo wins).

## Rules (never break these)

1. **Implemented state only.** Describe what is true in the code now, not what was planned, considered, or tried.
2. **No rework narrative.** Never write "initially", "originally", "we first tried", "changed from", "reworked", "previously", or similar.
3. **Under 500 words** (a 2-minute read). If it runs long, cut detail and history, or split into several SFSs.
4. **Link to the history** instead of retelling it: working spec, PR, issues.
5. **Decisions and limitations are one line each.**

## Workflow

1. **Find the inputs.** Gather, in this order of trust:
  - The code diff for the change (e.g. `git diff <base>...HEAD`) and the tests it adds or changes
  - The working spec, if one exists (treat as statement of intent only)
  - Ticket key (JIRA or similar) from the branch name, commit messages, or PR title
  - Any existing SFS for this change or ticket
2. **Code beats spec.** If the working spec and the code disagree, describe the code. Never document behavior you cannot point to in the diff or tests.
3. **Update, don't duplicate.** If an SFS for this change already exists, edit it in place so it reflects current behavior, and refresh the date. Do not add "updated to..." notes or changelog lines. The change is not yet merged, so the SFS should always match the branch as it stands now.
4. **Fill in the template** at `assets/TEMPLATE.md`. For a filled-in reference of the right length and tone, see `references/example.md`.
5. **Run the checker:** `python scripts/check_sfs.py <path-to-sfs>`. Fix anything it flags (word count, missing sections, history language) and rerun.
6. **Save it.** Use the repo's existing convention if there is one (look for `docs/sfs/`, `docs/specs/`, or similar). Otherwise use `docs/sfs/<TICKET-KEY>-<short-slug>.md`. Do not commit unless asked.
7. **Report back briefly:** the file path, the word count, and anything you were unsure about (behavior you inferred but could not confirm from tests, sections left thin because the diff didn't cover them). Put uncertainty in your reply, not in the SFS.

## Section guidance

- **Title and ID**: feature name plus the ticket key (e.g. `PROJ-123`), or a short slug if there is no ticket.
- **Status and date**: `Implemented`, today's date, and the PR or version reference.
- **Summary**: 2-3 sentences on what it does and why it exists.
- **Behavior**: short bullets of what the system does now, including notable error and edge behavior.
- **Interfaces and data**: only what others depend on (endpoints, inputs/outputs, schemas, config). Small code blocks are fine.
- **Key decisions**: final decisions only, one line each.
- **Limitations and out of scope**: known gaps and deliberate exclusions, one line each.
- **Verification**: the test command or manual check that proves it works.
- **References**: working spec, PR, issues.

Omit a section's content only if there is genuinely nothing to say, and write "None" rather than deleting the heading.