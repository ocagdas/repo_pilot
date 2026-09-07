# AI Context Entry Point

This is the single, provider neutral entry point for any AI assistant or agent working in this repository.

## Start here

At session start:

1. Read this file, `ai_workflow/context.yaml`, and its session requirements.
2. Resolve the requested action through `ai_workflow/actions.yaml`. Read the action contract and relevant activity and domain documents. Interpret the complete request; do not select an action from an isolated keyword.
3. For conceptual discussion, no repository bootstrap is needed. For a strictly read only session, inspect source directly and do not write caches. The user may separately authorise local knowledge refresh.
4. For code work where local cache writes are allowed, run `python3 ai_workflow/tools/repo_bootstrap.py prepare --pretty` if the environment supports it.
5. Read the returned JSON, including semantic status even when `action_required` is `none`. Follow `ai_workflow/bootstrap_analysis.md` for requested analysis. Start with a repository map and deepen the components relevant to the task; record coverage gaps explicitly.
6. Read the active task and specifications, inspect current code and build configuration, then apply the selected workflow and gates. Existing user authorisation counts; do not request the same approval again.

If bootstrap fails in `auto` or `disabled` mode, report the failure and inspect current source. If semantic mode is `required`, an unavailable or incomplete current index blocks dependent code work. Do not silently downgrade that mode. Never claim cached knowledge is current following a failed check.

Compatible partial semantic layers may inform navigation, but missing overlays require direct source checks, including deleted symbols and affected callers. Only a complete current view can satisfy required mode. Configured update commands are adapter instructions, not automatically executed by bootstrap. Never update the immutable base during an ordinary branch session.

If the provider has its own instruction file, that file is only an adapter. It may help the provider discover this entry point, but it must not redefine or weaken the canonical rules.

## Authority and precedence

Runtime system instructions, tool permissions, and organisational controls remain authoritative. Within repository guidance, use this order:

1. Explicit instructions from the authorised human for the current task.
2. Applicable legal, safety, security, and organisational policy.
3. The approved task and its acceptance criteria.
4. Repository specifications and architecture decisions listed in `ai_workflow/context.yaml`.
5. The canonical material in `ai_workflow/`.
6. Provider adapters such as `AGENTS.md`, `.cursor/`, `CLAUDE.md`, or Copilot instructions.

Do not silently resolve a material conflict. Stop, identify the conflicting sources, and request a decision.

## Core engineering rule

Make the smallest correct change that satisfies the approved task while preserving observable behaviour, real time constraints, hardware assumptions, compatibility, portability, and maintainability.

Facts, assumptions, estimates, and unverified claims must be labelled separately. A command counts as evidence only when it was actually run and its result was observed. An AI judgement never replaces a deterministic gate or a required human approval.

## Session bootstrap

The executable bootstrap check above is the canonical session trigger. Provider instruction files import or point to this file, so capable agents are instructed to run the same check. Markdown instructions are behavioural guidance, not guaranteed execution. A session wrapper, provider hook, or CI job is required when enforcement is mandatory.

A provider neutral opening instruction can be as short as:

```text
Read AI_CONTEXT.md completely and follow its loading instructions. Then inspect the task I provide. Do not edit until you have reported the relevant constraints, acceptance criteria, assumptions, and proposed plan.
```

For a role specific session, append one of: `planner`, `implementer`, `tester`, `debugger`, `reviewer`, `verifier`, or `orchestrator`. The neutral role contracts are indexed by `ai_workflow/context.yaml` and stored under `ai_workflow/roles/`.

## Action shorthand

The requested intent selects the reusable contract in `ai_workflow/actions.yaml`. For example, `analyse TASK_142`, `index the current branch`, `design the telemetry change`, or `implement TASK_142` supplies the operating method without repeating it in the prompt.

Read only actions must not mutate files merely because a possible improvement was discovered. The `implement` action invokes the complete development, focused checking, final review, correction, verification, and completion reporting lifecycle.
