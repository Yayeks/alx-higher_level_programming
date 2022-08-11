-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT `name`, SUM(`rate`) AS `rating` FROM `tv_genres` AS t1 INNER JOIN
`tv_show_genres` AS t2 ON t1.`id` = t2.`genre_id` INNER JOIN `tv_show_ratings`
AS t3 USING(`show_id`) GROUP BY `name` ORDER BY `rating` DESC;
