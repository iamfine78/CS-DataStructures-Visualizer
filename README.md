# CS-DataStructures-Visualizer

手写实现经典数据结构与算法，配合 matplotlib 可视化，用于 408 数据结构复习与工程实践。

## 项目动机

408 数据结构是零基础开始学的。为了真正理解每个算法的底层逻辑，而不是只背概念，我决定用 Python 手写实现所有核心数据结构，并辅以可视化加深理解。

## 已实现内容

| 数据结构/算法 | 文件 | 可视化 | 状态 |
|-------------|------|--------|------|
| 单链表 | `src/linked_list.py` | 🚧 | 🚧 |
| 双链表 | `src/linked_list.py` | 🚧 | 🚧 |
| 栈 | `src/stack_queue.py` | ❌ | 🚧 |
| 队列 | `src/stack_queue.py` | ❌ | 🚧 |
| 二叉树遍历 | `src/binary_tree.py` | 🚧 | 🚧 |
| 二叉搜索树 | `src/binary_tree.py` | 🚧 | 🚧 |
| 图（DFS/BFS） | `src/graph.py` | 🚧 | 🚧 |
| 排序算法 | `src/sorting.py` | 🚧 | 🚧 |
| 查找算法 | `src/searching.py` | ❌ | 🚧 |

> ✅ 已完成 | 🚧 进行中 | ❌ 暂不需要

## 快速开始

```bash
# 克隆仓库
git clone https://github.com/iamfine78/CS-DataStructures-Visualizer.git
cd CS-DataStructures-Visualizer

# 安装依赖
pip install -r requirements.txt

# 运行示例
python examples/demo_linked_list.py
python examples/demo_sorting.py
```

## 项目结构

```
src/           # 核心算法实现
visualizer/    # matplotlib 可视化
examples/      # 可运行的示例脚本
tests/         # 单元测试
```

## 技术栈

- Python 3.10+
- matplotlib（可视化）
- pytest（单元测试）

## 参考

- 王道考研《数据结构》
- 408 计算机学科专业基础考试大纲

## License

MIT
