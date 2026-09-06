# Repository guidance

This repository is a Chinese-language research handoff for tea-shoot active vision. Read `README.md`, `docs/CURRENT_STATE.md`, and `docs/DECISIONS.md` before proposing new work. User instructions in the active conversation take precedence.

- Preserve the distinction between user constraints, assistant proposals, published evidence, and untested hypotheses.
- Use `docs/TASKS.md` as the task-status source; search existing DOI/title/query indexes before repeating literature work.
- The Sensors 2025 count of 110 shoots does not establish autonomous region-wide visual discovery. Do not reintroduce that withdrawn inference.
- Do not require persistent target identity unless reusing identity-dependent evidence. Coarse off-camera locations are allowed. Rare entanglement and detailed map aging are conditional topics.
- Region-level perception experiments do not require a complete harvesting product. Separate detection, grading, physical picking, and timing denominators.
- Never invent hardware models, results, source-reading depth, JCR quartiles, or acceptance probabilities.
- Keep original files in `archive/reports/` unchanged. Add corrections to current documents and the decision log.
- Add source records and query records to their JSON inputs; regenerate CSV indexes with `python tools/build_indexes.py`.
- Run `python tools/validate_repository.py` after documentation changes. No model training or broad test runs are implied for documentation maintenance.
- Do not send collaborators direct messages, request reviews, or assign people without user authorization. Repository documentation is the handoff.
