-- 코드를 입력하세요
SELECT 진료과코드, 5월예약건수 FROM (
    SELECT MCDP_CD AS 진료과코드, COUNT(PT_NO) AS 5월예약건수
    FROM APPOINTMENT
    WHERE  APNT_YMD LIKE "2022-05%"
    GROUP BY MCDP_CD
    ) AS A
ORDER BY 5월예약건수 ASC, 진료과코드 ASC
;