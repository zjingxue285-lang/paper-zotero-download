# Zotero Attachment UI Notes

Read when a supported connector cannot attach files and desktop UI is available.

## Existing Parent, Stored Attachment

Select the exact parent in the requested collection. Verify its title in the item pane. Open Add Attachment and choose the operation equivalent to **Attach Stored Copy of File**, not Add Standalone File or Attach Link to File. Chinese labels vary; inspect the actual menu rather than hardcoding coordinates or menu indexes.

Type the verified local file path in the observed file-name field. Native file-dialog accessibility can lag behind its screenshot; reobserve rather than acting on stale indexes. Press Enter only after checking focus and path. A dialog closing is not proof of completion. PDF copying, renaming and indexing can finish later.

After import, expand the parent and verify the PDF child, preview title/page count and file metadata. Avoid counting expanded notes and attachments as additional studies. Keep the collection's parent count distinct from the displayed row count.

## Accidental Linked File

If the pilot created a link instead of a stored attachment, select only that child. Zotero may expose Tools > Manage Attachments > Convert Linked Files to Stored Files. Observe the actual dialog; preserve the source file by leaving any delete-original option unchecked. Follow the current environment's confirmation rules. Verify the new stored file and its hash before reporting success. Do not add a second PDF solely to correct storage mode.

## Automatic Find Full Text

The built-in Find Full Text command differs from third-party Get PDF plugins. It can fail even when the user's browser can download the paper. Use a verified lawful manual route as a fallback; failure is not proof that no free copy exists. Do not repeatedly queue the same request or cancel an unrelated pre-existing batch.

## Tool Failures

Window handles and element indexes are session-local. Never embed them in reusable instructions. After a context reset, use the runtime's documented recovery and select a newly observed window. If the runtime refuses browser control because it cannot verify the URL, stop that route and report the blocker; do not bypass it with shell-driven mouse/keyboard automation.

## Evidence Level

The development pilot verified three public PDFs on Windows in Zotero: a Frontiers PDF, a Scientific Reports copy from a national-library repository, and a Neural Regeneration Research PDF. These demonstrate the workflow, not guaranteed coverage of other publishers. Native-browser institutional downloading remains environment-dependent.
