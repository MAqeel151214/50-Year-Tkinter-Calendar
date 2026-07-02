## 2024-05-24 - Auto-Updating Tkinter Inputs
**Learning:** Tkinter dropdowns and text entries lack default form-submission behavior expected in modern web UX, requiring explicit event binding (`<<ComboboxSelected>>` and `<Return>`) to auto-trigger functions.
**Action:** Always bind `<<ComboboxSelected>>` to comboboxes and `<Return>` to related entry fields while ensuring target functions accept an optional `event=None` parameter.
