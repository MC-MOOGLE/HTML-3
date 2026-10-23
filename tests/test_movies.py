import pytest


@pytest.mark.parametrize(
    "params, expected_titles",
    [
        ({}, ["Матрица", "Интерстеллар", "Начало", "Аватар", "Титаник", "Дюна", "Довод"]),
        ({"year_min": 2010}, ["Интерстеллар", "Начало", "Дюна", "Довод"]),
        ({"year_max": 1999}, ["Матрица", "Титаник"]),
        ({"min_rating": 8.5}, ["Матрица", "Интерстеллар", "Начало"]),
        ({"year_min": 2000, "year_max": 2015, "min_rating": 8.0}, ["Интерстеллар", "Начало"]),
        ({"year_min": 2030}, []),
    ],
)
def test_movies_filters(client, params, expected_titles):
    response = client.get("/movies/", params=params)

    assert response.status_code == 200
    titles = [movie["title"] for movie in response.json()]
    assert sorted(titles) == sorted(expected_titles)
