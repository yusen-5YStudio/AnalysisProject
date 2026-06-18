##### 项目名称

​    Amazon Pet Food Reviews Analysis

##### 项目背景

​    某宠物食品品牌希望通过分析亚马逊用户评论，识别用户差评原因，并为产品优化提供数据支持

##### 项目目标

​    1.分析用户评分分布情况
​    2.提取高频差评评论关键词
​    3.识别差评主要原因
​    4.统计各原因占比
​    5.输出产品改良建议

##### 数据来源

​    1.数据集:Amazon Food Reviews Dataset
​    2.评论数量:560000+
​    3.字段包含:
​        3.1 Score 评分
​        3.2 Text 内容

##### 技术栈

​    Python
​    Pandas
​    Matplotlib
​    Nltk 
​    Collections
​    Re 数据清洗

##### 分析流程

​    1.数据清洗
​        删除空值
​        删除重复数据
​        文本标准化处理
​    2.探索性分析
​        统计各评分数量
​        用户满意度
​        情感分析
​    3.文本分析
​        筛选差评高频关键词
​    4.差评原因归类
​        价格问题：32%
​        口味问题：24%
​        质量问题：18%
​    5.可视化展示
​        星级分布柱状图
​        好评、差评、中等评价柱状图
​        高频差评词汇柱状图

##### 项目成果

######     核心发现

​        1.差评主要归结在口味与质量上面
​        2.价格词汇出现频率过高
​        3.少部分有产地问题

######     业务建议

​        1.讲究一份价钱一分货
​        2.价钱过高、质量也得跟上去
​        3.口味 应大众化。

##### 分析能力

```
	数据清洗(pandas)
	探索性数据分析
	文本挖掘(NLP)
	关键词提取(Ngrams、stopwords)
	数据可视化
	业务问题拆解
	数据驱动决策
```

##### 项目文件结构

```
AmazonFoodReviewsAnalysisProject
	data
		Reviews.csv
	images
		BadReviewsWords.png
		RatingDistribution.png
		SentimentAnalysis.png
	notebooks
		analysis.ipynb
		analysis.py(写了详细注释)
	report 
		analysis.html
		project_report.pdf
	README.md
```

##### 项目查看顺序

```
项目主要保存在 AmazonFoodReviewsAnalysisProject 文件夹中
	分析过程请查看:
		notebooks/analysis.ipynb
	可视化结果请查看:
		images 文件夹下
	项目介绍:
		REANME.md
```



