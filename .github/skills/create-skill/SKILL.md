---
name: create-skill
description: "Turn a repeated workflow, debugging pattern, or review checklist into a reusable VS Code skill. Use when you need to package a process, decision tree, or quality bar into a SKILL.md for the project or for personal use."
argument-hint: "Describe the workflow, decision points, and completion checks to turn into a skill."
user-invocable: true
disable-model-invocation: false
---

# Create a Reusable Skill

## When to Use
- You have a multi-step workflow that keeps repeating.
- A debugging, review, or implementation pattern should be reusable by the agent.
- You want to save a process in a project-scoped or personal skill.
- You need to convert a conversation, checklist, or methodology into a `SKILL.md` file.

## Procedure
1. Review the workflow already being followed in the conversation or project.
2. Extract the step-by-step process, including ordering and any key branching decisions.
3. Identify the quality bar or completion checks that prove the task is done correctly.
4. Decide the scope:
   - Project-scoped: place the skill under `.github/skills/<skill-name>/`
   - Personal: place it under `~/.copilot/skills/<skill-name>/` or the equivalent personal customization folder
5. Draft the `SKILL.md` using this structure:
   - YAML frontmatter with `name`, `description`, optional `argument-hint`, and `user-invocable`
   - clear section headings such as `When to Use`, `Procedure`, and `Quality Checks`
   - actionable steps written as a reusable workflow
6. Validate the skill:
   - `name` matches the folder name
   - description contains the trigger phrases that will make the skill discoverable
   - instructions are specific enough to be used without extra context
   - any referenced scripts or resources use relative paths
7. If the workflow is still ambiguous, ask the user targeted clarifying questions before finalizing.

## Decision Points
- Is this a general-purpose workflow or a task-specific one? If general, keep the skill broad; if task-specific, narrow the trigger wording.
- Does the workflow need to be automatic or user-invoked? Use `user-invocable` and `disable-model-invocation` intentionally.
- Is it a narrow, single workflow or a reusable multi-step process with bundled resources? Skills are best for multi-step workflows; prompts are better for single focused tasks.

## Quality Checks
- The skill has a discoverable description.
- The steps are ordered and practical.
- The workflow includes the key decision points and recovery steps.
- The completion criteria define when the task is “done.”
- The file is stored in the correct scope and path.

## Example Prompt to Trigger This Skill
- “Turn this debugging workflow into a reusable skill for the repo.”
- “Package our review checklist into a project skill.”
- “Create a personal skill for general workflow capture and reuse.”

## Related Customizations
- Create a project instruction when the guidance should apply broadly to all work.
- Create a prompt when the task is a single, focused action with input parameters.
- Create a custom agent when context isolation or tool restrictions are needed.
