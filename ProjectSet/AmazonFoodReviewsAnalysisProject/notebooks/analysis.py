# 读取数据
import pandas as pd
import matplotlib.pyplot as plt #画图
import re # 数据清洗 NLP
# 去停用词 也就是主谓宾词
import nltk 
nltk.download('stopwords',quiet=True)
from nltk.corpus import stopwords
# 定义两个组合在一起形成的差评词
from nltk.util import ngrams 
from collections import Counter # 查出差评高频关键词


# print(pd.__version__) 测试pandas 包版本 看看有没有安装成功
# print(os.getcwd()) 找目前路径
df = pd.read_csv("ProjectSet/AmazonFoodReviewsAnalysisProject/data/Reviews.csv")
print("找到数据：",df.head())

# ##查看数据 分析总评论数、缺失值数量、字段类型
print("分析总评论数:",df.shape) 
print("字段类型:",df.isnull().sum())
# # # 数据清洗
# #  #删除空评论
# print(df.columns) #文件里面的字段名
df = df.dropna(subset=["Text"])
#     #删除重复数据
df = df.drop_duplicates()
# # 评分分析
#     #统计各评分数量
rating_count = df["Score"].value_counts()
print("统计各评分数量:",rating_count)
#     #画图 评分分布图
#规定尺寸
# plt.figure(figsize=(6,4))
rating_count.sort_index().plot(kind = "bar")
plt.title("Score Distribution")
plt.xlabel("Score") #情感
plt.ylabel("Count")

plt.show()
# # 行业分析
#     #用户满意度
positive_rate = (
    len(df[df["Score"] >= 4]) / len(df)
)
print("用户满意度:",positive_rate)

# #情感分析
def sentiment_label(x):
    if x >= 4:
        return 'positive'
    elif x == 3:
        return 'neutral'
    else:
        return 'negitive'
df["sentiment"] = df["Score"].apply(sentiment_label)
# 情感分析图
# plt.figure(figsize=(6,4))
df["sentiment"].value_counts().plot(kind='bar')

plt.title("Sentiment Distribution")
plt.xlabel("Sentiment") #情感
plt.ylabel("Count")
plt.xticks(rotation=360)

plt.show()
#     #判断
    #统计情感分布
print("统计情感分布:",df["sentiment"].value_counts())
# 好评占据了 44万条 差评或者中立 占据了 12万条 总体来说 整体偏好评
print("评分 vs 情感关系:",df.groupby('sentiment')['Score'].mean())
# 输出 差评或者中立保持在 1.92 平均分 好评占据在 4.8 平均分 相之与统计情感分析匹配 
# groupby 算平均分
stop_words = set(stopwords.words('english'))
bad_review = df[df['Score'] <= 2]['Text'].fillna('').astype(str)
bad_review_text = " ".join(
    bad_review.apply(
        lambda x: re.sub(r'[^\w\s]','',x.lower())
    )
)
bad_words = bad_review_text.split()

clean_words = [
    w for w in bad_words
    if w not in stop_words
    and len(w) > 2
    and w.isalpha()
]
#筛选掉 由 not good 两个字组成的差评词 加入这个评论数据里面差评常常出现的高频谓语词
bad_words_gl = {
    'would','could','should','know','think','thought','like','first','time','much','better','good','really',
    'also'
}
Zh_bigrams = list(ngrams(clean_words,2))
filter_bigrams = [
    bg for bg in Zh_bigrams
    if bg[0] not in bad_words_gl
    and bg[1] not in bad_words_gl
]
#让差评高频词更加人性化
badReview_top10_num = Counter(filter_bigrams).most_common(10)
#差评图
keywordsList = [' '.join(x[0]).replace(' ','\n') for x in badReview_top10_num]
badReview_top10Num_Scores = [x[1] for x in badReview_top10_num]

# plt.figure(figsize=(8,4))
plt.bar(keywordsList,badReview_top10Num_Scores)
plt.title('Top 10 Negative KeyWords')
plt.xlabel('KeyWords')
plt.ylabel('Frequency')

plt.xticks(fontsize=8)
plt.show() 
# 评分 vs 情感关系
print("评分 vs 情感关系:",pd.crosstab(df["Score"],df["sentiment"]))
