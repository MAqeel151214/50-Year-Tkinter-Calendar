## 2024-05-24 - Auto-submission interaction patterns
**Learning:** Users of modern desktop applications expect web-like auto-submission behaviors, such as updating state immediately upon dropdown selection and pressing Return to submit text fields.
**Action:** Consistently bind <<ComboboxSelected>> and <Return> to primary actions using lambda wrappers to maintain function signatures without breaking mock tests.
