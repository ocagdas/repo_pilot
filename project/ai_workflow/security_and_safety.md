# Security and Safety Boundaries

## Protected information

Never place credentials, private keys, signing material, customer data, proprietary logs, production data, or secrets in prompts, patches, reports, fixtures, or handoffs.

## Human authority

The following remain human controlled unless an organisation policy defines a stronger external approval mechanism:

1. Merge and release approval.
2. Security or safety risk acceptance.
3. Production access or mutation.
4. Device flashing, fuse writes, bootloader changes, and hardware protection changes.
5. Package publication and artefact signing.
6. Approval of ABI, protocol, persistent format, or rollback incompatibility.
7. Acceptance of static analysis or compliance deviations.

## Safe execution

Prefer read only inspection and dry runs while scoping work. Before a destructive or difficult to reverse operation, resolve the exact target, explain impact and recovery, and obtain the configured approval.

## Project specific controls

`CUSTOMISE: Threat model, secure development requirements, safety classification, regulated processes, restricted commands, approved environments, and escalation contacts.`

