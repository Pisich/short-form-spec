# Short Form Spec (SFS)

A **Short Form Spec (SFS)** is a concise specification that records *what was implemented* in a software change, without the history of how the design got there. It is written at the very end of a spec-driven development (SDD) workflow, after implementation is complete.

> Coined by Pisich, September 2026.

## The problem

In spec-driven development (SDD), a spec typically is written before implementation and guides it. During development, that spec tends to accumulate context: discarded approaches, reworks, changed requirements, review comments and notes on why things moved. Over time it becomes long and noisy, and hard to use as a reference for how the system works *now*.

## The idea

Keep the working spec messy if it needs to be. When the work is done, distill it into an SFS: the final behavior, interfaces, and decisions, and nothing about the detours. The history stays in version control, pull requests, and the SFS provides a quick way to represent what was changed. Ideally, SFSs are generated automatically by an AI agent when implementation is done and updates whenever that unmerged change's behavior is updated.

## Where it sits in the SDD workflow

1. Write the working spec
2. Implement (revising the spec as needed)
3. Review and verify
4. **Write the SFS** as the final, canonical record of what shipped

## Rules

- **Implemented state only.** Describe what is true now, not what was planned or considered.
- **No rework narrative.** Lines like "we first tried X" don't belong.
- **Shouldn't take more than 2 minutes to read** The SFS should always be less than 500 words. If it runs longer, theres too much history or detail.
- **Link to the history.** Point to the working spec, PR, or issue for anyone who needs it.

## Structure

See [`TEMPLATE.md`](TEMPLATE.md) for a blank copy and [`examples/`](examples/) for a filled-in one.

1. **Title and ID**: name of the feature or change plus the task identifier, possibly a JIRA ticket key.
2. **Status and date**: e.g. Implemented, with date and version or PR reference.
3. **Summary**: 2-3 sentences on what it does and why it exists.
4. **Behavior**: what the system does now, as a short list.
5. **Interfaces and data**: APIs, inputs/outputs, schemas, or config others depend on.
6. **Key decisions**: final decisions only, one line each.
7. **Limitations and out of scope**: known gaps and intentional exclusions, one line each.
8. **Verification**: how to confirm it works (tests, manual checks).
9. **References**: links to the working spec, PR, and issues.

## Why bother

Separating the working spec from the SFS lets the working spec stay messy while the SFS which is committed to git history stays clean. That makes it reliable, low-noise context for future teammates and for AI coding agents.

## Contributing

Ideas, critiques, and real-world examples are welcome. Open an issue or a pull request.

## License

Content is available under CC BY 4.0. Please credit the original author when reusing.