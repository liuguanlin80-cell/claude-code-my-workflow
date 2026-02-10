---
paths:
  - "analysis/**/*.R"
  - "figures/**"
  - "explorations/**/*.R"
---

# Figure Style Guide: 论文图表规范

## 尺寸（Word A4 论文）

| 类型 | 宽度 | 高度 | 用途 |
|------|------|------|------|
| 单面板 | 170 mm | 120 mm | 大多数图（UMAP、火山图、柱状图） |
| 宽幅/热图 | 170 mm | 200 mm | 热图、通路图、大型网络 |
| 多面板 (A/B/C/D) | 170 mm | 240 mm | 组合图 |
| 半幅 | 80 mm | 80 mm | 内嵌小图 |

## 输出格式

- **首选：** PDF（矢量，用 `cairo_pdf` 设备支持中文字符）
- **备选：** PNG（300 DPI，Word 兼容性后备）
- 两种都保存：
  ```r
  ggsave(path_pdf, width = 170, height = 120, units = "mm", device = cairo_pdf)
  ggsave(path_png, width = 170, height = 120, units = "mm", dpi = 300)
  ```

## 命名约定

```
figures/fig_章节_序号_描述.pdf
figures/fig_3.1_01_umap_d09_d12.pdf
figures/fig_3.2_03_volcano_sixbp1.pdf
figures/fig_3.3_02_rtqpcr_bar.pdf
```

## 调色板

（完整定义见 `r-code-conventions.md` Section 4。）

| 语义 | 颜色 | 用途 |
|------|------|------|
| D09 | 暖橙 #F39C12 | D09 时间点 |
| D12 | 紫色 #8E44AD | D12 时间点 |
| 上调 | 绿色 #27AE60 | 火山图/MA 图上调基因 |
| 下调 | 红色 #C0392B | 火山图/MA 图下调基因 |
| 不显著 | 灰色 #95A5A6 | 火山图 ns 基因 |
| 细胞类型 | `Seurat::DiscretePalette(n, "polychrome")` | UMAP 聚类 |

## 字体

- **英文：** Arial 或 Helvetica，10-12pt
- **中文轴标签：** 尽量避免；用英文标签 + 中文图注
- 若必须中文：`showtext::font_add("SimHei", "simhei.ttf")` + `showtext_auto()`

## 图注模板（每张图必须包含）

1. 简短描述标题
2. 组别/条件
3. 样本量 (n)
4. 统计检验与阈值（如"Wilcoxon rank-sum test, padj < 0.05, BH correction"）
5. 软件/包及版本
6. 关键参数（如"SCTransform, 30 PCs, resolution 0.5"）

## Anti-Patterns

| 错误做法 | 正确做法 |
|----------|----------|
| 用 ggplot2 默认颜色 | 项目调色板 |
| 坐标轴缺少单位 | "Gene expression (log2 CPM)" |
| 图例在绘图区内 | `legend.position = "bottom"` |
| ggsave 不写 units/dpi | `units = "mm", dpi = 300` |
| 手工修改图片 | 脚本生成，禁止 PS/截图修改 |
