# Taxiway agents state

Run state of the [Taxiway](https://github.com/taxiway-sh/taxiway) scheduled
agents. This repository holds state and improvement records, never rules:
agent declarations, prompts and the run contract live in Taxiway's
[`taxiway-agents` skill](https://github.com/taxiway-sh/taxiway/blob/main/.agents/skills/taxiway-agents/SKILL.md).

- `status/<id>.json`: the heartbeat each agent writes at the end of every run,
  validated against
  [`status.schema.json`](https://github.com/taxiway-sh/taxiway/blob/main/.agents/agents/status.schema.json).
- `queue/machine/<id>.json`: machine-bound checks requested by cloud agents
  and served by the machine agent, validated against
  [`queue.schema.json`](https://github.com/taxiway-sh/taxiway/blob/main/.agents/agents/queue.schema.json).
- `queue/machine/<id>.md`: the public report of a finished item.
- `improvement/` and `learn/campaigns/`: records defined by the
  [`taxiway-improve`](https://github.com/taxiway-sh/taxiway/blob/main/.agents/skills/taxiway-improve/SKILL.md#state-layout)
  and [`taxiway-learn`](https://github.com/taxiway-sh/taxiway/blob/main/.agents/skills/taxiway-learn/SKILL.md#history-campaigns)
  skills.
- `deployed.json`: the installed agents, with their schedule and the
  `promptVersion` they were installed from.

Everything here is public: no secrets, host details, private paths or raw logs.
