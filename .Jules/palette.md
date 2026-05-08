## 2026-05-08 - Added Event Bindings
**Learning:** Tkinter interfaces benefit significantly from common web patterns like auto-updating dropdowns and enter-to-submit. Binding `<<ComboboxSelected>>` to dropdowns and `<Return>` to inputs makes the interface feel more responsive and reduces the number of clicks required.
**Action:** When creating forms in Tkinter, always consider if `<<ComboboxSelected>>` or `<Return>` bindings would improve the workflow. Remember to make the callback functions accept an optional `event=None` argument to be triggered both by events and direct calls.
