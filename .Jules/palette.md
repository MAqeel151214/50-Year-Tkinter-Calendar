## 2026-06-23 - Modern Desktop UX Patterns
**Learning:** Desktop users expect web-like auto-submission for form fields (e.g., auto-updating on dropdown changes and submitting on Enter key). Standard Tkinter interfaces feel clunky if users are forced to click buttons for every state change.
**Action:** Bind `<<ComboboxSelected>>` to dropdown menus and `<Return>` to text entry fields, ensuring target function signatures accept an optional `event=None` argument for both manual and event-driven invocation.
