-- 코드를 입력하세요
with high_view as (
    select *
    from used_goods_board
    order by views desc
    limit 1
)

SELECT concat('/home/grep/src/', f.board_id,'/', f.file_id, f.file_name, f.file_ext) as FILE_PATH
from high_view v, used_goods_file f
where v.board_id=f.board_id
order by f.file_id desc






