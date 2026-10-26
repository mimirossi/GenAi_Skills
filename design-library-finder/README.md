---
name: Design Library Finder
summary: Skill (for Claude) and universal prompt (for ChatGPT and other agents) that searches this repository's catalogue by area, work phase and topic and returns the resources to use, with links and how to apply them.
area: [UX, UI, Research]
phase: [Discovery, Define, Ideate, Design, Test, Handoff]
format: [Skill]
topics: [resource-search, library, skill-discovery, onboarding]
language: en
platform: Claude (SKILL.md); ChatGPT, Copilot, Gemini and enterprise agents (PROMPT.md)
how_to_use: On Claude install this folder as a skill; on any other agent paste the prompt in PROMPT.md into its instructions. Then ask e.g. "find UX material for usability testing".
entry_point: SKILL.md
maintainer: mimirossi
added: 2026-10-26
---

# Design Library Finder

Searches this library by **area**, **work phase** and **topic**, and answers with the resources to use, a link to each, and how to apply them to your task.

It always reads the live [`catalog.json`](../catalog.json), so it knows about new material as soon as it is catalogued. It replies in the language you write in.

## Install

| You use… | Use this file | How |
|---|---|---|
| **Claude** | [`SKILL.md`](SKILL.md) | Download this folder, zip it, and upload it from the Skills section of Claude's settings. |
| **ChatGPT, Copilot, Gemini, an internal agent platform** | [`PROMPT.md`](PROMPT.md) | Paste the prompt into the agent's instructions. Setup per platform is explained in the file. |

## Try it

- "Find UX material for usability testing"
- "Is there a checklist for reviewing a date picker?"
- "Cosa abbiamo per preparare interviste utente?"

If the library has nothing on a topic, the skill says so instead of stretching an unrelated resource.
