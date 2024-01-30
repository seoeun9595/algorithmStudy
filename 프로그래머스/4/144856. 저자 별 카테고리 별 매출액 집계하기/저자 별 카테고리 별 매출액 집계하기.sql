-- 코드를 입력하세요
SELECT A.AUTHOR_ID
     , A.AUTHOR_NAME
     , B.CATEGORY
     , SUM(B.PRICE * BS.SALES) AS 'SALES'
FROM BOOK AS B
JOIN AUTHOR AS A ON B.AUTHOR_ID = A.AUTHOR_ID
JOIN BOOK_SALES AS BS ON B.BOOK_ID = BS.BOOK_ID
WHERE BS.SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31'
GROUP BY A.AUTHOR_ID, B.CATEGORY
ORDER BY A.AUTHOR_ID, B.CATEGORY DESC;