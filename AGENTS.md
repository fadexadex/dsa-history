# Agent instructions — dsa-history

This repo stores daily DSA practice solutions. When processing a **Submit DSA solution** GitHub issue (label `dsa-submit`), follow this pipeline exactly.

## Goal

Take pasted / messy solution code from the issue and commit a clean file into the correct `day-N/` folder on `master` (or the default branch), then mark the issue done.

## Steps

1. **Read the issue body**
   - Extract: day mode, optional day number, optional problem name, solution code, notes.
   - Code may be incomplete, mis-indented, or mixed with Excalidraw pseudocode. That is expected.

2. **Choose the day folder**
   - **Latest day folder (default):** use the highest existing `day-N/` directory.
   - **Create next day folder:** create `day-(N+1)/` where `N` is the current highest.
   - **Specific day:** use `day-<number>/` (create it if missing).

3. **Choose the filename**
   - Prefer **problem name** from the issue when provided → kebab-case, e.g. `Merge Sorted Array` → `merge-sorted-array.py`.
   - Otherwise derive from the **main function / method** definition → kebab-case, e.g. `def containsDuplicate` → `contains-duplicate.py`, `def twoSum` → `two-sum.py`.
   - Always use a `.py` extension unless the code is clearly another language.
   - Do **not** use spaces in filenames.
   - If the file already exists in that day folder, append a short disambiguator (e.g. `two-sum-alt.py`) or update only if the issue clearly asks to replace it.

4. **Normalize the code**
   - Keep the author’s logic; fix indentation/syntax enough for a readable practice file.
   - Preserve useful comments; strip obvious junk / broken Excalidraw noise that is not meaningful.
   - Match existing style in nearby day folders (often LeetCode `class Solution` + method, sometimes a bare `def`).
   - If notes were provided, put a short comment block at the top of the file.

5. **Commit and push**
   - Commit message style for this repo is casual / short (examples: `steady`, `progress`, `Add merge-sorted-array`). Prefer: `Add <filename-stem>` or a short vibe message.
   - Push to the default branch (`master`) unless the issue asks for a PR.
   - Do **not** invent unrelated refactors.

6. **Close the loop on the issue**
   - Comment on the issue with: path of the new file, commit SHA or link, and one-line summary.
   - Add / replace label: remove `dsa-submit` if you can, add `processed` if the label exists.
   - Close the issue when the file is successfully pushed.

## Non-goals

- Do not rewrite solutions into a different algorithm unless asked.
- Do not add README/docs/tests unless asked.
- Do not process issues that lack solution code.
