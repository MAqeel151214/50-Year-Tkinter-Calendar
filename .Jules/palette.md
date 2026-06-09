## 2024-05-18 - Keyboard Navigation and Auto-Updating
**Learning:** Users naturally expect modern web-like behaviors even in desktop GUI apps (like Tkinter). Dropdowns that require a separate "Submit/Update" click are unintuitive; auto-updating on selection (`<<ComboboxSelected>>`) and submitting forms on Enter (`<Return>`) significantly improves perceived responsiveness and usability.
**Action:** Default to binding `<<ComboboxSelected>>` for all select-menus and `<Return>` for all primary text input fields in desktop applications to avoid requiring redundant button clicks.
