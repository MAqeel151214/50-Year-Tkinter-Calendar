## 2024-05-18 - Tkinter Auto-Update on Selection
**Learning:** Users of desktop GUI applications expect immediate feedback when changing dropdown selections (like month or year) rather than requiring an explicit "submit" or "update" button click. Similarly, form submissions should respond to the Return/Enter key.
**Action:** Bind `<<ComboboxSelected>>` to dropdown menus for auto-updating content and bind `<Return>` to text entry fields, ensuring target function signatures accept an optional `event=None` argument.
