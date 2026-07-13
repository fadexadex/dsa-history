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

1. Read the issue title + body (day mode, day number, problem name, code, notes).
2. Write a cleaned Python file into the correct day-N/ folder.
3. Filename = problem name (kebab-case) if provided, else main function/method name (kebab-case) + .py. No spaces.
4. Commit and push to master. Prefer commit message like `Add <stem>` (casual messages are also fine).
5. Comment on the issue with the file path + commit link, add `processed` if possible, and close the issue.

If the issue has no code, comment asking for a paste and stop.
Do not refactor unrelated files.
```

## Create the labels (one-time, if missing)

In the repo: **Issues → Labels → New label**

| Name | Color | Description |
|------|--------|-------------|
| `dsa-submit` | `#0E8A16` | Paste DSA solution; Cursor automation will commit it |
| `processed` | `#BFDADC` | Solution has been committed to the repo |

The issue form also requests `dsa-submit` automatically when you use the template.

## How to use it every day

1. Open [New issue](https://github.com/fadexadex/dsa-history/issues/new/choose).
2. Choose **Submit DSA solution**.
3. Paste your code (messy is fine). Optionally set day / problem name.
4. Submit the issue — it should already have the `dsa-submit` label.
5. Wait for the Cursor automation to commit the file and comment on the issue.

### Manual fallback (no automation)

On any issue, comment:

```text
@cursor Process this DSA submission per AGENTS.md. Commit and push to master.
```

## Privacy note

This repository is **public**. Issue bodies (including pasted solutions) are visible to anyone. That is usually fine for LeetCode practice code. If you ever need private pastes, make the repo private or use a private fork — collaborators can still open issues.
