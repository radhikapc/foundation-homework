# Notes #

I had problem with the last question. I am still not sure why should we use the aggregate function count, such as count(rating),  in the query to find out the answer.

The following worked fine, though i did not use release_date in SELECT. Still it displayed the release dates. Both avg(udata. rating) and avg(rating) gave the correct answer. How ?

SELECT uitem.movie_title, avg(rating) FROM udata JOIN uitem on item_id = movie_id WHERE horror=1 GROUP BY uitem.movie_title HAVING count(rating) > 10 ORDER BY avg(udata.rating) limit 10;"
