---
name: Design Library Finder
summary: Skill that searches this repository's catalogue by area, work phase and topic and returns the resources to use, with links and how to apply them.
area: [UX, UI, Research]
phase: [Discovery, Define, Ideate, Design, Test, Handoff]
format: [Skill]
topics: [resource-search, library, skill-discovery, onboarding]
language: en
platform: Claude (claude.ai skills); the logic can be reused as agent instructions elsewhere
how_to_use: Install this folder as a skill, then ask e.g. "find UX material for usability testing".
entry_point: SKILL.md
maintainer: mimirossi
added: 2026-10-26
---

# Design Library Finder

A Claude skill that searches this library by **area**, **work phase** and **topic**, and answers with the resources to use, a link to each, and how to apply them to your task.

It always reads the live [`catalog.json`](../catalog.json), so it knows about new material as soon as it is catalogued. It replies in the language you write in.

## Install

1. Download this folder.
2. Zip it and upload it from the Skills section of Claude's settings.

## Try it

- "Find UX material for usability testing"
- "Is there a checklist for reviewing a date picker?"
- "Cosa abbiamo per preparare interviste utente?"

If the library has nothing on a topic, the skill says so instead of stretching an unrelated resource.
