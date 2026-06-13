## 2024-11-09 - Modern Web UX Patterns in Desktop Apps
**Learning:** Desktop interfaces often lack the immediacy users expect from modern web applications. Users expect instant feedback when changing dropdown selections, and the ability to submit single-field forms by pressing the Enter key, reducing reliance on explicit mouse clicks.
**Action:** Always bind `<<ComboboxSelected>>` to Tkinter `ttk.Combobox` elements for auto-updating content, and bind `<Return>` to `tk.Entry` fields for seamless form submission. Update target function signatures to accept an optional `event=None` parameter.
