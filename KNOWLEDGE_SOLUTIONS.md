# Code knowledge and graph integration research

Researched 8 September 2026 from maintainer repositories and official documentation. This section records the original candidate research. Subsequent implementation added CGC and Sourcegraph adapters; see project/ai_workflow/knowledge_backends.md and VALIDATION.md. Actual CGC indexing and same-machine bundle reuse were exercised; Sourcegraph has protocol-fixture evidence only. No token-saving benchmark was run. Documentation on moving branches can change; pin a release/commit when piloting.

## Recommendation for this project

Shortlist CodeGraphContext for portable code graphs, Serena as a symbol-retrieval baseline, and Sourcegraph for an established centralised team service. GitNexus has useful bounded MCP responses, but its current noncommercial license makes licensing a prerequisite for a commercial pilot. Select using a representative C/C++ and Python repository, not popularity or headline savings alone.

Our trunk snapshot/branch overlay contract should remain independent of the backend. I found useful indexing, query and sharing features, but did not establish that any candidate supplies our complete exact-base, build-context-aware overlay composition workflow out of the box. Branch/revision query support is not proof of reusable local semantic deltas.

## Candidates

| Candidate | Documented integration and strengths | Fit and remaining questions |
| --- | --- | --- |
| Sourcegraph | Official MCP endpoints expose code search, bounded file reads, definitions/references and history. Revision parameters, authentication and repository permissions support centralised team access. | Strong central service candidate. Need deployment/licensing assessment and a design for local dirty worktrees; revision-aware server queries do not automatically supply portable overlay bundles. [Official MCP documentation](https://sourcegraph.com/docs/api/mcp) |
| Serena | MCP tools retrieve symbols, references and file outlines rather than requiring whole-file reads. Its default analysis backend uses language servers, with C/C++ and Python among supported languages. | Useful local baseline for reducing navigation context. It is an IDE-style retrieval layer, not evidence of a ready-made shared trunk graph artifact format. Pilot startup cost and compiler configuration. [Maintainer README](https://github.com/oraios/serena) |
| CodeGraphContext | MCP and CLI, persistent graph backends, filesystem watching, pre-indexed `.cgc` bundles, and optional SCIP indexing. C/C++ SCIP uses scip-clang with a compilation database; documentation describes fallback to Tree-sitter when unavailable. | Closest documented match to our portable graph direction. Validate bundle relocation, schema/version compatibility, deletion handling and target-dependent graph correctness; do not equate heuristic fallback with compiler-derived coverage. [Maintainer README](https://github.com/CodeGraphContext/CodeGraphContext) |
| GitNexus | Local CLI/MCP graph queries, symbol context and impact queries; configurable MCP response budgets and parser caching. | Promising local candidate. Documentation mentions incremental operation/cache controls while its roadmap still lists changed-file incremental indexing as unfinished; validate actual behaviour at a pinned revision. Token budgets are estimates, not verified end-to-end savings. [Maintainer README](https://github.com/abhigyanpatwari/GitNexus) |
| Neo4j official MCP | Official MCP access to a graph database. | Suitable storage/query infrastructure if we own extraction and schemas. It does not by itself turn C++ source and build variants into a correct code graph. [Official repository](https://github.com/neo4j/mcp) |
| Graphiti | Maintainer project for incremental temporal knowledge graphs, with an MCP server for agent integration. | Candidate for evolving project facts, decisions and conversational knowledge. Assess separately from compiler facts; temporal memory is not Git branch semantics. [Maintainer repository](https://github.com/getzep/graphiti) |
| Microsoft GraphRAG | Knowledge-graph-based retrieval methodology with indexing/query tooling. Its repository explicitly describes the code as a demonstration, not an officially supported Microsoft offering, and warns that indexing can be expensive. | Potential document/architecture knowledge layer. I would not choose it as our first compiler/code indexing backend. [Maintainer README](https://github.com/microsoft/graphrag) |

For compiler-derived C/C++ facts, also examine [scip-clang](https://github.com/sourcegraph/scip-clang). Treat it as an extraction component behind retrieval adapters, rather than a complete MCP knowledge service.

## Reputation and evidence

CodeGraphContext and Serena currently publish MIT licenses. GitNexus currently publishes PolyForm Noncommercial 1.0.0, so it should not be adopted as this commercial tooling package's default backend without suitable licensing terms. These are observations of the current license files, not a dependency license audit. [CodeGraphContext license](https://github.com/CodeGraphContext/CodeGraphContext/blob/main/LICENSE), [Serena license](https://github.com/oraios/serena/blob/main/LICENSE), [GitNexus license](https://github.com/abhigyanpatwari/GitNexus/blob/main/LICENSE).

Sourcegraph and Neo4j provide vendor-owned integration documentation. Serena, CodeGraphContext and GitNexus expose inspectable source and public issue histories, but this review does not establish production reliability on our repositories. Microsoft's authorship does not override GraphRAG's stated support limits. Check release activity, licenses, unresolved correctness issues and dependencies at the exact version selected for a pilot.

No comparable, independently reproduced token-reduction figure was established in the reviewed sources. Maintainer claims, agent testimonials and a response-size cap are different forms of evidence. A tool may return fewer tokens per call while causing more calls, missing dependencies, or shifting LLM cost into indexing.

## Pilot acceptance plan

Use the same repository revision, build targets, model/client, prompts and task set for source-only and assisted runs. Include symbol lookup, cross-file impact analysis, malformed-input fixes, header changes, renames/deletions and a branch whose trunk has advanced independently.

Measure:

- Input/output tokens, tool response tokens, tool-call count and any LLM indexing/summarisation cost. Report cached-token billing separately from context volume.
- Correctness and evidence quality against source/build results, not just answer confidence.
- Cold indexing, warm startup, incremental refresh, peak memory, artifact size and transfer volume.
- Coverage for conditional compilation, generated headers, Python dynamic behaviour and unresolved references.
- Reuse between different clone paths, two build variants, release/RC trunks and dirty worktrees.

Begin with Serena/source search as retrieval baselines and CodeGraphContext as the first portable-graph experiment. Compare GitNexus at a pinned version only after resolving licensing for the intended use. Consider Sourcegraph if central hosting and team access outweigh offline bundle requirements. Keep graph publication and branch composition in our adapter contract until a backend proves it can implement them correctly.
