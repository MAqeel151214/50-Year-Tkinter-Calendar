## 2024-05-24 - Auto-submission in Tkinter
**Learning:** Users expect modern web-like auto-submission in desktop apps, where dropdown selections and Enter key presses instantly update the UI.
**Action:** Consistently bind `<<ComboboxSelected>>` to dropdowns and `<Return>` to text entries, modifying target functions to accept an `event=None` argument.
