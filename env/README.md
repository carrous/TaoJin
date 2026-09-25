# 云端环境记录

## 云端是什么
- Claude 的云端会话，不是显卡服务器。
- 处理器：Intel Xeon 2.10GHz，4 核；内存 15GB；硬盘约 30GB 可用；没有显卡。
- 操作系统：Ubuntu 24.04.4；Python 3.11.15。
- 每次新会话都是一台全新的机器，装过的东西会清空。

## 已测试能装、能跑（2026-09-25）
- tensorflow-cpu 2.21.0（只用处理器的版本）：小模型训练测试通过。
- pybamm 26.8.0.0：单粒子模型放电仿真测试通过。
- 完整的包版本清单：`cloud_cpu_requirements.txt`
- 当次运行环境：`cloud_cpu_env.json`

## 重建这个环境
```
python3 -m venv venv
. venv/bin/activate
pip install -r env/cloud_cpu_requirements.txt
```

## 每次训练都记录环境
```
python env/record_env.py 结果文件夹/environment.json
```
论文里每张表对应的结果文件夹里都放一份，就能写清是在哪个环境训练的。

## 网络限制
- 访问 OneDrive（onedrive.live.com、graph.microsoft.com）被云端网络规则拦住了。
- Python 的软件包网站（pypi.org）和 GitHub 能正常访问。
