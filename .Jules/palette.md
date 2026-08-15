## 2026-08-15 - Interactive Tkinter Event Binding
**Learning:** Adding web-like auto-updating via `<<ComboboxSelected>>` and `<Return>` bindings dramatically improves desktop Tkinter app usability by reducing required clicks, but requires adjusting bound function signatures to accept the `event` parameter.
**Action:** Always map primary interactive patterns (like Enter-to-submit and select-to-update) in desktop GUIs to match web UX expectations, ensuring function signatures gracefully handle both manual and event-driven invocations.
