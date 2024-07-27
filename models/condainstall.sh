#!/bin/bash

# 定义 Miniconda 下载 URL
  MINICONDA_URL="http://192.168.1.16:8082/Miniconda3-latest-Linux-aarch64.sh"

  # 统一脚本名
  MINICONDA_FILENAME="miniconda_install.sh"

  # miniconda3 安装路径
  PREFIX="/nas/opt"

install::miniconda3() {
  # 下载 Miniconda 安装程序
  wget ${MINICONDA_URL} -O ${MINICONDA_FILENAME}

  # 安装 Miniconda
  mkdir -p  ${PREFIX}/miniconda3
  bash ${MINICONDA_FILENAME} -b -u -p ${PREFIX}/miniconda3

  # 激活 conda
  ${PREFIX}/miniconda3/bin/conda init bash
  ${PREFIX}/miniconda3/bin/conda init zsh
  source ${PREFIX}/miniconda3/bin/activate

  rm ${MINICONDA_FILENAME}
  echo "Conda 已成功安装并配置。您可以使用 'conda activate test' 切换到测试环境。"
}

install::miniconda3



