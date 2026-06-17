## 2026-06-17 - Event Binding for Seamless Interactions
**Learning:** Users naturally expect immediate feedback in modern Tkinter applications. Requiring manual button clicks after selecting from a dropdown or typing an entry creates unnecessary friction and breaks the web-like UX paradigm.
**Action:** Bind `<<ComboboxSelected>>` to auto-update on dropdown changes and `<Return>` to submit forms directly from text entries, while ensuring the target callback functions accept an optional `event=None` argument to remain compatible with both programmatic calls and event bindings.
