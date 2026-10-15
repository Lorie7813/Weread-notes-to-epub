# 把微信读书划线笔记变成自己的 EPUB 电子书

**读书成册 · Mac 零基础免费教程及个人转换脚本**

本项目适合想保存自己阅读划线和想法的微信读书用户：先通过 Obsidian 的第三方 Weread 插件把笔记同步为 Markdown 文件，再使用转换脚本批量生成 EPUB 电子书（含彩色 PNG 封面）。

**免费教程和脚本，不会直接连接微信读书。**

## 使用流程

`微信读书 → Obsidian + Weread 插件 → .md 笔记 → readnotes.py + Pandoc → EPUB`

## 下载

- **[转换脚本 readnotes.py](readnotes.py)**：已经发布，可直接下载；建议不要从 PDF 手动复制长代码，避免缩进被 PDF 阅读器破坏。
- **[零基础图文 PDF 教程 2.0](https://github.com/Lorie7813/Weread-notes-to-epub/blob/main/%E6%8A%8A%E5%BE%AE%E4%BF%A1%E8%AF%BB%E4%B9%A6%E5%88%92%E7%BA%BF%E7%AC%94%E8%AE%B0%E5%8F%98%E6%88%90%E8%87%AA%E5%B7%B1%E7%9A%84%20EPUB%E7%94%B5%E5%AD%90%E4%B9%A6%202.0.pdf)**：15 页 Mac 图文教程，已上传；可进入页面点击 Download raw file 下载。
- [个人免费使用许可 LICENSE.txt](LICENSE.txt)。

下载脚本的方法：打开 `readnotes.py` 文件，点击 **Raw / Download raw file**，将文件以 `readnotes.py` 名称保存到 Mac 的**桌面**。

## 你需要准备的工具

1. [Obsidian](https://obsidian.md/)：个人 Markdown 笔记软件。
2. [Obsidian Weread 插件](https://github.com/zhaohongxuan/obsidian-weread-plugin)：第三方同步插件，在 Obsidian 中启用并登录自己的微信读书。
3. [Pandoc](https://pandoc.org/installing.html)：文档/EPUB 格式转换程序。
4. [Python 3](https://www.python.org/downloads/macos/) 和 Pillow：运行转换程序及生成笔记封面。

## Mac 快速使用

先按插件说明将自己的微信读书划线同步到 Obsidian，确认指定文件夹里有 `.md` 笔记。

在 Mac 终端依次运行以下命令。前两项用于核对安装，接下来两项只需在首次使用时运行：

```bash
pandoc --version
python3 --version
python3 -m venv "$HOME/readnotes-venv"
"$HOME/readnotes-venv/bin/python" -m pip install Pillow
```

确保 `readnotes.py` 已经保存在 Mac 桌面，然后运行：

```bash
"$HOME/readnotes-venv/bin/python" "$HOME/Desktop/readnotes.py"
```

出现选择文件夹窗口后，选中存放微信读书 Markdown 笔记的文件夹。生成结果保存在 **桌面 → 读书成册 EPUB**。

- 每份 `书名.md` 会生成 `书名｜笔记.epub`；例如 `012-书名.md` 会得到 `012-书名｜笔记.epub`。
- 当原 Markdown 文件修改时间不晚于现有 EPUB 时，程序会跳过转换；它不会自动删除历史 EPUB。
- 附带彩色 PNG 文字封面；文件名开头的编号在封面中单独显示。
- 如果 `pandoc --version` 或 `python3 --version` 报错，请先完成安装，不要直接运行转换脚本。

> 已使用虚构 Markdown 示例完成基本的 Python 语法、EPUB 包结构和封面元数据测试。**正式公开宣传前仍需要在真实 Mac/Obsidian 环境完整走一遍图文教程**；不同软件版本的界面可能变化。

## 常见问题

- **提示找不到 Pillow**：请重新执行上面的 `pip install Pillow` 命令。
- **提示找不到 readnotes.py**：确认它在 Mac 桌面，扩展名是 `.py`，不是 `.py.txt`。
- **EPUB 只有标题**：先用 Obsidian 打开源 Markdown，检查里面是否实际有划线内容。
- **没有弹出文件夹窗口**：脚本目前面向 macOS；你也可以手动传入源文件夹路径作为第一个参数。
- **微信读书同步失败**：请查看原 Weread 插件的项目文档；这个转换脚本不会替代插件的同步功能。

## 隐私与版权

- 不要公开微信读书 API Key、Cookie、真实私人笔记或未经许可的原书全文。
- 本项目并非微信读书、Obsidian、Pandoc 或 Weread 插件的官方产品。第三方依赖分别遵循其服务条款与许可证；无需 Fork 原 Weread 插件。
- 本仓库原创转换代码与原创教程**仅授权个人非商业使用**，不授权未经许可的代码重新分发、销售或商业集成，详见 [LICENSE.txt](LICENSE.txt)。这不是标准开源许可证；GitHub 平台条款允许的查看与 Fork 另行适用。
