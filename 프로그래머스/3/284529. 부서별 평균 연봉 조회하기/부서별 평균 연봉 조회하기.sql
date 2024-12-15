-- 코드를 작성해주세요
SELECT DP.DEPT_ID, DEPT_NAME_EN, ROUND(AVG(SAL), 0) AS AVG_SAL
FROM HR_DEPARTMENT DP INNER JOIN HR_EMPLOYEES EM
ON DP.DEPT_ID = EM.DEPT_ID
GROUP BY DP.DEPT_ID, DEPT_NAME_EN
ORDER BY AVG_SAL DESC;