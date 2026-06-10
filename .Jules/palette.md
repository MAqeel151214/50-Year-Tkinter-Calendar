## 2024-05-24 - Tkinter Event Binding for UX
**Learning:** Users naturally expect dropdown menus to immediately apply changes without clicking an "update" button, and expect pressing Enter in a text field to submit the form. Tkinter requires functions to accept an `event=None` parameter to work seamlessly for both event bindings and direct calls.
**Action:** Always bind `<<ComboboxSelected>>` to dropdowns and `<Return>` to entry fields in Tkinter apps to match web-like UX expectations, ensuring target functions have `event=None` in their signature.
