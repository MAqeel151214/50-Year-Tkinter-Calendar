## 2024-10-24 - [Tkinter Auto-submit Pattern]
**Learning:** Tkinter interfaces benefit greatly from modern web-like auto-submission patterns, like updating UI instantly when dropdowns are changed or when users press Enter in input fields.
**Action:** Bind `<<ComboboxSelected>>` to dropdowns and `<Return>` to text entries to trigger instant updates instead of requiring users to explicitly click submit buttons. Ensure bound functions accept an optional `event=None` parameter.
