## 2026-05-16 - Add UX keyboard events to Tkinter
**Learning:** Tkinter forms are more accessible and fluid when bound to keyboard/interaction events like `<Return>` for entry fields and `<<ComboboxSelected>>` for menus, eliminating the need to always click a button. Event handlers need an optional `event=None` argument to avoid crashing when triggered programmatically.
**Action:** Always add keyboard/event bindings (e.g. `<Return>`, `<<ComboboxSelected>>`) to Tkinter interactive elements where appropriate and ensure handler signatures accept optional event arguments.
