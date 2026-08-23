## 2024-05-24 - Dropdown Selection Updates
**Learning:** In Tkinter applications, requiring users to click a "Show Calendar" button after changing the month or year from a dropdown menu is an unnecessary step. The UI feels unresponsive compared to modern web applications.
**Action:** Bind the `<<ComboboxSelected>>` event to the dropdowns to automatically trigger the update action, reducing friction.

## 2024-05-24 - Form Submission via Enter Key
**Learning:** Users naturally expect to be able to submit forms (like the "Find Day of Week" entry) by pressing the Enter key. In Tkinter, this is not enabled by default for text entries.
**Action:** Bind the `<Return>` event to the text entry field to improve keyboard accessibility and navigation flow.
