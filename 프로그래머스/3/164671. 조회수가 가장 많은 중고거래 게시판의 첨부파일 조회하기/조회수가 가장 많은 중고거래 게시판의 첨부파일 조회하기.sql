-- 코드를 입력하세요
SELECT CONCAT_WS("/", "/home/grep/src", BOARD_ID, CONCAT(FILE_ID, FILE_NAME, FILE_EXT)) AS FILE_PATH
FROM (
    SELECT USED_GOODS_FILE.*
    FROM USED_GOODS_BOARD LEFT JOIN USED_GOODS_FILE
    ON USED_GOODS_BOARD.BOARD_ID = USED_GOODS_FILE.BOARD_ID
    ORDER BY USED_GOODS_BOARD.VIEWS DESC
     ) as A
WHERE BOARD_ID = (SELECT BOARD_ID 
                  FROM USED_GOODS_BOARD
                  ORDER BY VIEWS DESC
                  LIMIT 1
                 )
ORDER BY FILE_ID DESC
;