# DSA inbox automation (Cursor)

GitHub issue templates live in this repo. The **Cursor Automation** that reacts to those issues must be created once in your Cursor account (cloud agents cannot create Automations via API yet).

## Create the automation (one-time)

1. Open [cursor.com/automations](https://cursor.com/automations) (or Agents Window → Automations).
2. Click **New automation**.
3. **Repository:** `fadexadex/dsa-history` (branch: `master`).
4. **Trigger:** GitHub → **Issue label changed**
   - Label: `dsa-submit`
   - On added: **yes**
   - On removed: **no**
5. Optional second trigger: GitHub → **Issue comment** (so `@cursor process this` also works).
6. **Tools:** enable pull request creation if you want PRs; for this repo we usually **commit + push to `master`** instead — say that in the prompt.
7. Paste the prompt below into the automation instructions.
8. Save / activate.

### Automation prompt (copy/paste)

```text
You are processing a DSA submission for the fadexadex/dsa-history repo.

Trigger context: a GitHub issue was labeled `dsa-submit` (or someone asked you to process the issue).

Follow AGENTS.md in the repo exactly:

1. Read the issue title + body (day mode, day number, solutions, notes).
2. One issue may contain MULTIPLE solutions for the SAME day. Split on lines that are only `---`. Optional per-block headers: `# name` or `problem: name`.
3. Write one cleaned Python file per solution into the same day-N/ folder.
4. Filename = problem name (kebab-case) if provided, else main function/method name (kebab-case) + .py. No spaces.
5. Commit all files (one commit preferred) and push to master. Prefer `Add <stem>` or `Add <stem1>, <stem2>`.
6. Comment on the issue listing every file path + commit link, add `processed` if possible, and close the issue.

If the issue has no code, comment asking for a paste and stop.
Do not refactor unrelated files.
```

If you already created the automation, **update its Agent Instructions** to the prompt above so multi-solution issues work.

## Create the labels (one-time, if missing)

In the repo: **Issues → Labels → New label**

| Name | Color | Description |
|------|--------|-------------|
| `dsa-submit` | `#0E8A16` | Paste DSA solution; Cursor automation will commit it |
| `processed` | `#BFDADC` | Solution has been committed to the repo |

The issue form also requests `dsa-submit` automatically when you use the template.

## How to use it every day

1. Open [New issue](https://github.com/fadexadex/dsa-history/issues/new/choose).
2. Choose **Submit DSA solution(s)**.
3. Paste one or more solutions. Separate problems with a line that is only `---`. Optionally start each block with `# problem-name`.
4. Submit the issue — it should already have the `dsa-submit` label.
5. Wait for the Cursor automation to commit the file(s) and comment on the issue.

### Manual fallback (no automation)

On any issue, comment:

```text
@cursor Process this DSA submission per AGENTS.md. Commit and push to master.
```

## Privacy note

This repository is **public**. Issue bodies (including pasted solutions) are visible to anyone. That is usually fine for LeetCode practice code. If you ever need private pastes, make the repo private or use a private fork — collaborators can still open issues.
