## 2026-05-24 - Auto-update on Selection and Enter to Submit
**Learning:** Users expect dropdown menus to auto-update and input fields to submit via Enter key in desktop apps for smoother interactions. Missing these bindings breaks modern web-like UX expectations even in Tkinter apps.
**Action:** Always bind `<<ComboboxSelected>>` for dropdown menus and `<Return>` for text entries to matching actions, and ensure target functions accept an `event=None` argument.
