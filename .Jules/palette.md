## 2024-05-24 - Auto-updating forms and keyboard bindings
**Learning:** Users in desktop Tkinter apps benefit from modern web-like patterns such as auto-submitting on combobox selection and submitting text entries on Enter, rather than relying exclusively on discrete buttons.
**Action:** Bind `<<ComboboxSelected>>` to dropdowns and `<Return>` to entries, ensuring callbacks accept `event=None` for programmatic compatibility.
