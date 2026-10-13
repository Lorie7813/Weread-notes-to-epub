#!/usr/bin/env python3
"""把 Obsidian 里的微信读书 Markdown 笔记批量制成 EPUB。"""
import hashlib
import re
import shutil
import subprocess
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

CSS = '''body {line-height: 1.8; margin: 0 7%;}
h1 {text-align: center; font-size: 1.5em; margin: 2em 0;}
p {margin: 0 0 1.8em; text-align: justify;}'''
COLORS = ["#E5EDE8", "#ECE5D9", "#E4E9F2", "#F1E1DC", "#E9E3F1"]
FONT_PATHS = [
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]

def font(size):
    for path in FONT_PATHS:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def wrap(text, draw, fnt, limit):
    lines, cur = [], ""
    for char in text:
        trial = cur + char
        if cur and draw.textbbox((0, 0), trial, font=fnt)[2] > limit:
            lines.append(cur)
            cur = char
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines

def cover_for(name, dest):
    match = re.match(r"^(\d+)[-_ ]+(.+)$", name)
    number, title = (match.group(1), match.group(2)) if match else ("", name)
    h = hashlib.sha256(name.encode()).hexdigest()
    color = COLORS[int(h[:6], 16) % len(COLORS)]
    img = Image.new("RGB", (1200, 1800), color)
    draw = ImageDraw.Draw(img)
    draw.line((145, 165, 1055, 165), fill="#A6A6A6", width=3)
    if number:
        draw.text((600, 270), number, fill="#36475D",
                  font=font(76), anchor="mm")
    size = 88
    while size > 48:
        ft = font(size)
        lines = wrap(title, draw, ft, 900)
        if len(lines) <= 5:
            break
        size -= 5
    first_y = 760 - (len(lines) - 1) * (size + 25) / 2
    for idx, line in enumerate(lines):
        draw.text((600, first_y + idx * (size + 25)), line,
                  fill="#252525", font=ft, anchor="mm")
    draw.line((450, 1395, 750, 1395), fill="#A6A6A6", width=2)
    draw.text((600, 1490), "笔记", fill="#495B51", font=font(56), anchor="mm")
    img.save(dest, "PNG")

def choose_folder():
    if len(sys.argv) > 1:
        return Path(sys.argv[1]).expanduser()
    dialog = 'POSIX path of (choose folder with prompt "请选择微信读书 Markdown 文件夹")'
    result = subprocess.run(["osascript", "-e", dialog],
                            capture_output=True, text=True)
    if result.returncode != 0:
        return None
    return Path(result.stdout.strip())

def main():
    if not shutil.which("pandoc"):
        sys.exit("找不到 Pandoc，请先安装并检查 pandoc --version")
    source = choose_folder()
    if not source or not source.is_dir():
        sys.exit("没有选择有效的文件夹，程序结束。")
    output = Path.home() / "Desktop" / "读书成册 EPUB"
    output.mkdir(parents=True, exist_ok=True)
    covers = output / "_covers"
    covers.mkdir(exist_ok=True)
    css = output / "readnotes.css"
    css.write_text(CSS, encoding="utf-8")
    made = skipped = failed = 0
    for md in sorted(source.rglob("*.md")):
        name = md.stem
        target = output / (name + "｜笔记.epub")
        if target.exists() and target.stat().st_mtime >= md.stat().st_mtime:
            skipped += 1
            continue
        png = covers / (name + ".png")
        try:
            cover_for(name, png)
            args = ["pandoc", str(md), "-f", "markdown", "-t", "epub3",
                    "--css", str(css), "--epub-cover-image", str(png),
                    "--epub-title-page=false", "-M", "title=" + name,
                    "-M", "lang=zh-CN", "-o", str(target)]
            subprocess.run(args, check=True)
            made += 1
        except Exception as exc:
            print("失败：", name, str(exc))
            failed += 1
    print(f"完成：生成 {made}，跳过 {skipped}，失败 {failed}")
    print("文件位置：", output)
    if sys.platform == "darwin":
        subprocess.run(["open", str(output)], check=False)

if __name__ == "__main__":
    main()
