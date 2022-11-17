# coding: utf8
""" 
@File: GetIndexData.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/9 18:56
"""

from source.tools.DataFormat import DataFormat
from source.tools.ToolsMySQL import Query


class GetIndexData(object):

    def __init__(self):
        self.DataFormat = DataFormat()
        self.data = self.DataFormat.data_matrix()
        self.actor_list = self.DataFormat.data_format_to_list('actors')
        self.director_list = self.DataFormat.data_format_to_list('directors')
        self.movie_country_list = self.DataFormat.data_format_to_list('movie_country')
        self.movie_type_list = self.DataFormat.data_format_to_list('movie_type')
        self.movie_lang_list = self.DataFormat.data_format_to_list('movie_lang')
        self.score_list = self.DataFormat.data_format_to_list('score')

    def get_movies_amount(self):
        return self.data.shape[0]

    def get_movies_score_max(self):
        return self.data['score'].max()

    def get_movies_actor_max(self):
        return max(self.actor_list, key=self.actor_list.count)

    def get_movies_director_max(self):
        return max(self.director_list, key=self.director_list.count)

    def get_movies_movie_country_max(self):
        return max(self.movie_country_list, key=self.movie_country_list.count)

    def get_movies_movie_type_amount(self):
        return len(set(self.movie_type_list))

    def get_movies_movie_lang_max(self):
        return max(self.movie_lang_list, key=self.movie_lang_list.count)

    def get_movies_movie_type_echarts(self):
        movies_type_dict = {}
        for movie_type in self.movie_type_list:
            if movies_type_dict.get('{}'.format(movie_type)) is None:
                movies_type_dict.update({'{}'.format(movie_type): 1})
            else:
                movies_type_dict.update({'{}'.format(movie_type): movies_type_dict.get('{}'.format(movie_type)) + 1})
        result = []
        for key, value in movies_type_dict.items():
            result.append({'value': value, 'name': key})
        return result

    def get_movies_score_echarts(self):
        movies_score_dict = {}
        for movie_type in self.score_list:
            if movies_score_dict.get('{}'.format(movie_type)) is None:
                movies_score_dict.update({'{}'.format(movie_type): 1})
            else:
                movies_score_dict.update({'{}'.format(movie_type): movies_score_dict.get('{}'.format(movie_type)) + 1})
        result_score = []
        result_amount = []
        for key, value in movies_score_dict.items():
            result_score.append(key)
            result_amount.append(value)
        return result_score, result_amount

    def get_movies_data(self):
        return self.data.values


class GetIndexDataMysql(Query):

    def __init__(self, limit: int = 50):
        super().__init__()
        self.id, self.directors, self.score, self.title, self.actors, \
        self.playbill_link, self.detail_link, self.release_year, self.movie_type, self.movie_country, \
        self.movie_lang, self.release_time, self.movie_long, self.short_review_num, self.star_compare, \
        self.summary, self.movie_review, self.about_img_url, self.movie_url, self.data = (list() for _ in range(20))
        query = "select tb_douban_movies.tb_movies_used_info_bak_all.id, " \
                "tb_douban_movies.tb_movies_used_info_bak_all.directors, " \
                "tb_douban_movies.tb_movies_used_info_bak_all.score, " \
                "tb_douban_movies.tb_movies_used_info_bak_all.title, " \
                "tb_douban_movies.tb_movies_used_info_bak_all.actors, " \
                "tb_douban_movies.tb_movies_used_info_bak_all.playbill_link, " \
                "tb_douban_movies.tb_movies_used_info_bak_all.detail_link, " \
                "tb_douban_movies.tb_movies_used_info_bak_all.release_year, " \
                "tb_douban_movies.tb_movies_used_info_bak_all.movie_type, " \
                "tb_douban_movies.tb_movies_used_info_bak_all.movie_country, " \
                "tb_douban_movies.tb_movies_used_info_bak_all.movie_lang, " \
                "tb_douban_movies.tb_movies_used_info_bak_all.release_time, " \
                "tb_douban_movies.tb_movies_used_info_bak_all.movie_long, " \
                "tb_douban_movies.tb_movies_used_info_bak_all.short_review_num, " \
                "tb_douban_movies.tb_movies_used_info_bak_all.star_compare, " \
                "tb_douban_movies.tb_movies_used_info_bak_all.summary, " \
                "tb_douban_movies.tb_movies_used_info_bak_all.movie_review, " \
                "tb_douban_movies.tb_movies_used_info_bak_all.about_img_url, " \
                "tb_douban_movies.tb_movies_used_info_bak_all.movie_url " \
                "from tb_douban_movies.tb_movies_used_info_bak_all " \
                "where tb_douban_movies.tb_movies_used_info_bak_all.is_delete = false " \
                "limit {} ;".format(limit)
        self.result = self.execute(query=query)
        for did, directors, score, title, actors, \
            playbill_link, detail_link, release_year, movie_type, movie_country, \
            movie_lang, release_time, movie_long, short_review_num, star_compare, \
            summary, movie_review, about_img_url, movie_url in self.result:
            self.id.append(did)
            self.directors.append(directors)
            self.score.append(score)
            self.title.append(title)
            self.actors.append(actors)
            self.playbill_link.append(playbill_link)
            self.detail_link.append(detail_link)
            self.release_year.append(release_year)
            self.movie_type.append(movie_type)
            self.movie_country.append(movie_country)
            self.movie_lang.append(movie_lang)
            self.release_time.append(release_time)
            self.movie_long.append(movie_long)
            self.short_review_num.append(short_review_num)
            self.star_compare.append(star_compare)
            self.summary.append(summary)
            self.movie_review.append(movie_review)
            self.about_img_url.append(about_img_url)
            self.movie_url.append(movie_url)
            self.data.append([
                id, directors, score, title, actors,
                playbill_link, detail_link, release_year, movie_type, movie_country,
                movie_lang, release_time, movie_long, short_review_num, star_compare,
                summary, movie_review, about_img_url, movie_url
            ])

    def get_movies_amount(self):
        return len(self.id)

    def get_movies_score_max(self, ):
        temp_score_list = []
        for row in self.score:
            row: str
            temp_score_list.append(float(row))
        return max(temp_score_list)

    def get_movies_actor_max(self):
        temp_actors_list = []
        for row in self.actors:
            row: str
            for actor in row.split(','):
                temp_actors_list.append(actor)
        return max(temp_actors_list, key=temp_actors_list.count)

    def get_movies_director_max(self):
        temp_director_list = []
        for row in self.directors:
            row: str
            for director in row.split(','):
                temp_director_list.append(director)
        return max(temp_director_list, key=temp_director_list.count)

    def get_movies_country_max(self):
        temp_movie_country_list = []
        for row in self.movie_country:
            row: str
            for movie_country in row.split(','):
                temp_movie_country_list.append(movie_country)
        return max(temp_movie_country_list, key=temp_movie_country_list.count)

    def get_movies_type_amount(self):
        temp_movie_type_list = []
        for row in self.movie_type:
            row: str
            for movie_type in row.split(','):
                temp_movie_type_list.append(movie_type)
        return len(set(temp_movie_type_list))

    def get_movies_languages_max(self):
        temp_movie_lang_list = []
        for row in self.movie_lang:
            row: str
            for movie_lang in row.split(','):
                temp_movie_lang_list.append(movie_lang)
        return max(temp_movie_lang_list, key=temp_movie_lang_list.count)

    def get_movies_type_echarts(self):
        movies_type_dict = {}
        result_list = []
        for row in self.movie_type:
            row: str
            for movie_type in row.split(','):
                if movies_type_dict.get('{}'.format(movie_type)) is None:
                    movies_type_dict.update({'{}'.format(movie_type): 1})
                else:
                    movies_type_dict.update({'{}'.format(movie_type): movies_type_dict.get('{}'.format(movie_type)) + 1})
        for key, value in movies_type_dict.items():
            result_list.append({'name': key, 'value': value})
        return result_list

    def get_movies_score_echarts(self):
        movies_score_dict = {}
        result_score = []
        result_amount = []
        for row in self.score:
            row: str
            for movie_type in row.split(','):
                if movies_score_dict.get('{}'.format(movie_type)) is None:
                    movies_score_dict.update({'{}'.format(movie_type): 1})
                else:
                    movies_score_dict.update({'{}'.format(movie_type): movies_score_dict.get('{}'.format(movie_type)) + 1})
        movies_score_dict = {data[0]: data[1] for data in sorted(movies_score_dict.items(), key=lambda x: x[0])}
        for key, value in movies_score_dict.items():
            result_score.append(key)
            result_amount.append(value)
        return result_score, result_amount

    def get_movies_data(self):
        return self.data
