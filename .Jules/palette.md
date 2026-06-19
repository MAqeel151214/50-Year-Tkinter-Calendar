## 2024-05-24 - Auto-update and Keyboard Submission
**Learning:** Users expect modern web-like interactions even in desktop apps; requiring manual button clicks after selecting from a dropdown or typing an entry is an outdated friction point.
**Action:** Always bind auto-update events to dropdowns (<<ComboboxSelected>>) and Enter key (<Return>) to text inputs in Tkinter interfaces by defaulting handler signatures to (event=None).
