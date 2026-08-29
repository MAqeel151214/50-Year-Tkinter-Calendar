## 2024-08-29 - Auto-update on selection
**Learning:** Tkinter dropdowns and text inputs lack web-like auto-submission patterns by default, requiring extra clicks and degrading the UX.
**Action:** Bind `<<ComboboxSelected>>` and `<Return>` to functions, ensuring they accept an optional `event=None` parameter.
