---
name: commit-message
description: "Draft Conventional Commit messages from staged changes."
disable-model-invocation: true
---

仅分析并输出提交消息，保持工作区和暂存区不变。

1. 读取整个暂存区的 diff；为空时提示用户并结束。
2. 按需查阅相关背景，确定每项暂存改动的用途。相关改动归入同一提交，明显独立的改动拆为不同提交，确保所有暂存改动都有归属。
3. 为每个建议的提交生成符合 Conventional Commits 的完整消息，改动描述以暂存内容为准，分别放入可复制的代码块。建议拆分时，说明拆分理由及每个提交对应的文件或具体改动。
