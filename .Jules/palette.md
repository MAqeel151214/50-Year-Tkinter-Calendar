## 2024-05-24 - Tkinter Event Bindings
**Learning:** Adding web-like interaction patterns (like auto-updating on dropdown selection and submitting on enter) in Tkinter significantly improves perceived usability. However, we must ensure functions connected via event bindings default to `event=None` so they can still be triggered programmatically without issues.
**Action:** Always add `event=None` to GUI callback function signatures and hook up `<<ComboboxSelected>>` and `<Return>` bindings by default for relevant widgets.
