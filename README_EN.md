# Turn WeRead Highlights into EPUB Ebooks

[简体中文](README.md) | **English**

**读书成册 (Reading Notes to EPUB)** — a macOS walkthrough and personal-use Python conversion script for turning your own WeRead reading highlights and notes into EPUB ebooks.

WeRead (微信读书) is a Chinese ebook-reading service. This project is **not an official WeRead integration** and does **not** connect to WeRead directly. Instead, a third-party Obsidian plugin exports your synced highlights as Markdown files, and the local script converts those files into EPUBs with generated PNG covers.

## How it works

```text
WeRead → Obsidian + Weread Plugin → Markdown (.md) → readnotes.py + Pandoc → EPUB
```

**What this workflow does**

- Sync your own WeRead highlights and notes to Markdown through the third-party Obsidian Weread Plugin.
- Convert multiple Markdown notes into EPUB 3 files in one batch.
- Generate a colored PNG title cover for each book.
- Add a leading numeric prefix (such as `012-`) to the cover when present in the Markdown filename.
- Skip EPUBs that are already at least as new as their Markdown source files.

**Platform:** macOS (primarily intended for Apple Silicon Macs). Installation and plugin interfaces may differ by version. The script has also been checked against synthetic Markdown samples; the complete workflow may vary in a real Obsidian/WeRead setup.

## Requirements

1. [Obsidian](https://obsidian.md/) — stores the synced notes.
2. [Obsidian Weread Plugin](https://github.com/zhaohongxuan/obsidian-weread-plugin) — a third-party plugin that syncs your WeRead highlights and notes into Obsidian.
3. [Pandoc](https://pandoc.org/installing.html) — converts Markdown to EPUB.
4. [Python 3](https://www.python.org/downloads/macos/) — runs the local conversion script.
5. [Pillow](https://pillow.readthedocs.io/) — a Python library used to generate cover images.

## Step-by-step setup

### 1. Sync your WeRead notes with Obsidian

1. Install Obsidian and open or create a vault.
2. In **Settings → Community plugins**, search for **Weread Plugin**, install it, and enable it.
3. Open the plugin settings. Follow its current instructions to sign in to your own WeRead account. In versions supporting API Key authentication, use **Scan to get** in the API Key section and complete the sign-in steps.
4. Click the WeRead icon in Obsidian's sidebar, or open the command palette with `Cmd + P` and run `Sync Weread`.
5. Open the resulting notes folder and confirm that its `.md` files contain your actual highlights or notes. Remember the location of that folder.

**Important:** The Obsidian plugin handles syncing, not this repository's conversion script. Its settings and authentication flow may change; refer to the [plugin's own documentation](https://github.com/zhaohongxuan/obsidian-weread-plugin) if syncing fails. The plugin may overwrite synced note files on later syncs, so keep any personal edits in separate notes or backups.

### 2. Install Pandoc and Python 3

Install Pandoc and Python 3 from the links above. Open the **Terminal** app on your Mac and check that both commands work:

```bash
pandoc --version
python3 --version
```

If either command is not found, finish installing the corresponding tool before continuing.

### 3. Create a Python environment and install Pillow

Run these commands in Terminal (one-time setup):

```bash
python3 -m venv "$HOME/readnotes-venv"
"$HOME/readnotes-venv/bin/python" -m pip install Pillow
```

### 4. Download the script

Open [`readnotes.py`](readnotes.py), choose **Raw** or **Download raw file**, and save it to your **Mac Desktop** with the exact filename `readnotes.py` (not `readnotes.py.txt`).

### 5. Convert your notes

Run:

```bash
"$HOME/readnotes-venv/bin/python" "$HOME/Desktop/readnotes.py"
```

When the macOS folder picker appears, select the folder containing the Markdown notes synced from WeRead. The script searches its subfolders for `.md` files as well.

Alternatively, pass a folder path directly:

```bash
"$HOME/readnotes-venv/bin/python" "$HOME/Desktop/readnotes.py" "/path/to/your/markdown-notes"
```

### 6. Find your EPUBs

The converted files appear in:

```text
~/Desktop/读书成册 EPUB/
```

For example:

```text
书名.md         → 书名｜笔记.epub
012-书名.md     → 012-书名｜笔记.epub
```

The `_covers` subfolder stores generated PNG covers, and `readnotes.css` contains the default EPUB styling. You can open the resulting EPUBs in any reader that supports the format.

Rerunning the script skips a file when its existing EPUB is at least as recent as the Markdown source. It **does not automatically delete** previously generated EPUBs.

## Troubleshooting

| Problem | What to check |
| --- | --- |
| `pandoc` or `python3` is not found | Install the missing program and rerun the version check. |
| Python reports `No module named PIL` | Re-run the Pillow installation command using the virtual environment above. |
| `readnotes.py` cannot be found | Put the script on your Desktop; confirm it ends in `.py`, not `.py.txt`. |
| The EPUB contains only a title | Open the source `.md` file in Obsidian and check that it contains actual note content. |
| No folder picker appears | Use macOS and check that Terminal can display the folder dialog, or supply the source folder path as an argument. |
| WeRead notes do not sync | Consult the [third-party plugin documentation](https://github.com/zhaohongxuan/obsidian-weread-plugin); this script cannot fetch notes itself. |

## Files and Chinese-language guide

- [`readnotes.py`](readnotes.py) — batch EPUB conversion script.
- [`README.md`](README.md) — Chinese README and usage instructions.
- [Chinese illustrated PDF guide (version 2.0)](%E6%8A%8A%E5%BE%AE%E4%BF%A1%E8%AF%BB%E4%B9%A6%E5%88%92%E7%BA%BF%E7%AC%94%E8%AE%B0%E5%8F%98%E6%88%90%E8%87%AA%E5%B7%B1%E7%9A%84%20EPUB%E7%94%B5%E5%AD%90%E4%B9%A6%202.0.pdf) — 15-page walkthrough (Chinese).
- [`LICENSE.txt`](LICENSE.txt) — terms for this repository's original materials.

## Privacy, copyright, and license

- Only process reading notes and excerpts you are entitled to use. Do not publish copyrighted book text without permission.
- Do not share WeRead API keys, cookies, login credentials, or private notes.
- This is an independent personal project, **not** an official product of WeRead, Obsidian, Pandoc, or the Weread Plugin. Each third-party dependency has its own terms and license.
- The original script and tutorial in this repository are provided for **personal, noncommercial use only** under the custom [`LICENSE.txt`](LICENSE.txt). You may download, run, and modify your private copy for personal use, but redistribution, commercial use, and integration into distributed products require prior written permission, subject to the terms and exceptions in the license.
- **This repository is source-available, not open-source under an OSI-approved license.** GitHub's platform-specific viewing and forking permissions still apply.

Suggestions and bug reports are welcome.
