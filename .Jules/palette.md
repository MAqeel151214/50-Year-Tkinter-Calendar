## 2024-05-16 - [Keyboard & Auto-Update UX]
**Learning:** Users expect Tkinter widgets to feel like modern web apps, meaning form elements should submit on `<Return>` and dropdowns should trigger updates immediately without needing an explicit "Submit" or "Show" button.
**Action:** Always bind `<<ComboboxSelected>>` to auto-update actions for dropdowns and `<Return>` to form submission functions, while ensuring the bound functions accept an `event=None` parameter.
