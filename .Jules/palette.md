## 2024-10-27 - Auto-update and Keybindings in Tkinter
**Learning:** Users naturally expect immediate feedback when selecting items from a dropdown and attempt to press Enter/Return to submit forms in desktop applications. Explicit buttons are not always the intuitive first interaction point for form submissions.
**Action:** Always bind `<<ComboboxSelected>>` to auto-update dependent UI elements and bind `<Return>` to form submission functions. Ensure target functions accept an optional `event=None` parameter to handle both programmatic and event-driven invocations without raising errors.
