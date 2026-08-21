# CLI Capability Map

This page is the compact capability map for the `ChatBili` CLI. Use it to review which commands are first-class entries and which are still boundary or planned slots. After scaffolding, update it with the real command tree; do not present unimplemented commands as available operations.

Importable Python functions are mapped in [Interface Tree](interface-tree.md). Current package boundaries are tracked in [Capability Map](capability-map.md).

## Top-Level Commands

```text
chatbili
├── --help                     # Show CLI help and registered commands
├── --version                  # Print the current package version
├── --tree                     # Print the registered CLI tree with parameter signatures
└── --tree-brief               # Keep command nodes and descriptions, but omit signatures
```

## Base Entries

```text
chatbili --help           # Verify the command is installed and inspect the current command tree
chatbili --version        # Verify the installed version
chatbili --tree           # Read back the CLI contract with parameter signatures
chatbili --tree-brief     # Read back the brief CLI contract without parameter signatures
```

`--help`, `--version`, `--tree`, and `--tree-brief` are the scaffolded verification entries. The top-level CLI registers both tree flags through ChatStyle's shared `add_tree_option()`. There are no business commands yet, so both trees currently contain only flag nodes without parameter signatures. Once commands are registered, `--tree` shows their parameter signatures and `--tree-brief` keeps their nodes and descriptions while omitting those signatures.

## Business Command Slots

```text
chatbili <group>          # Command group named after real package capability
├── <command>                  # Explain what this command does
└── <command>                  # Explain status, boundary, or checkpoint behavior
```

This is a structural placeholder, not a promise of future capability. Only document a command as implemented after the command, Python function, and tests exist.

## Status Contract

| Status | Meaning |
| --- | --- |
| Implemented | Command, function, and tests exist |
| Verified | Covered by CI, local smoke, or real-service practice |
| Planned / checkpoint | Keep only boundary notes; do not write operation tutorials before implementation |

## Implementation Contract

- Every implemented command must map back to a Python function, class, or service layer.
- If a command writes remote state, document credentials, permissions, dry-run/checkpoint behavior, or confirmation boundaries.
- When adding a command, update README, the interface tree, capability map, tests, and related flow pages together.
