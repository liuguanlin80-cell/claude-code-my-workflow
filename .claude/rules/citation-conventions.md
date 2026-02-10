---
paths:
  - "refs/**"
  - "thesis/**"
---

# GB/T 7714-2015 引用规范

## 格式模式（中国国家标准）

### 期刊论文
[序号] 作者1, 作者2, 作者3, 等. 题名[J]. 刊名, 年, 卷(期): 起始页-终止页.

示例：
[1] YOSHIDA H, MATSUI T, YAMAMOTO A, et al. XBP1 mRNA is induced by ATF6 and spliced by IRE1 in response to ER stress to produce a highly active transcription factor[J]. Cell, 2001, 107(7): 881-891.

### 专著
[序号] 作者. 书名[M]. 版次. 出版地: 出版社, 年: 页码.

### 学位论文
[序号] 作者. 题名[D]. 保存地: 保存机构, 年.

### 在线数据库/软件
[序号] 作者. 题名[DB/OL]. 年. URL.

## 规则

1. **作者格式：**
   - 3 人及以下：全部列出
   - 超过 3 人：列前 3 人 + "等"（中文）或 "et al"（英文）
   - 姓名格式：姓全大写 + 名缩写（YOSHIDA H）
2. **文献类型标志：** [J] 期刊、[M] 专著、[D] 学位论文、[C] 会议论文、[P] 专利、[DB/OL] 在线数据库
3. **DOI：** 有则附上 `DOI: 10.xxxx/xxxxx`
4. **正文引用：** 顺序编码 `[1]`、`[2,3]`、`[4-7]`
5. **参考文献列表：** 按正文首次引用顺序排列

## BibTeX 键名约定

格式：`AuthorYear_keyword`
示例：`Yoshida2001_xbp1`、`Stuart2019_seurat_v3`、`Jin2021_cellchat`

## Claude 的职责边界

- Claude 验证 BibTeX 条目字段完整性（author/title/journal/year/volume/pages/doi）
- Claude **不会**自动格式化最终参考文献列表（那是 Word 引文管理器或 CSL 的工作）
- Claude 在正文中使用 `[AuthorYear]` 占位符，由用户在 Word 中替换为正式引用
- **禁止编造引用**——无法确认的引用标注为"[需核实: 描述]"

## Anti-Patterns

| 错误做法 | 正确做法 |
|----------|----------|
| `(Zhang et al., 2021)` | `[1]` 或 `[Zhang2021]` 占位符 |
| 编造 DOI | 标注"[需核实: DOI]" |
| 只用英文格式 | GB/T 7714-2015 格式 |
| 引用无来源的数据 | 标注出处或标记为"[需补充引用]" |
