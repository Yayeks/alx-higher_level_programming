-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT DISTINCT `name` FROM `tv_genres` AS t1 INNER JOIN `tv_show_genres` AS t2
ON t1.`id` = t2.`genre_id` INNER JOIN `tv_shows` AS t3 ON t2.`show_id` = t3.`id`
WHERE t1.`name` NOT IN (SELECT `name` FROM `tv_genres` AS t1 INNER JOIN
	ON t1.`id` = t2.`genre_id` INNER JOIN `tv_shows` AS t3 ON
	t2.`show_id` = t3.`id` WHERE t3.`title` = "Dexter")
ORDER BY t1.`name`;
