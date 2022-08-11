-- lists all shows, and all genres linked to that show, from the database
SELECT t1.`title`, t3.`name` FROM `tv_shows` AS t1 LEFT JOIN `tv_show_genres` AS
t2 ON t1.`id` = t2.`show_id` LEFT JOIN `tv_genres` AS t3 ON t2.`genre_id` =
t3.`id` ORDER BY t1.`title`, t3.`name`;
