#!/usr/bin/env python
# coding: utf-8

# In[522]:


import numpy as np
import pandas as pd
import seaborn as sns
import operator
import itertools
import matplotlib.pyplot as plt
from collections import Counter


# In[523]:


data = pd.read_csv('movie_bd_v5.xls')
data.sample(5)


# In[524]:


data.columns = ['id','budget','revenue', 'title', 'cast', 'dir', 'tag', 'overview',
                'minutes', 'genres', 'production', 'date', 'score', 'year']
data2 = data.drop(columns = ['cast', 'dir', 'tag', 'overview','production', 'date'])


# In[525]:


genres_unique = pd.DataFrame(data.genres.str.split('|').tolist()).stack().unique()
genres_unique = pd.DataFrame(genres_unique, columns = ['genre'])


# In[526]:


data['profit'] = data['revenue'] - data['budget']


# # Предобработка

# In[ ]:





# In[ ]:





# In[439]:


answers = {} # создадим словарь для ответов

# тут другие ваши предобработки колонок например:

#the time given in the dataset is in string format.
#So we need to change this in datetime format
# ...


# # 1. У какого фильма из списка самый большой бюджет?

# Использовать варианты ответов в коде решения запрещено.    
# Вы думаете и в жизни у вас будут варианты ответов?)

# In[527]:


data.budget.sort_values(ascending=False)


# In[528]:


data[data.budget == data.budget.max()].title


# In[529]:


# в словарь вставляем номер вопроса и ваш ответ на него
# Пример: 
answers['1'] = '2. Spider-Man 3 (tt0413300)'
# запишите свой вариант ответа
answers['1'] = '723    Pirates of the Caribbean: On Stranger Tides'
# если ответили верно, можете добавить комментарий со значком "+"
#+


# In[530]:


# тут пишем ваш код для решения данного вопроса:
data[data.budget == data.budget.max()].title


# ВАРИАНТ 2

# In[531]:


# можно добавлять разные варианты решения


# # 2. Какой из фильмов самый длительный (в минутах)?

# In[532]:


# думаю логику работы с этим словарем вы уже поняли, 
# по этому не буду больше его дублировать
answers['2'] = 'Gods and Generals'


# In[533]:


data2[data2.minutes == data2.minutes.max()].title


# In[534]:


data.minutes.max()


# # 3. Какой из фильмов самый короткий (в минутах)?
# 
# 
# 
# 

# In[535]:


data2[data2.minutes == data2.minutes.min()].title
answers['3'] = 'Winnie the Pooh'


# # 4. Какова средняя длительность фильмов?
# 

# In[536]:


data.minutes.mean()
answers['4'] = '110'


# # 5. Каково медианное значение длительности фильмов? 

# In[537]:


data.minutes.median()
answers['5'] = '107'


# # 6. Какой самый прибыльный фильм?
# #### Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма. (прибыль = сборы - бюджет) в нашем датасете это будет (profit = revenue - budget) 

# In[538]:


# лучше код получения столбца profit вынести в Предобработку что в начале
data[data.profit == data.profit.max()].title
answers['6'] = '239    Avatar'


# # 7. Какой фильм самый убыточный? 

# In[539]:


data[data.profit == data.profit.min()].title
answers['7'] = '1245    The Lone Ranger'


# # 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

# In[540]:


data[data.revenue > data.budget].id.count()
answers['8'] = '1478'


# # 9. Какой фильм оказался самым кассовым в 2008 году?

# In[541]:


data3 = data[data.year == 2008]
data3[data3.revenue == data3.revenue.max()]
answers['9'] = 'The Dark Knight'


# # 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?
# 

# In[542]:


data3 = data[(data.year >= 2012) & (data.year <= 2014)]
data3[data3.profit == data3.profit.min()]
answers['10'] = 'The Lone Ranger'


# # 11. Какого жанра фильмов больше всего?

# In[543]:


data2.genres = data2.genres.str.split('|')
data4 = data2.explode('genres')
data4.genres.value_counts()


# In[544]:


# эту задачу тоже можно решать разными подходами, попробуй реализовать разные варианты
# если будешь добавлять функцию - выноси ее в предобработку что в начале
answers['11'] = 'Drama'


# ВАРИАНТ 2

# In[ ]:





# # 12. Фильмы какого жанра чаще всего становятся прибыльными? 

# In[545]:


data4['profit'] = data4.revenue - data4.budget
data4[data4['profit'] > 0].groupby(['genres'])['title'].count().sort_values()
answers['12'] = 'Drama'


# # 13. У какого режиссера самые большие суммарные кассовые сбооры?

# In[564]:


data5 = data.copy()
data5['dir'] = data.dir.str.split('|')
data5 = data.explode('dir')
data5.groupby(['dir'])['revenue'].sum().sort_values(ascending=False)


# In[547]:


answers['13'] = 'Peter Jackson'


# # 14. Какой режисер снял больше всего фильмов в стиле Action?

# In[569]:


s = data.copy()
s = s[s.genres.str.contains('Action')]
s = s.explode('dir')


# In[ ]:





# In[572]:


s.dir.value_counts()


# In[573]:


answers['14'] = 'Robert Rodriguez'


# # 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году? 

# In[576]:


data_cast = data.copy()
data_cast = data_cast[data_cast.year == 2012]
data_cast.cast = data_cast.cast.str.split('|')
data_cast = data_cast.explode('cast')


# In[577]:


data_cast.groupby(by='cast')['revenue'].max().sort_values(ascending=False)


# In[578]:


answers['15'] = 'Chris Hemsworth'


# # 16. Какой актер снялся в большем количестве высокобюджетных фильмов?

# In[579]:


data_cast_bg = data[data.budget > data.budget.mean()]
data_cast_bg.cast = data.cast.str.split('|')
data_cast_bg = data_cast_bg.explode('cast')
data_cast_bg.cast.value_counts()


# In[580]:


answers['16'] = 'Matt Damon'


# # 17. В фильмах какого жанра больше всего снимался Nicolas Cage? 

# In[581]:


data_cast_act = data.copy()
data_cast_act.genres = data.genres.str.split('|')
data_cast_act = data_cast_act.explode('genres')
data_cast_act[data.cast.str.contains('Nicolas Cage')].groupby(by='genres')['title'].count().sort_values(ascending=False)


# In[582]:


answers['17'] = 'Action'


# # 18. Самый убыточный фильм от Paramount Pictures

# In[585]:


minprod = data.copy()
minprod = minprod[minprod.production.str.contains('Paramount Pictures')]
minprod['profit']= minprod.revenue - minprod.budget
minprod[minprod.profit == minprod.profit.min()].title


# In[586]:


answers['18'] = 'K-19:The Widowmaker'


# # 19. Какой год стал самым успешным по суммарным кассовым сборам?

# In[587]:


goodyear = data.copy()
goodyear['profit'] = goodyear.revenue - goodyear.budget
gy = goodyear.groupby(by='year')['profit'].sum()
gy.sort_values(ascending=False)


# In[588]:


answers['19'] = '2015'


# # 20. Какой самый прибыльный год для студии Warner Bros?

# In[589]:


wb = data.copy()
wb['profit'] = wb.revenue - wb.budget
wb1 = wb[wb.production.str.contains('Warner Bros')]
wb1.groupby(by='year')['profit'].sum().sort_values(ascending=False)


# In[590]:


answers['20']='2014'


# # 21. В каком месяце за все годы суммарно вышло больше всего фильмов?

# In[591]:


data_month = data.copy()
data_month['date'] = pd.to_datetime(data_month['date'])
data_month['month'] = data_month['date'].dt.month
data_month.groupby(by='month')['title'].count()


# In[592]:


answers['21'] = 'Сентябрь'


# # 22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)

# In[593]:


data_month.groupby(by='month')['title'].count()[5:8].sum()


# In[594]:


answers['22'] = '450'


# # 23. Для какого режиссера зима – самое продуктивное время года? 

# In[598]:


dirdf = data.copy()
dirdf = dirdf.explode('dir')
dirdf['date'] = pd.to_datetime(dirdf['date'])
dirdf['month'] = dirdf['date'].dt.month
dirs = dirdf[dirdf.month.isin(['1','2','12'])]
dirs.groupby(by='dir')['title'].count().sort_values(ascending=False)


# In[599]:


answers['23'] = 'Peter Jackson'


# # 24. Какая студия дает самые длинные названия своим фильмам по количеству символов?

# In[600]:


df = data.copy()
df['production'] = df.production.str.split('|')
df = df.explode('production')

films = pd.Series(data['production'].str.cat(sep='|').split('|')).value_counts(ascending=False)
df['title_length'] = data.title.map(lambda x: len(x))
for company in films.index:
    films[company] = df['title_length'][df['production'].map(lambda x: True if company in x else False)].mean()
films = pd.DataFrame(films).sort_values(0, ascending=False)
films


# In[601]:


answers['24'] = 'Four By Two Productions'


# # 25. Описание фильмов какой студии в среднем самые длинные по количеству слов?

# In[604]:


films = pd.Series(df['production'].str.cat(sep='|').split('|')).value_counts(ascending=False)
df['overview_length'] = data.overview.map(lambda x: len(x.split(' ')))
for company in films.index:
    films[company] = df['overview_length'][df['production'].map(lambda x: True if company in x else False)].mean()
films = pd.DataFrame(films).sort_values(0, ascending=False)
films


# In[605]:


answers['25'] = 'Midnight Picture Show'


# # 26. Какие фильмы входят в 1 процент лучших по рейтингу? 
# по vote_average

# In[606]:


df[df.score >= df.score.quantile(.99)].title


# In[607]:


answers['26'] = 'Inside Out, The Dark Knight, 12 Years a Slave'


# # 27. Какие актеры чаще всего снимаются в одном фильме вместе?
# 

# ВАРИАНТ 2

# In[608]:


#если в фильме есть актёры, 
# 1 сделать из них неповторяющиеся пары 
# 2 и посчитать их
actors_data = data.copy()
pair_dict = {}
pairs = []
actors = pd.Series(actors_data.cast.str.cat(sep='|').split('|'))
pair_dict = {}
for cast in actors_data.cast:
    cast_pair = itertools.combinations(cast.split('|'), 2)
    cast_pairs = ['|'.join(i) for i in cast_pair]
    for pair in cast_pairs:
        if pair in pair_dict:
            pair_dict[pair] += 1
        else:
            pair_dict[pair] = 1

max(pair_dict.items(), key=operator.itemgetter(1))[0]


# In[609]:


answers['27'] = 'Daniel Radcliffe|Rupert Grint'


# # Submission

# In[610]:


# в конце можно посмотреть свои ответы к каждому вопросу
answers


# In[611]:


# и убедиться что ни чего не пропустил)
len(answers)


# In[ ]:





# In[ ]:




