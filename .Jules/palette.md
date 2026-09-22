## 2023-10-24 - Modern Web-like Auto-submission in Tkinter
**Learning:** Desktop Tkinter applications can feel antiquated to web-native users when explicit submit buttons are required for simple selection changes.
**Action:** Consistently bind `<<ComboboxSelected>>` to dropdowns and `<Return>` to text entries to enable instant UI updates without explicit button clicks, modifying target functions to accept an optional `event=None` parameter.
