# BOM 合并工具

这是一个用于合并多个BOM（物料清单）Excel文件的工具。该工具可以将指定目录下的所有Excel文件中的sheet合并到一个新的Excel文件中。

## 功能特点

- 自动扫描指定目录下的所有Excel文件
- 使用文件名中的有意义部分作为sheet名称（如ComputeCore）
- 支持多个Excel文件的合并
- 自动处理sheet名称长度限制

## 环境要求

- Python 3.6+
- pandas
- openpyxl

## 安装

1. 克隆仓库：
```bash
git clone [repository-url]
cd [repository-name]
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 使用方法

1. 将需要合并的BOM Excel文件放在 `boms` 目录下

2. 运行脚本：
```bash
python merge_boms.py
```

3. 合并后的文件将生成在根目录下，名为 `boms.xlsx`

## 文件结构

```
.
├── README.md
├── requirements.txt
├── merge_boms.py
└── boms/
    ├── BOM_ComputeCore_PCB1_2025-05-08.xlsx
    ├── BOM_DUAL_DRV8870_PCB1_2025-05-08.xlsx
    └── ...
```

## 注意事项

- 确保Excel文件没有被其他程序打开
- 合并后的sheet名称将使用文件名中的有意义部分（如从 `BOM_ComputeCore_PCB1_2025-05-08.xlsx` 提取 `BOM_ComputeCore`）
- 如果多个文件提取出的sheet名称相同，后面的文件会覆盖前面的文件

## 许可证

MIT License 