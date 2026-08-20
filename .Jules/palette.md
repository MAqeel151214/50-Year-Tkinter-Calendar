## 2026-08-20 - Auto-updating dropdowns and Enter key support
**Learning:** Adding auto-update to dropdown menus (`<<ComboboxSelected>>`) and Enter key support (`<Return>`) to forms makes the GUI feel much faster and reduces unnecessary clicks, significantly improving the UX. Binding standard tkinter event loops requires optionally taking the `event` parameter.
**Action:** When adding standard event bindings for elements that can also be called programmatically, modify the target function to accept an `event=None` argument to satisfy both use cases seamlessly.
