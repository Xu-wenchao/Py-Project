from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pylab as plt


back_color = imread("./dragon.jpg")
font = "C:\Windows\Fonts\STXINGKA.TTF"
wc = WordCloud(background_color="white",
               max_words=500,
               mask=back_color,             #   掩膜，产生词云背景的区域，以该参数值作图绘制词云，这个参数不为空时，width,height会被忽略
               max_font_size=80,
               stopwords=STOPWORDS.add("其他"),   # 屏蔽词
               font_path=font,              #   解决显示口型乱码问题
               random_state=42,             #   为每一词返回一个PIL颜色
               prefer_horizontal=10)        #   调整词云中字体水平和垂直的多少

text = open("./dragon.txt", "r", encoding="utf-8").read()
wc.generate(text)
#   从背景图片生成颜色值
image_colors = ImageColorGenerator(back_color)
plt.imshow(wc)
plt.axis("off")
plt.show()
wc.to_file("test01.png")
plt.figure()

plt.imshow(wc.recolor(color_func=image_colors))
plt.show()
plt.axis("off")
wc.to_file("test02.png")