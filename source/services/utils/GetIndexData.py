# coding: utf8
""" 
@File: GetIndexData.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/9 18:56
"""

# from source.tools.DataFormat import DataFormat
from source.tools.ToolsMySQL import ConnectMySQL


# class GetIndexData(object):
# 
#     def __init__(self):
#         self.DataFormat = DataFormat()
#         self.data = self.DataFormat.data_matrix()
#         self.actor_list = self.DataFormat.data_format_to_list('actors')
#         self.director_list = self.DataFormat.data_format_to_list('directors')
#         self.movie_country_list = self.DataFormat.data_format_to_list('movie_country')
#         self.movie_type_list = self.DataFormat.data_format_to_list('movie_type')
#         self.movie_lang_list = self.DataFormat.data_format_to_list('movie_lang')
#         self.score_list = self.DataFormat.data_format_to_list('score')
# 
#     def get_movies_amount(self):
#         return self.data.shape[0]
# 
#     def get_movies_score_max(self):
#         return self.data['score'].max()
# 
#     def get_movies_actor_max(self):
#         return max(self.actor_list, key=self.actor_list.count)
# 
#     def get_movies_director_max(self):
#         return max(self.director_list, key=self.director_list.count)
# 
#     def get_movies_movie_country_max(self):
#         return max(self.movie_country_list, key=self.movie_country_list.count)
# 
#     def get_movies_movie_type_amount(self):
#         return len(set(self.movie_type_list))
# 
#     def get_movies_movie_lang_max(self):
#         return max(self.movie_lang_list, key=self.movie_lang_list.count)
# 
#     def get_movies_movie_type_echarts(self):
#         movies_type_dict = {}
#         for movie_type in self.movie_type_list:
#             if movies_type_dict.get('{}'.format(movie_type)) is None:
#                 movies_type_dict.update({'{}'.format(movie_type): 1})
#             else:
#                 movies_type_dict.update({'{}'.format(movie_type): movies_type_dict.get('{}'.format(movie_type)) + 1})
#         result = []
#         for key, value in movies_type_dict.items():
#             result.append({'value': value, 'name': key})
#         return result
# 
#     def get_movies_score_echarts(self):
#         movies_score_dict = {}
#         for movie_type in self.score_list:
#             if movies_score_dict.get('{}'.format(movie_type)) is None:
#                 movies_score_dict.update({'{}'.format(movie_type): 1})
#             else:
#                 movies_score_dict.update({'{}'.format(movie_type): movies_score_dict.get('{}'.format(movie_type)) + 1})
#         result_score = []
#         result_amount = []
#         for key, value in movies_score_dict.items():
#             result_score.append(key)
#             result_amount.append(value)
#         return result_score, result_amount
# 
#     def get_movies_data(self):
#         return self.data.values


# class GetIndexDataMysql(Query):
# 
#     def __init__(self, limit_s: int = 1, limit_e: int = 300):
#         limit_s -= 1
#         limit_e -= limit_s
#         super().__init__()
#         self.id, self.directors, self.score, self.title, self.actors, \
#         self.playbill_link, self.detail_link, self.release_year, self.movie_type, self.movie_country, \
#         self.movie_lang, self.release_time, self.movie_long, self.short_review_num, self.star_compare, \
#         self.summary, self.movie_review, self.about_img_url, self.movie_url, self.data = (list() for _ in range(20))
#         query = "select tb_douban_movies.tb_movies_used_info_bak_all.id, " \
#                 "tb_douban_movies.tb_movies_used_info_bak_all.directors, " \
#                 "tb_douban_movies.tb_movies_used_info_bak_all.score, " \
#                 "tb_douban_movies.tb_movies_used_info_bak_all.title, " \
#                 "tb_douban_movies.tb_movies_used_info_bak_all.actors, " \
#                 "tb_douban_movies.tb_movies_used_info_bak_all.playbill_link, " \
#                 "tb_douban_movies.tb_movies_used_info_bak_all.detail_link, " \
#                 "tb_douban_movies.tb_movies_used_info_bak_all.release_year, " \
#                 "tb_douban_movies.tb_movies_used_info_bak_all.movie_type, " \
#                 "tb_douban_movies.tb_movies_used_info_bak_all.movie_country, " \
#                 "tb_douban_movies.tb_movies_used_info_bak_all.movie_lang, " \
#                 "tb_douban_movies.tb_movies_used_info_bak_all.release_time, " \
#                 "tb_douban_movies.tb_movies_used_info_bak_all.movie_long, " \
#                 "tb_douban_movies.tb_movies_used_info_bak_all.short_review_num, " \
#                 "tb_douban_movies.tb_movies_used_info_bak_all.star_compare, " \
#                 "tb_douban_movies.tb_movies_used_info_bak_all.summary, " \
#                 "tb_douban_movies.tb_movies_used_info_bak_all.movie_review, " \
#                 "tb_douban_movies.tb_movies_used_info_bak_all.about_img_url, " \
#                 "tb_douban_movies.tb_movies_used_info_bak_all.movie_url " \
#                 "from tb_douban_movies.tb_movies_used_info_bak_all " \
#                 "where tb_douban_movies.tb_movies_used_info_bak_all.is_delete = false " \
#                 "limit {}, {} ;".format(limit_s, limit_e)
#         self.result = self.execute(query=query)
#         for did, directors, score, title, actors, \
#             playbill_link, detail_link, release_year, movie_type, movie_country, \
#             movie_lang, release_time, movie_long, short_review_num, star_compare, \
#             summary, movie_review, about_img_url, movie_url in self.result:
#             self.id.append(did)
#             self.directors.append(directors)
#             self.score.append(score)
#             self.title.append(title)
#             self.actors.append(actors)
#             self.playbill_link.append(playbill_link)
#             self.detail_link.append(detail_link)
#             self.release_year.append(release_year)
#             self.movie_type.append(movie_type)
#             self.movie_country.append(movie_country)
#             self.movie_lang.append(movie_lang)
#             self.release_time.append(release_time)
#             self.movie_long.append(movie_long)
#             self.short_review_num.append(short_review_num)
#             self.star_compare.append(star_compare)
#             self.summary.append(summary)
#             self.movie_review.append(movie_review)
#             self.about_img_url.append(about_img_url)
#             self.movie_url.append(movie_url)
#             self.data.append([
#                 id, directors, score, title, actors,
#                 playbill_link, detail_link, release_year, movie_type, movie_country,
#                 movie_lang, release_time, movie_long, short_review_num, star_compare,
#                 summary, movie_review, about_img_url, movie_url
#             ])
# 
#     def get_movies_amount(self):
#         return len(self.id)
# 
#     def get_movies_score_max(self, ):
#         temp_score_list = []
#         for row in self.score:
#             row: str
#             temp_score_list.append(float(row))
#         return max(temp_score_list)
# 
#     def get_movies_actor_max(self):
#         temp_actors_list = []
#         for row in self.actors:
#             row: str
#             for actor in row.split(','):
#                 temp_actors_list.append(actor)
#         return max(temp_actors_list, key=temp_actors_list.count)
# 
#     def get_movies_director_max(self):
#         temp_director_list = []
#         for row in self.directors:
#             row: str
#             for director in row.split(','):
#                 temp_director_list.append(director)
#         return max(temp_director_list, key=temp_director_list.count)
# 
#     def get_movies_country_max(self):
#         temp_movie_country_list = []
#         for row in self.movie_country:
#             row: str
#             for movie_country in row.split(','):
#                 temp_movie_country_list.append(movie_country)
#         return max(temp_movie_country_list, key=temp_movie_country_list.count)
# 
#     def get_movies_type_amount(self):
#         temp_movie_type_list = []
#         for row in self.movie_type:
#             row: str
#             for movie_type in row.split(','):
#                 temp_movie_type_list.append(movie_type)
#         return len(set(temp_movie_type_list))
# 
#     def get_movies_languages_max(self):
#         temp_movie_lang_list = []
#         for row in self.movie_lang:
#             row: str
#             for movie_lang in row.split(','):
#                 temp_movie_lang_list.append(movie_lang)
#         return max(temp_movie_lang_list, key=temp_movie_lang_list.count)
# 
#     def get_movies_type_echarts(self):
#         movies_type_dict = {}
#         result_list = []
#         for row in self.movie_type:
#             row: str
#             for movie_type in row.split(','):
#                 if movies_type_dict.get('{}'.format(movie_type)) is None:
#                     movies_type_dict.update({'{}'.format(movie_type): 1})
#                 else:
#                     movies_type_dict.update({'{}'.format(movie_type): movies_type_dict.get('{}'.format(movie_type)) + 1})
#         for key, value in movies_type_dict.items():
#             result_list.append({'name': key, 'value': value})
#         return result_list
# 
#     def get_movies_score_echarts(self):
#         movies_score_dict = {}
#         result_score = []
#         result_amount = []
#         for row in self.score:
#             row: str
#             for movie_type in row.split(','):
#                 if movies_score_dict.get('{}'.format(movie_type)) is None:
#                     movies_score_dict.update({'{}'.format(movie_type): 1})
#                 else:
#                     movies_score_dict.update({'{}'.format(movie_type): movies_score_dict.get('{}'.format(movie_type)) + 1})
#         movies_score_dict = {data[0]: data[1] for data in sorted(movies_score_dict.items(), key=lambda x: x[0])}
#         for key, value in movies_score_dict.items():
#             result_score.append(key)
#             result_amount.append(value)
#         return result_score, result_amount
# 
#     def get_movies_data(self):
#         return self.data


class GetIndexData(object):
    
    def __init__(self):
        self.connect = ConnectMySQL()
        pass
    
    def test(self):
        sql = """
        select count(tb_movies_used_info.id) from tb_movies_used_info where tb_movies_used_info.is_delete is FALSE ;
        """
        return self.connect.query(sql=sql)[0][0]
    
    def get_movies_score_max(self, limit):
        sql = """
        select tb_movies_used_info.score from tb_movies_used_info where tb_movies_used_info.is_delete is false limit {} ;
        """.format(limit)
        score_list_temp = [row[0] for row in self.connect.query(sql=sql)]
        score_dict_temp = {}
        score_list = []
        score_num_list = []
        for score in score_list_temp:
            if score_dict_temp.get('{}'.format(score)) is None:
                score_dict_temp['{}'.format(score)] = 1
            else:
                score_dict_temp['{}'.format(score)] += 1
        score_dict_temp = {data[0]: data[1] for data in sorted(score_dict_temp.items(), key=lambda x: x[0])}
        for score, score_num in score_dict_temp.items():
            score_list.append(score)
            score_num_list.append(score_num)
        return max(score_list_temp), score_list, score_num_list
    # @numba.jit()
    def get_movies_actor_max(self, limit):
        sql = """
        select tb_movies_used_info.actors from tb_movies_used_info where tb_movies_used_info.is_delete is false limit {} ;
        """.format(limit)
        actors_list_temp = [row[0] for row in self.connect.query(sql=sql)]
        actors_list = []
        actors_dict_temp = {}
        for actors in actors_list_temp:
            actors: str
            for actor in actors.split(','):
                actors_list.append(actor)
        for item in actors_list:
            print(item)
            actors_dict_temp['{}'.format(item)] = actors_dict_temp.setdefault(item, 0) + 1
        print(actors_dict_temp)
        return max(set(actors_list), key=actors_list.count)
    
    def get_movies_country_max(self, limit):
        sql = """
        select tb_movies_used_info.movie_country from tb_movies_used_info where tb_movies_used_info.is_delete is false limit {} ;
        """.format(limit)
        countrys_list_temp = [row[0] for row in self.connect.query(sql=sql)]
        country_list = []
        for countrys in countrys_list_temp:
            countrys: str
            for country in countrys.split(','):
                country_list.append(country)
        return max(country_list, key=country_list.count)
    
    def get_movies_type(self, limit):
        sql = """
        select tb_movies_used_info.movie_type from tb_movies_used_info where tb_movies_used_info.is_delete is false limit {} ;    
        """.format(limit)
        m_types_list_temp = [row[0] for row in self.connect.query(sql=sql)]
        m_type_list = []
        m_type_echarts_dict = {}
        m_type_echarts_list = []
        for m_types in m_types_list_temp:
            m_types: str
            for m_type in m_types.split(','):
                m_type_list.append(m_type)
        for m_type in m_type_list:
            if m_type_echarts_dict.get('{}'.format(m_type)) is None:
                m_type_echarts_dict['{}'.format(m_type)] = 1
            else:
                m_type_echarts_dict['{}'.format(m_type)] += 1
        for key, value in m_type_echarts_dict.items():
            m_type_echarts_list.append({'name': key, 'value': value})
        
        return len(set(m_type_list)), m_type_echarts_list
    
    def get_movies_languange_max(self, limit):
        sql = """
        select tb_movies_used_info.movie_lang from tb_movies_used_info where tb_movies_used_info.is_delete is false limit {} ;
        """.format(limit)
        languages_list_temp = [row[0] for row in self.connect.query(sql=sql)]
        languages_list = []
        for languages in languages_list_temp:
            languages: str
            for language in languages.split(','):
                languages_list.append(language)
        return max(languages_list, key=languages_list.count)



