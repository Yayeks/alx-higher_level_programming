-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT t1.`name`, COUNT(*) AS `number_of_shows` FROM `tv_genres` AS t1 INNER 
JOIN `tv_show_genres` AS t2 ON t1.`id` = t2.`genre_id` GROUP BY t1.`name`
ORDER BY `number_of_shows` DESC;
