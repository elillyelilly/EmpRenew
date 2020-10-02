from django.shortcuts import render
from .models import Tdm0101Shain
from .models import Empcolumn
from django.db import connection

from django.http import HttpResponse

def edit(request):
    return render(request, 'EmpRenew/edit.html', {})
def disp(request):
    with connection.cursor() as cursor:
        sql = '''
        DECLARE @cd int;
        SET @cd =2714; 
        select
        TDM0101_SHAIN.TDM0101_SHAIN_CD as id 
        ,TDM0101_SHAIN.TDM0101_SHAIN_CD as shain_cd
        ,TDM0101_SHAIN.TDM0101_SHAIN_NM as shain_nm
        ,TDM0101_SHAIN.TDM0101_SHAIN_NM_K as shain_nm_k
        ,TDM0101_SHAIN.TDM0101_ADRS1 as adr1
        ,TDM0101_SHAIN.TDM0101_ADRS2 as adr2
        ,TDM0101_SHAIN.TDM0101_TEL1 as tel1
        ,TDM0101_SHAIN.TDM0101_BIRTH_DATE as birth_date
        ,TDM0108_KOYOU_KEIYAKU.TDM0108_KEIYAKU_START_DATE as keiyaku_start_date
        ,TDM0108_KOYOU_KEIYAKU.TDM0108_KEIYAKU_END_DATE as keiyaku_end_date
        ,TBM0018_GENBA.TBM0018_GENBA_NAME as genba_name
        ,TDM0108_KOYOU_KEIYAKU.TDM0108_SHUGYOU1_TO as shugyou1_to
        ,TDM0108_KOYOU_KEIYAKU.TDM0108_SHUGYOU2_TO as shugyou2_to
        ,TDM0108_KOYOU_KEIYAKU.TDM0108_SHUGYOU3_TO as shugyou3_to
        ,TDM0108_KOYOU_KEIYAKU.TDM0108_SHUGYOU4_TO as shugyou4_to
        ,TDM0108_KOYOU_KEIYAKU.TDM0108_SHUGYOU1_FROM as shugyou1_from
        ,TDM0108_KOYOU_KEIYAKU.TDM0108_SHUGYOU2_FROM as shugyou2_from
        ,TDM0108_KOYOU_KEIYAKU.TDM0108_SHUGYOU3_FROM as shugyou3_from
        ,TDM0108_KOYOU_KEIYAKU.TDM0108_SHUGYOU4_FROM as shugyou4_from
        ,TDM0108_KOYOU_KEIYAKU.TDM0108_SHUGYOU1_BREAK as shugyou1_break
        ,TDM0108_KOYOU_KEIYAKU.TDM0108_SHUGYOU2_BREAK as shugyou2_break
        ,TDM0108_KOYOU_KEIYAKU.TDM0108_SHUGYOU3_BREAK as shugyou3_break
        ,TDM0108_KOYOU_KEIYAKU.TDM0108_SHUGYOU4_BREAK as shugyou4_break
        ,TDM0108_KOYOU_KEIYAKU.TDM0108_SYUROU_NISSU as shurou_nissu
        ,TBM0019_SHOKU_SHU.TBM0019_SHOKU_NAME as shoku_name
        ,TDM0108_KOYOU_KEIYAKU.TDM0108_CHINGIN_KBN as chingin_kbn
        ,TDM0108_KOYOU_KEIYAKU.TDM0108_CHINGIN_DT_1 as chingin_dt_1
        ,TDM0108_KOYOU_KEIYAKU.TDM0108_CHINGIN_DT_2 as chingin_dt_2
        ,TDM0108_KOYOU_KEIYAKU.TDM0108_CHINGIN_DT_3 as chingin_dt_3
        ,TDT0306_NEXT_UQ_DATE as next_uq_date
        ,TDM0108_SHUGYOU1_KOSU as shugyou1_kosu
        ,TDM0108_SHUGYOU1_KOSU as shugyou2_kosu
        ,TDM0108_SHUGYOU1_KOSU as shugyou3_kosu
        ,TDM0108_SHUGYOU1_KOSU as shugyou4_kosu
        ,TDT0306_NEXT_UQ_DAY_NUM as next_uq_day_num
        ,TDT0306_TOU_STR_UQ_ZAN_NUM as tou_str_uq_zan_num
        ,TDM0101_SHAIN.TDM0101_KOYOU_HOKEN_KBN_CD as koyou_hoken_kbn
        ,TDM0101_SHAIN.TDM0101_SHAKAI_HOKEN_KBN_CD as shakai_hoken_kbn_cd
        ,GETDATE() as created_date
        FROM
        TDM0101_SHAIN
        ,TDT0306_UQ_INFO
        ,TDM0108_KOYOU_KEIYAKU
        LEFT JOIN TBM0019_SHOKU_SHU ON TDM0108_KOYOU_KEIYAKU.TDM0108_SHOKU_SHU_CD = TBM0019_SHOKU_CD
        LEFT JOIN TBM0018_GENBA ON TBM0018_GENBA_CD = TDM0108_GENBA_CD
        WHERE 
        TDM0101_SHAIN.TDM0101_SHAIN_CD = @cd 
        AND TDM0101_DEL_FLG <> 1
        AND TDM0108_DEL_FLG <> 1
        AND TDM0101_SHAIN.TDM0101_SHAIN_CD = TDM0108_KOYOU_KEIYAKU.TDM0101_SHAIN_CD
        AND TDM0101_SHAIN.TDM0101_SHAIN_CD = TDT0306_UQ_INFO.TDT0306_SHAIN_CD
        AND TDT0306_NENDO = 2020 
        AND TDT0306_GETSUDO = 2 
        '''
        display = Empcolumn.objects.raw(sql)
 #       cursor.execute(sql)
 #       display = cursor.fetchall()
 #       disp = cursor.fetchall()
#        display = list(disp)

        return render(request, 'EmpRenew/disp.html', {'display':display })
