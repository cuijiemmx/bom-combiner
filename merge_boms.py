import pandas as pd
import os
from pathlib import Path

def merge_bom_files():
    # 获取boms目录下的所有xlsx文件
    boms_dir = Path('boms')
    excel_files = list(boms_dir.glob('*.xlsx'))
    
    # 创建一个ExcelWriter对象
    output_file = 'boms.xlsx'
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        # 遍历每个Excel文件
        for excel_file in excel_files:
            # 读取Excel文件中的所有sheet
            excel = pd.ExcelFile(excel_file)
            
            # 遍历每个sheet
            for sheet_name in excel.sheet_names:
                # 读取sheet内容
                df = pd.read_excel(excel_file, sheet_name=sheet_name)
                
                # 从文件名中提取有意义的部分（如ComputeCore）
                # 例如：从 BOM_ComputeCore_PCB1_2025-05-08.xlsx 提取 ComputeCore
                file_parts = excel_file.stem.split('_PCB')
                meaningful_name = file_parts[0]
                
                # 将数据写入到新的Excel文件中
                df.to_excel(writer, sheet_name=meaningful_name, index=False)
    
    print(f"所有BOM文件已合并到 {output_file}")

if __name__ == '__main__':
    merge_bom_files() 