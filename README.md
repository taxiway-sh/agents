# Taxiway agents state

Run state of the [Taxiway](https://github.com/taxiway-sh/taxiway) scheduled
agents. This repository holds state only, never rules: agent declarations,
prompts and the run contract live in Taxiway's
[`taxiway-agents` skill](https://github.com/taxiway-sh/taxiway/blob/main/.agents/skills/taxiway-agents/SKILL.md).

- `status/<id>.json`: the heartbeat each agent writes at the end of every run,
  validated against
  [`status.schema.json`](https://github.com/taxiway-sh/taxiway/blob/main/.agents/agents/status.schema.json).
- `deployed.json`: the installed agents, with their schedule and the
  `promptVersion` they were installed from.

Everything here is public: no secrets, host details, private paths or raw logs.
