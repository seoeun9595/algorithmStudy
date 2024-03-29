-- 코드를 입력하세요
SELECT DISTINCT CAR_ID
FROM CAR_RENTAL_COMPANY_CAR AS C
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS RH USING (CAR_ID)
WHERE (C.CAR_TYPE = '세단')
  AND (RH.START_DATE BETWEEN '2022-10-01' AND '2022-10-31')
ORDER BY CAR_ID DESC;