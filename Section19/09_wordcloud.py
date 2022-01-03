import matplotlib.pyplot as plt
import wordcloud

words ={
    '파이썬':20,
    '빅데이터':5,
    '웹크롤링':7,
    '인공지능':9,
    '딥러닝':12
}
wc = wordcloud.WordCloud(font_path='C:/Windows/Fonts/gulim.ttc')
cloud = wc.generate_from_frequencies(words)

plt.figure()
plt.imshow(cloud)

plt.show()