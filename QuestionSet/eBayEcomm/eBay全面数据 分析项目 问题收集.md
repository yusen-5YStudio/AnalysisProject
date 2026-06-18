# eBay全面数据 分析项目 问题收集

- all_price 这一列出现 245 to 456

  ```
  解决办法:
  	主页-转换数据-打开Power Query
  	选中all_price($)列
  	添加列-自定义列-出现的框
  		名字:price_min
  		公式:if Text.Contains([#"all_price ($)"],"to")
  			then Text.BeforeDelimiter([#"all_price ($)"]," to ")
  			else [#"all_price ($)"]
  		名字:price_max
  		公式:if Text.Contains([#"all_price ($)"],"to")
  			then Text.AfterDelimiter([#"all_price ($)"]," to ")
  			else [#"all_price ($)"]
  	创建平均价格
  		名字:avg_price
  		公式:([price_min] + [price_max] ) / 2
  ```

- rating 这一列不像是评分像评论总数 而且 是文本类型不是数字

  ​	左侧类型改成 数字

- 商品总数/品牌数 统计

  distinctcount 代表 统计一列或者一组中唯一数据值(更精确)

- shipping_cost (+$) 运费 出现了free none shipping

  ```
  添加列-自定义列
  名字:shipping_cost_num
  公式:
  	try Number.From([#"shipping_cost (+$) "]) otherwise null
  ```

- 把powerBI修改好的数据更新到vscode的数据集

  ```
  - 使用DAX Studio 工具软件
  - 选中需要导出的表-Advanced-ExportData
  - 选择导出数据
  - CSV Delimiter: 选择 Comma(英文逗号分隔符)
  - 会变成 删除了空行、筛选行、删除数据的精确数据(从总数据1920 变成了 540)
    - 检查power query 为什么把数据1920条变成了 540条
    - 右侧的查询设置
      - 筛选的行 1920 - 999+
      - 筛选的行2 817条
      - 筛选的行3 540条(删掉了导致错误 )
    - 推翻了 重新来(从头来一遍)
  ```

- PowerBI 筛选过滤掉的数据导致从1920条变成了540条，从头来

  ```
  - rating 字段(评论数) 有None值 导致类型变成了文本。把None改成null值
    - 选中rating 字段 转换-替换值-要查找的值None替换为(不输入任何内容，因为替换为空)
    - 修改类型为整数
  - shipping_cost 字段出现了 数字、Free、None、shipping 导致类型变成了文本
    - 添加列-自定义列
    - 名字:shipping_cost_num
    - 公式:if [#"shipping_cost (+$) "] = "Free" then 0
           else if [#"shipping_cost (+$) "] = "None" then null
           else if [#"shipping_cost (+$) "] = "Shipping" then null
           else Number.FromText([#"shipping_cost (+$) "])
    sold_quantity/view_quantity 字段里有None(没销量)
    	选中该字段-转换-替换值 把None替换成空值
   经过抢救 恢复成了 1920条
  ```

pd.cut()函数使用时报错，是bin键值要比labels键值少一个参数

PowerBI 没有更新python处理过的数据(像 价格区间)

```
PowerBI-选中数据集-转换数据-添加列-条件列
if avg_price <= 20 then 0-20 以此类推
else 200+
```

