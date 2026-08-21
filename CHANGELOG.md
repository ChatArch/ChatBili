# Changelog

## 0.0.2 - 2026-08-21

### Added

- Added `chatbili --tree-brief` for a command-and-description view without parameter signatures.

### Changed

- Migrated the top-level Click tree output to ChatStyle's shared runtime; `chatbili --tree` now includes parameter signatures by default.
- Updated the supported runtime ranges to `chatstyle>=0.2.0,<0.3.0` and `chatenv>=0.2.10,<0.3.0`.
