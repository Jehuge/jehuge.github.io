---
layout: post
title: 配置 github 图床，vscode 和 cursor使用 picgo 插件
categories: [插件, 图床]
description: 配置 github 图床，vscode 和 cursor使用 picgo 插件
keywords: vscode,  picgo, 图床
mermaid: false
sequence: false
flow: false
mathjax: false
mindmap: false
mindmap2: false
---
## 配置 github 图床，vscode 和 cursor使用 picgo 插件
### 1. 首先获取 github 的 token
在 setting 中找到 developer settings ，然后找到 personal access tokens ，点击 generate new token ，然后输入你的 github 用户名，选择你要授权的权限，然后点击 generate token ，然后复制生成的 token ，这个 token 是用来访问你的 github 仓库的。
    ![20250118095447](https://raw.gitmirror.com/Jehuge/blogimg/master/img/20250118095447.png)
    ![20250118095541](https://raw.gitmirror.com/Jehuge/blogimg/master/img/20250118095541.png)

### 2. 创建仓库
在 github 中创建一个仓库，这个仓库是用来存储你的图片的，仓库名可以随便取。必须创建**公开**的仓库，因为 picgo 需要访问你的 github 仓库。初始化一下分支，选择 master 分支。
    ![20250118095946](https://raw.gitmirror.com/Jehuge/blogimg/master/img/20250118095946.png)

### 3. 配置 picgo
在 picgo 中配置 github 图床，选择 github 图床，然后输入你的 github 用户名，仓库名，token，分支名，然后点击确定。
    ![20250118100042](https://raw.gitmirror.com/Jehuge/blogimg/master/img/20250118100042.png)

### 4. 配置 vscode 和 cursor
在 vscode 和 cursor 中配置 picgo 插件，在 vscode 中，点击设置，然后搜索 picgo ，然后点击 picgo ，然后点击配置，然后选择 github 图床，然后输入你的 github 用户名，仓库名，token，分支名，然后点击确定。
    ![20250118100121](https://raw.gitmirror.com/Jehuge/blogimg/master/img/20250118100121.png)
为了更好的编辑 md 文件，可以安装 vscode 的插件。
    ![20250118100232](https://raw.gitmirror.com/Jehuge/blogimg/master/img/20250118100232.png)
设置 picgo 插件
    ![20250118100321](https://raw.gitmirror.com/Jehuge/blogimg/master/img/20250118100321.png)
使用快捷键上传图片
    ![20250118100414](https://raw.gitmirror.com/Jehuge/blogimg/master/img/20250118100414.png)

### 5. 使用 gitmirror 加速图床
![20250125112410](https://raw.gitmirror.com/Jehuge/blogimg/refs/heads/main/blogimg/20250125112410.png)