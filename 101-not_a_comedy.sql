-- lists all shows without the genre Comedy in the database 
SELECT DISTINCT `title` FROM `tv_shows` AS t1 LEFT JOIN `tv_show_genres` AS t2
ON t1.`id` = t2.`show_id` LEFT JOIN `tv_genres` AS t3 ON t2.`genre_id` = t3.`id`
WHERE t1.`title` NOT IN (SELECT `title` FROM `tv_shows` AS t1 INNER JOIN
	`tv_show_genres` AS t2 ON t1.`id` = t2.`show_id` INNER JOIN `tv_genres`
	AS t3 ON t2.`genre_id` = t3.`id` WHERE t3.`name` = "Comedy")
ORDER BY `title`;
