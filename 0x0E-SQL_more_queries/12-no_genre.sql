-- lists all shows contained in the db without a genre linked
-- each record should display tv_shows.title, tv_show_genres.genre_id
-- results are ordered in ascending order by
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
