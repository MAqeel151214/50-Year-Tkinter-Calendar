## 2026-07-07 - Tkinter Event Bindings for Auto-Update
**Learning:** Users expect dropdown selections to immediately update the view (auto-update) and enter keys to submit forms in Tkinter applications, mirroring modern web UX.
**Action:** Bind `<<ComboboxSelected>>` to dropdowns and `<Return>` to entry fields, modifying target function signatures to accept an optional `event=None` argument.
