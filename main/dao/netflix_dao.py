import sqlite3
import os


class NetflixDAO:

    def __init__(self, path):
        self.path = path

    def load_netflix_bd(self, query):
        '''
        :param query: get query for data base
        :return: returns all rows by query
        '''
        with sqlite3.connect(os.path.join(self.path)) as con_bd_netflix:
            cur = con_bd_netflix.cursor()
            cur.execute(query)
            return cur.fetchall()

    def qury_data_by_title(self, title):
        '''
        :param title: get movie title
        :return: returns rows with title, country, release_year, genre, description
        '''
        query = f'''
            SELECT DISTINCT title, country, release_year, listed_in, description
            FROM netflix
            WHERE title == "{title}"
            ORDER BY release_year DESC
            '''

        result_query = self.load_netflix_bd(query)[0]

        result = {"title": result_query[0],
                  "country": result_query[1],
                  "release_year": result_query[2],
                  "genre": result_query[3],
                  "description": result_query[4].strip()}

        return result

    def query_year_to_year(self, first_year, second_year):
        '''
        :param first_year: get first year, and second year
        :param second_year:
        :return: returns rows title, release_year by given years
        '''
        query = f'''
                    SELECT title, release_year
                    FROM netflix
                    WHERE release_year BETWEEN {first_year} AND {second_year}
                    ORDER BY release_year DESC
                    LIMIT 100
                    '''
        result_query = self.load_netflix_bd(query)

        result = list(map(lambda item: {'title': item[0], 'release_year': item[1]} , result_query))

        return result

    def query_rating(self, type_rating):
        '''
        :param type_rating: get type age rating
        :return: returns rows with title, rating, description
        '''
        rating = {'children': ['G'], 'family': ['G', 'PG', 'PG-13'], 'adult': ['R', 'NC-17']}
        join_rating_for_query = '"' + '", "'.join(rating[type_rating]) + '"'

        query = f'''
                            SELECT title, rating, description
                            FROM netflix
                            WHERE rating IN ({join_rating_for_query})
                            LIMIT 100
                            '''
        result_query = self.load_netflix_bd(query)

        result = list(map(lambda item: {'title': item[0], 'rating': item[1], 'description': item[2].strip()}, result_query))
        return result

    def query_by_genre(self, genre):
        '''
        :param genre: get genre
        :return: returns rows - title, description
        '''
        query = f'''
                            SELECT title, description
                            FROM netflix
                            WHERE listed_in LIKE "%{genre}%"
                            ORDER BY release_year DESC
                            LIMIT 10  
                            '''
        result_query = self.load_netflix_bd(query)
        result = list(map(lambda item: {'title': item[0], 'description': item[1].strip()}, result_query))
        return result