import streamlit as st
import pandas as pd
import numpy as np

# 生成西乡塘的随机点，其中22.842269，108.246567是北京的经纬度
# 首先使用np.random.randn()方法生成1000行2列的符合正态分布的随机点
# 然后在第一列上除以20进行缩小，在第二列上除以50进行缩小
# 最后加上北京市的经纬度。
df = pd.DataFrame(
    np.random.randn(10, 2) / [20, 50] + [22.842269,108.246567],
    columns=['latitude', 'longitude'])
# 设置索引列的名称
df.index.name='序号'

st.subheader('南宁地图')
st.map(df)

st.title('⭐餐厅评分')
# 定义数据,以便创建数据框
data = {
    '门店':['门店1', '门店2', '门店3', '门店4', '门店5'],
    '评分':[4.8, 4.5,3.8,4.8,4.6],
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3, 4, 5], name='序号')
# 将新索引应用到数据框上
df.index = index

# 通过x指定月份所在这一列为条形图的x轴
df_indexed = df.set_index('门店')
st.bar_chart(df_indexed)

st.title('💰不同类型餐厅价格')
# 定义数据,以便创建数据框
data = {
    '月份':['1月份', '2月份', '3月份','4月份', '5月份', '6月份','7月份', '8月份', '9月份','10月份', '11月份', '12月份',],
    '1号门店':[11,13,15,11,12,13,10,15,14,12,12,16],
    '2号门店':[20,15,14,16,17,21,20,16,17,18,19,17],
    '3号门店':[50,56,57,85,95,53,78,84,78,45,87,78],
    '4号门店':[787,789,213,584,456,798,132,456,798,123,546,798],
    '5号门店':[170, 190, 169,741,201,420,532,650,566,430,452,456],
}
data = {
    '餐厅类型':['西餐', '快餐', '日料','火锅','快餐'],
    '门店':[200, 300, 250, 400,50]
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3, 4, 5], name='序号')
# 将新索引应用到数据框上
df.index = index

# 通过x指定月份所在这一列为折线图的x轴
df_indexed = df.set_index('餐厅类型')
st.line_chart(df_indexed)

st.title('🍲用餐高分时段')
# 定义数据,以便创建数据框
data = {
    '时间':['11', '12', '13'],
    '1号门店':[200, 150, 180],
    '2号门店':[120, 160, 123],
    '3号门店':[115, 100, 160],
    '4号门店':[160, 130, 143],
    '5号门店':[170, 190, 169],
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3], name='序号')
# 将新索引应用到数据框上
df.index = index

# 通过x指定月份所在这一列为面积图的x轴
df_indexed = df.set_index('时间')
st.area_chart(df_indexed)

st.title('🍽餐厅详情')
with st.expander("塔斯汀"):
    st.markdown("**好吃**")
    st.button("点我点我！！！")
c1, c2= st.columns(2)
c1.markdown('## 塔斯汀')
c1.markdown('##### 评分')
c1.markdown('# 4.7/5.0')
c1.markdown('#### 人均消费')
c1.markdown('# 25元')

c2.markdown('**推荐菜品：**')
c2.markdown(' • &#8194;特色套餐')
c2.markdown(' • &#8194;单人套餐')
c2.markdown(' • &#8194;巨无霸套餐')


st.subheader('当前拥挤程度')
st.progress(89,text="89%拥挤")


st.title('😍今日午餐推荐')
st.markdown("<span style='color:red; border:2px solid red; border-radius:8px; padding:4px;'>干饭首选👍</span>", unsafe_allow_html=True)
if st.button('帮我选午餐'):
    st.write('已帮你选好了')
st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px; background-color:green;'>今日推荐：烧鸭粉（晚餐）</span>", unsafe_allow_html=True)

image_url="https://ts1.tc.mm.bing.net/th/id/R-C.fad4e971c5cb87d18637d9cc9106c11b?rik=TmYA58qAuk5HTg&riu=http%3a%2f%2fpuui.qpic.cn%2fqqvideo_ori%2f0%2fk00319inpon_1280_720%2f0&ehk=Jb1YQw5YuBB%2bCr9F3S4IykBcWPmkJZ7oCC47GMLrRZY%3d&risl=&pid=ImgRaw&r=0"
st.image(image_url,caption="烧鸭腿粉",use_container_width=True)
#st.markdown("![图片](https://ts1.tc.mm.bing.net/th/id/R-C.fad4e971c5cb87d18637d9cc9106c11b?rik=TmYA58qAuk5HTg&riu=http%3a%2f%2fpuui.qpic.cn%2fqqvideo_ori%2f0%2fk00319inpon_1280_720%2f0&ehk=Jb1YQw5YuBB%2bCr9F3S4IykBcWPmkJZ7oCC47GMLrRZY%3d&risl=&pid=ImgRaw&r=0", unsafe_allow_html=True)


