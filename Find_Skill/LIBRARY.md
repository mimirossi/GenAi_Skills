---
name: Find Skills (Vercel skills CLI)
summary: Skill that helps an AI agent discover and install public agent skills from the open skills ecosystem, bundled with the source of Vercel's skills CLI.
area: [UX, UI, Research]
phase: [Discovery, Define, Ideate, Design, Test, Handoff]
format: [Skill]
topics: [skill-discovery, ai-agents, tooling, workflow, automation]
language: en
platform: Coding agents (Claude Code, Cursor, Codex…). The CLI needs Node.js; designers will mostly use the SKILL.md only.
how_to_use: For designers, install skills/find-skills/SKILL.md as a skill. The rest of the folder is the CLI source code (MIT, © Vercel) and is for developers.
entry_point: skills/find-skills/SKILL.md
maintainer: Vercel (third party, MIT licence)
added: 2026-10-26
---

# Find Skills — library notes

This folder is a third-party project: the [skills CLI](https://github.com/vercel-labs/skills) by Vercel, Inc., released under the MIT licence (see `LICENSE`). Its own `README.md` is left unchanged; this file holds the library metadata instead.

**For designers:** the useful part is [`skills/find-skills/SKILL.md`](skills/find-skills/SKILL.md) — a skill that helps an AI agent find and install public skills when you ask "is there a skill for…?".

**For developers:** everything else is the CLI's source code (Node.js, pnpm).
