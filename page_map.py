import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd # / GeoPandas
st.set_page_config(layout="wide")
st.title("Leafmap + GeoPandas")

url="/workspaces/streamlit-gisdemo-app/hospital.zip"
gdf=gpd.read_file(url)
st.dataframe(gdf.head())

#-2.建立地圖
m=leafmap.Map(center=[0, 0])
#-3.將 GeoDataFrame 加入地圖
#使用 add_gdf() 方法
m.add_gdf(
    gdf,
    layer_name="醫院",
    style={"fill Opacity": 0, "color":"black", "weight":0.5}, #設為透明,只留邊界
    highlight=False
)
#加入圖層控制器(右上角)
m.add_Jayer_control()
#-4.顯示地圖
m.to_streamlit(height=700)