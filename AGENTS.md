# Agent instructions — dsa-history

This repo stores daily DSA practice solutions. When processing a **Submit DSA solution(s)** GitHub issue (label `dsa-submit`), follow this pipeline exactly.

## Goal

Take pasted / messy solution code from the issue and commit **one or more** clean files into the correct `day-N/` folder on `master` (or the default branch), then mark the issue done.

One issue may contain **multiple problems for a single day**. Process every solution in that issue in one run.

## Steps

1. **Read the issue body**
   - Extract: day mode, optional day number, solutions block, optional notes.
   - Older issues may use a single `Solution code` / `Problem name` field — still support that.
   - Code may be incomplete, mis-indented, or mixed with Excalidraw pseudocode. That is expected.

2. **Split into individual solutions**
   - Prefer splitting the solutions field on a line that is only `---` (horizontal rule / separator).
   - Within each block, if the first non-empty line looks like a problem header, use it as the problem name:
     - `# two-sum` / `## Two Sum`
     - `problem: two-sum` / `name: two-sum`
   - If there is **no** `---` separator, treat the whole paste as **one** solution (unless there are clearly separate top-level problem headers with distinct main functions — then split on those headers).
   - Skip empty blocks after splitting.
   - Shared **Day notes** may apply to all files; if notes are labeled per problem (`two-sum: ...`), attach each note only to that file.

3. **Choose the day folder** (once for the whole issue)
   - **Latest day folder (default):** use the highest existing `day-N/` directory.
   - **Create next day folder:** create `day-(N+1)/` where `N` is the current highest.
   - **Specific day:** use `day-<number>/` (create it if missing).
   - All solutions from this issue go into that same folder.

4. **Choose each filename**
   - Prefer the **problem name** from that block’s header (or legacy single problem-name field) → kebab-case, e.g. `Merge Sorted Array` → `merge-sorted-array.py`.
   - Otherwise derive from the **main function / method** definition → kebab-case, e.g. `def containsDuplicate` → `contains-duplicate.py`, `def twoSum` → `two-sum.py`.
   - Always use a `.py` extension unless the code is clearly another language.
   - Do **not** use spaces in filenames.
   - If a file already exists in that day folder, append a short disambiguator (e.g. `two-sum-alt.py`) or update only if the issue clearly asks to replace it.
   - If two blocks would produce the same filename, disambiguate (`two-sum-2.py`, etc.).

5. **Normalize each solution**
   - Keep the author’s logic; fix indentation/syntax enough for a readable practice file.
   - Preserve useful comments; strip obvious junk / broken Excalidraw noise that is not meaningful.
   - Match existing style in nearby day folders (often LeetCode `class Solution` + method, sometimes a bare `def`).
   - If notes were provided for that problem (or shared day notes), put a short comment block at the top of the file.

6. **Commit and push**
   - Write **all** new files from this issue, then commit once (preferred) or in a small batch.
   - Commit message: `Add <stem>` for one file, or `Add <stem1>, <stem2>, …` / a short vibe message for multiple.
   - Push to the default branch (`master`) unless the issue asks for a PR.
   - Do **not** invent unrelated refactors.

7. **Close the loop on the issue**
   - Comment with a list of every file path created, the commit SHA or link, and a one-line summary.
   - Add / replace label: remove `dsa-submit` if you can, add `processed` if the label exists.
   - Close the issue when all solutions were successfully pushed.
   - If some blocks failed (no code / cannot infer a name), still commit the successful ones, and list failures in the issue comment.

## Non-goals

- Do not rewrite solutions into a different algorithm unless asked.
- Do not add README/docs/tests unless asked.
- Do not process issues that lack solution code.
- Do not put solutions from one issue into different day folders unless the issue explicitly asks for that.
