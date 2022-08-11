-- lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT `title`, SUM(`rate`) AS `rating` FROM `tv_shows` AS t1
INNER JOIN `tv_show_ratings` AS t2 ON t.`id` = t2.`show_id`
GROUP BY `title` ORDER BY `rating` DESC;
