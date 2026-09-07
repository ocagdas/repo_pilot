# Coding Style and Design Rules

Repository formatters, linters, compiler settings, and selected standards are authoritative. This file records the design intent that automated tools cannot fully express.

## Selected standards

`CUSTOMISE: C and C++ language versions, compiler extensions policy, formatting configuration, naming rules, MISRA, AUTOSAR, CERT, internal rules, and deviation process.`

Do not apply a standard merely because it is common in embedded development.

## Design rules

`CUSTOMISE: Module boundaries, dependency direction, ownership model, error model, allocation policy, exception policy, logging, configuration, and test seams.`

## C and C++ review concerns

Review lifetime, ownership, aliasing, alignment, endianness, signedness, integer conversion, overflow, buffer bounds, cleanup paths, volatile and atomic semantics, interrupt context, lock order, data races, blocking, reentrancy, error propagation, and undefined or implementation defined behaviour.

## Constrained paths

`CUSTOMISE: Paths where dynamic allocation, blocking, locks, exceptions, recursion, logging, floating point, or unbounded work are restricted.`

## Generated and third party code

Do not edit generated or third party paths unless the task explicitly requires it and identifies the regeneration or patch maintenance process.

## Change discipline

Prefer the smallest coherent change. Do not mix functional work with unrelated cleanup, broad formatting, renaming, or speculative abstraction.

