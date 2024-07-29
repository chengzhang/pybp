#!/bin/bash

# 初始化子模块
git submodule init

# 更新子模块
git submodule update

# 获取子模块的最新更改
git submodule update --remote

# 提交和推送更新
git add .
git commit -m "Update submodule to latest version"
git push origin main  # 或者你的分支名称
