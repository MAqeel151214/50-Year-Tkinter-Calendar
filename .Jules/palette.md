## 2026-06-16 - Tkinter Auto-submission and Event Binding
**Learning:** Users expect modern web-like interactions in desktop apps, such as auto-updating content on dropdown selection and submitting forms with the Enter key, to avoid redundant clicks.
**Action:** Always bind `<<ComboboxSelected>>` to dropdowns and `<Return>` to text entries to trigger their respective actions, ensuring handler functions accept an optional `event=None` argument.
