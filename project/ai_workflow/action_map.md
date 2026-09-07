# Action routing

Interpret the complete user request. These are logical command names; installed integrations determine invocation syntax. Read the installed command if no slash command interface exists.

| User intent | Command or procedure | Mutation scope |
| --- | --- | --- |
| Discuss or explore | speckit.engineering.discuss | Conversation only |
| Analyse repository or diagnose | speckit.engineering.assess | Read source, report findings |
| Specify behaviour | speckit.specify | Feature specification |
| Design or plan | speckit.plan | Feature plan |
| Break down work | speckit.tasks | Canonical tasks.md |
| Analyse artefact consistency | speckit.analyze | Read specifications |
| Implement or fix authorised work | speckit.implement | Agreed source changes |
| Test | speckit.engineering.test | Check outputs only |
| Review | speckit.engineering.review | Review report when authorised |
| Refresh knowledge | speckit.engineering.bootstrap | Local cache |
| Close or report completion | speckit.engineering.report | Derived completion report |

Design that has no feature yet can remain a discussion. Do not manufacture a specification from a vague request. Use the user's agreed scope to decide when a new feature specification is appropriate. Review and test instructions do not grant permission to repair source unless the request also authorises implementation.
