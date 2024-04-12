-- 코드를 입력하세요
SELECT b.WRITER_ID AS USER_ID, u.NICKNAME, SUM(b.PRICE) AS TOTAL_SALES FROM USED_GOODS_BOARD AS b ,USED_GOODS_USER AS u
WHERE b.STATUS = 'DONE' AND b.WRITER_ID = u.USER_ID
GROUP BY b.WRITER_ID
HAVING SUM(b.PRICE)>=700000
ORDER BY SUM(b.PRICE)

