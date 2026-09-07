# Domain guidance

Choose active domains in project.yaml and load only those relevant to the task. This is agent guidance; an external runner must enforce command selection and required gates. A mixed repository can use several domains with different target commands. Record which gate groups apply and why others do not.

## Common core

Use explicit scope, acceptance criteria, component ownership, dependency boundaries, command evidence and completion status. Keep analyse, discuss and design free of source changes. Implementation includes coherent slices, focused checks, checkpoint review, final validation and correction. Use the configured formatter and test tooling. CUSTOMISE means unconfigured, never a successful or skipped gate.

## Embedded C and C++

Record language standard, compiler version, target triple, sysroot, board, build configuration, feature macros, generated headers and linker script. Keep semantic indexes separate for incompatible compilation contexts, even for the same commit. Review ownership, undefined behaviour, interrupt context, atomic access, DMA and cache coherence, timing, stack and heap, allocation constraints, ABI and wire compatibility. Host tests do not establish hardware timing or electrical behaviour. Record hardware and firmware revisions with target evidence. Apply only the standards explicitly selected by the project.

## Python

Record Python version, package manager and dependency lock. Configure formatter, linter, type checker and tests through the existing project files and commands.yaml. Review mutable defaults, exception handling, resource cleanup, concurrency and cancellation, numerical dtype conversions, packaging and public interfaces. Use clean environment reproduction where dependency changes matter. Compilation databases are unnecessary for pure Python; native extension components use the relevant C or C++ context.

## Data science

Record dataset identifiers and hashes, schema, provenance, feature pipeline, split definition, seed, dependency environment and experiment configuration. Keep private data and large models outside the prompt and Git workflow pack. Reference approved storage and immutable versions instead.

Check train and evaluation leakage, temporal ordering, group separation, missing data, imbalance, baselines, metric choice and uncertainty. Fix the final evaluation protocol before using the held out set. Record tuning separately from final evaluation. Preserve failed experiments and explain changes in metrics. Reproduce notebooks from a fresh kernel and move reusable transformations into tested modules when appropriate. Never treat a favourable metric alone as completion. Record nondeterminism and compute cost limits.

## Command selection

Use existing commands.yaml IDs where suitable, with project specific command values. Add domain specific command IDs for typing, data validation, notebook execution, training smoke tests and evaluation when needed, and include them in the selected completion profile. Profile selection is declarative until a runner is installed. No universal default commands or performance thresholds are assumed.
