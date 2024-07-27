#!/bin/bash

  # 定义 exo 项目下载地址（文件服务器）
  EXO_URL="http://192.168.1.16:8082/exo/"

  # exo 代码存放路径
  EXO_CODE="/nasroot/code"

install::exo() {
  conda create --name exo  python=3.12 -y
  conda activate exo

  mkdir -p ${EXO_CODE} && cd ${EXO_CODE}

  wget -r -np -nH --cut-dirs=1 -P ${EXO_CODE}/exo ${EXO_URL}
  cd ${EXO_CODE}/exo
  pip install -e . -i https://pypi.tuna.tsinghua.edu.cn/simple/
  conda install -c conda-forge mlx
  pip install mlx_lm  -i https://pypi.tuna.tsinghua.edu.cn/simple/
  pip install  pyudev -i https://pypi.tuna.tsinghua.edu.cn/simple/
  DEBUG=9 python3 main.py
}

install::exo



