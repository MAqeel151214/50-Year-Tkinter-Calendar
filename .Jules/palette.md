## 2026-06-14 - Tkinter Auto-Update and Enter Submission
**Learning:** Tkinter default Comboboxes and Entry fields do not inherently submit or update on enter/selection, causing friction.
**Action:** Bind `<<ComboboxSelected>>` and `<Return>` to UI functions, adding `event=None` to function signatures for auto-triggering.
