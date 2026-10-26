---
name: Design Library Finder
area: [UX, UI, Research]
phase: [Discovery, Define, Ideate, Design, Test, Handoff]
format: [Skill]
topics: [resource-search, library, skill-discovery, onboarding]
language: en
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
