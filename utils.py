import sqlite3
import os
import json


def load_bd(query):
    with sqlite3.connect(os.path.join('netflix.db')) as con_bd_netflix:
        cur = con_bd_netflix.cursor()
        cur.execute(query)
        return cur.fetchall()


def query_two_actors(actor_first, actor_second):
    '''
    :param actor_first: get name first actor
    :param actor_second: get name second actor
    :return: returns the names of the actors who played with the given more than two times
    '''
    query = f'''
    SELECT "cast"
    FROM netflix
    WHERE "cast" LIKE "%{actor_first}%"
    AND "cast" LIKE "%{actor_second}%"
    '''

    query_result = load_bd(query)

    actors = []
    actors_more_two = set()

    for films in query_result:
        actors += films[0].split(', ')

    for actor in actors:
        if actors.count(actor) > 2:
            if actor != actor_first and actor != actor_second:
                actors_more_two.add(actor)

    return list(actors_more_two)


def query_three_options(type, year, genre):
    '''
    :param type: get type
    :param year: get year
    :param genre: get genre
    :return: returns a list according to the given criteria
    '''

    query = f'''
            SELECT title, description
            FROM netflix
            WHERE type LIKE "%{type}%"
            AND release_year == {year}
            AND listed_in LIKE "%{genre}%"
            LIMIT 10
                                        '''
    query_result = load_bd(query)

    result = list(map(lambda item: {'title': item[0], 'description': item[1].strip()}, query_result))

    return json.dumps(result, indent=2)


test1 = query_two_actors('Rose McIver', 'Ben Lamb')
test2 = query_two_actors('Jack Black', 'Dustin Hoffman')
test3 = query_three_options('TV Show', 2010, 'Dramas')

# print(test3)

for row in test1:
    print(row)



