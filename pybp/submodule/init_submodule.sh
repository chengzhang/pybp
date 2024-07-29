# usage: bash init_submodule.sh repo_name

repo_name=$1

# 声明子模块
git submodule add https://github.com/chengzhang/"${repo_name}".git "${repo_name}"

# 同步子模块的更新
git submodule update --init --recursive

# 提交本地修改到子模块
git add .gitmodules "${repo_name}"
git commit -m "add submodule ${repo_name}"
git push
