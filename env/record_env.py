"""把当前运行环境写成一个 JSON 文件，训练结果旁边各放一份，论文里每张表都能查到出处。

用法：python env/record_env.py 输出路径.json
"""
import json
import os
import platform
import subprocess
import sys
from datetime import datetime, timezone


def _version(name):
    try:
        module = __import__(name)
        return getattr(module, "__version__", "未知")
    except ImportError:
        return None


def _cpu_model():
    try:
        with open("/proc/cpuinfo") as f:
            for line in f:
                if line.startswith("model name"):
                    return line.split(":", 1)[1].strip()
    except OSError:
        pass
    return platform.processor() or "未知"


def _gpus():
    try:
        import tensorflow as tf
        return [d.name for d in tf.config.list_physical_devices("GPU")]
    except ImportError:
        return None


def _git_commit():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def collect():
    return {
        "记录时间": datetime.now(timezone.utc).isoformat(),
        "机器": platform.node(),
        "操作系统": platform.platform(),
        "处理器": _cpu_model(),
        "处理器核数": os.cpu_count(),
        "显卡": _gpus(),
        "Python": platform.python_version(),
        "tensorflow": _version("tensorflow"),
        "pybamm": _version("pybamm"),
        "numpy": _version("numpy"),
        "代码版本": _git_commit(),
    }


if __name__ == "__main__":
    info = collect()
    text = json.dumps(info, ensure_ascii=False, indent=2)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w", encoding="utf-8") as f:
            f.write(text + "\n")
    print(text)
