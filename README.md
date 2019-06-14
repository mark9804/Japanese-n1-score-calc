# 日语N1分数计算器

## 为什么造这个轮子

* 估分。

## 这个轮子的特别之处

* 比传统的估分方式更加精确，会判断单科/总分是否合格。
* 考虑到了做卷子时没有包含听力的情况。

![Demo](src\demo.png)

## 计算方法

使用以下方式进行总分计算：
* 词汇语法
    * 问题1：1 点 × 6 问 =  6  点
    * 问题2：1 点 × 7 问 =  7  点
    * 问题3：1 点 × 6 问 =  6  点
    * 问题4：2 点 × 6 问 = 12 点
    * 问题5：1点 × 10问 = 10 点
    * 问题6：1 点 × 5 问 =  5  点
    * 问题7：2 点 × 5 问 = 10 点
    
    **合计：56点**
    
    **词汇语法部分得分：（得分点\* / 56） × 60 = 得分**
    
* 读解

    * 问题8：2 点 × 4 问 =  8  点
    * 问题9：2 点 × 9 问 = 18 点
    * 问题10：3点 × 4问 = 12 点
    * 问题11：2点 × 2问 =  4  点
    * 问题12：3点 × 4问 = 12 点
    * 问题13：2点 × 2问 =  4  点

    **合计：58点**

    **读解部分得分：（得分点\* / 58 ）× 60 = 得分**

* 听解

    * 问题1：2 点 × 6 问 = 12 点
    * 问题2：1 点 × 7 问 =  7  点
    * 问题3：2 点 × 6 问 = 12 点
    * 问题4：1点 × 13问 = 12 点
    * 问题5：3 点 × 4 问 = 12 点

    **合计：56点**

    **听解部分得分：（得分点\* / 56） × 60 = 得分**

\* 由于方便计数，得分采用扣分表示：这种方式可能会比原本的估算更不精确，因为各个题型的题目数量不是固定的。但是会比（每部分错题数 / 每部分题数） × 60之后相加来的精确一些。

## 运行

1. 运行`n1score.py`，按照提示输入每一部分错题数。

   \* 暂时还不需要额外的library，如果后期加入统计功能的话就需要了

## 版本更新

### v0.1.0

* Initial release.

## TODO

- [ ] exe封包
- [ ] 网页端
- [ ] 加入错题频率统计（在多次使用时比较有效，显示哪一道问题错的最多）