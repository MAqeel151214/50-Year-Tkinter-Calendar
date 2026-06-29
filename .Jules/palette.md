## 2024-05-24 - Auto-submit Pattern for Tkinter
**Learning:** Users expect web-like auto-submit interactions in desktop apps. Requiring explicit clicks for dropdown changes or simple text entry (like a day number) adds unnecessary friction.
**Action:** Implement auto-update patterns by binding `<<ComboboxSelected>>` to dropdowns and `<Return>` to entry fields, ensuring event handlers accept an `event=None` parameter for compatibility.
