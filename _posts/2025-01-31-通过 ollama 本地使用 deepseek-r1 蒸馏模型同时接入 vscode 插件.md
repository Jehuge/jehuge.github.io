---
layout: post
title: 通过 ollama 本地使用 deepseek-r1 蒸馏模型同时接入 vscode 插件
categories: [ai, deepseek]
description: 通过 ollama 本地使用 deepseek-r1 蒸馏模型同时接入 vscode 插件
keywords: deepseek, ollama, vscode
mermaid: false
sequence: false
flow: false
mathjax: false
mindmap: false
mindmap2: false
---

## 通过 ollama 本地使用 deepseek-r1 蒸馏模型同时接入 vscode 插件

### 1. 前言
ollama 是一个开源的本地 AI 模型库，支持多种模型，包括 deepseek-r1 蒸馏模型。
建议先安装 n 卡的 cuda ，可以解决显存不足的问题。
    ![20250131112026](https://raw.gitmirror.com/Jehuge/blogimg/refs/heads/main/blogimg/20250131112026.png)
本文通过 ollama 本地使用 deepseek-r1 蒸馏模型同时接入 vscode 插件，可以让你在本地使用 deepseek-r1 蒸馏模型，同时可以接入 vscode 插件，让你在 vscode 中使用 deepseek-r1 蒸馏模型。
    ![20250131112127](https://raw.gitmirror.com/Jehuge/blogimg/refs/heads/main/blogimg/20250131112127.png)
ollama 的官网：https://ollama.com/
### 2. 安装 ollama
ollama 提供了多种平台安装方式，这里选择 windows 平台，下载 ollama.exe 文件，然后解压到本地，然后添加到环境变量中。
默认安装模型的路径为：C:\Users\用户名\ollama\models，通过改变系统变量来修改路径。添加图中所示的一行。
    ![20250131112614](https://raw.gitmirror.com/Jehuge/blogimg/refs/heads/main/blogimg/20250131112614.png)
运行 ollama.exe 文件，然后输入 `ollama pull deepseek-r1:14b` 来下载 deepseek-r1 模型。
### 3. 下载 deepseek-r1 模型
对于不同配置的显卡，下载的模型也不同，这里选择 14b 的模型，可以自己多试试，下载的模型越大，效果越好，但是显存占用也越大。ollama 提供了多种模型，可以自己选择。
    ![20250131112843](https://raw.gitmirror.com/Jehuge/blogimg/refs/heads/main/blogimg/20250131112843.png)
### 4. 配置 vscode 插件
下载安装 vscode 插件，然后配置 ollama 的地址和模型。vscode 插件有很多比如 cline，codegpt，continue，这里用 continue 演示。
    ![20250131113203](https://raw.gitmirror.com/Jehuge/blogimg/refs/heads/main/blogimg/20250131113203.png)
vscode 左边栏会出现 continue 的图标，点击即可配置。配置 ollama 模型地址和模型名称。
    ![20250131113319](https://raw.gitmirror.com/Jehuge/blogimg/refs/heads/main/blogimg/20250131113319.png)

### 5. 使用浏览器插件来实现与本地模型交互
安装插件page-asist，github 地址 `https://github.com/n4ze3m/page-assist` ,配置好插件参数。
    ![20250131113820](https://raw.gitmirror.com/Jehuge/blogimg/refs/heads/main/blogimg/20250131113820.png)
    ![20250131113847](https://raw.gitmirror.com/Jehuge/blogimg/refs/heads/main/blogimg/20250131113847.png)
此时已经显示可用了。
    ![20250131113946](https://raw.gitmirror.com/Jehuge/blogimg/refs/heads/main/blogimg/20250131113946.png)
