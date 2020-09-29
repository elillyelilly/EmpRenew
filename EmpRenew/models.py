from django.conf import settings
from django.db import models
from django.utils import timezone

class Empcol(models.Model):
    shain_cd = models.CharField(max_length=10)
    shain_nm = models.CharField(max_length=50)
    shain_nm_k = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EmprenewEmpcolumn(models.Model):
    shain_cd = models.CharField(max_length=10)
    shain_nm = models.CharField(max_length=50)
    adr1 = models.CharField(max_length=50)
    adr2 = models.CharField(max_length=50)
    tel1 = models.CharField(max_length=50)
    birth_date = models.CharField(max_length=50)
    keiyaku_start_date = models.CharField(max_length=50)
    keiyaku_end_date = models.CharField(max_length=50)
    genba_name = models.CharField(max_length=50)
    shugyou1_to = models.CharField(max_length=50)
    shugyou2_to = models.CharField(max_length=50)
    shugyou3_to = models.CharField(max_length=50)
    shugyou4_to = models.CharField(max_length=50)
    shugyou1_from = models.CharField(max_length=50)
    shugyou2_from = models.CharField(max_length=50)
    shugyou3_from = models.CharField(max_length=50)
    shugyou4_from = models.CharField(max_length=50)
    shugyou1_break = models.CharField(max_length=50)
    shugyou2_break = models.CharField(max_length=50)
    shugyou3_break = models.CharField(max_length=50)
    shugyou4_break = models.CharField(max_length=50)
    shurou_nissu = models.CharField(max_length=50)
    shoku_name = models.CharField(max_length=50)
    chingin_kbn = models.CharField(max_length=50)
    chingin_dt_1 = models.CharField(max_length=50)
    chingin_dt_2 = models.CharField(max_length=50)
    chingin_dt_3 = models.CharField(max_length=50)
    chingin_dt_4 = models.CharField(max_length=50)
    next_uq_date = models.CharField(max_length=50)
    shugyou1_kosu = models.CharField(max_length=50)
    shugyou2_kosu = models.CharField(max_length=50)
    shugyou3_kosu = models.CharField(max_length=50)
    shugyou4_kosu = models.CharField(max_length=50)
    next_uq_day_num = models.CharField(max_length=50)
    tou_str_uq_zan_num = models.CharField(max_length=50)
    koyou_hoken_kbn = models.CharField(max_length=50)
    shakai_hoken_kbn_cd = models.CharField(max_length=50)
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'EmpRenew_empcolumn'


class Tam01Sys(models.Model):
    tam01_sys_id = models.CharField(db_column='TAM01_SYS_ID', primary_key=True, max_length=2)  # Field name made lowercase.
    tam01_sys_nm = models.CharField(db_column='TAM01_SYS_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tam01_del_flg = models.CharField(db_column='TAM01_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tam01_crt_datetime = models.DateTimeField(db_column='TAM01_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tam01_crt_user_id = models.CharField(db_column='TAM01_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tam01_crt_prog_nm = models.CharField(db_column='TAM01_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tam01_upd_datetime = models.DateTimeField(db_column='TAM01_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tam01_upd_user_id = models.CharField(db_column='TAM01_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tam01_upd_prog_nm = models.CharField(db_column='TAM01_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tam01_upd_cnt = models.DecimalField(db_column='TAM01_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tam01_kisy = models.SmallIntegerField(db_column='TAM01_KISY', blank=True, null=True)  # Field name made lowercase.
    tam01_hnkan_nen = models.SmallIntegerField(db_column='TAM01_HNKAN_NEN', blank=True, null=True)  # Field name made lowercase.
    tam01_sime_day = models.SmallIntegerField(db_column='TAM01_SIME_DAY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAM01_SYS'


class Tam02Menu(models.Model):
    tam01_sys_id = models.CharField(db_column='TAM01_SYS_ID', primary_key=True, max_length=2)  # Field name made lowercase.
    tam02_menu_id_tree_1 = models.CharField(db_column='TAM02_MENU_ID_TREE_1', max_length=2)  # Field name made lowercase.
    tam02_menu_id_tree_2 = models.CharField(db_column='TAM02_MENU_ID_TREE_2', max_length=2)  # Field name made lowercase.
    tam02_menu_id_tree_3 = models.CharField(db_column='TAM02_MENU_ID_TREE_3', max_length=2)  # Field name made lowercase.
    tam02_menu_nm = models.CharField(db_column='TAM02_MENU_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tam02_app_id = models.CharField(db_column='TAM02_APP_ID', max_length=9, blank=True, null=True)  # Field name made lowercase.
    tam02_del_flg = models.CharField(db_column='TAM02_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tam02_crt_datetime = models.DateTimeField(db_column='TAM02_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tam02_crt_user_id = models.CharField(db_column='TAM02_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tam02_crt_prog_nm = models.CharField(db_column='TAM02_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tam02_upd_datetime = models.DateTimeField(db_column='TAM02_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tam02_upd_user_id = models.CharField(db_column='TAM02_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tam02_upd_prog_nm = models.CharField(db_column='TAM02_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tam02_upd_cnt = models.DecimalField(db_column='TAM02_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAM02_MENU'
        unique_together = (('tam01_sys_id', 'tam02_menu_id_tree_1', 'tam02_menu_id_tree_2', 'tam02_menu_id_tree_3'),)


class Tam03Appli(models.Model):
    tam03_app_id = models.CharField(db_column='TAM03_APP_ID', primary_key=True, max_length=9)  # Field name made lowercase.
    tam03_app_nm = models.CharField(db_column='TAM03_APP_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tam03_sub_menu_flg = models.CharField(db_column='TAM03_SUB_MENU_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tam03_kido_pg = models.CharField(db_column='TAM03_KIDO_PG', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tam03_del_flg = models.CharField(db_column='TAM03_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tam03_crt_datetime = models.DateTimeField(db_column='TAM03_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tam03_crt_user_id = models.CharField(db_column='TAM03_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tam03_crt_prog_nm = models.CharField(db_column='TAM03_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tam03_upd_datetime = models.DateTimeField(db_column='TAM03_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tam03_upd_user_id = models.CharField(db_column='TAM03_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tam03_upd_prog_nm = models.CharField(db_column='TAM03_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tam03_upd_cnt = models.DecimalField(db_column='TAM03_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tam03_batch_flg = models.CharField(db_column='TAM03_BATCH_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAM03_APPLI'


class Tam04Kngn(models.Model):
    tam04_kngn_ptn_kbn = models.CharField(db_column='TAM04_KNGN_PTN_KBN', primary_key=True, max_length=2)  # Field name made lowercase.
    tam04_kngn_ptn_nm = models.CharField(db_column='TAM04_KNGN_PTN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tam04_del_flg = models.CharField(db_column='TAM04_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tam04_crt_datetime = models.DateTimeField(db_column='TAM04_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tam04_crt_user_id = models.CharField(db_column='TAM04_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tam04_crt_prog_nm = models.CharField(db_column='TAM04_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tam04_upd_datetime = models.DateTimeField(db_column='TAM04_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tam04_upd_user_id = models.CharField(db_column='TAM04_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tam04_upd_prog_nm = models.CharField(db_column='TAM04_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tam04_upd_cnt = models.DecimalField(db_column='TAM04_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAM04_KNGN'


class Tam05AppliKngn(models.Model):
    tam04_kngn_ptn_kbn = models.CharField(db_column='TAM04_KNGN_PTN_KBN', primary_key=True, max_length=2)  # Field name made lowercase.
    tam03_app_id = models.CharField(db_column='TAM03_APP_ID', max_length=9)  # Field name made lowercase.
    tam05_kngn_flg = models.CharField(db_column='TAM05_KNGN_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tam05_del_flg = models.CharField(db_column='TAM05_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tam05_crt_datetime = models.DateTimeField(db_column='TAM05_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tam05_crt_user_id = models.CharField(db_column='TAM05_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tam05_crt_prog_nm = models.CharField(db_column='TAM05_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tam05_upd_datetime = models.DateTimeField(db_column='TAM05_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tam05_upd_user_id = models.CharField(db_column='TAM05_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tam05_upd_prog_nm = models.CharField(db_column='TAM05_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tam05_upd_cnt = models.DecimalField(db_column='TAM05_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAM05_APPLI_KNGN'
        unique_together = (('tam04_kngn_ptn_kbn', 'tam03_app_id'),)


class Tam06Msg(models.Model):
    tam06_msg_cd = models.CharField(db_column='TAM06_MSG_CD', primary_key=True, max_length=7)  # Field name made lowercase.
    tam06_msg = models.CharField(db_column='TAM06_MSG', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tam06_del_flg = models.CharField(db_column='TAM06_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tam06_crt_datetime = models.DateTimeField(db_column='TAM06_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tam06_crt_user_id = models.CharField(db_column='TAM06_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tam06_crt_prog_nm = models.CharField(db_column='TAM06_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tam06_upd_datetime = models.DateTimeField(db_column='TAM06_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tam06_upd_user_id = models.CharField(db_column='TAM06_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tam06_upd_prog_nm = models.CharField(db_column='TAM06_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tam06_upd_cnt = models.DecimalField(db_column='TAM06_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAM06_MSG'


class Tam07User(models.Model):
    tam07_user_id = models.CharField(db_column='TAM07_USER_ID', primary_key=True, max_length=12)  # Field name made lowercase.
    tam07_user_nm = models.CharField(db_column='TAM07_USER_NM', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tam07_user_kana_nm = models.CharField(db_column='TAM07_USER_KANA_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tam07_pwd = models.CharField(db_column='TAM07_PWD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tam07_kngn_ptn_kbn = models.CharField(db_column='TAM07_KNGN_PTN_KBN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tam07_del_flg = models.CharField(db_column='TAM07_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tam07_crt_datetime = models.DateTimeField(db_column='TAM07_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tam07_crt_user_id = models.CharField(db_column='TAM07_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tam07_crt_prog_nm = models.CharField(db_column='TAM07_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tam07_upd_datetime = models.DateTimeField(db_column='TAM07_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tam07_upd_user_id = models.CharField(db_column='TAM07_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tam07_upd_prog_nm = models.CharField(db_column='TAM07_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tam07_upd_cnt = models.DecimalField(db_column='TAM07_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tam07_sys_id = models.CharField(db_column='TAM07_SYS_ID', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tam07_bmn_cd = models.CharField(db_column='TAM07_BMN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tam07_shain_cd = models.CharField(db_column='TAM07_SHAIN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tam07_hyoj_no = models.DecimalField(db_column='TAM07_HYOJ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAM07_USER'


class Tas01Cdnm(models.Model):
    tas01_data_kind = models.CharField(db_column='TAS01_DATA_KIND', primary_key=True, max_length=3)  # Field name made lowercase.
    tas01_item_cd = models.CharField(db_column='TAS01_ITEM_CD', max_length=4)  # Field name made lowercase.
    tas01_item_nm = models.CharField(db_column='TAS01_ITEM_NM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tas01_item_ryak = models.CharField(db_column='TAS01_ITEM_RYAK', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tas01_del_flg = models.CharField(db_column='TAS01_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tas01_crt_datetime = models.DateTimeField(db_column='TAS01_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tas01_crt_user_id = models.CharField(db_column='TAS01_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tas01_crt_prog_nm = models.CharField(db_column='TAS01_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tas01_upd_datetime = models.DateTimeField(db_column='TAS01_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tas01_upd_user_id = models.CharField(db_column='TAS01_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tas01_upd_prog_nm = models.CharField(db_column='TAS01_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tas01_upd_cnt = models.DecimalField(db_column='TAS01_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAS01_CDNM'
        unique_together = (('tas01_data_kind', 'tas01_item_cd'),)


class Tas02Geng(models.Model):
    tas02_gngo_kbn = models.CharField(db_column='TAS02_GNGO_KBN', primary_key=True, max_length=1)  # Field name made lowercase.
    tas02_gngo_nm = models.CharField(db_column='TAS02_GNGO_NM', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tas02_gngo_ryak_nm = models.CharField(db_column='TAS02_GNGO_RYAK_NM', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tas02_hnkan_nen = models.SmallIntegerField(db_column='TAS02_HNKAN_NEN', blank=True, null=True)  # Field name made lowercase.
    tas02_date_start = models.CharField(db_column='TAS02_DATE_START', max_length=8, blank=True, null=True)  # Field name made lowercase.
    tas02_date_end = models.CharField(db_column='TAS02_DATE_END', max_length=8, blank=True, null=True)  # Field name made lowercase.
    tas02_date_w_start = models.CharField(db_column='TAS02_DATE_W_START', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tas02_date_w_end = models.CharField(db_column='TAS02_DATE_W_END', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tas02_del_flg = models.CharField(db_column='TAS02_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tas02_crt_datetime = models.DateTimeField(db_column='TAS02_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tas02_crt_user_id = models.CharField(db_column='TAS02_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tas02_crt_prog_nm = models.CharField(db_column='TAS02_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tas02_upd_datetime = models.DateTimeField(db_column='TAS02_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tas02_upd_user_id = models.CharField(db_column='TAS02_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tas02_upd_prog_nm = models.CharField(db_column='TAS02_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tas02_upd_cnt = models.DecimalField(db_column='TAS02_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAS02_GENG'


class Tat01Info(models.Model):
    tat01_info_no = models.AutoField(db_column='TAT01_INFO_NO', primary_key=True)  # Field name made lowercase.
    tat01_date_start = models.DateTimeField(db_column='TAT01_DATE_START', blank=True, null=True)  # Field name made lowercase.
    tat01_date_end = models.DateTimeField(db_column='TAT01_DATE_END', blank=True, null=True)  # Field name made lowercase.
    tat01_info = models.CharField(db_column='TAT01_INFO', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    tat01_del_flg = models.CharField(db_column='TAT01_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tat01_crt_datetime = models.DateTimeField(db_column='TAT01_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tat01_crt_user_id = models.CharField(db_column='TAT01_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tat01_crt_prog_nm = models.CharField(db_column='TAT01_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tat01_upd_datetime = models.DateTimeField(db_column='TAT01_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tat01_upd_user_id = models.CharField(db_column='TAT01_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tat01_upd_prog_nm = models.CharField(db_column='TAT01_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tat01_upd_cnt = models.DecimalField(db_column='TAT01_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAT01_INFO'


class Taw01ApiSdtWork(models.Model):
    taw01_session_id = models.CharField(db_column='TAW01_SESSION_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    taw01_gmn_id = models.CharField(db_column='TAW01_GMN_ID', max_length=30)  # Field name made lowercase.
    taw01_crt_date = models.DateTimeField(db_column='TAW01_CRT_DATE', blank=True, null=True)  # Field name made lowercase.
    taw01_sdt_save_1 = models.TextField(db_column='TAW01_SDT_SAVE_1', blank=True, null=True)  # Field name made lowercase.
    taw01_sdt_save_2 = models.TextField(db_column='TAW01_SDT_SAVE_2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAW01_API_SDT_WORK'
        unique_together = (('taw01_session_id', 'taw01_gmn_id'),)


class Tbm0004SzeiTnkKbn(models.Model):
    tbm0004_szei_tnk_kbn_cd = models.CharField(db_column='TBM0004_SZEI_TNK_KBN_CD', primary_key=True, max_length=3)  # Field name made lowercase.
    tbm0004_szei_tnk_kbn_nm = models.CharField(db_column='TBM0004_SZEI_TNK_KBN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0004_hnbai_knri_flg = models.BooleanField(db_column='TBM0004_HNBAI_KNRI_FLG', blank=True, null=True)  # Field name made lowercase.
    tbm0004_kobai_knri_flg = models.BooleanField(db_column='TBM0004_KOBAI_KNRI_FLG', blank=True, null=True)  # Field name made lowercase.
    tbm0004_del_flg = models.CharField(db_column='TBM0004_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0004_crt_datetime = models.DateTimeField(db_column='TBM0004_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0004_crt_user_id = models.CharField(db_column='TBM0004_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0004_crt_prog_nm = models.CharField(db_column='TBM0004_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0004_upd_datetime = models.DateTimeField(db_column='TBM0004_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0004_upd_user_id = models.CharField(db_column='TBM0004_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0004_upd_prog_nm = models.CharField(db_column='TBM0004_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0004_upd_cnt = models.DecimalField(db_column='TBM0004_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM0004_SZEI_TNK_KBN'


class Tbm0005PayMonthKbn(models.Model):
    tbm0005_pay_month_kbn_cd = models.CharField(db_column='TBM0005_PAY_MONTH_KBN_CD', primary_key=True, max_length=3)  # Field name made lowercase.
    tbm0005_pay_month_kbn_nm = models.CharField(db_column='TBM0005_PAY_MONTH_KBN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0005_del_flg = models.CharField(db_column='TBM0005_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0005_crt_datetime = models.DateTimeField(db_column='TBM0005_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0005_crt_user_id = models.CharField(db_column='TBM0005_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0005_crt_prog_nm = models.CharField(db_column='TBM0005_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0005_upd_datetime = models.DateTimeField(db_column='TBM0005_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0005_upd_user_id = models.CharField(db_column='TBM0005_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0005_upd_prog_nm = models.CharField(db_column='TBM0005_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0005_upd_cnt = models.DecimalField(db_column='TBM0005_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM0005_PAY_MONTH_KBN'


class Tbm0007KeihiKbn(models.Model):
    tbm0007_keihi_kbn_cd = models.CharField(db_column='TBM0007_KEIHI_KBN_CD', primary_key=True, max_length=3)  # Field name made lowercase.
    tbm0007_keihi_kbn_nm = models.CharField(db_column='TBM0007_KEIHI_KBN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0007_del_flg = models.CharField(db_column='TBM0007_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0007_crt_datetime = models.DateTimeField(db_column='TBM0007_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0007_crt_user_id = models.CharField(db_column='TBM0007_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0007_crt_prog_nm = models.CharField(db_column='TBM0007_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0007_upd_datetime = models.DateTimeField(db_column='TBM0007_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0007_upd_user_id = models.CharField(db_column='TBM0007_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0007_upd_prog_nm = models.CharField(db_column='TBM0007_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0007_upd_cnt = models.DecimalField(db_column='TBM0007_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbm0007_keihi_siyo_flg = models.CharField(db_column='TBM0007_KEIHI_SIYO_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0007_sizai_siyo_flg = models.CharField(db_column='TBM0007_SIZAI_SIYO_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0007_jnknhi_siyo_flg = models.CharField(db_column='TBM0007_JNKNHI_SIYO_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0007_kosu_siyo_flg = models.CharField(db_column='TBM0007_KOSU_SIYO_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0007_ssk_gen_shoku_flg = models.CharField(db_column='TBM0007_SSK_GEN_SHOKU_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0007_ssk_bumon_flg = models.CharField(db_column='TBM0007_SSK_BUMON_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0007_ssk_zensha_flg = models.CharField(db_column='TBM0007_SSK_ZENSHA_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0007_uke_ou_flg = models.CharField(db_column='TBM0007_UKE_OU_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM0007_KEIHI_KBN'


class Tbm0010GyomuShohinKbn(models.Model):
    tbm0010_gyomu_shohin_kbn_cd = models.CharField(db_column='TBM0010_GYOMU_SHOHIN_KBN_CD', primary_key=True, max_length=3)  # Field name made lowercase.
    tbm0010_gyomu_shohin_kbn_nm = models.CharField(db_column='TBM0010_GYOMU_SHOHIN_KBN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0010_del_flg = models.CharField(db_column='TBM0010_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0010_crt_datetime = models.DateTimeField(db_column='TBM0010_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0010_crt_user_id = models.CharField(db_column='TBM0010_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0010_crt_prog_nm = models.CharField(db_column='TBM0010_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0010_upd_datetime = models.DateTimeField(db_column='TBM0010_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0010_upd_user_id = models.CharField(db_column='TBM0010_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0010_upd_prog_nm = models.CharField(db_column='TBM0010_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0010_upd_cnt = models.DecimalField(db_column='TBM0010_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbm0010_uriage_siyo_flg = models.CharField(db_column='TBM0010_URIAGE_SIYO_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0010_siire_shohin_siyo_flg = models.CharField(db_column='TBM0010_SIIRE_SHOHIN_SIYO_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0010_jyuchu_siyo_flg = models.CharField(db_column='TBM0010_JYUCHU_SIYO_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0010_order_siyo_flg = models.CharField(db_column='TBM0010_ORDER_SIYO_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0010_siire_gaityu_siyo_flg = models.CharField(db_column='TBM0010_SIIRE_GAITYU_SIYO_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0010_sizai_siyo_flg = models.CharField(db_column='TBM0010_SIZAI_SIYO_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM0010_GYOMU_SHOHIN_KBN'


class Tbm0014KaiInfo(models.Model):
    tbm0014_kaisha_cd = models.CharField(db_column='TBM0014_KAISHA_CD', primary_key=True, max_length=3)  # Field name made lowercase.
    tbm0014_kaisha_name = models.CharField(db_column='TBM0014_KAISHA_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0014_kaisha_name_k = models.CharField(db_column='TBM0014_KAISHA_NAME_K', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0014_tel = models.CharField(db_column='TBM0014_TEL', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tbm0014_fax = models.CharField(db_column='TBM0014_FAX', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tbm0014_post = models.CharField(db_column='TBM0014_POST', max_length=8, blank=True, null=True)  # Field name made lowercase.
    tbm0014_address1 = models.CharField(db_column='TBM0014_ADDRESS1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0014_address2 = models.CharField(db_column='TBM0014_ADDRESS2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0014_hasu_id = models.SmallIntegerField(db_column='TBM0014_HASU_ID', blank=True, null=True)  # Field name made lowercase.
    tbm0014_crnt_nend = models.SmallIntegerField(db_column='TBM0014_CRNT_NEND', blank=True, null=True)  # Field name made lowercase.
    tbm0014_crnt_month = models.SmallIntegerField(db_column='TBM0014_CRNT_MONTH', blank=True, null=True)  # Field name made lowercase.
    tbm0014_ki_str_day = models.DateTimeField(db_column='TBM0014_KI_STR_DAY', blank=True, null=True)  # Field name made lowercase.
    tbm0014_ki_end_day = models.DateTimeField(db_column='TBM0014_KI_END_DAY', blank=True, null=True)  # Field name made lowercase.
    tbm0014_kinmu_shime_day = models.SmallIntegerField(db_column='TBM0014_KINMU_SHIME_DAY', blank=True, null=True)  # Field name made lowercase.
    tbm0014_str_week = models.SmallIntegerField(db_column='TBM0014_STR_WEEK', blank=True, null=True)  # Field name made lowercase.
    tbm0014_del_flg = models.CharField(db_column='TBM0014_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0014_crt_datetime = models.DateTimeField(db_column='TBM0014_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0014_crt_user_id = models.CharField(db_column='TBM0014_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0014_crt_prog_nm = models.CharField(db_column='TBM0014_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0014_upd_datetime = models.DateTimeField(db_column='TBM0014_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0014_upd_user_id = models.CharField(db_column='TBM0014_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0014_upd_prog_nm = models.CharField(db_column='TBM0014_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0014_upd_cnt = models.DecimalField(db_column='TBM0014_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbm0014_uri_sir_close_day = models.SmallIntegerField(db_column='TBM0014_URI_SIR_CLOSE_DAY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM0014_KAI_INFO'


class Tbm0015KaiBk(models.Model):
    tbm0014_kaisha_cd = models.CharField(db_column='TBM0014_KAISHA_CD', primary_key=True, max_length=3)  # Field name made lowercase.
    tbm0015_kaisha_bank_cd = models.CharField(db_column='TBM0015_KAISHA_BANK_CD', max_length=4)  # Field name made lowercase.
    tbm0015_bank_cd = models.CharField(db_column='TBM0015_BANK_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbm0015_siten_cd = models.CharField(db_column='TBM0015_SITEN_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbm0015_yokin_kbn = models.SmallIntegerField(db_column='TBM0015_YOKIN_KBN', blank=True, null=True)  # Field name made lowercase.
    tbm0015_koza_no = models.CharField(db_column='TBM0015_KOZA_NO', max_length=7, blank=True, null=True)  # Field name made lowercase.
    tbm0015_bank_name = models.CharField(db_column='TBM0015_BANK_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0015_siten_name = models.CharField(db_column='TBM0015_SITEN_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0015_all_kamoku_cd = models.CharField(db_column='TBM0015_ALL_KAMOKU_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbm0015_sub_kamoku_cd = models.CharField(db_column='TBM0015_SUB_KAMOKU_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbm0015_del_flg = models.CharField(db_column='TBM0015_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0015_crt_datetime = models.DateTimeField(db_column='TBM0015_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0015_crt_user_id = models.CharField(db_column='TBM0015_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0015_crt_prog_nm = models.CharField(db_column='TBM0015_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0015_upd_datetime = models.DateTimeField(db_column='TBM0015_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0015_upd_user_id = models.CharField(db_column='TBM0015_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0015_upd_prog_nm = models.CharField(db_column='TBM0015_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0015_upd_cnt = models.DecimalField(db_column='TBM0015_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM0015_KAI_BK'
        unique_together = (('tbm0014_kaisha_cd', 'tbm0015_kaisha_bank_cd'),)


class Tbm0018Genba(models.Model):
    tbm0018_genba_cd = models.CharField(db_column='TBM0018_GENBA_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tbm0018_genba_name = models.CharField(db_column='TBM0018_GENBA_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0018_genba_name_k = models.CharField(db_column='TBM0018_GENBA_NAME_K', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0018_tel = models.CharField(db_column='TBM0018_TEL', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tbm0018_fax = models.CharField(db_column='TBM0018_FAX', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tbm0018_post = models.CharField(db_column='TBM0018_POST', max_length=8, blank=True, null=True)  # Field name made lowercase.
    tbm0018_address1 = models.CharField(db_column='TBM0018_ADDRESS1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0018_address2 = models.CharField(db_column='TBM0018_ADDRESS2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0018_del_flg = models.CharField(db_column='TBM0018_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0018_crt_datetime = models.DateTimeField(db_column='TBM0018_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0018_crt_user_id = models.CharField(db_column='TBM0018_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0018_crt_prog_nm = models.CharField(db_column='TBM0018_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0018_upd_datetime = models.DateTimeField(db_column='TBM0018_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0018_upd_user_id = models.CharField(db_column='TBM0018_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0018_upd_prog_nm = models.CharField(db_column='TBM0018_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0018_upd_cnt = models.DecimalField(db_column='TBM0018_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbm0018_genba_name_r = models.CharField(db_column='TBM0018_GENBA_NAME_R', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0018_ninsho_meth = models.CharField(db_column='TBM0018_NINSHO_METH', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0018_import_kbn = models.CharField(db_column='TBM0018_IMPORT_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0018_import_shonin_user = models.CharField(db_column='TBM0018_IMPORT_SHONIN_USER', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM0018_GENBA'


class Tbm0019ShokuShu(models.Model):
    tbm0019_shoku_cd = models.CharField(db_column='TBM0019_SHOKU_CD', primary_key=True, max_length=2)  # Field name made lowercase.
    tbm0019_shoku_name = models.CharField(db_column='TBM0019_SHOKU_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0019_shoku_name_k = models.CharField(db_column='TBM0019_SHOKU_NAME_K', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0019_del_flg = models.CharField(db_column='TBM0019_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0019_crt_datetime = models.DateTimeField(db_column='TBM0019_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0019_crt_user_id = models.CharField(db_column='TBM0019_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0019_crt_prog_nm = models.CharField(db_column='TBM0019_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0019_upd_datetime = models.DateTimeField(db_column='TBM0019_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0019_upd_user_id = models.CharField(db_column='TBM0019_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0019_upd_prog_nm = models.CharField(db_column='TBM0019_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0019_upd_cnt = models.DecimalField(db_column='TBM0019_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbm0019_shoku_name_r = models.CharField(db_column='TBM0019_SHOKU_NAME_R', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM0019_SHOKU_SHU'


class Tbm0020GenShoku(models.Model):
    tbm0020_genba_cd = models.CharField(db_column='TBM0020_GENBA_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tbm0020_shoku_cd = models.CharField(db_column='TBM0020_SHOKU_CD', max_length=2)  # Field name made lowercase.
    tbm0020_bmn_cd = models.CharField(db_column='TBM0020_BMN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbm0020_tanto_cd = models.CharField(db_column='TBM0020_TANTO_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbm0020_to_exist_date = models.DateTimeField(db_column='TBM0020_TO_EXIST_DATE', blank=True, null=True)  # Field name made lowercase.
    tbm0020_del_flg = models.CharField(db_column='TBM0020_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0020_crt_datetime = models.DateTimeField(db_column='TBM0020_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0020_crt_user_id = models.CharField(db_column='TBM0020_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0020_crt_prog_nm = models.CharField(db_column='TBM0020_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0020_upd_datetime = models.DateTimeField(db_column='TBM0020_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0020_upd_user_id = models.CharField(db_column='TBM0020_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0020_upd_prog_nm = models.CharField(db_column='TBM0020_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0020_upd_cnt = models.DecimalField(db_column='TBM0020_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbm0020_mng_cd = models.CharField(db_column='TBM0020_MNG_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbm0020_insp_term_kaisu = models.SmallIntegerField(db_column='TBM0020_INSP_TERM_KAISU', blank=True, null=True)  # Field name made lowercase.
    tbm0020_insp_term_tanni = models.CharField(db_column='TBM0020_INSP_TERM_TANNI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0020_insp_start_ym = models.CharField(db_column='TBM0020_INSP_START_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tbm0020_yosan_tokubetu_flg = models.CharField(db_column='TBM0020_YOSAN_TOKUBETU_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM0020_GEN_SHOKU'
        unique_together = (('tbm0020_genba_cd', 'tbm0020_shoku_cd'),)


class Tbm0021GyomuShohin(models.Model):
    tbm0021_gyomu_shohin_cd = models.CharField(db_column='TBM0021_GYOMU_SHOHIN_CD', primary_key=True, max_length=12)  # Field name made lowercase.
    tbm0021_gyomu_shohin_name = models.CharField(db_column='TBM0021_GYOMU_SHOHIN_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0021_gyomu_shohin_kbn_cd = models.CharField(db_column='TBM0021_GYOMU_SHOHIN_KBN_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbm0021_tani_mei = models.CharField(db_column='TBM0021_TANI_MEI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tbm0021_siire_tanka = models.DecimalField(db_column='TBM0021_SIIRE_TANKA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbm0021_hanbai_tanka = models.DecimalField(db_column='TBM0021_HANBAI_TANKA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbm0021_teika = models.DecimalField(db_column='TBM0021_TEIKA', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbm0021_kazei_id = models.CharField(db_column='TBM0021_KAZEI_ID', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbm0021_sub_kamoku_cd = models.CharField(db_column='TBM0021_SUB_KAMOKU_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbm0021_del_flg = models.CharField(db_column='TBM0021_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0021_crt_datetime = models.DateTimeField(db_column='TBM0021_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0021_crt_user_id = models.CharField(db_column='TBM0021_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0021_crt_prog_nm = models.CharField(db_column='TBM0021_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0021_upd_datetime = models.DateTimeField(db_column='TBM0021_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0021_upd_user_id = models.CharField(db_column='TBM0021_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0021_upd_prog_nm = models.CharField(db_column='TBM0021_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0021_upd_cnt = models.DecimalField(db_column='TBM0021_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbm0021_zaiko_taisyo_flg = models.BooleanField(db_column='TBM0021_ZAIKO_TAISYO_FLG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM0021_GYOMU_SHOHIN'


class Tbm0022ShohiZei(models.Model):
    tbm0022_hkko_date = models.DateTimeField(db_column='TBM0022_HKKO_DATE', primary_key=True)  # Field name made lowercase.
    tbm0022_szei_rate = models.DecimalField(db_column='TBM0022_SZEI_RATE', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbm0022_skko_date = models.DateTimeField(db_column='TBM0022_SKKO_DATE', blank=True, null=True)  # Field name made lowercase.
    tbm0022_del_flg = models.CharField(db_column='TBM0022_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0022_crt_datetime = models.DateTimeField(db_column='TBM0022_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0022_crt_user_id = models.CharField(db_column='TBM0022_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0022_crt_prog_nm = models.CharField(db_column='TBM0022_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0022_upd_datetime = models.DateTimeField(db_column='TBM0022_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0022_upd_user_id = models.CharField(db_column='TBM0022_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0022_upd_prog_nm = models.CharField(db_column='TBM0022_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0022_upd_cnt = models.DecimalField(db_column='TBM0022_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM0022_SHOHI_ZEI'


class Tbm0023SiireSaki(models.Model):
    tbm0023_siire_saki_cd = models.CharField(db_column='TBM0023_SIIRE_SAKI_CD', primary_key=True, max_length=4)  # Field name made lowercase.
    tbm0023_siire_saki_name = models.CharField(db_column='TBM0023_SIIRE_SAKI_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0023_siire_saki_name_k = models.CharField(db_column='TBM0023_SIIRE_SAKI_NAME_K', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0023_tel = models.CharField(db_column='TBM0023_TEL', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tbm0023_fax = models.CharField(db_column='TBM0023_FAX', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tbm0023_bumon_name = models.CharField(db_column='TBM0023_BUMON_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0023_tanto_name = models.CharField(db_column='TBM0023_TANTO_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0023_post = models.CharField(db_column='TBM0023_POST', max_length=8, blank=True, null=True)  # Field name made lowercase.
    tbm0023_address1 = models.CharField(db_column='TBM0023_ADDRESS1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0023_address2 = models.CharField(db_column='TBM0023_ADDRESS2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0023_email = models.CharField(db_column='TBM0023_EMAIL', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tbm0023_close_day = models.SmallIntegerField(db_column='TBM0023_CLOSE_DAY', blank=True, null=True)  # Field name made lowercase.
    tbm0023_szei_tnk_kbn_id = models.CharField(db_column='TBM0023_SZEI_TNK_KBN_ID', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbm0023_pay_month_kbn_id = models.CharField(db_column='TBM0023_PAY_MONTH_KBN_ID', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbm0023_pay_day = models.SmallIntegerField(db_column='TBM0023_PAY_DAY', blank=True, null=True)  # Field name made lowercase.
    tbm0023_tanto_cd = models.CharField(db_column='TBM0023_TANTO_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbm0023_zan_kingaku = models.DecimalField(db_column='TBM0023_ZAN_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbm0023_sub_kamoku_cd = models.CharField(db_column='TBM0023_SUB_KAMOKU_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbm0023_shiwake_flg = models.BooleanField(db_column='TBM0023_SHIWAKE_FLG', blank=True, null=True)  # Field name made lowercase.
    tbm0023_del_flg = models.CharField(db_column='TBM0023_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0023_crt_datetime = models.DateTimeField(db_column='TBM0023_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0023_crt_user_id = models.CharField(db_column='TBM0023_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0023_crt_prog_nm = models.CharField(db_column='TBM0023_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0023_upd_datetime = models.DateTimeField(db_column='TBM0023_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0023_upd_user_id = models.CharField(db_column='TBM0023_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0023_upd_prog_nm = models.CharField(db_column='TBM0023_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0023_upd_cnt = models.DecimalField(db_column='TBM0023_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbm0023_bmn_cd = models.CharField(db_column='TBM0023_BMN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM0023_SIIRE_SAKI'


class Tbm0024SiireSakiBk(models.Model):
    tbm0023_siire_saki_cd = models.CharField(db_column='TBM0023_SIIRE_SAKI_CD', primary_key=True, max_length=4)  # Field name made lowercase.
    tbm0024_siire_saki_bank_cd = models.CharField(db_column='TBM0024_SIIRE_SAKI_BANK_CD', max_length=4)  # Field name made lowercase.
    tbm0024_bank_cd = models.CharField(db_column='TBM0024_BANK_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbm0024_siten_cd = models.CharField(db_column='TBM0024_SITEN_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbm0024_yokin_kbn = models.SmallIntegerField(db_column='TBM0024_YOKIN_KBN', blank=True, null=True)  # Field name made lowercase.
    tbm0024_koza_no = models.CharField(db_column='TBM0024_KOZA_NO', max_length=7, blank=True, null=True)  # Field name made lowercase.
    tbm0024_bank_name = models.CharField(db_column='TBM0024_BANK_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0024_siten_name = models.CharField(db_column='TBM0024_SITEN_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0024_sub_kamoku_cd = models.CharField(db_column='TBM0024_SUB_KAMOKU_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbm0024_koza_name = models.CharField(db_column='TBM0024_KOZA_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0024_koza_name_k = models.CharField(db_column='TBM0024_KOZA_NAME_K', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0024_del_flg = models.CharField(db_column='TBM0024_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0024_crt_datetime = models.DateTimeField(db_column='TBM0024_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0024_crt_user_id = models.CharField(db_column='TBM0024_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0024_crt_prog_nm = models.CharField(db_column='TBM0024_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0024_upd_datetime = models.DateTimeField(db_column='TBM0024_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0024_upd_user_id = models.CharField(db_column='TBM0024_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0024_upd_prog_nm = models.CharField(db_column='TBM0024_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0024_upd_cnt = models.DecimalField(db_column='TBM0024_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM0024_SIIRE_SAKI_BK'
        unique_together = (('tbm0023_siire_saki_cd', 'tbm0024_siire_saki_bank_cd'),)


class Tbm0025TokuiSaki(models.Model):
    tbm0025_tokui_saki_cd = models.CharField(db_column='TBM0025_TOKUI_SAKI_CD', primary_key=True, max_length=4)  # Field name made lowercase.
    tbm0025_tokui_saki_name = models.CharField(db_column='TBM0025_TOKUI_SAKI_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0025_tokui_saki_name_k = models.CharField(db_column='TBM0025_TOKUI_SAKI_NAME_K', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0025_tel = models.CharField(db_column='TBM0025_TEL', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tbm0025_fax = models.CharField(db_column='TBM0025_FAX', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tbm0025_bumon_name = models.CharField(db_column='TBM0025_BUMON_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0025_tanto_name = models.CharField(db_column='TBM0025_TANTO_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0025_post = models.CharField(db_column='TBM0025_POST', max_length=8, blank=True, null=True)  # Field name made lowercase.
    tbm0025_address1 = models.CharField(db_column='TBM0025_ADDRESS1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0025_address2 = models.CharField(db_column='TBM0025_ADDRESS2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0025_email = models.CharField(db_column='TBM0025_EMAIL', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tbm0025_close_day = models.SmallIntegerField(db_column='TBM0025_CLOSE_DAY', blank=True, null=True)  # Field name made lowercase.
    tbm0025_szei_tnk_kbn_id = models.CharField(db_column='TBM0025_SZEI_TNK_KBN_ID', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbm0025_pay_month_kbn_id = models.CharField(db_column='TBM0025_PAY_MONTH_KBN_ID', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbm0025_pay_day = models.SmallIntegerField(db_column='TBM0025_PAY_DAY', blank=True, null=True)  # Field name made lowercase.
    tbm0025_tanto_cd = models.CharField(db_column='TBM0025_TANTO_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbm0025_zan_kingaku = models.DecimalField(db_column='TBM0025_ZAN_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbm0025_sub_kamoku_cd = models.CharField(db_column='TBM0025_SUB_KAMOKU_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbm0025_shiwake_flg = models.BooleanField(db_column='TBM0025_SHIWAKE_FLG', blank=True, null=True)  # Field name made lowercase.
    tbm0025_del_flg = models.CharField(db_column='TBM0025_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0025_crt_datetime = models.DateTimeField(db_column='TBM0025_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0025_crt_user_id = models.CharField(db_column='TBM0025_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0025_crt_prog_nm = models.CharField(db_column='TBM0025_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0025_upd_datetime = models.DateTimeField(db_column='TBM0025_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0025_upd_user_id = models.CharField(db_column='TBM0025_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0025_upd_prog_nm = models.CharField(db_column='TBM0025_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0025_upd_cnt = models.DecimalField(db_column='TBM0025_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbm0025_bmn_cd = models.CharField(db_column='TBM0025_BMN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM0025_TOKUI_SAKI'


class Tbm0026TokuiSakiBk(models.Model):
    tbm0025_tokui_saki_cd = models.CharField(db_column='TBM0025_TOKUI_SAKI_CD', primary_key=True, max_length=4)  # Field name made lowercase.
    tbm0026_tokui_saki_bank_cd = models.CharField(db_column='TBM0026_TOKUI_SAKI_BANK_CD', max_length=4)  # Field name made lowercase.
    tbm0026_bank_cd = models.CharField(db_column='TBM0026_BANK_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbm0026_siten_cd = models.CharField(db_column='TBM0026_SITEN_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbm0026_yokin_kbn = models.SmallIntegerField(db_column='TBM0026_YOKIN_KBN', blank=True, null=True)  # Field name made lowercase.
    tbm0026_koza_no = models.CharField(db_column='TBM0026_KOZA_NO', max_length=7, blank=True, null=True)  # Field name made lowercase.
    tbm0026_bank_name = models.CharField(db_column='TBM0026_BANK_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0026_siten_name = models.CharField(db_column='TBM0026_SITEN_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0026_sub_kamoku_cd = models.CharField(db_column='TBM0026_SUB_KAMOKU_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbm0026_koza_name = models.CharField(db_column='TBM0026_KOZA_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0026_koza_name_k = models.CharField(db_column='TBM0026_KOZA_NAME_K', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0026_del_flg = models.CharField(db_column='TBM0026_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0026_crt_datetime = models.DateTimeField(db_column='TBM0026_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0026_crt_user_id = models.CharField(db_column='TBM0026_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0026_crt_prog_nm = models.CharField(db_column='TBM0026_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0026_upd_datetime = models.DateTimeField(db_column='TBM0026_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0026_upd_user_id = models.CharField(db_column='TBM0026_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0026_upd_prog_nm = models.CharField(db_column='TBM0026_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0026_upd_cnt = models.DecimalField(db_column='TBM0026_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM0026_TOKUI_SAKI_BK'
        unique_together = (('tbm0025_tokui_saki_cd', 'tbm0026_tokui_saki_bank_cd'),)


class Tbm0027SeikyuSaki(models.Model):
    tbm0025_tokui_saki_cd = models.CharField(db_column='TBM0025_TOKUI_SAKI_CD', primary_key=True, max_length=4)  # Field name made lowercase.
    tbm0027_seikyu_saki_cd = models.CharField(db_column='TBM0027_SEIKYU_SAKI_CD', max_length=4)  # Field name made lowercase.
    tbm0027_seikyu_saki_name = models.CharField(db_column='TBM0027_SEIKYU_SAKI_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0027_seikyu_saki_name_k = models.CharField(db_column='TBM0027_SEIKYU_SAKI_NAME_K', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0027_tel = models.CharField(db_column='TBM0027_TEL', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tbm0027_fax = models.CharField(db_column='TBM0027_FAX', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tbm0027_bumon_name = models.CharField(db_column='TBM0027_BUMON_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0027_tanto_name = models.CharField(db_column='TBM0027_TANTO_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0027_post = models.CharField(db_column='TBM0027_POST', max_length=8, blank=True, null=True)  # Field name made lowercase.
    tbm0027_address1 = models.CharField(db_column='TBM0027_ADDRESS1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0027_address2 = models.CharField(db_column='TBM0027_ADDRESS2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0027_email = models.CharField(db_column='TBM0027_EMAIL', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tbm0027_biko = models.CharField(db_column='TBM0027_BIKO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbm0027_tanto_cd = models.CharField(db_column='TBM0027_TANTO_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbm0027_del_flg = models.CharField(db_column='TBM0027_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0027_crt_datetime = models.DateTimeField(db_column='TBM0027_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0027_crt_user_id = models.CharField(db_column='TBM0027_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0027_crt_prog_nm = models.CharField(db_column='TBM0027_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0027_upd_datetime = models.DateTimeField(db_column='TBM0027_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0027_upd_user_id = models.CharField(db_column='TBM0027_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0027_upd_prog_nm = models.CharField(db_column='TBM0027_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0027_upd_cnt = models.DecimalField(db_column='TBM0027_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbm0027_bmn_cd = models.CharField(db_column='TBM0027_BMN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM0027_SEIKYU_SAKI'
        unique_together = (('tbm0025_tokui_saki_cd', 'tbm0027_seikyu_saki_cd'),)


class Tbm0028Soko(models.Model):
    tbm0028_soko_cd = models.CharField(db_column='TBM0028_SOKO_CD', primary_key=True, max_length=3)  # Field name made lowercase.
    tbm0028_soko_name = models.CharField(db_column='TBM0028_SOKO_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0028_soko_name_k = models.CharField(db_column='TBM0028_SOKO_NAME_K', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0028_tel = models.CharField(db_column='TBM0028_TEL', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tbm0028_fax = models.CharField(db_column='TBM0028_FAX', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tbm0028_post = models.CharField(db_column='TBM0028_POST', max_length=8, blank=True, null=True)  # Field name made lowercase.
    tbm0028_address1 = models.CharField(db_column='TBM0028_ADDRESS1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0028_address2 = models.CharField(db_column='TBM0028_ADDRESS2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0028_tanto_cd = models.CharField(db_column='TBM0028_TANTO_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbm0028_del_flg = models.CharField(db_column='TBM0028_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0028_crt_datetime = models.DateTimeField(db_column='TBM0028_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0028_crt_user_id = models.CharField(db_column='TBM0028_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0028_crt_prog_nm = models.CharField(db_column='TBM0028_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0028_upd_datetime = models.DateTimeField(db_column='TBM0028_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0028_upd_user_id = models.CharField(db_column='TBM0028_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0028_upd_prog_nm = models.CharField(db_column='TBM0028_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0028_upd_cnt = models.DecimalField(db_column='TBM0028_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbm0028_bmn_cd = models.CharField(db_column='TBM0028_BMN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM0028_SOKO'


class Tbm0029HaifPtn(models.Model):
    tbm0029_haif_ptn_cd = models.CharField(db_column='TBM0029_HAIF_PTN_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tbm0029_haif_ptn_nm = models.CharField(db_column='TBM0029_HAIF_PTN_NM', max_length=100)  # Field name made lowercase.
    tbm0029_uri_hi = models.DecimalField(db_column='TBM0029_URI_HI', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tbm0029_area_hi = models.DecimalField(db_column='TBM0029_AREA_HI', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tbm0029_devide_flg = models.CharField(db_column='TBM0029_DEVIDE_FLG', max_length=1)  # Field name made lowercase.
    tbm0029_del_flg = models.CharField(db_column='TBM0029_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0029_crt_datetime = models.DateTimeField(db_column='TBM0029_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0029_crt_user_id = models.CharField(db_column='TBM0029_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0029_crt_prog_nm = models.CharField(db_column='TBM0029_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0029_upd_datetime = models.DateTimeField(db_column='TBM0029_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0029_upd_user_id = models.CharField(db_column='TBM0029_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0029_upd_prog_nm = models.CharField(db_column='TBM0029_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0029_upd_cnt = models.DecimalField(db_column='TBM0029_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM0029_HAIF_PTN'


class Tbm0031ShuKuSet(models.Model):
    tbm0031_cal_date = models.DateTimeField(db_column='TBM0031_CAL_DATE', primary_key=True)  # Field name made lowercase.
    tbm0031_cal_nm = models.CharField(db_column='TBM0031_CAL_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0031_del_flg = models.CharField(db_column='TBM0031_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0031_crt_datetime = models.DateTimeField(db_column='TBM0031_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0031_crt_user_id = models.CharField(db_column='TBM0031_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0031_crt_prog_nm = models.CharField(db_column='TBM0031_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0031_upd_datetime = models.DateTimeField(db_column='TBM0031_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0031_upd_user_id = models.CharField(db_column='TBM0031_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0031_upd_prog_nm = models.CharField(db_column='TBM0031_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0031_upd_cnt = models.DecimalField(db_column='TBM0031_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbm0031_holiday_flg = models.CharField(db_column='TBM0031_HOLIDAY_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM0031_SHU_KU_SET'


class Tbm0034Location(models.Model):
    tbm0034_location_cd = models.CharField(db_column='TBM0034_LOCATION_CD', primary_key=True, max_length=3)  # Field name made lowercase.
    tbm0034_location_name = models.CharField(db_column='TBM0034_LOCATION_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0034_location_name_k = models.CharField(db_column='TBM0034_LOCATION_NAME_K', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm0034_memo = models.CharField(db_column='TBM0034_MEMO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbm0034_del_flg = models.CharField(db_column='TBM0034_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0034_crt_datetime = models.DateTimeField(db_column='TBM0034_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0034_crt_user_id = models.CharField(db_column='TBM0034_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0034_crt_prog_nm = models.CharField(db_column='TBM0034_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0034_upd_datetime = models.DateTimeField(db_column='TBM0034_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0034_upd_user_id = models.CharField(db_column='TBM0034_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0034_upd_prog_nm = models.CharField(db_column='TBM0034_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0034_upd_cnt = models.DecimalField(db_column='TBM0034_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM0034_LOCATION'


class Tbm0035SokoLocation(models.Model):
    tbm0035_soko_cd = models.CharField(db_column='TBM0035_SOKO_CD', primary_key=True, max_length=3)  # Field name made lowercase.
    tbm0035_location_cd = models.CharField(db_column='TBM0035_LOCATION_CD', max_length=3)  # Field name made lowercase.
    tbm0035_del_flg = models.CharField(db_column='TBM0035_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm0035_crt_datetime = models.DateTimeField(db_column='TBM0035_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0035_crt_user_id = models.CharField(db_column='TBM0035_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0035_crt_prog_nm = models.CharField(db_column='TBM0035_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0035_upd_datetime = models.DateTimeField(db_column='TBM0035_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm0035_upd_user_id = models.CharField(db_column='TBM0035_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm0035_upd_prog_nm = models.CharField(db_column='TBM0035_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm0035_upd_cnt = models.DecimalField(db_column='TBM0035_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM0035_SOKO_LOCATION'
        unique_together = (('tbm0035_soko_cd', 'tbm0035_location_cd'),)


class Tbm1001YosanUtwk(models.Model):
    tbm1001_yosan_utwk_cd = models.CharField(db_column='TBM1001_YOSAN_UTWK_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tbm1001_yosan_utwk_nm = models.CharField(db_column='TBM1001_YOSAN_UTWK_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm1001_yosan_tais_tbl = models.CharField(db_column='TBM1001_YOSAN_TAIS_TBL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbm1001_jisk_tais_tbl = models.CharField(db_column='TBM1001_JISK_TAIS_TBL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbm1001_srch_cond_1 = models.CharField(db_column='TBM1001_SRCH_COND_1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbm1001_enable_false_kbn_znsy = models.CharField(db_column='TBM1001_ENABLE_FALSE_KBN_ZNSY', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm1001_enable_false_kbn_bmn = models.CharField(db_column='TBM1001_ENABLE_FALSE_KBN_BMN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm1001_enable_false_kbn_genba = models.CharField(db_column='TBM1001_ENABLE_FALSE_KBN_GENBA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm1001_par_yosan_utwk_cd = models.CharField(db_column='TBM1001_PAR_YOSAN_UTWK_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbm1001_empty_line_num = models.SmallIntegerField(db_column='TBM1001_EMPTY_LINE_NUM', blank=True, null=True)  # Field name made lowercase.
    tbm1001_out_line_no = models.SmallIntegerField(db_column='TBM1001_OUT_LINE_NO', blank=True, null=True)  # Field name made lowercase.
    tbm1001_out_column_no = models.SmallIntegerField(db_column='TBM1001_OUT_COLUMN_NO', blank=True, null=True)  # Field name made lowercase.
    tbm1001_hyoj_no = models.DecimalField(db_column='TBM1001_HYOJ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbm1001_del_flg = models.CharField(db_column='TBM1001_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm1001_crt_datetime = models.DateTimeField(db_column='TBM1001_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm1001_crt_user_id = models.CharField(db_column='TBM1001_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm1001_crt_prog_nm = models.CharField(db_column='TBM1001_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm1001_upd_datetime = models.DateTimeField(db_column='TBM1001_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm1001_upd_user_id = models.CharField(db_column='TBM1001_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm1001_upd_prog_nm = models.CharField(db_column='TBM1001_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm1001_upd_cnt = models.DecimalField(db_column='TBM1001_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbm1001_srch_cond_2 = models.CharField(db_column='TBM1001_SRCH_COND_2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbm1001_jisk_cond = models.CharField(db_column='TBM1001_JISK_COND', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbm1001_tyok_bmn_syukei_flg = models.CharField(db_column='TBM1001_TYOK_BMN_SYUKEI_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm1001_syukei_yosan_utwk_cd = models.CharField(db_column='TBM1001_SYUKEI_YOSAN_UTWK_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbm1001_yosan_utwk_dtl_nm = models.CharField(db_column='TBM1001_YOSAN_UTWK_DTL_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm1001_uri_keih_kbn = models.CharField(db_column='TBM1001_URI_KEIH_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM1001_YOSAN_UTWK'


class Tbm1002YosanPtn(models.Model):
    tbm1002_nendo = models.SmallIntegerField(db_column='TBM1002_NENDO', primary_key=True)  # Field name made lowercase.
    tbm1002_yosan_ptn_cd = models.CharField(db_column='TBM1002_YOSAN_PTN_CD', max_length=15)  # Field name made lowercase.
    tbm1002_yosan_ptn_nm = models.CharField(db_column='TBM1002_YOSAN_PTN_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm1002_yosan_tani = models.CharField(db_column='TBM1002_YOSAN_TANI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tbm1002_bumon_cd = models.CharField(db_column='TBM1002_BUMON_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbm1002_rp_format_cd_kisy = models.CharField(db_column='TBM1002_RP_FORMAT_CD_KISY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbm1002_rp_format_cd_mikm = models.CharField(db_column='TBM1002_RP_FORMAT_CD_MIKM', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbm1002_rp_format_cd_sksn = models.CharField(db_column='TBM1002_RP_FORMAT_CD_SKSN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbm1002_rp_format_cd_syus = models.CharField(db_column='TBM1002_RP_FORMAT_CD_SYUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbm1002_rp_format_cd_yojt = models.CharField(db_column='TBM1002_RP_FORMAT_CD_YOJT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbm1002_del_flg = models.CharField(db_column='TBM1002_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm1002_crt_datetime = models.DateTimeField(db_column='TBM1002_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm1002_crt_user_id = models.CharField(db_column='TBM1002_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm1002_crt_prog_nm = models.CharField(db_column='TBM1002_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm1002_upd_datetime = models.DateTimeField(db_column='TBM1002_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm1002_upd_user_id = models.CharField(db_column='TBM1002_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm1002_upd_prog_nm = models.CharField(db_column='TBM1002_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm1002_upd_cnt = models.DecimalField(db_column='TBM1002_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbm1002_rp_format_cd_sisn = models.CharField(db_column='TBM1002_RP_FORMAT_CD_SISN', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM1002_YOSAN_PTN'
        unique_together = (('tbm1002_nendo', 'tbm1002_yosan_ptn_cd'),)


class Tbm1003YosanPtnDtl(models.Model):
    tbm1002_nendo = models.SmallIntegerField(db_column='TBM1002_NENDO', primary_key=True)  # Field name made lowercase.
    tbm1002_yosan_ptn_cd = models.CharField(db_column='TBM1002_YOSAN_PTN_CD', max_length=15)  # Field name made lowercase.
    tbm1003_yosan_utwk_cd = models.CharField(db_column='TBM1003_YOSAN_UTWK_CD', max_length=10)  # Field name made lowercase.
    tbm1003_par_yosan_utwk_cd = models.CharField(db_column='TBM1003_PAR_YOSAN_UTWK_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbm1003_kais_kbn = models.SmallIntegerField(db_column='TBM1003_KAIS_KBN', blank=True, null=True)  # Field name made lowercase.
    tbm1003_hyoj_no = models.DecimalField(db_column='TBM1003_HYOJ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbm1003_enable_false_kbn = models.CharField(db_column='TBM1003_ENABLE_FALSE_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm1003_empty_line_num = models.SmallIntegerField(db_column='TBM1003_EMPTY_LINE_NUM', blank=True, null=True)  # Field name made lowercase.
    tbm1003_out_line_no = models.SmallIntegerField(db_column='TBM1003_OUT_LINE_NO', blank=True, null=True)  # Field name made lowercase.
    tbm1003_out_column_no = models.SmallIntegerField(db_column='TBM1003_OUT_COLUMN_NO', blank=True, null=True)  # Field name made lowercase.
    tbm1003_last_kais_flg = models.CharField(db_column='TBM1003_LAST_KAIS_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm1003_del_flg = models.CharField(db_column='TBM1003_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm1003_crt_datetime = models.DateTimeField(db_column='TBM1003_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm1003_crt_user_id = models.CharField(db_column='TBM1003_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm1003_crt_prog_nm = models.CharField(db_column='TBM1003_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm1003_upd_datetime = models.DateTimeField(db_column='TBM1003_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm1003_upd_user_id = models.CharField(db_column='TBM1003_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm1003_upd_prog_nm = models.CharField(db_column='TBM1003_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm1003_upd_cnt = models.DecimalField(db_column='TBM1003_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM1003_YOSAN_PTN_DTL'
        unique_together = (('tbm1002_nendo', 'tbm1002_yosan_ptn_cd', 'tbm1003_yosan_utwk_cd'),)


class Tbm1004RpFormat(models.Model):
    tbm1004_rp_format_cd = models.CharField(db_column='TBM1004_RP_FORMAT_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tbm1004_rp_format_nm = models.CharField(db_column='TBM1004_RP_FORMAT_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbm1004_rp_format_file = models.BinaryField(db_column='TBM1004_RP_FORMAT_FILE', blank=True, null=True)  # Field name made lowercase.
    tbm1004_del_flg = models.CharField(db_column='TBM1004_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm1004_crt_datetime = models.DateTimeField(db_column='TBM1004_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm1004_crt_user_id = models.CharField(db_column='TBM1004_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm1004_crt_prog_nm = models.CharField(db_column='TBM1004_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm1004_upd_datetime = models.DateTimeField(db_column='TBM1004_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm1004_upd_user_id = models.CharField(db_column='TBM1004_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm1004_upd_prog_nm = models.CharField(db_column='TBM1004_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm1004_upd_cnt = models.DecimalField(db_column='TBM1004_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM1004_RP_FORMAT'


class Tbm2001HanbaiKengenUser(models.Model):
    tbm2001_user_id = models.CharField(db_column='TBM2001_USER_ID', primary_key=True, max_length=12)  # Field name made lowercase.
    tbm2001_del_flg = models.CharField(db_column='TBM2001_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm2001_crt_datetime = models.DateTimeField(db_column='TBM2001_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm2001_crt_user_id = models.CharField(db_column='TBM2001_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm2001_crt_prog_nm = models.CharField(db_column='TBM2001_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm2001_upd_datetime = models.DateTimeField(db_column='TBM2001_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm2001_upd_user_id = models.CharField(db_column='TBM2001_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm2001_upd_prog_nm = models.CharField(db_column='TBM2001_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm2001_upd_cnt = models.DecimalField(db_column='TBM2001_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbm2001_jyuchu_shonin_flg = models.BooleanField(db_column='TBM2001_JYUCHU_SHONIN_FLG', blank=True, null=True)  # Field name made lowercase.
    tbm2001_uriage_kakutei_flg = models.BooleanField(db_column='TBM2001_URIAGE_KAKUTEI_FLG', blank=True, null=True)  # Field name made lowercase.
    tbm2001_uriage_shime_flg = models.BooleanField(db_column='TBM2001_URIAGE_SHIME_FLG', blank=True, null=True)  # Field name made lowercase.
    tbm2001_seikyu_shime_flg = models.BooleanField(db_column='TBM2001_SEIKYU_SHIME_FLG', blank=True, null=True)  # Field name made lowercase.
    tbm2001_nyukin_kanri_flg = models.BooleanField(db_column='TBM2001_NYUKIN_KANRI_FLG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM2001_HANBAI_KENGEN_USER'


class Tbm2002KobaiKengenUser(models.Model):
    tbm2002_user_id = models.CharField(db_column='TBM2002_USER_ID', primary_key=True, max_length=12)  # Field name made lowercase.
    tbm2002_user_nm = models.CharField(db_column='TBM2002_USER_NM', max_length=30)  # Field name made lowercase.
    tbm2002_hatchu_shonin_flg = models.BooleanField(db_column='TBM2002_HATCHU_SHONIN_FLG', blank=True, null=True)  # Field name made lowercase.
    tbm2002_shiire_kakutei_flg = models.BooleanField(db_column='TBM2002_SHIIRE_KAKUTEI_FLG', blank=True, null=True)  # Field name made lowercase.
    tbm2002_shiire_shime_flg = models.BooleanField(db_column='TBM2002_SHIIRE_SHIME_FLG', blank=True, null=True)  # Field name made lowercase.
    tbm2002_shiharai_kanri_flg = models.BooleanField(db_column='TBM2002_SHIHARAI_KANRI_FLG', blank=True, null=True)  # Field name made lowercase.
    tbm2002_del_flg = models.CharField(db_column='TBM2002_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm2002_crt_datetime = models.DateTimeField(db_column='TBM2002_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm2002_crt_user_id = models.CharField(db_column='TBM2002_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm2002_crt_prog_nm = models.CharField(db_column='TBM2002_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm2002_upd_datetime = models.DateTimeField(db_column='TBM2002_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm2002_upd_user_id = models.CharField(db_column='TBM2002_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm2002_upd_prog_nm = models.CharField(db_column='TBM2002_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm2002_upd_cnt = models.DecimalField(db_column='TBM2002_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM2002_KOBAI_KENGEN_USER'


class Tbm2003KeihiKengenUser(models.Model):
    tbm2003_user_id = models.CharField(db_column='TBM2003_USER_ID', primary_key=True, max_length=12)  # Field name made lowercase.
    tbm2003_user_nm = models.CharField(db_column='TBM2003_USER_NM', max_length=30)  # Field name made lowercase.
    tbm2003_keihi_kanri_flg = models.BooleanField(db_column='TBM2003_KEIHI_KANRI_FLG', blank=True, null=True)  # Field name made lowercase.
    tbm2003_del_flg = models.CharField(db_column='TBM2003_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm2003_crt_datetime = models.DateTimeField(db_column='TBM2003_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm2003_crt_user_id = models.CharField(db_column='TBM2003_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm2003_crt_prog_nm = models.CharField(db_column='TBM2003_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm2003_upd_datetime = models.DateTimeField(db_column='TBM2003_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm2003_upd_user_id = models.CharField(db_column='TBM2003_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm2003_upd_prog_nm = models.CharField(db_column='TBM2003_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm2003_upd_cnt = models.DecimalField(db_column='TBM2003_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM2003_KEIHI_KENGEN_USER'


class Tbm2004ZaikoKengenUser(models.Model):
    tbm2004_user_id = models.CharField(db_column='TBM2004_USER_ID', primary_key=True, max_length=12)  # Field name made lowercase.
    tbm2004_del_flg = models.CharField(db_column='TBM2004_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbm2004_crt_datetime = models.DateTimeField(db_column='TBM2004_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm2004_crt_user_id = models.CharField(db_column='TBM2004_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm2004_crt_prog_nm = models.CharField(db_column='TBM2004_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm2004_upd_datetime = models.DateTimeField(db_column='TBM2004_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbm2004_upd_user_id = models.CharField(db_column='TBM2004_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbm2004_upd_prog_nm = models.CharField(db_column='TBM2004_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbm2004_upd_cnt = models.DecimalField(db_column='TBM2004_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbm2004_zaiko_kanri_flg = models.BooleanField(db_column='TBM2004_ZAIKO_KANRI_FLG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBM2004_ZAIKO_KENGEN_USER'


class Tbt0005Keiyaku(models.Model):
    tbt0005_keiyaku_no = models.CharField(db_column='TBT0005_KEIYAKU_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt0005_nendo = models.SmallIntegerField(db_column='TBT0005_NENDO', blank=True, null=True)  # Field name made lowercase.
    tbt0005_sub_flg = models.CharField(db_column='TBT0005_SUB_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0005_tokui_saki_cd = models.CharField(db_column='TBT0005_TOKUI_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbt0005_genba_cd = models.CharField(db_column='TBT0005_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tbt0005_shoku_cd = models.CharField(db_column='TBT0005_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tbt0005_bumon_cd = models.CharField(db_column='TBT0005_BUMON_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbt0005_tanto_cd = models.CharField(db_column='TBT0005_TANTO_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbt0005_keizoku_kbn_cd = models.CharField(db_column='TBT0005_KEIZOKU_KBN_CD', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0005_str_month = models.SmallIntegerField(db_column='TBT0005_STR_MONTH', blank=True, null=True)  # Field name made lowercase.
    tbt0005_keiyaku_str_ym = models.CharField(db_column='TBT0005_KEIYAKU_STR_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tbt0005_keiyaku_end_ym = models.CharField(db_column='TBT0005_KEIYAKU_END_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tbt0005_cur_str_ym = models.CharField(db_column='TBT0005_CUR_STR_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tbt0005_cur_end_ym = models.CharField(db_column='TBT0005_CUR_END_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tbt0005_keiyaku_sho_no = models.CharField(db_column='TBT0005_KEIYAKU_SHO_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0005_keiyaku_name = models.CharField(db_column='TBT0005_KEIYAKU_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0005_memo = models.CharField(db_column='TBT0005_MEMO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0005_omit_flg = models.BooleanField(db_column='TBT0005_OMIT_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt0005_del_flg = models.CharField(db_column='TBT0005_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0005_crt_datetime = models.DateTimeField(db_column='TBT0005_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0005_crt_user_id = models.CharField(db_column='TBT0005_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0005_crt_prog_nm = models.CharField(db_column='TBT0005_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0005_upd_datetime = models.DateTimeField(db_column='TBT0005_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0005_upd_user_id = models.CharField(db_column='TBT0005_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0005_upd_prog_nm = models.CharField(db_column='TBT0005_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0005_upd_cnt = models.DecimalField(db_column='TBT0005_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0005_keiyaku_eda_no = models.IntegerField(db_column='TBT0005_KEIYAKU_EDA_NO', blank=True, null=True)  # Field name made lowercase.
    tbt0005_mtmr_sho_no = models.CharField(db_column='TBT0005_MTMR_SHO_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0005_henk_oboe_gaki = models.CharField(db_column='TBT0005_HENK_OBOE_GAKI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0005_jyu_kihyo_flg = models.BooleanField(db_column='TBT0005_JYU_KIHYO_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt0005_next_year_copy_flg = models.BooleanField(db_column='TBT0005_NEXT_YEAR_COPY_FLG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0005_KEIYAKU'


class Tbt0006KeiyakuDtl(models.Model):
    tbt0005_keiyaku_no = models.CharField(db_column='TBT0005_KEIYAKU_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt0006_keiyaku_dtl_no = models.SmallIntegerField(db_column='TBT0006_KEIYAKU_DTL_NO')  # Field name made lowercase.
    tbt0006_seikyu_saki_cd = models.CharField(db_column='TBT0006_SEIKYU_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbt0006_title = models.CharField(db_column='TBT0006_TITLE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0006_memo = models.CharField(db_column='TBT0006_MEMO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0006_tekiyo = models.CharField(db_column='TBT0006_TEKIYO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0006_del_flg = models.CharField(db_column='TBT0006_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0006_crt_datetime = models.DateTimeField(db_column='TBT0006_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0006_crt_user_id = models.CharField(db_column='TBT0006_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0006_crt_prog_nm = models.CharField(db_column='TBT0006_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0006_upd_datetime = models.DateTimeField(db_column='TBT0006_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0006_upd_user_id = models.CharField(db_column='TBT0006_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0006_upd_prog_nm = models.CharField(db_column='TBT0006_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0006_upd_cnt = models.DecimalField(db_column='TBT0006_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0006_KEIYAKU_DTL'
        unique_together = (('tbt0005_keiyaku_no', 'tbt0006_keiyaku_dtl_no'),)


class Tbt0007KeiyakuUri(models.Model):
    tbt0005_keiyaku_no = models.CharField(db_column='TBT0005_KEIYAKU_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt0006_keiyaku_dtl_no = models.SmallIntegerField(db_column='TBT0006_KEIYAKU_DTL_NO')  # Field name made lowercase.
    tbt0007_uri_no = models.SmallIntegerField(db_column='TBT0007_URI_NO')  # Field name made lowercase.
    tbt0007_gyomu_shohin_cd = models.CharField(db_column='TBT0007_GYOMU_SHOHIN_CD', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0007_tani_nm = models.CharField(db_column='TBT0007_TANI_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tbt0007_del_flg = models.CharField(db_column='TBT0007_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0007_crt_datetime = models.DateTimeField(db_column='TBT0007_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0007_crt_prog_nm = models.CharField(db_column='TBT0007_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0007_crt_user_id = models.CharField(db_column='TBT0007_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0007_upd_datetime = models.DateTimeField(db_column='TBT0007_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0007_upd_prog_nm = models.CharField(db_column='TBT0007_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0007_upd_user_id = models.CharField(db_column='TBT0007_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0007_upd_cnt = models.DecimalField(db_column='TBT0007_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0007_shuka_kbn = models.CharField(db_column='TBT0007_SHUKA_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0007_soko_cd = models.CharField(db_column='TBT0007_SOKO_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0007_location_cd = models.CharField(db_column='TBT0007_LOCATION_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0007_KEIYAKU_URI'
        unique_together = (('tbt0005_keiyaku_no', 'tbt0006_keiyaku_dtl_no', 'tbt0007_uri_no'),)


class Tbt0008KeiyakuUriDtl(models.Model):
    tbt0005_keiyaku_no = models.CharField(db_column='TBT0005_KEIYAKU_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt0006_keiyaku_dtl_no = models.SmallIntegerField(db_column='TBT0006_KEIYAKU_DTL_NO')  # Field name made lowercase.
    tbt0007_uri_no = models.SmallIntegerField(db_column='TBT0007_URI_NO')  # Field name made lowercase.
    tbt0008_getsudo = models.SmallIntegerField(db_column='TBT0008_GETSUDO')  # Field name made lowercase.
    tbt0008_uri_date = models.DateTimeField(db_column='TBT0008_URI_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt0008_seikyu_yotei_ym = models.CharField(db_column='TBT0008_SEIKYU_YOTEI_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tbt0008_yuko_flg = models.BooleanField(db_column='TBT0008_YUKO_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt0008_tanka = models.DecimalField(db_column='TBT0008_TANKA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0008_suryo = models.DecimalField(db_column='TBT0008_SURYO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0008_szei_rate = models.DecimalField(db_column='TBT0008_SZEI_RATE', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0008_kingaku = models.DecimalField(db_column='TBT0008_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0008_uchi_zei = models.DecimalField(db_column='TBT0008_UCHI_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0008_soto_zei = models.DecimalField(db_column='TBT0008_SOTO_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0008_kazei_kbn = models.CharField(db_column='TBT0008_KAZEI_KBN', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0008_biko = models.CharField(db_column='TBT0008_BIKO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0008_del_flg = models.CharField(db_column='TBT0008_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0008_crt_datetime = models.DateTimeField(db_column='TBT0008_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0008_crt_user_id = models.CharField(db_column='TBT0008_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0008_crt_prog_nm = models.CharField(db_column='TBT0008_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0008_upd_datetime = models.DateTimeField(db_column='TBT0008_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0008_upd_user_id = models.CharField(db_column='TBT0008_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0008_upd_prog_nm = models.CharField(db_column='TBT0008_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0008_upd_cnt = models.DecimalField(db_column='TBT0008_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0008_jyuchu_denpyo_no = models.CharField(db_column='TBT0008_JYUCHU_DENPYO_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0008_KEIYAKU_URI_DTL'
        unique_together = (('tbt0005_keiyaku_no', 'tbt0006_keiyaku_dtl_no', 'tbt0007_uri_no', 'tbt0008_getsudo'),)


class Tbt0009JikoYsn(models.Model):
    tbt0009_nendo = models.SmallIntegerField(db_column='TBT0009_NENDO', primary_key=True)  # Field name made lowercase.
    tbt0009_genba_cd = models.CharField(db_column='TBT0009_GENBA_CD', max_length=5)  # Field name made lowercase.
    tbt0009_shoku_cd = models.CharField(db_column='TBT0009_SHOKU_CD', max_length=2)  # Field name made lowercase.
    tbt0009_str_month = models.SmallIntegerField(db_column='TBT0009_STR_MONTH', blank=True, null=True)  # Field name made lowercase.
    tbt0009_ord_kihyo_flg = models.BooleanField(db_column='TBT0009_ORD_KIHYO_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt0009_simyu_ritu_uri = models.DecimalField(db_column='TBT0009_SIMYU_RITU_URI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0009_simyu_ritu_gaityu = models.DecimalField(db_column='TBT0009_SIMYU_RITU_GAITYU', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0009_simyu_ritu_shohin = models.DecimalField(db_column='TBT0009_SIMYU_RITU_SHOHIN', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0009_simyu_ritu_keih = models.DecimalField(db_column='TBT0009_SIMYU_RITU_KEIH', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0009_simyu_ritu_sizai = models.DecimalField(db_column='TBT0009_SIMYU_RITU_SIZAI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0009_simyu_ritu_jnkn_hi = models.DecimalField(db_column='TBT0009_SIMYU_RITU_JNKN_HI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0009_simyu_gaku_uri = models.DecimalField(db_column='TBT0009_SIMYU_GAKU_URI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0009_simyu_gaku_gaityu = models.DecimalField(db_column='TBT0009_SIMYU_GAKU_GAITYU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0009_simyu_gaku_shohin = models.DecimalField(db_column='TBT0009_SIMYU_GAKU_SHOHIN', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0009_simyu_gaku_keih = models.DecimalField(db_column='TBT0009_SIMYU_GAKU_KEIH', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0009_simyu_gaku_sizai = models.DecimalField(db_column='TBT0009_SIMYU_GAKU_SIZAI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0009_simyu_gaku_jnkn_hi = models.DecimalField(db_column='TBT0009_SIMYU_GAKU_JNKN_HI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0009_simyu_upd_date = models.DateTimeField(db_column='TBT0009_SIMYU_UPD_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt0009_del_flg = models.CharField(db_column='TBT0009_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0009_crt_datetime = models.DateTimeField(db_column='TBT0009_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0009_crt_user_id = models.CharField(db_column='TBT0009_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0009_crt_prog_nm = models.CharField(db_column='TBT0009_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0009_upd_datetime = models.DateTimeField(db_column='TBT0009_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0009_upd_user_id = models.CharField(db_column='TBT0009_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0009_upd_prog_nm = models.CharField(db_column='TBT0009_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0009_upd_cnt = models.DecimalField(db_column='TBT0009_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0009_omit_flg = models.BooleanField(db_column='TBT0009_OMIT_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt0009_avg_kingaku = models.DecimalField(db_column='TBT0009_AVG_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0009_JIKO_YSN'
        unique_together = (('tbt0009_nendo', 'tbt0009_genba_cd', 'tbt0009_shoku_cd'),)


class Tbt0010JikoYsnSir(models.Model):
    tbt0009_nendo = models.SmallIntegerField(db_column='TBT0009_NENDO', primary_key=True)  # Field name made lowercase.
    tbt0009_genba_cd = models.CharField(db_column='TBT0009_GENBA_CD', max_length=5)  # Field name made lowercase.
    tbt0009_shoku_cd = models.CharField(db_column='TBT0009_SHOKU_CD', max_length=2)  # Field name made lowercase.
    tbt0010_sir_no = models.SmallIntegerField(db_column='TBT0010_SIR_NO')  # Field name made lowercase.
    tbt0010_nyuka_kbn = models.CharField(db_column='TBT0010_NYUKA_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0010_kenmei = models.CharField(db_column='TBT0010_KENMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0010_gyomu_shohin_cd = models.CharField(db_column='TBT0010_GYOMU_SHOHIN_CD', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0010_tani_nm = models.CharField(db_column='TBT0010_TANI_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tbt0010_siire_saki_cd = models.CharField(db_column='TBT0010_SIIRE_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbt0010_soko_cd = models.CharField(db_column='TBT0010_SOKO_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0010_haif_keiyaku_no = models.CharField(db_column='TBT0010_HAIF_KEIYAKU_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0010_del_flg = models.CharField(db_column='TBT0010_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0010_crt_datetime = models.DateTimeField(db_column='TBT0010_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0010_crt_user_id = models.CharField(db_column='TBT0010_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0010_crt_prog_nm = models.CharField(db_column='TBT0010_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0010_upd_datetime = models.DateTimeField(db_column='TBT0010_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0010_upd_user_id = models.CharField(db_column='TBT0010_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0010_upd_prog_nm = models.CharField(db_column='TBT0010_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0010_upd_cnt = models.DecimalField(db_column='TBT0010_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0010_omit_flg = models.BooleanField(db_column='TBT0010_OMIT_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt0010_location_cd = models.CharField(db_column='TBT0010_LOCATION_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0010_JIKO_YSN_SIR'
        unique_together = (('tbt0009_nendo', 'tbt0009_genba_cd', 'tbt0009_shoku_cd', 'tbt0010_sir_no'),)


class Tbt0011JikoYsnSirDtl(models.Model):
    tbt0009_nendo = models.SmallIntegerField(db_column='TBT0009_NENDO', primary_key=True)  # Field name made lowercase.
    tbt0009_genba_cd = models.CharField(db_column='TBT0009_GENBA_CD', max_length=5)  # Field name made lowercase.
    tbt0009_shoku_cd = models.CharField(db_column='TBT0009_SHOKU_CD', max_length=2)  # Field name made lowercase.
    tbt0010_sir_no = models.SmallIntegerField(db_column='TBT0010_SIR_NO')  # Field name made lowercase.
    tbt0011_getsudo = models.SmallIntegerField(db_column='TBT0011_GETSUDO')  # Field name made lowercase.
    tbt0011_yuko_flg = models.BooleanField(db_column='TBT0011_YUKO_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt0011_sir_date = models.DateTimeField(db_column='TBT0011_SIR_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt0011_tanka = models.DecimalField(db_column='TBT0011_TANKA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0011_suryo = models.DecimalField(db_column='TBT0011_SURYO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0011_kingaku = models.DecimalField(db_column='TBT0011_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0011_kazei_kbn = models.CharField(db_column='TBT0011_KAZEI_KBN', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0011_szei_rate = models.DecimalField(db_column='TBT0011_SZEI_RATE', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0011_uchi_zei = models.DecimalField(db_column='TBT0011_UCHI_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0011_soto_zei = models.DecimalField(db_column='TBT0011_SOTO_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0011_biko = models.CharField(db_column='TBT0011_BIKO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0011_order_denpyo_no = models.CharField(db_column='TBT0011_ORDER_DENPYO_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbt0011_del_flg = models.CharField(db_column='TBT0011_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0011_crt_datetime = models.DateTimeField(db_column='TBT0011_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0011_crt_user_id = models.CharField(db_column='TBT0011_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0011_crt_prog_nm = models.CharField(db_column='TBT0011_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0011_upd_datetime = models.DateTimeField(db_column='TBT0011_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0011_upd_user_id = models.CharField(db_column='TBT0011_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0011_upd_prog_nm = models.CharField(db_column='TBT0011_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0011_upd_cnt = models.DecimalField(db_column='TBT0011_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0011_JIKO_YSN_SIR_DTL'
        unique_together = (('tbt0009_nendo', 'tbt0009_genba_cd', 'tbt0009_shoku_cd', 'tbt0010_sir_no', 'tbt0011_getsudo'),)


class Tbt0012JikoYsnKeih(models.Model):
    tbt0009_nendo = models.SmallIntegerField(db_column='TBT0009_NENDO', primary_key=True)  # Field name made lowercase.
    tbt0009_genba_cd = models.CharField(db_column='TBT0009_GENBA_CD', max_length=5)  # Field name made lowercase.
    tbt0009_shoku_cd = models.CharField(db_column='TBT0009_SHOKU_CD', max_length=2)  # Field name made lowercase.
    tbt0012_keih_no = models.SmallIntegerField(db_column='TBT0012_KEIH_NO')  # Field name made lowercase.
    tbt0012_uke_ou_renban = models.SmallIntegerField(db_column='TBT0012_UKE_OU_RENBAN')  # Field name made lowercase.
    tbt0012_keih_kbn_cd = models.CharField(db_column='TBT0012_KEIH_KBN_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0012_memo = models.CharField(db_column='TBT0012_MEMO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0012_haif_keiyaku_no = models.CharField(db_column='TBT0012_HAIF_KEIYAKU_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0012_moto_genba_cd = models.CharField(db_column='TBT0012_MOTO_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tbt0012_moto_shoku_cd = models.CharField(db_column='TBT0012_MOTO_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tbt0012_moto_avg_kingaku = models.DecimalField(db_column='TBT0012_MOTO_AVG_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0012_omit_flg = models.BooleanField(db_column='TBT0012_OMIT_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt0012_del_flg = models.CharField(db_column='TBT0012_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0012_crt_datetime = models.DateTimeField(db_column='TBT0012_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0012_crt_user_id = models.CharField(db_column='TBT0012_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0012_crt_prog_nm = models.CharField(db_column='TBT0012_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0012_upd_datetime = models.DateTimeField(db_column='TBT0012_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0012_upd_user_id = models.CharField(db_column='TBT0012_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0012_upd_prog_nm = models.CharField(db_column='TBT0012_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0012_upd_cnt = models.DecimalField(db_column='TBT0012_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0012_JIKO_YSN_KEIH'
        unique_together = (('tbt0009_nendo', 'tbt0009_genba_cd', 'tbt0009_shoku_cd', 'tbt0012_keih_no', 'tbt0012_uke_ou_renban'),)


class Tbt0013JikoYsnKeihDtl(models.Model):
    tbt0009_nendo = models.SmallIntegerField(db_column='TBT0009_NENDO', primary_key=True)  # Field name made lowercase.
    tbt0009_genba_cd = models.CharField(db_column='TBT0009_GENBA_CD', max_length=5)  # Field name made lowercase.
    tbt0009_shoku_cd = models.CharField(db_column='TBT0009_SHOKU_CD', max_length=2)  # Field name made lowercase.
    tbt0012_keih_no = models.SmallIntegerField(db_column='TBT0012_KEIH_NO')  # Field name made lowercase.
    tbt0012_uke_ou_renban = models.SmallIntegerField(db_column='TBT0012_UKE_OU_RENBAN')  # Field name made lowercase.
    tbt0013_getsudo = models.SmallIntegerField(db_column='TBT0013_GETSUDO')  # Field name made lowercase.
    tbt0013_yuko_flg = models.BooleanField(db_column='TBT0013_YUKO_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt0013_keih_date = models.DateTimeField(db_column='TBT0013_KEIH_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt0013_kingaku = models.DecimalField(db_column='TBT0013_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0013_tekiyo = models.CharField(db_column='TBT0013_TEKIYO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0013_zei_flg = models.BooleanField(db_column='TBT0013_ZEI_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt0013_szei_rate = models.DecimalField(db_column='TBT0013_SZEI_RATE', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0013_uchi_zei = models.DecimalField(db_column='TBT0013_UCHI_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0013_kosu = models.DecimalField(db_column='TBT0013_KOSU', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0013_del_flg = models.CharField(db_column='TBT0013_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0013_crt_datetime = models.DateTimeField(db_column='TBT0013_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0013_crt_user_id = models.CharField(db_column='TBT0013_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0013_crt_prog_nm = models.CharField(db_column='TBT0013_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0013_upd_datetime = models.DateTimeField(db_column='TBT0013_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0013_upd_user_id = models.CharField(db_column='TBT0013_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0013_upd_prog_nm = models.CharField(db_column='TBT0013_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0013_upd_cnt = models.DecimalField(db_column='TBT0013_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0013_JIKO_YSN_KEIH_DTL'
        unique_together = (('tbt0009_nendo', 'tbt0009_genba_cd', 'tbt0009_shoku_cd', 'tbt0012_keih_no', 'tbt0012_uke_ou_renban', 'tbt0013_getsudo'),)


class Tbt0014JikoYsnShain(models.Model):
    tbt0009_nendo = models.SmallIntegerField(db_column='TBT0009_NENDO', primary_key=True)  # Field name made lowercase.
    tbt0009_genba_cd = models.CharField(db_column='TBT0009_GENBA_CD', max_length=5)  # Field name made lowercase.
    tbt0009_shoku_cd = models.CharField(db_column='TBT0009_SHOKU_CD', max_length=2)  # Field name made lowercase.
    tbt0014_shain_cd = models.CharField(db_column='TBT0014_SHAIN_CD', max_length=10)  # Field name made lowercase.
    tbt0014_shain_nm = models.CharField(db_column='TBT0014_SHAIN_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbt0014_shain_nm_k = models.CharField(db_column='TBT0014_SHAIN_NM_K', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbt0014_chingin_kbn = models.CharField(db_column='TBT0014_CHINGIN_KBN', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0014_tanka = models.IntegerField(db_column='TBT0014_TANKA', blank=True, null=True)  # Field name made lowercase.
    tbt0014_syurou_nissu = models.DecimalField(db_column='TBT0014_SYUROU_NISSU', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0014_syurou_jikan = models.DecimalField(db_column='TBT0014_SYUROU_JIKAN', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0014_tukin_hi = models.IntegerField(db_column='TBT0014_TUKIN_HI', blank=True, null=True)  # Field name made lowercase.
    tbt0014_hendo_tukin_hi = models.IntegerField(db_column='TBT0014_HENDO_TUKIN_HI', blank=True, null=True)  # Field name made lowercase.
    tbt0014_syo_teate = models.IntegerField(db_column='TBT0014_SYO_TEATE', blank=True, null=True)  # Field name made lowercase.
    tbt0014_syyo_ari_flg = models.BooleanField(db_column='TBT0014_SYYO_ARI_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt0014_syky_ari_flg = models.BooleanField(db_column='TBT0014_SYKY_ARI_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt0014_yuko_tuki_01 = models.BooleanField(db_column='TBT0014_YUKO_TUKI_01', blank=True, null=True)  # Field name made lowercase.
    tbt0014_yuko_tuki_02 = models.BooleanField(db_column='TBT0014_YUKO_TUKI_02', blank=True, null=True)  # Field name made lowercase.
    tbt0014_yuko_tuki_03 = models.BooleanField(db_column='TBT0014_YUKO_TUKI_03', blank=True, null=True)  # Field name made lowercase.
    tbt0014_yuko_tuki_04 = models.BooleanField(db_column='TBT0014_YUKO_TUKI_04', blank=True, null=True)  # Field name made lowercase.
    tbt0014_yuko_tuki_05 = models.BooleanField(db_column='TBT0014_YUKO_TUKI_05', blank=True, null=True)  # Field name made lowercase.
    tbt0014_yuko_tuki_06 = models.BooleanField(db_column='TBT0014_YUKO_TUKI_06', blank=True, null=True)  # Field name made lowercase.
    tbt0014_yuko_tuki_07 = models.BooleanField(db_column='TBT0014_YUKO_TUKI_07', blank=True, null=True)  # Field name made lowercase.
    tbt0014_yuko_tuki_08 = models.BooleanField(db_column='TBT0014_YUKO_TUKI_08', blank=True, null=True)  # Field name made lowercase.
    tbt0014_yuko_tuki_09 = models.BooleanField(db_column='TBT0014_YUKO_TUKI_09', blank=True, null=True)  # Field name made lowercase.
    tbt0014_yuko_tuki_10 = models.BooleanField(db_column='TBT0014_YUKO_TUKI_10', blank=True, null=True)  # Field name made lowercase.
    tbt0014_yuko_tuki_11 = models.BooleanField(db_column='TBT0014_YUKO_TUKI_11', blank=True, null=True)  # Field name made lowercase.
    tbt0014_yuko_tuki_12 = models.BooleanField(db_column='TBT0014_YUKO_TUKI_12', blank=True, null=True)  # Field name made lowercase.
    tbt0014_holiday_shift_code_1 = models.CharField(db_column='TBT0014_HOLIDAY_SHIFT_CODE_1', max_length=11, blank=True, null=True)  # Field name made lowercase.
    tbt0014_holiday_shift_code_2 = models.CharField(db_column='TBT0014_HOLIDAY_SHIFT_CODE_2', max_length=11, blank=True, null=True)  # Field name made lowercase.
    tbt0014_holiday_shift_code_3 = models.CharField(db_column='TBT0014_HOLIDAY_SHIFT_CODE_3', max_length=11, blank=True, null=True)  # Field name made lowercase.
    tbt0014_syyo_hkat_siyo_flg = models.BooleanField(db_column='TBT0014_SYYO_HKAT_SIYO_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt0014_syyo_hkat_ritu = models.DecimalField(db_column='TBT0014_SYYO_HKAT_RITU', max_digits=8, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
    tbt0014_syyo_hkat_gaku = models.IntegerField(db_column='TBT0014_SYYO_HKAT_GAKU', blank=True, null=True)  # Field name made lowercase.
    tbt0014_syyo_hotei_fuku_ritu = models.DecimalField(db_column='TBT0014_SYYO_HOTEI_FUKU_RITU', max_digits=8, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
    tbt0014_hotei_fuku_mode = models.SmallIntegerField(db_column='TBT0014_HOTEI_FUKU_MODE', blank=True, null=True)  # Field name made lowercase.
    tbt0014_kenk_hken_flg = models.BooleanField(db_column='TBT0014_KENK_HKEN_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt0014_ksei_nenk_flg = models.BooleanField(db_column='TBT0014_KSEI_NENK_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt0014_ksei_nenk_kkn_flg = models.BooleanField(db_column='TBT0014_KSEI_NENK_KKN_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt0014_koyo_hkn_flg = models.BooleanField(db_column='TBT0014_KOYO_HKN_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt0014_kaig_hkn_flg = models.BooleanField(db_column='TBT0014_KAIG_HKN_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt0014_hotei_fuku_gaku = models.IntegerField(db_column='TBT0014_HOTEI_FUKU_GAKU', blank=True, null=True)  # Field name made lowercase.
    tbt0014_yukyu_mode = models.SmallIntegerField(db_column='TBT0014_YUKYU_MODE', blank=True, null=True)  # Field name made lowercase.
    tbt0014_yukyu_time = models.DecimalField(db_column='TBT0014_YUKYU_TIME', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0014_yukyu_gaku = models.IntegerField(db_column='TBT0014_YUKYU_GAKU', blank=True, null=True)  # Field name made lowercase.
    tbt0014_omit_flg = models.BooleanField(db_column='TBT0014_OMIT_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt0014_del_flg = models.CharField(db_column='TBT0014_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0014_crt_datetime = models.DateTimeField(db_column='TBT0014_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0014_crt_user_id = models.CharField(db_column='TBT0014_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0014_crt_prog_nm = models.CharField(db_column='TBT0014_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0014_upd_datetime = models.DateTimeField(db_column='TBT0014_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0014_upd_user_id = models.CharField(db_column='TBT0014_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0014_upd_prog_nm = models.CharField(db_column='TBT0014_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0014_upd_cnt = models.DecimalField(db_column='TBT0014_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0014_holiday_shift_pkey_1 = models.IntegerField(db_column='TBT0014_HOLIDAY_SHIFT_PKEY_1', blank=True, null=True)  # Field name made lowercase.
    tbt0014_holiday_shift_pkey_2 = models.IntegerField(db_column='TBT0014_HOLIDAY_SHIFT_PKEY_2', blank=True, null=True)  # Field name made lowercase.
    tbt0014_holiday_shift_pkey_3 = models.IntegerField(db_column='TBT0014_HOLIDAY_SHIFT_PKEY_3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0014_JIKO_YSN_SHAIN'
        unique_together = (('tbt0009_nendo', 'tbt0009_genba_cd', 'tbt0009_shoku_cd', 'tbt0014_shain_cd'),)


class Tbt0015JikoYsnShainKinPtn(models.Model):
    tbt0009_nendo = models.SmallIntegerField(db_column='TBT0009_NENDO', primary_key=True)  # Field name made lowercase.
    tbt0009_genba_cd = models.CharField(db_column='TBT0009_GENBA_CD', max_length=5)  # Field name made lowercase.
    tbt0009_shoku_cd = models.CharField(db_column='TBT0009_SHOKU_CD', max_length=2)  # Field name made lowercase.
    tbt0014_shain_cd = models.CharField(db_column='TBT0014_SHAIN_CD', max_length=10)  # Field name made lowercase.
    tbt0015_week_no = models.SmallIntegerField(db_column='TBT0015_WEEK_NO')  # Field name made lowercase.
    tbt0015_day = models.SmallIntegerField(db_column='TBT0015_DAY')  # Field name made lowercase.
    tbt0015_renban = models.SmallIntegerField(db_column='TBT0015_RENBAN')  # Field name made lowercase.
    tbt0015_shift_code = models.CharField(db_column='TBT0015_SHIFT_CODE', max_length=11, blank=True, null=True)  # Field name made lowercase.
    tbt0015_del_flg = models.CharField(db_column='TBT0015_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0015_crt_datetime = models.DateTimeField(db_column='TBT0015_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0015_crt_user_id = models.CharField(db_column='TBT0015_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0015_crt_prog_nm = models.CharField(db_column='TBT0015_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0015_upd_datetime = models.DateTimeField(db_column='TBT0015_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0015_upd_user_id = models.CharField(db_column='TBT0015_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0015_upd_prog_nm = models.CharField(db_column='TBT0015_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0015_upd_cnt = models.DecimalField(db_column='TBT0015_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0015_shift_pkey = models.IntegerField(db_column='TBT0015_SHIFT_PKEY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0015_JIKO_YSN_SHAIN_KIN_PTN'
        unique_together = (('tbt0009_nendo', 'tbt0009_genba_cd', 'tbt0009_shoku_cd', 'tbt0014_shain_cd', 'tbt0015_week_no', 'tbt0015_day', 'tbt0015_renban'),)


class Tbt0016JikoYsnCalendar(models.Model):
    tbt0009_nendo = models.SmallIntegerField(db_column='TBT0009_NENDO', primary_key=True)  # Field name made lowercase.
    tbt0009_genba_cd = models.CharField(db_column='TBT0009_GENBA_CD', max_length=5)  # Field name made lowercase.
    tbt0009_shoku_cd = models.CharField(db_column='TBT0009_SHOKU_CD', max_length=2)  # Field name made lowercase.
    tbt0016_getsudo = models.SmallIntegerField(db_column='TBT0016_GETSUDO')  # Field name made lowercase.
    tbt0016_calendar = models.CharField(db_column='TBT0016_CALENDAR', max_length=31, blank=True, null=True)  # Field name made lowercase.
    tbt0016_del_flg = models.CharField(db_column='TBT0016_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0016_crt_datetime = models.DateTimeField(db_column='TBT0016_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0016_crt_user_id = models.CharField(db_column='TBT0016_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0016_crt_prog_nm = models.CharField(db_column='TBT0016_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0016_upd_datetime = models.DateTimeField(db_column='TBT0016_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0016_upd_user_id = models.CharField(db_column='TBT0016_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0016_upd_prog_nm = models.CharField(db_column='TBT0016_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0016_upd_cnt = models.DecimalField(db_column='TBT0016_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0016_JIKO_YSN_CALENDAR'
        unique_together = (('tbt0009_nendo', 'tbt0009_genba_cd', 'tbt0009_shoku_cd', 'tbt0016_getsudo'),)


class Tbt0017HifPtnSeksan(models.Model):
    tbt0009_nendo = models.SmallIntegerField(db_column='TBT0009_NENDO', primary_key=True)  # Field name made lowercase.
    tbt0009_genba_cd = models.CharField(db_column='TBT0009_GENBA_CD', max_length=5)  # Field name made lowercase.
    tbt0009_shoku_cd = models.CharField(db_column='TBT0009_SHOKU_CD', max_length=2)  # Field name made lowercase.
    tbt0017_keiyaku_no = models.CharField(db_column='TBT0017_KEIYAKU_NO', max_length=25)  # Field name made lowercase.
    tbt0017_hif_ptn_gaityu = models.DecimalField(db_column='TBT0017_HIF_PTN_GAITYU', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0017_hif_ptn_shohin = models.DecimalField(db_column='TBT0017_HIF_PTN_SHOHIN', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0017_hif_ptn_keih = models.DecimalField(db_column='TBT0017_HIF_PTN_KEIH', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0017_hif_ptn_sizai = models.DecimalField(db_column='TBT0017_HIF_PTN_SIZAI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0017_hif_ptn_jnkn_hi = models.DecimalField(db_column='TBT0017_HIF_PTN_JNKN_HI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0017_seksan_mnsk = models.DecimalField(db_column='TBT0017_SEKSAN_MNSK', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0017_seksan_kosu = models.DecimalField(db_column='TBT0017_SEKSAN_KOSU', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0017_seksan_jnkn_hi = models.DecimalField(db_column='TBT0017_SEKSAN_JNKN_HI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0017_seksan_sikizai = models.DecimalField(db_column='TBT0017_SEKSAN_SIKIZAI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0017_seksan_keih = models.DecimalField(db_column='TBT0017_SEKSAN_KEIH', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0017_mtmr_sho_no = models.CharField(db_column='TBT0017_MTMR_SHO_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0017_seksan_henk_date = models.DateTimeField(db_column='TBT0017_SEKSAN_HENK_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt0017_del_flg = models.CharField(db_column='TBT0017_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0017_crt_datetime = models.DateTimeField(db_column='TBT0017_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0017_crt_user_id = models.CharField(db_column='TBT0017_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0017_crt_prog_nm = models.CharField(db_column='TBT0017_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0017_upd_datetime = models.DateTimeField(db_column='TBT0017_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0017_upd_user_id = models.CharField(db_column='TBT0017_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0017_upd_prog_nm = models.CharField(db_column='TBT0017_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0017_upd_cnt = models.DecimalField(db_column='TBT0017_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0017_omit_flg = models.BooleanField(db_column='TBT0017_OMIT_FLG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0017_HIF_PTN_SEKSAN'
        unique_together = (('tbt0009_nendo', 'tbt0009_genba_cd', 'tbt0009_shoku_cd', 'tbt0017_keiyaku_no'),)


class Tbt0018KeiyCopySeigyo(models.Model):
    tbt0018_nendo = models.SmallIntegerField(db_column='TBT0018_NENDO', primary_key=True)  # Field name made lowercase.
    tbt0018_lock_flg = models.CharField(db_column='TBT0018_LOCK_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0018_del_flg = models.CharField(db_column='TBT0018_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0018_crt_datetime = models.DateTimeField(db_column='TBT0018_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0018_crt_user_id = models.CharField(db_column='TBT0018_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0018_crt_prog_nm = models.CharField(db_column='TBT0018_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0018_upd_datetime = models.DateTimeField(db_column='TBT0018_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0018_upd_user_id = models.CharField(db_column='TBT0018_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0018_upd_prog_nm = models.CharField(db_column='TBT0018_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0018_upd_cnt = models.DecimalField(db_column='TBT0018_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0018_KEIY_COPY_SEIGYO'


class Tbt0020NyusSnsei(models.Model):
    tbt0020_nyus_snsei_no = models.AutoField(db_column='TBT0020_NYUS_SNSEI_NO', primary_key=True)  # Field name made lowercase.
    tbt0020_sisn_ban = models.CharField(db_column='TBT0020_SISN_BAN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0020_kenmei = models.CharField(db_column='TBT0020_KENMEI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbt0020_tokui_saki = models.CharField(db_column='TBT0020_TOKUI_SAKI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbt0020_bunsyo_syrui = models.CharField(db_column='TBT0020_BUNSYO_SYRUI', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0020_gyomu_syrui = models.CharField(db_column='TBT0020_GYOMU_SYRUI', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0020_sakusei_shain_cd = models.CharField(db_column='TBT0020_SAKUSEI_SHAIN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbt0020_sakusei_date = models.DateTimeField(db_column='TBT0020_SAKUSEI_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt0020_teistu_shain_cd = models.CharField(db_column='TBT0020_TEISTU_SHAIN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbt0020_teistu_date = models.DateTimeField(db_column='TBT0020_TEISTU_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt0020_sinsei_date_from = models.DateTimeField(db_column='TBT0020_SINSEI_DATE_FROM', blank=True, null=True)  # Field name made lowercase.
    tbt0020_sinsei_date_to = models.DateTimeField(db_column='TBT0020_SINSEI_DATE_TO', blank=True, null=True)  # Field name made lowercase.
    tbt0020_mail_date = models.DateTimeField(db_column='TBT0020_MAIL_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt0020_kakunin_zumi = models.CharField(db_column='TBT0020_KAKUNIN_ZUMI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0020_send_mail_addr1 = models.CharField(db_column='TBT0020_SEND_MAIL_ADDR1', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tbt0020_send_mail_addr2 = models.CharField(db_column='TBT0020_SEND_MAIL_ADDR2', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tbt0020_send_mail_addr3 = models.CharField(db_column='TBT0020_SEND_MAIL_ADDR3', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tbt0020_send_mail_addr4 = models.CharField(db_column='TBT0020_SEND_MAIL_ADDR4', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tbt0020_send_mail_addr5 = models.CharField(db_column='TBT0020_SEND_MAIL_ADDR5', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tbt0020_file_1 = models.BinaryField(db_column='TBT0020_FILE_1', blank=True, null=True)  # Field name made lowercase.
    tbt0020_file_1_name = models.CharField(db_column='TBT0020_FILE_1_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbt0020_file_2 = models.BinaryField(db_column='TBT0020_FILE_2', blank=True, null=True)  # Field name made lowercase.
    tbt0020_file_2_name = models.CharField(db_column='TBT0020_FILE_2_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbt0020_file_3 = models.BinaryField(db_column='TBT0020_FILE_3', blank=True, null=True)  # Field name made lowercase.
    tbt0020_file_3_name = models.CharField(db_column='TBT0020_FILE_3_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbt0020_biko = models.CharField(db_column='TBT0020_BIKO', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tbt0020_del_flg = models.CharField(db_column='TBT0020_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0020_crt_datetime = models.DateTimeField(db_column='TBT0020_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0020_crt_user_id = models.CharField(db_column='TBT0020_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0020_crt_prog_nm = models.CharField(db_column='TBT0020_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0020_upd_datetime = models.DateTimeField(db_column='TBT0020_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0020_upd_user_id = models.CharField(db_column='TBT0020_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0020_upd_prog_nm = models.CharField(db_column='TBT0020_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0020_upd_cnt = models.DecimalField(db_column='TBT0020_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0020_NYUS_SNSEI'


class Tbt0301Jyuchu(models.Model):
    tbt0301_jyuchu_no = models.CharField(db_column='TBT0301_JYUCHU_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt0301_jyuchu_ed_no = models.SmallIntegerField(db_column='TBT0301_JYUCHU_ED_NO')  # Field name made lowercase.
    tbt0301_jyuchu_tei_ed_no = models.SmallIntegerField(db_column='TBT0301_JYUCHU_TEI_ED_NO')  # Field name made lowercase.
    tbt0301_jyuchu_tei_kbn_no = models.CharField(db_column='TBT0301_JYUCHU_TEI_KBN_NO', max_length=1)  # Field name made lowercase.
    tbt0301_teisei_saki_no = models.CharField(db_column='TBT0301_TEISEI_SAKI_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0301_teisei_moto_no = models.CharField(db_column='TBT0301_TEISEI_MOTO_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0301_keiyaku_no = models.CharField(db_column='TBT0301_KEIYAKU_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0301_chumon_no = models.CharField(db_column='TBT0301_CHUMON_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0301_jyuchu_denpyo_kbn_no = models.CharField(db_column='TBT0301_JYUCHU_DENPYO_KBN_NO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0301_jyuchu_denpyo_kind_no = models.CharField(db_column='TBT0301_JYUCHU_DENPYO_KIND_NO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0301_jyuchu_date = models.DateTimeField(db_column='TBT0301_JYUCHU_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt0301_uriage_date = models.DateTimeField(db_column='TBT0301_URIAGE_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt0301_seikyu_yotei_ym = models.CharField(db_column='TBT0301_SEIKYU_YOTEI_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tbt0301_hanbai_sts = models.CharField(db_column='TBT0301_HANBAI_STS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0301_hanbai_sub_sts = models.CharField(db_column='TBT0301_HANBAI_SUB_STS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0301_tokui_saki_cd = models.CharField(db_column='TBT0301_TOKUI_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbt0301_seikyu_saki_cd = models.CharField(db_column='TBT0301_SEIKYU_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbt0301_genba_cd = models.CharField(db_column='TBT0301_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tbt0301_shoku_cd = models.CharField(db_column='TBT0301_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tbt0301_szei_tnk_kbn_cd = models.CharField(db_column='TBT0301_SZEI_TNK_KBN_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0301_denpyo_memo = models.CharField(db_column='TBT0301_DENPYO_MEMO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0301_keiyaku_ttl_kingaku = models.DecimalField(db_column='TBT0301_KEIYAKU_TTL_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0301_keiyaku_ttl_uchi_zei = models.DecimalField(db_column='TBT0301_KEIYAKU_TTL_UCHI_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0301_keiyaku_ttl_soto_zei = models.DecimalField(db_column='TBT0301_KEIYAKU_TTL_SOTO_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0301_jyuchu_ttl_kingaku = models.DecimalField(db_column='TBT0301_JYUCHU_TTL_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0301_jyuchu_ttl_uchi_zei = models.DecimalField(db_column='TBT0301_JYUCHU_TTL_UCHI_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0301_jyuchu_ttl_soto_zei = models.DecimalField(db_column='TBT0301_JYUCHU_TTL_SOTO_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0301_del_flg = models.CharField(db_column='TBT0301_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0301_crt_datetime = models.DateTimeField(db_column='TBT0301_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0301_crt_user_id = models.CharField(db_column='TBT0301_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0301_crt_prog_nm = models.CharField(db_column='TBT0301_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0301_upd_datetime = models.DateTimeField(db_column='TBT0301_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0301_upd_user_id = models.CharField(db_column='TBT0301_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0301_upd_prog_nm = models.CharField(db_column='TBT0301_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0301_upd_cnt = models.DecimalField(db_column='TBT0301_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0301_chumon_uke_day = models.DateTimeField(db_column='TBT0301_CHUMON_UKE_DAY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0301_JYUCHU'
        unique_together = (('tbt0301_jyuchu_no', 'tbt0301_jyuchu_ed_no', 'tbt0301_jyuchu_tei_ed_no', 'tbt0301_jyuchu_tei_kbn_no'),)


class Tbt0302JyuchuDtl(models.Model):
    tbt0301_jyuchu_no = models.CharField(db_column='TBT0301_JYUCHU_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt0301_jyuchu_ed_no = models.SmallIntegerField(db_column='TBT0301_JYUCHU_ED_NO')  # Field name made lowercase.
    tbt0301_jyuchu_tei_ed_no = models.SmallIntegerField(db_column='TBT0301_JYUCHU_TEI_ED_NO')  # Field name made lowercase.
    tbt0301_jyuchu_tei_kbn_no = models.CharField(db_column='TBT0301_JYUCHU_TEI_KBN_NO', max_length=1)  # Field name made lowercase.
    tbt0302_jyuchu_dtl_no = models.SmallIntegerField(db_column='TBT0302_JYUCHU_DTL_NO')  # Field name made lowercase.
    tbt0302_gyomu_shohin_cd = models.CharField(db_column='TBT0302_GYOMU_SHOHIN_CD', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0302_gyomu_shohin_kbn_cd = models.CharField(db_column='TBT0302_GYOMU_SHOHIN_KBN_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0302_keiyaku_tani_nm = models.CharField(db_column='TBT0302_KEIYAKU_TANI_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tbt0302_keiyaku_tanka = models.DecimalField(db_column='TBT0302_KEIYAKU_TANKA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0302_keiyaku_suryo = models.DecimalField(db_column='TBT0302_KEIYAKU_SURYO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0302_keiyaku_kingaku = models.DecimalField(db_column='TBT0302_KEIYAKU_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0302_keiyaku_uchi_zei = models.DecimalField(db_column='TBT0302_KEIYAKU_UCHI_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0302_keiyaku_soto_zei = models.DecimalField(db_column='TBT0302_KEIYAKU_SOTO_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0302_jyuchu_tanka = models.DecimalField(db_column='TBT0302_JYUCHU_TANKA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0302_jyuchu_tani_nm = models.CharField(db_column='TBT0302_JYUCHU_TANI_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tbt0302_jyuchu_suryo = models.DecimalField(db_column='TBT0302_JYUCHU_SURYO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0302_jyuchu_kingaku = models.DecimalField(db_column='TBT0302_JYUCHU_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0302_jyuchu_uchi_zei = models.DecimalField(db_column='TBT0302_JYUCHU_UCHI_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0302_jyuchu_soto_zei = models.DecimalField(db_column='TBT0302_JYUCHU_SOTO_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0302_szei_rate = models.DecimalField(db_column='TBT0302_SZEI_RATE', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0302_kazei_kbn = models.CharField(db_column='TBT0302_KAZEI_KBN', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0302_shuka_kbn = models.CharField(db_column='TBT0302_SHUKA_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0302_soko_cd = models.CharField(db_column='TBT0302_SOKO_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0302_location_cd = models.CharField(db_column='TBT0302_LOCATION_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0302_biko = models.CharField(db_column='TBT0302_BIKO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0302_del_flg = models.CharField(db_column='TBT0302_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0302_crt_datetime = models.DateTimeField(db_column='TBT0302_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0302_crt_user_id = models.CharField(db_column='TBT0302_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0302_crt_prog_nm = models.CharField(db_column='TBT0302_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0302_upd_datetime = models.DateTimeField(db_column='TBT0302_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0302_upd_user_id = models.CharField(db_column='TBT0302_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0302_upd_prog_nm = models.CharField(db_column='TBT0302_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0302_upd_cnt = models.DecimalField(db_column='TBT0302_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0302_JYUCHU_DTL'
        unique_together = (('tbt0301_jyuchu_no', 'tbt0301_jyuchu_ed_no', 'tbt0301_jyuchu_tei_ed_no', 'tbt0301_jyuchu_tei_kbn_no', 'tbt0302_jyuchu_dtl_no'),)


class Tbt0303Uriage(models.Model):
    tbt0303_uriage_no = models.CharField(db_column='TBT0303_URIAGE_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt0303_uriage_ed_no = models.SmallIntegerField(db_column='TBT0303_URIAGE_ED_NO')  # Field name made lowercase.
    tbt0303_uriage_tei_kbn_no = models.CharField(db_column='TBT0303_URIAGE_TEI_KBN_NO', max_length=1)  # Field name made lowercase.
    tbt0303_jyuchu_no = models.CharField(db_column='TBT0303_JYUCHU_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0303_jyuchu_ed_no = models.SmallIntegerField(db_column='TBT0303_JYUCHU_ED_NO', blank=True, null=True)  # Field name made lowercase.
    tbt0303_jyuchu_tei_ed_no = models.SmallIntegerField(db_column='TBT0303_JYUCHU_TEI_ED_NO', blank=True, null=True)  # Field name made lowercase.
    tbt0303_jyuchu_tei_kbn_no = models.CharField(db_column='TBT0303_JYUCHU_TEI_KBN_NO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0303_teisei_saki_no = models.CharField(db_column='TBT0303_TEISEI_SAKI_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0303_teisei_moto_no = models.CharField(db_column='TBT0303_TEISEI_MOTO_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0303_keiyaku_no = models.CharField(db_column='TBT0303_KEIYAKU_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0303_chumon_no = models.CharField(db_column='TBT0303_CHUMON_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0303_uriage_denpyo_kbn_no = models.CharField(db_column='TBT0303_URIAGE_DENPYO_KBN_NO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0303_uriage_denpyo_kind_no = models.CharField(db_column='TBT0303_URIAGE_DENPYO_KIND_NO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0303_uriage_date = models.DateTimeField(db_column='TBT0303_URIAGE_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt0303_seikyu_yotei_ym = models.CharField(db_column='TBT0303_SEIKYU_YOTEI_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tbt0303_tokui_saki_cd = models.CharField(db_column='TBT0303_TOKUI_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbt0303_seikyu_saki_cd = models.CharField(db_column='TBT0303_SEIKYU_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbt0303_szei_tnk_kbn_cd = models.CharField(db_column='TBT0303_SZEI_TNK_KBN_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0303_genba_cd = models.CharField(db_column='TBT0303_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tbt0303_shoku_cd = models.CharField(db_column='TBT0303_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tbt0303_denpyo_memo = models.CharField(db_column='TBT0303_DENPYO_MEMO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0303_uriage_ttl_kingaku = models.DecimalField(db_column='TBT0303_URIAGE_TTL_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0303_uriage_ttl_uchi_zei = models.DecimalField(db_column='TBT0303_URIAGE_TTL_UCHI_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0303_uriage_ttl_soto_zei = models.DecimalField(db_column='TBT0303_URIAGE_TTL_SOTO_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0303_del_flg = models.CharField(db_column='TBT0303_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0303_crt_datetime = models.DateTimeField(db_column='TBT0303_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0303_crt_user_id = models.CharField(db_column='TBT0303_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0303_crt_prog_nm = models.CharField(db_column='TBT0303_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0303_upd_datetime = models.DateTimeField(db_column='TBT0303_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0303_upd_user_id = models.CharField(db_column='TBT0303_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0303_upd_prog_nm = models.CharField(db_column='TBT0303_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0303_upd_cnt = models.DecimalField(db_column='TBT0303_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0303_seikyu_no = models.CharField(db_column='TBT0303_SEIKYU_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0303_seikyu_ed_no = models.SmallIntegerField(db_column='TBT0303_SEIKYU_ED_NO', blank=True, null=True)  # Field name made lowercase.
    tbt0303_seikyusho_no = models.CharField(db_column='TBT0303_SEIKYUSHO_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0303_seikyusho_ed_no = models.SmallIntegerField(db_column='TBT0303_SEIKYUSHO_ED_NO', blank=True, null=True)  # Field name made lowercase.
    tbt0303_seikyusho_sai_ed_no = models.SmallIntegerField(db_column='TBT0303_SEIKYUSHO_SAI_ED_NO', blank=True, null=True)  # Field name made lowercase.
    tbt0303_nouhin_day = models.DateTimeField(db_column='TBT0303_NOUHIN_DAY', blank=True, null=True)  # Field name made lowercase.
    tbt0303_seikyu_day = models.DateTimeField(db_column='TBT0303_SEIKYU_DAY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0303_URIAGE'
        unique_together = (('tbt0303_uriage_no', 'tbt0303_uriage_ed_no', 'tbt0303_uriage_tei_kbn_no'),)


class Tbt0304UriageDtl(models.Model):
    tbt0303_uriage_no = models.CharField(db_column='TBT0303_URIAGE_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt0303_uriage_ed_no = models.SmallIntegerField(db_column='TBT0303_URIAGE_ED_NO')  # Field name made lowercase.
    tbt0303_uriage_tei_kbn_no = models.CharField(db_column='TBT0303_URIAGE_TEI_KBN_NO', max_length=1)  # Field name made lowercase.
    tbt0304_uriage_dtl_no = models.SmallIntegerField(db_column='TBT0304_URIAGE_DTL_NO')  # Field name made lowercase.
    tbt0304_gyomu_shohin_cd = models.CharField(db_column='TBT0304_GYOMU_SHOHIN_CD', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0304_gyomu_shohin_kbn_cd = models.CharField(db_column='TBT0304_GYOMU_SHOHIN_KBN_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0304_uriage_tani_nm = models.CharField(db_column='TBT0304_URIAGE_TANI_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tbt0304_uriage_tanka = models.DecimalField(db_column='TBT0304_URIAGE_TANKA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0304_uriage_suryo = models.DecimalField(db_column='TBT0304_URIAGE_SURYO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0304_uriage_kingaku = models.DecimalField(db_column='TBT0304_URIAGE_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0304_uriage_uchi_zei = models.DecimalField(db_column='TBT0304_URIAGE_UCHI_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0304_uriage_soto_zei = models.DecimalField(db_column='TBT0304_URIAGE_SOTO_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0304_szei_rate = models.DecimalField(db_column='TBT0304_SZEI_RATE', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0304_kazei_kbn = models.CharField(db_column='TBT0304_KAZEI_KBN', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0304_shuka_kbn = models.CharField(db_column='TBT0304_SHUKA_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0304_soko_cd = models.CharField(db_column='TBT0304_SOKO_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0304_location_cd = models.CharField(db_column='TBT0304_LOCATION_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0304_biko = models.CharField(db_column='TBT0304_BIKO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0304_del_flg = models.CharField(db_column='TBT0304_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0304_crt_datetime = models.DateTimeField(db_column='TBT0304_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0304_crt_user_id = models.CharField(db_column='TBT0304_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0304_crt_prog_nm = models.CharField(db_column='TBT0304_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0304_upd_datetime = models.DateTimeField(db_column='TBT0304_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0304_upd_user_id = models.CharField(db_column='TBT0304_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0304_upd_prog_nm = models.CharField(db_column='TBT0304_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0304_upd_cnt = models.DecimalField(db_column='TBT0304_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0304_uriage_kakutei_suryo = models.DecimalField(db_column='TBT0304_URIAGE_KAKUTEI_SURYO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0304_URIAGE_DTL'
        unique_together = (('tbt0303_uriage_no', 'tbt0303_uriage_ed_no', 'tbt0303_uriage_tei_kbn_no', 'tbt0304_uriage_dtl_no'),)


class Tbt0305UriageShime(models.Model):
    tbt0305_uriage_shime_seq_no = models.AutoField(db_column='TBT0305_URIAGE_SHIME_SEQ_NO', primary_key=True)  # Field name made lowercase.
    tbt0305_uriage_shime_day_from = models.DateTimeField(db_column='TBT0305_URIAGE_SHIME_DAY_FROM', blank=True, null=True)  # Field name made lowercase.
    tbt0305_uriage_shime_day_to = models.DateTimeField(db_column='TBT0305_URIAGE_SHIME_DAY_TO', blank=True, null=True)  # Field name made lowercase.
    tbt0305_del_flg = models.CharField(db_column='TBT0305_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0305_crt_datetime = models.DateTimeField(db_column='TBT0305_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0305_crt_user_id = models.CharField(db_column='TBT0305_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0305_crt_prog_nm = models.CharField(db_column='TBT0305_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0305_upd_datetime = models.DateTimeField(db_column='TBT0305_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0305_upd_user_id = models.CharField(db_column='TBT0305_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0305_upd_prog_nm = models.CharField(db_column='TBT0305_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0305_upd_cnt = models.DecimalField(db_column='TBT0305_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0305_URIAGE_SHIME'


class Tbt0306Seikyu(models.Model):
    tbt0306_seikyu_no = models.CharField(db_column='TBT0306_SEIKYU_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt0306_seikyu_ed_no = models.SmallIntegerField(db_column='TBT0306_SEIKYU_ED_NO')  # Field name made lowercase.
    tbt0306_seikyusho_no = models.CharField(db_column='TBT0306_SEIKYUSHO_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0306_seikyusho_ed_no = models.SmallIntegerField(db_column='TBT0306_SEIKYUSHO_ED_NO', blank=True, null=True)  # Field name made lowercase.
    tbt0306_seikyusho_sai_ed_no = models.SmallIntegerField(db_column='TBT0306_SEIKYUSHO_SAI_ED_NO', blank=True, null=True)  # Field name made lowercase.
    tbt0306_uriage_ttl_kingaku = models.DecimalField(db_column='TBT0306_URIAGE_TTL_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0306_nyukin_keshikomi_kingaku = models.DecimalField(db_column='TBT0306_NYUKIN_KESHIKOMI_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0306_seikyu_shime_date = models.DateTimeField(db_column='TBT0306_SEIKYU_SHIME_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt0306_nyukin_date = models.DateTimeField(db_column='TBT0306_NYUKIN_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt0306_tokui_saki_cd = models.CharField(db_column='TBT0306_TOKUI_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbt0306_seikyu_saki_cd = models.CharField(db_column='TBT0306_SEIKYU_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbt0306_szei_tnk_kbn_cd = models.CharField(db_column='TBT0306_SZEI_TNK_KBN_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0306_seikyu_shime_date_from = models.DateTimeField(db_column='TBT0306_SEIKYU_SHIME_DATE_FROM', blank=True, null=True)  # Field name made lowercase.
    tbt0306_seikyu_shime_date_to = models.DateTimeField(db_column='TBT0306_SEIKYU_SHIME_DATE_TO', blank=True, null=True)  # Field name made lowercase.
    tbt0306_shime_exec_date = models.DateTimeField(db_column='TBT0306_SHIME_EXEC_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt0306_del_flg = models.CharField(db_column='TBT0306_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0306_crt_datetime = models.DateTimeField(db_column='TBT0306_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0306_crt_user_id = models.CharField(db_column='TBT0306_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0306_crt_prog_nm = models.CharField(db_column='TBT0306_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0306_upd_datetime = models.DateTimeField(db_column='TBT0306_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0306_upd_user_id = models.CharField(db_column='TBT0306_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0306_upd_prog_nm = models.CharField(db_column='TBT0306_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0306_upd_cnt = models.DecimalField(db_column='TBT0306_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0306_uriage_ttl_soto_zei = models.DecimalField(db_column='TBT0306_URIAGE_TTL_SOTO_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0306_kurikoshi_kingaku = models.DecimalField(db_column='TBT0306_KURIKOSHI_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0306_seikyu_day = models.DateTimeField(db_column='TBT0306_SEIKYU_DAY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0306_SEIKYU'
        unique_together = (('tbt0306_seikyu_no', 'tbt0306_seikyu_ed_no'),)


class Tbt0307Nyukin(models.Model):
    tbt0307_nyukin_no = models.CharField(db_column='TBT0307_NYUKIN_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt0307_nyukin_ed_no = models.SmallIntegerField(db_column='TBT0307_NYUKIN_ED_NO')  # Field name made lowercase.
    tbt0307_nyukin_date = models.DateTimeField(db_column='TBT0307_NYUKIN_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt0307_tokui_saki_cd = models.CharField(db_column='TBT0307_TOKUI_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbt0307_kaisha_cd = models.CharField(db_column='TBT0307_KAISHA_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0307_nyukin_ttl_kingaku = models.DecimalField(db_column='TBT0307_NYUKIN_TTL_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0307_chousei_ttl_kingaku = models.DecimalField(db_column='TBT0307_CHOUSEI_TTL_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0307_nyukin_keshikomi_ttl_kingaku = models.DecimalField(db_column='TBT0307_NYUKIN_KESHIKOMI_TTL_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0307_furikae_ttl_kingaku = models.DecimalField(db_column='TBT0307_FURIKAE_TTL_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0307_biko = models.CharField(db_column='TBT0307_BIKO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0307_del_flg = models.CharField(db_column='TBT0307_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0307_crt_datetime = models.DateTimeField(db_column='TBT0307_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0307_crt_user_id = models.CharField(db_column='TBT0307_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0307_crt_prog_nm = models.CharField(db_column='TBT0307_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0307_upd_datetime = models.DateTimeField(db_column='TBT0307_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0307_upd_user_id = models.CharField(db_column='TBT0307_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0307_upd_prog_nm = models.CharField(db_column='TBT0307_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0307_upd_cnt = models.DecimalField(db_column='TBT0307_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0307_NYUKIN'
        unique_together = (('tbt0307_nyukin_no', 'tbt0307_nyukin_ed_no'),)


class Tbt0308NyukinInfo(models.Model):
    tbt0307_nyukin_no = models.CharField(db_column='TBT0307_NYUKIN_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt0307_nyukin_ed_no = models.SmallIntegerField(db_column='TBT0307_NYUKIN_ED_NO')  # Field name made lowercase.
    tbt0308_nyukin_dtl_no = models.SmallIntegerField(db_column='TBT0308_NYUKIN_DTL_NO')  # Field name made lowercase.
    tbt0308_nyukin_kbn = models.CharField(db_column='TBT0308_NYUKIN_KBN', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0308_nyukin_kingaku = models.DecimalField(db_column='TBT0308_NYUKIN_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0308_tegata_date = models.DateTimeField(db_column='TBT0308_TEGATA_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt0308_tegata_no = models.CharField(db_column='TBT0308_TEGATA_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0308_furikae_kingaku = models.DecimalField(db_column='TBT0308_FURIKAE_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0308_kaisha_bank_seq_cd = models.CharField(db_column='TBT0308_KAISHA_BANK_SEQ_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbt0308_tokui_saki_bank_seq_cd = models.CharField(db_column='TBT0308_TOKUI_SAKI_BANK_SEQ_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbt0308_biko = models.CharField(db_column='TBT0308_BIKO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0308_del_flg = models.CharField(db_column='TBT0308_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0308_crt_datetime = models.DateTimeField(db_column='TBT0308_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0308_crt_user_id = models.CharField(db_column='TBT0308_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0308_crt_prog_nm = models.CharField(db_column='TBT0308_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0308_upd_datetime = models.DateTimeField(db_column='TBT0308_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0308_upd_user_id = models.CharField(db_column='TBT0308_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0308_upd_prog_nm = models.CharField(db_column='TBT0308_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0308_upd_cnt = models.DecimalField(db_column='TBT0308_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0308_kaisha_cd = models.CharField(db_column='TBT0308_KAISHA_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0308_tokui_saki_cd = models.CharField(db_column='TBT0308_TOKUI_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0308_NYUKIN_INFO'
        unique_together = (('tbt0307_nyukin_no', 'tbt0307_nyukin_ed_no', 'tbt0308_nyukin_dtl_no'),)


class Tbt0309NyukinSeikyuInfo(models.Model):
    tbt0307_nyukin_no = models.CharField(db_column='TBT0307_NYUKIN_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt0307_nyukin_ed_no = models.SmallIntegerField(db_column='TBT0307_NYUKIN_ED_NO')  # Field name made lowercase.
    tbt0309_seikyu_no = models.CharField(db_column='TBT0309_SEIKYU_NO', max_length=25)  # Field name made lowercase.
    tbt0309_seikyu_ed_no = models.SmallIntegerField(db_column='TBT0309_SEIKYU_ED_NO')  # Field name made lowercase.
    tbt0309_nyukin_keshikomi_kingaku = models.DecimalField(db_column='TBT0309_NYUKIN_KESHIKOMI_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0309_del_flg = models.CharField(db_column='TBT0309_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0309_crt_datetime = models.DateTimeField(db_column='TBT0309_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0309_crt_user_id = models.CharField(db_column='TBT0309_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0309_crt_prog_nm = models.CharField(db_column='TBT0309_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0309_upd_datetime = models.DateTimeField(db_column='TBT0309_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0309_upd_user_id = models.CharField(db_column='TBT0309_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0309_upd_prog_nm = models.CharField(db_column='TBT0309_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0309_upd_cnt = models.DecimalField(db_column='TBT0309_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0309_NYUKIN_SEIKYU_INFO'
        unique_together = (('tbt0307_nyukin_no', 'tbt0307_nyukin_ed_no', 'tbt0309_seikyu_no', 'tbt0309_seikyu_ed_no'),)


class Tbt0310UriShimeCntl(models.Model):
    tbt0310_nendo = models.SmallIntegerField(db_column='TBT0310_NENDO', primary_key=True)  # Field name made lowercase.
    tbt0310_getsudo = models.SmallIntegerField(db_column='TBT0310_GETSUDO')  # Field name made lowercase.
    tbt0310_shime_flg = models.CharField(db_column='TBT0310_SHIME_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0310_del_flg = models.CharField(db_column='TBT0310_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0310_crt_datetime = models.DateTimeField(db_column='TBT0310_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0310_crt_user_id = models.CharField(db_column='TBT0310_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0310_crt_prog_nm = models.CharField(db_column='TBT0310_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0310_upd_datetime = models.DateTimeField(db_column='TBT0310_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0310_upd_user_id = models.CharField(db_column='TBT0310_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0310_upd_prog_nm = models.CharField(db_column='TBT0310_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0310_upd_cnt = models.DecimalField(db_column='TBT0310_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0310_URI_SHIME_CNTL'
        unique_together = (('tbt0310_nendo', 'tbt0310_getsudo'),)


class Tbt0401Hatchu(models.Model):
    tbt0401_hatchu_no = models.CharField(db_column='TBT0401_HATCHU_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt0401_ed_no = models.SmallIntegerField(db_column='TBT0401_ED_NO')  # Field name made lowercase.
    tbt0401_tei_ed_no = models.SmallIntegerField(db_column='TBT0401_TEI_ED_NO')  # Field name made lowercase.
    tbt0401_tei_kbn = models.CharField(db_column='TBT0401_TEI_KBN', max_length=1)  # Field name made lowercase.
    tbt0401_teisei_saki_no = models.CharField(db_column='TBT0401_TEISEI_SAKI_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0401_teisei_moto_no = models.CharField(db_column='TBT0401_TEISEI_MOTO_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0401_denpyo_kbn = models.CharField(db_column='TBT0401_DENPYO_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0401_denpyo_kind = models.CharField(db_column='TBT0401_DENPYO_KIND', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0401_hatchu_yotei_ym = models.DateTimeField(db_column='TBT0401_HATCHU_YOTEI_YM', blank=True, null=True)  # Field name made lowercase.
    tbt0401_siire_date = models.DateTimeField(db_column='TBT0401_SIIRE_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt0401_hatchu_sts = models.CharField(db_column='TBT0401_HATCHU_STS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0401_hatchu_sub_sts = models.CharField(db_column='TBT0401_HATCHU_SUB_STS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0401_siire_saki_cd = models.CharField(db_column='TBT0401_SIIRE_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbt0401_genba_cd = models.CharField(db_column='TBT0401_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tbt0401_shoku_cd = models.CharField(db_column='TBT0401_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tbt0401_kenmei = models.CharField(db_column='TBT0401_KENMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0401_siharai_jouken = models.CharField(db_column='TBT0401_SIHARAI_JOUKEN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0401_nounyu_basho = models.CharField(db_column='TBT0401_NOUNYU_BASHO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0401_denpyo_tekiyou = models.CharField(db_column='TBT0401_DENPYO_TEKIYOU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0401_keiyaku_ttl_kingaku = models.DecimalField(db_column='TBT0401_KEIYAKU_TTL_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0401_keiyaku_ttl_uchi_zei = models.DecimalField(db_column='TBT0401_KEIYAKU_TTL_UCHI_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0401_keiyaku_ttl_soto_zei = models.DecimalField(db_column='TBT0401_KEIYAKU_TTL_SOTO_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0401_hatchu_ttl_kingaku = models.DecimalField(db_column='TBT0401_HATCHU_TTL_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0401_hatchu_ttl_uchi_zei = models.DecimalField(db_column='TBT0401_HATCHU_TTL_UCHI_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0401_hatchu_ttl_soto_zei = models.DecimalField(db_column='TBT0401_HATCHU_TTL_SOTO_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0401_del_flg = models.CharField(db_column='TBT0401_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0401_crt_datetime = models.DateTimeField(db_column='TBT0401_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0401_crt_user_id = models.CharField(db_column='TBT0401_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0401_crt_prog_nm = models.CharField(db_column='TBT0401_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0401_upd_datetime = models.DateTimeField(db_column='TBT0401_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0401_upd_user_id = models.CharField(db_column='TBT0401_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0401_upd_prog_nm = models.CharField(db_column='TBT0401_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0401_upd_cnt = models.DecimalField(db_column='TBT0401_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0401_hatchu_day = models.DateTimeField(db_column='TBT0401_HATCHU_DAY', blank=True, null=True)  # Field name made lowercase.
    tbt0401_sagyo_houkoku_day = models.DateTimeField(db_column='TBT0401_SAGYO_HOUKOKU_DAY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0401_HATCHU'
        unique_together = (('tbt0401_hatchu_no', 'tbt0401_ed_no', 'tbt0401_tei_ed_no', 'tbt0401_tei_kbn'),)


class Tbt0402HatchuDtl(models.Model):
    tbt0401_hatchu_no = models.CharField(db_column='TBT0401_HATCHU_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt0401_ed_no = models.SmallIntegerField(db_column='TBT0401_ED_NO')  # Field name made lowercase.
    tbt0401_tei_ed_no = models.SmallIntegerField(db_column='TBT0401_TEI_ED_NO')  # Field name made lowercase.
    tbt0401_tei_kbn = models.CharField(db_column='TBT0401_TEI_KBN', max_length=1)  # Field name made lowercase.
    tbt0402_hatchu_dtl_no = models.SmallIntegerField(db_column='TBT0402_HATCHU_DTL_NO')  # Field name made lowercase.
    tbt0402_gyomu_shohin_cd = models.CharField(db_column='TBT0402_GYOMU_SHOHIN_CD', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0402_gyomu_shohin_kbn_cd = models.CharField(db_column='TBT0402_GYOMU_SHOHIN_KBN_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0402_keiyaku_tani_nm = models.CharField(db_column='TBT0402_KEIYAKU_TANI_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tbt0402_keiyaku_tanka = models.DecimalField(db_column='TBT0402_KEIYAKU_TANKA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0402_keiyaku_suryo = models.DecimalField(db_column='TBT0402_KEIYAKU_SURYO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0402_keiyaku_kingaku = models.DecimalField(db_column='TBT0402_KEIYAKU_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0402_keiyaku_uchi_zei = models.DecimalField(db_column='TBT0402_KEIYAKU_UCHI_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0402_keiyaku_soto_zei = models.DecimalField(db_column='TBT0402_KEIYAKU_SOTO_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0402_hatchu_tani_nm = models.CharField(db_column='TBT0402_HATCHU_TANI_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tbt0402_hatchu_tanka = models.DecimalField(db_column='TBT0402_HATCHU_TANKA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0402_hatchu_suryo = models.DecimalField(db_column='TBT0402_HATCHU_SURYO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0402_hatchu_kingaku = models.DecimalField(db_column='TBT0402_HATCHU_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0402_hatchu_uchi_zei = models.DecimalField(db_column='TBT0402_HATCHU_UCHI_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0402_hatchu_soto_zei = models.DecimalField(db_column='TBT0402_HATCHU_SOTO_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0402_szei_rate = models.DecimalField(db_column='TBT0402_SZEI_RATE', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0402_kazei_kbn = models.CharField(db_column='TBT0402_KAZEI_KBN', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0402_nyuka_kbn = models.CharField(db_column='TBT0402_NYUKA_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0402_soko_cd = models.CharField(db_column='TBT0402_SOKO_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0402_location_cd = models.CharField(db_column='TBT0402_LOCATION_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0402_keiyaku_haifu = models.CharField(db_column='TBT0402_KEIYAKU_HAIFU', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0402_keiyaku_haifu_nm = models.CharField(db_column='TBT0402_KEIYAKU_HAIFU_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0402_nouhin_kigen = models.DateTimeField(db_column='TBT0402_NOUHIN_KIGEN', blank=True, null=True)  # Field name made lowercase.
    tbt0402_biko = models.CharField(db_column='TBT0402_BIKO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0402_del_flg = models.CharField(db_column='TBT0402_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0402_crt_datetime = models.DateTimeField(db_column='TBT0402_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0402_crt_user_id = models.CharField(db_column='TBT0402_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0402_crt_prog_nm = models.CharField(db_column='TBT0402_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0402_upd_datetime = models.DateTimeField(db_column='TBT0402_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0402_upd_user_id = models.CharField(db_column='TBT0402_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0402_upd_prog_nm = models.CharField(db_column='TBT0402_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0402_upd_cnt = models.DecimalField(db_column='TBT0402_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0402_HATCHU_DTL'
        unique_together = (('tbt0401_hatchu_no', 'tbt0401_ed_no', 'tbt0401_tei_ed_no', 'tbt0401_tei_kbn', 'tbt0402_hatchu_dtl_no'),)


class Tbt0403Siire(models.Model):
    tbt0403_siire_no = models.CharField(db_column='TBT0403_SIIRE_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt0403_siire_tei_ed_no = models.SmallIntegerField(db_column='TBT0403_SIIRE_TEI_ED_NO')  # Field name made lowercase.
    tbt0403_siire_tei_kbn = models.CharField(db_column='TBT0403_SIIRE_TEI_KBN', max_length=1)  # Field name made lowercase.
    tbt0403_teisei_saki_no = models.CharField(db_column='TBT0403_TEISEI_SAKI_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0403_teisei_moto_no = models.CharField(db_column='TBT0403_TEISEI_MOTO_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0403_hatchu_no = models.CharField(db_column='TBT0403_HATCHU_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0403_hatchu_ed_no = models.SmallIntegerField(db_column='TBT0403_HATCHU_ED_NO', blank=True, null=True)  # Field name made lowercase.
    tbt0403_hatchu_tei_ed_no = models.SmallIntegerField(db_column='TBT0403_HATCHU_TEI_ED_NO', blank=True, null=True)  # Field name made lowercase.
    tbt0403_hatchu_tei_kbn = models.CharField(db_column='TBT0403_HATCHU_TEI_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0403_denpyo_kbn = models.CharField(db_column='TBT0403_DENPYO_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0403_denpyo_kind = models.CharField(db_column='TBT0403_DENPYO_KIND', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0403_siire_date = models.DateTimeField(db_column='TBT0403_SIIRE_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt0403_siire_saki_cd = models.CharField(db_column='TBT0403_SIIRE_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbt0403_szei_tnk_kbn_cd = models.CharField(db_column='TBT0403_SZEI_TNK_KBN_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0403_genba_cd = models.CharField(db_column='TBT0403_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tbt0403_shoku_cd = models.CharField(db_column='TBT0403_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tbt0403_kenmei = models.CharField(db_column='TBT0403_KENMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0403_siharai_jouken = models.CharField(db_column='TBT0403_SIHARAI_JOUKEN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0403_nounyu_basho = models.CharField(db_column='TBT0403_NOUNYU_BASHO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0403_denpyo_tekiyou = models.CharField(db_column='TBT0403_DENPYO_TEKIYOU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0403_ttl_kingaku = models.DecimalField(db_column='TBT0403_TTL_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0403_ttl_uchi_zei = models.DecimalField(db_column='TBT0403_TTL_UCHI_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0403_ttl_soto_zei = models.DecimalField(db_column='TBT0403_TTL_SOTO_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0403_del_flg = models.CharField(db_column='TBT0403_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0403_crt_datetime = models.DateTimeField(db_column='TBT0403_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0403_crt_user_id = models.CharField(db_column='TBT0403_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0403_crt_prog_nm = models.CharField(db_column='TBT0403_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0403_upd_datetime = models.DateTimeField(db_column='TBT0403_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0403_upd_user_id = models.CharField(db_column='TBT0403_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0403_upd_prog_nm = models.CharField(db_column='TBT0403_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0403_upd_cnt = models.DecimalField(db_column='TBT0403_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0403_shiharai_keshikomi_kingaku = models.DecimalField(db_column='TBT0403_SHIHARAI_KESHIKOMI_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0403_SIIRE'
        unique_together = (('tbt0403_siire_no', 'tbt0403_siire_tei_ed_no', 'tbt0403_siire_tei_kbn'),)


class Tbt0404SiireDtl(models.Model):
    tbt0403_siire_no = models.CharField(db_column='TBT0403_SIIRE_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt0403_siire_tei_ed_no = models.SmallIntegerField(db_column='TBT0403_SIIRE_TEI_ED_NO')  # Field name made lowercase.
    tbt0403_siire_tei_kbn = models.CharField(db_column='TBT0403_SIIRE_TEI_KBN', max_length=1)  # Field name made lowercase.
    tbt0404_siire_dtl_no = models.SmallIntegerField(db_column='TBT0404_SIIRE_DTL_NO')  # Field name made lowercase.
    tbt0404_gyomu_shohin_cd = models.CharField(db_column='TBT0404_GYOMU_SHOHIN_CD', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0404_gyomu_shohin_kbn_cd = models.CharField(db_column='TBT0404_GYOMU_SHOHIN_KBN_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0404_tani_nm = models.CharField(db_column='TBT0404_TANI_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tbt0404_tanka = models.DecimalField(db_column='TBT0404_TANKA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0404_suryo = models.DecimalField(db_column='TBT0404_SURYO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0404_kakutei_suryo = models.DecimalField(db_column='TBT0404_KAKUTEI_SURYO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0404_kingaku = models.DecimalField(db_column='TBT0404_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0404_uchi_zei = models.DecimalField(db_column='TBT0404_UCHI_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0404_soto_zei = models.DecimalField(db_column='TBT0404_SOTO_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0404_szei_rate = models.DecimalField(db_column='TBT0404_SZEI_RATE', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0404_kazei_kbn = models.CharField(db_column='TBT0404_KAZEI_KBN', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0404_nyuka_kbn = models.CharField(db_column='TBT0404_NYUKA_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0404_soko_cd = models.CharField(db_column='TBT0404_SOKO_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0404_location_cd = models.CharField(db_column='TBT0404_LOCATION_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0404_keiyaku_haifu = models.CharField(db_column='TBT0404_KEIYAKU_HAIFU', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0404_keiyaku_haifu_nm = models.CharField(db_column='TBT0404_KEIYAKU_HAIFU_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0404_nouhin_kigen = models.DateTimeField(db_column='TBT0404_NOUHIN_KIGEN', blank=True, null=True)  # Field name made lowercase.
    tbt0404_biko = models.CharField(db_column='TBT0404_BIKO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0404_del_flg = models.CharField(db_column='TBT0404_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0404_crt_datetime = models.DateTimeField(db_column='TBT0404_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0404_crt_user_id = models.CharField(db_column='TBT0404_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0404_crt_prog_nm = models.CharField(db_column='TBT0404_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0404_upd_datetime = models.DateTimeField(db_column='TBT0404_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0404_upd_user_id = models.CharField(db_column='TBT0404_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0404_upd_prog_nm = models.CharField(db_column='TBT0404_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0404_upd_cnt = models.DecimalField(db_column='TBT0404_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0404_bumon_cd = models.CharField(db_column='TBT0404_BUMON_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbt0404_keizoku_kbn_cd = models.CharField(db_column='TBT0404_KEIZOKU_KBN_CD', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0404_SIIRE_DTL'
        unique_together = (('tbt0403_siire_no', 'tbt0403_siire_tei_ed_no', 'tbt0403_siire_tei_kbn', 'tbt0404_siire_dtl_no'),)


class Tbt0405SiireShime(models.Model):
    tbt0405_siire_shime_seq = models.AutoField(db_column='TBT0405_SIIRE_SHIME_SEQ', primary_key=True)  # Field name made lowercase.
    tbt0405_siire_shime_date_from = models.DateTimeField(db_column='TBT0405_SIIRE_SHIME_DATE_FROM', blank=True, null=True)  # Field name made lowercase.
    tbt0405_siire_shime_date_to = models.DateTimeField(db_column='TBT0405_SIIRE_SHIME_DATE_TO', blank=True, null=True)  # Field name made lowercase.
    tbt0405_del_flg = models.CharField(db_column='TBT0405_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0405_crt_datetime = models.DateTimeField(db_column='TBT0405_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0405_crt_user_id = models.CharField(db_column='TBT0405_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0405_crt_prog_nm = models.CharField(db_column='TBT0405_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0405_upd_datetime = models.DateTimeField(db_column='TBT0405_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0405_upd_user_id = models.CharField(db_column='TBT0405_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0405_upd_prog_nm = models.CharField(db_column='TBT0405_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0405_upd_cnt = models.DecimalField(db_column='TBT0405_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0405_SIIRE_SHIME'


class Tbt0406Shiharai(models.Model):
    tbt0406_shiharai_no = models.CharField(db_column='TBT0406_SHIHARAI_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt0406_shiharai_ed_no = models.SmallIntegerField(db_column='TBT0406_SHIHARAI_ED_NO')  # Field name made lowercase.
    tbt0406_shiharai_date = models.DateTimeField(db_column='TBT0406_SHIHARAI_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt0406_kaisha_cd = models.CharField(db_column='TBT0406_KAISHA_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0406_siire_saki_cd = models.CharField(db_column='TBT0406_SIIRE_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbt0406_shiharai_ttl_kingaku = models.DecimalField(db_column='TBT0406_SHIHARAI_TTL_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0406_sousai_ttl_kingaku = models.DecimalField(db_column='TBT0406_SOUSAI_TTL_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0406_furikae_ttl_kingaku = models.DecimalField(db_column='TBT0406_FURIKAE_TTL_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0406_shiharai_keshikomi_ttl_kingaku = models.DecimalField(db_column='TBT0406_SHIHARAI_KESHIKOMI_TTL_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0406_denpyo_tekiyou = models.CharField(db_column='TBT0406_DENPYO_TEKIYOU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0406_del_flg = models.CharField(db_column='TBT0406_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0406_crt_datetime = models.DateTimeField(db_column='TBT0406_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0406_crt_user_id = models.CharField(db_column='TBT0406_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0406_crt_prog_nm = models.CharField(db_column='TBT0406_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0406_upd_datetime = models.DateTimeField(db_column='TBT0406_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0406_upd_user_id = models.CharField(db_column='TBT0406_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0406_upd_prog_nm = models.CharField(db_column='TBT0406_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0406_upd_cnt = models.DecimalField(db_column='TBT0406_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0406_SHIHARAI'
        unique_together = (('tbt0406_shiharai_no', 'tbt0406_shiharai_ed_no'),)


class Tbt0407ShiharaiInfo(models.Model):
    tbt0406_shiharai_no = models.CharField(db_column='TBT0406_SHIHARAI_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt0406_shiharai_ed_no = models.SmallIntegerField(db_column='TBT0406_SHIHARAI_ED_NO')  # Field name made lowercase.
    tbt0407_shiharai_dtl_no = models.SmallIntegerField(db_column='TBT0407_SHIHARAI_DTL_NO')  # Field name made lowercase.
    tbt0407_shiharai_kbn = models.CharField(db_column='TBT0407_SHIHARAI_KBN', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0407_shiharai_kingaku = models.DecimalField(db_column='TBT0407_SHIHARAI_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0407_tegata_date = models.DateTimeField(db_column='TBT0407_TEGATA_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt0407_tegata_no = models.CharField(db_column='TBT0407_TEGATA_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0407_furikae_kingaku = models.DecimalField(db_column='TBT0407_FURIKAE_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0407_kaisha_bank_seq_cd = models.CharField(db_column='TBT0407_KAISHA_BANK_SEQ_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbt0407_siire_saki_bank_seq_cd = models.CharField(db_column='TBT0407_SIIRE_SAKI_BANK_SEQ_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbt0407_biko = models.CharField(db_column='TBT0407_BIKO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0407_del_flg = models.CharField(db_column='TBT0407_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0407_crt_datetime = models.DateTimeField(db_column='TBT0407_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0407_crt_user_id = models.CharField(db_column='TBT0407_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0407_crt_prog_nm = models.CharField(db_column='TBT0407_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0407_upd_datetime = models.DateTimeField(db_column='TBT0407_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0407_upd_user_id = models.CharField(db_column='TBT0407_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0407_upd_prog_nm = models.CharField(db_column='TBT0407_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0407_upd_cnt = models.DecimalField(db_column='TBT0407_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0407_kaisha_cd = models.CharField(db_column='TBT0407_KAISHA_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0407_siire_saki_cd = models.CharField(db_column='TBT0407_SIIRE_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0407_SHIHARAI_INFO'
        unique_together = (('tbt0406_shiharai_no', 'tbt0406_shiharai_ed_no', 'tbt0407_shiharai_dtl_no'),)


class Tbt0408SiireInfo(models.Model):
    tbt0406_shiharai_no = models.CharField(db_column='TBT0406_SHIHARAI_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt0406_shiharai_ed_no = models.SmallIntegerField(db_column='TBT0406_SHIHARAI_ED_NO')  # Field name made lowercase.
    tbt0408_siire_no = models.CharField(db_column='TBT0408_SIIRE_NO', max_length=25)  # Field name made lowercase.
    tbt0408_siire_tei_ed_no = models.SmallIntegerField(db_column='TBT0408_SIIRE_TEI_ED_NO')  # Field name made lowercase.
    tbt0408_siire_tei_kbn = models.CharField(db_column='TBT0408_SIIRE_TEI_KBN', max_length=1)  # Field name made lowercase.
    tbt0408_shiharai_keshikomi_kingaku = models.DecimalField(db_column='TBT0408_SHIHARAI_KESHIKOMI_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0408_del_flg = models.CharField(db_column='TBT0408_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0408_crt_datetime = models.DateTimeField(db_column='TBT0408_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0408_crt_user_id = models.CharField(db_column='TBT0408_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0408_crt_prog_nm = models.CharField(db_column='TBT0408_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0408_upd_datetime = models.DateTimeField(db_column='TBT0408_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0408_upd_user_id = models.CharField(db_column='TBT0408_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0408_upd_prog_nm = models.CharField(db_column='TBT0408_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0408_upd_cnt = models.DecimalField(db_column='TBT0408_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0408_SIIRE_INFO'
        unique_together = (('tbt0406_shiharai_no', 'tbt0406_shiharai_ed_no', 'tbt0408_siire_no', 'tbt0408_siire_tei_ed_no', 'tbt0408_siire_tei_kbn'),)


class Tbt0409SiireShimeCntl(models.Model):
    tbt0409_nendo = models.SmallIntegerField(db_column='TBT0409_NENDO', primary_key=True)  # Field name made lowercase.
    tbt0409_getsudo = models.SmallIntegerField(db_column='TBT0409_GETSUDO')  # Field name made lowercase.
    tbt0409_shime_flg = models.CharField(db_column='TBT0409_SHIME_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0409_del_flg = models.CharField(db_column='TBT0409_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0409_crt_datetime = models.DateTimeField(db_column='TBT0409_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0409_crt_user_id = models.CharField(db_column='TBT0409_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0409_crt_prog_nm = models.CharField(db_column='TBT0409_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0409_upd_datetime = models.DateTimeField(db_column='TBT0409_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0409_upd_user_id = models.CharField(db_column='TBT0409_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0409_upd_prog_nm = models.CharField(db_column='TBT0409_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0409_upd_cnt = models.DecimalField(db_column='TBT0409_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0409_keihi_jin_crt_flg = models.CharField(db_column='TBT0409_KEIHI_JIN_CRT_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0409_SIIRE_SHIME_CNTL'
        unique_together = (('tbt0409_nendo', 'tbt0409_getsudo'),)


class Tbt0501Keihi(models.Model):
    tbt0501_keihi_denpyo_no = models.CharField(db_column='TBT0501_KEIHI_DENPYO_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt0501_tei_ed_no = models.SmallIntegerField(db_column='TBT0501_TEI_ED_NO')  # Field name made lowercase.
    tbt0501_tei_kbn_no = models.CharField(db_column='TBT0501_TEI_KBN_NO', max_length=1)  # Field name made lowercase.
    tbt0501_teisei_saki_no = models.CharField(db_column='TBT0501_TEISEI_SAKI_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0501_teisei_moto_no = models.CharField(db_column='TBT0501_TEISEI_MOTO_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0501_keihi_denpyo_date = models.DateTimeField(db_column='TBT0501_KEIHI_DENPYO_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt0501_denpyo_kbn = models.CharField(db_column='TBT0501_DENPYO_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0501_sosiki_kbn_cd = models.CharField(db_column='TBT0501_SOSIKI_KBN_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0501_keihi_sts = models.CharField(db_column='TBT0501_KEIHI_STS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0501_keihi_sub_sts = models.CharField(db_column='TBT0501_KEIHI_SUB_STS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0501_nendo = models.SmallIntegerField(db_column='TBT0501_NENDO', blank=True, null=True)  # Field name made lowercase.
    tbt0501_bumon_cd = models.CharField(db_column='TBT0501_BUMON_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbt0501_bumon_nm = models.CharField(db_column='TBT0501_BUMON_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0501_genba_cd = models.CharField(db_column='TBT0501_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tbt0501_genba_nm = models.CharField(db_column='TBT0501_GENBA_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbt0501_shoku_cd = models.CharField(db_column='TBT0501_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tbt0501_shoku_nm = models.CharField(db_column='TBT0501_SHOKU_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tbt0501_keihi_tekiyou = models.CharField(db_column='TBT0501_KEIHI_TEKIYOU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0501_del_flg = models.CharField(db_column='TBT0501_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0501_crt_datetime = models.DateTimeField(db_column='TBT0501_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0501_crt_user_id = models.CharField(db_column='TBT0501_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0501_crt_prog_nm = models.CharField(db_column='TBT0501_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0501_upd_datetime = models.DateTimeField(db_column='TBT0501_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0501_upd_user_id = models.CharField(db_column='TBT0501_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0501_upd_prog_nm = models.CharField(db_column='TBT0501_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0501_upd_cnt = models.DecimalField(db_column='TBT0501_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0501_kingaku_komi = models.DecimalField(db_column='TBT0501_KINGAKU_KOMI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0501_szei_kingaku = models.DecimalField(db_column='TBT0501_SZEI_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0501_kingaku_nuki = models.DecimalField(db_column='TBT0501_KINGAKU_NUKI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0501_denpyo_kind = models.CharField(db_column='TBT0501_DENPYO_KIND', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0501_keihi_jin_crt_flg = models.CharField(db_column='TBT0501_KEIHI_JIN_CRT_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0501_KEIHI'
        unique_together = (('tbt0501_keihi_denpyo_no', 'tbt0501_tei_ed_no', 'tbt0501_tei_kbn_no'),)


class Tbt0502KeihiDtl(models.Model):
    tbt0501_keihi_denpyo_no = models.CharField(db_column='TBT0501_KEIHI_DENPYO_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt0501_tei_ed_no = models.SmallIntegerField(db_column='TBT0501_TEI_ED_NO')  # Field name made lowercase.
    tbt0501_tei_kbn_no = models.CharField(db_column='TBT0501_TEI_KBN_NO', max_length=1)  # Field name made lowercase.
    tbt0502_keihi_dtl_no = models.SmallIntegerField(db_column='TBT0502_KEIHI_DTL_NO')  # Field name made lowercase.
    tbt0502_keihi_kbn = models.CharField(db_column='TBT0502_KEIHI_KBN', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt0502_keihi_kbn_nm = models.CharField(db_column='TBT0502_KEIHI_KBN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0502_kingaku_inp = models.CharField(db_column='TBT0502_KINGAKU_INP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0502_kingaku_komi = models.DecimalField(db_column='TBT0502_KINGAKU_KOMI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0502_szei_kingaku = models.DecimalField(db_column='TBT0502_SZEI_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0502_kingaku_nuki = models.DecimalField(db_column='TBT0502_KINGAKU_NUKI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0502_keiyaku_haifu = models.CharField(db_column='TBT0502_KEIYAKU_HAIFU', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt0502_keiyaku_haifu_nm = models.CharField(db_column='TBT0502_KEIYAKU_HAIFU_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0502_bikou = models.CharField(db_column='TBT0502_BIKOU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt0502_del_flg = models.CharField(db_column='TBT0502_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0502_crt_datetime = models.DateTimeField(db_column='TBT0502_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0502_crt_user_id = models.CharField(db_column='TBT0502_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0502_crt_prog_nm = models.CharField(db_column='TBT0502_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0502_upd_datetime = models.DateTimeField(db_column='TBT0502_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0502_upd_user_id = models.CharField(db_column='TBT0502_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0502_upd_prog_nm = models.CharField(db_column='TBT0502_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0502_upd_cnt = models.DecimalField(db_column='TBT0502_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt0502_keihi_jin_crt_flg = models.CharField(db_column='TBT0502_KEIHI_JIN_CRT_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0502_kosu = models.DecimalField(db_column='TBT0502_KOSU', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0502_shoku_cd = models.CharField(db_column='TBT0502_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tbt0502_genba_cd = models.CharField(db_column='TBT0502_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tbt0502_uke_ou_dtl_no = models.SmallIntegerField(db_column='TBT0502_UKE_OU_DTL_NO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0502_KEIHI_DTL'
        unique_together = (('tbt0501_keihi_denpyo_no', 'tbt0501_tei_ed_no', 'tbt0501_tei_kbn_no', 'tbt0502_keihi_dtl_no'),)


class Tbt0601Zaiko(models.Model):
    tbt0601_gyomu_shohin_cd = models.CharField(db_column='TBT0601_GYOMU_SHOHIN_CD', primary_key=True, max_length=12)  # Field name made lowercase.
    tbt0601_soko_cd = models.CharField(db_column='TBT0601_SOKO_CD', max_length=3)  # Field name made lowercase.
    tbt0601_location_cd = models.CharField(db_column='TBT0601_LOCATION_CD', max_length=3)  # Field name made lowercase.
    tbt0601_shuka_yotei_suryo = models.DecimalField(db_column='TBT0601_SHUKA_YOTEI_SURYO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0601_nyuka_yotei_suryo = models.DecimalField(db_column='TBT0601_NYUKA_YOTEI_SURYO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0601_zaiko_suryo = models.DecimalField(db_column='TBT0601_ZAIKO_SURYO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt0601_del_flg = models.CharField(db_column='TBT0601_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt0601_crt_datetime = models.DateTimeField(db_column='TBT0601_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0601_crt_user_id = models.CharField(db_column='TBT0601_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0601_crt_prog_nm = models.CharField(db_column='TBT0601_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0601_upd_datetime = models.DateTimeField(db_column='TBT0601_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt0601_upd_user_id = models.CharField(db_column='TBT0601_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt0601_upd_prog_nm = models.CharField(db_column='TBT0601_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt0601_upd_cnt = models.DecimalField(db_column='TBT0601_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT0601_ZAIKO'
        unique_together = (('tbt0601_gyomu_shohin_cd', 'tbt0601_soko_cd', 'tbt0601_location_cd'),)


class Tbt1000Saiban(models.Model):
    tbt1000_nendo = models.SmallIntegerField(db_column='TBT1000_NENDO', primary_key=True)  # Field name made lowercase.
    tbt1000_kbn_cd = models.CharField(db_column='TBT1000_KBN_CD', max_length=10)  # Field name made lowercase.
    tbt1000_number_cnt = models.IntegerField(db_column='TBT1000_NUMBER_CNT')  # Field name made lowercase.
    tbt1000_upd_cnt = models.DecimalField(db_column='TBT1000_UPD_CNT', max_digits=10, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT1000_SAIBAN'
        unique_together = (('tbt1000_nendo', 'tbt1000_kbn_cd'),)


class Tbt1001YosanNendo(models.Model):
    tbt1001_nendo = models.SmallIntegerField(db_column='TBT1001_NENDO', primary_key=True)  # Field name made lowercase.
    tbt1001_sime_month = models.SmallIntegerField(db_column='TBT1001_SIME_MONTH', blank=True, null=True)  # Field name made lowercase.
    tbt1001_uri_jisk_trkm_flg = models.CharField(db_column='TBT1001_URI_JISK_TRKM_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt1001_sir_jisk_trkm_flg = models.CharField(db_column='TBT1001_SIR_JISK_TRKM_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt1001_kih_jisk_trkm_flg = models.CharField(db_column='TBT1001_KIH_JISK_TRKM_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt1001_del_flg = models.CharField(db_column='TBT1001_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt1001_crt_datetime = models.DateTimeField(db_column='TBT1001_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt1001_crt_user_id = models.CharField(db_column='TBT1001_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt1001_crt_prog_nm = models.CharField(db_column='TBT1001_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt1001_upd_datetime = models.DateTimeField(db_column='TBT1001_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt1001_upd_user_id = models.CharField(db_column='TBT1001_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt1001_upd_prog_nm = models.CharField(db_column='TBT1001_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt1001_upd_cnt = models.DecimalField(db_column='TBT1001_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT1001_YOSAN_NENDO'


class Tbt1002Yosan(models.Model):
    tbt1001_nendo = models.SmallIntegerField(db_column='TBT1001_NENDO', primary_key=True)  # Field name made lowercase.
    tbt1002_yosan_no = models.DecimalField(db_column='TBT1002_YOSAN_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tbt1002_yosan_type = models.CharField(db_column='TBT1002_YOSAN_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tbt1002_lock_flg = models.CharField(db_column='TBT1002_LOCK_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt1002_fusaiyo_flg = models.CharField(db_column='TBT1002_FUSAIYO_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt1002_del_flg = models.CharField(db_column='TBT1002_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt1002_crt_datetime = models.DateTimeField(db_column='TBT1002_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt1002_crt_user_id = models.CharField(db_column='TBT1002_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt1002_crt_prog_nm = models.CharField(db_column='TBT1002_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt1002_upd_datetime = models.DateTimeField(db_column='TBT1002_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt1002_upd_user_id = models.CharField(db_column='TBT1002_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt1002_upd_prog_nm = models.CharField(db_column='TBT1002_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt1002_upd_cnt = models.DecimalField(db_column='TBT1002_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt1002_mikm_getsudo = models.SmallIntegerField(db_column='TBT1002_MIKM_GETSUDO', blank=True, null=True)  # Field name made lowercase.
    tbt1002_syusei_ysn_name = models.CharField(db_column='TBT1002_SYUSEI_YSN_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT1002_YOSAN'
        unique_together = (('tbt1001_nendo', 'tbt1002_yosan_no'),)


class Tbt1003YosanTani(models.Model):
    tbt1001_nendo = models.SmallIntegerField(db_column='TBT1001_NENDO', primary_key=True)  # Field name made lowercase.
    tbt1002_yosan_no = models.DecimalField(db_column='TBT1002_YOSAN_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tbt1003_yosan_dtl_no = models.DecimalField(db_column='TBT1003_YOSAN_DTL_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tbt1003_yosan_tani = models.CharField(db_column='TBT1003_YOSAN_TANI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tbt1003_bumon_cd = models.CharField(db_column='TBT1003_BUMON_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbt1003_genba_cd = models.CharField(db_column='TBT1003_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tbt1003_shoku_cd = models.CharField(db_column='TBT1003_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tbt1003_tokui_saki_cd = models.CharField(db_column='TBT1003_TOKUI_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbt1003_del_flg = models.CharField(db_column='TBT1003_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt1003_crt_datetime = models.DateTimeField(db_column='TBT1003_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt1003_crt_user_id = models.CharField(db_column='TBT1003_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt1003_crt_prog_nm = models.CharField(db_column='TBT1003_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt1003_upd_datetime = models.DateTimeField(db_column='TBT1003_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt1003_upd_user_id = models.CharField(db_column='TBT1003_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt1003_upd_prog_nm = models.CharField(db_column='TBT1003_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt1003_upd_cnt = models.DecimalField(db_column='TBT1003_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt1003_yosan_ptn_cd = models.CharField(db_column='TBT1003_YOSAN_PTN_CD', max_length=15, blank=True, null=True)  # Field name made lowercase.
    tbt1003_keiyaku_no = models.CharField(db_column='TBT1003_KEIYAKU_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt1003_yosan_crt_flg = models.CharField(db_column='TBT1003_YOSAN_CRT_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt1003_yosan_crt_cmp_flg = models.CharField(db_column='TBT1003_YOSAN_CRT_CMP_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt1003_yosan_pro_lock_flg = models.CharField(db_column='TBT1003_YOSAN_PRO_LOCK_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT1003_YOSAN_TANI'
        unique_together = (('tbt1001_nendo', 'tbt1002_yosan_no', 'tbt1003_yosan_dtl_no'),)


class Tbt1004YosanDtl(models.Model):
    tbt1001_nendo = models.SmallIntegerField(db_column='TBT1001_NENDO', primary_key=True)  # Field name made lowercase.
    tbt1002_yosan_no = models.DecimalField(db_column='TBT1002_YOSAN_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tbt1003_yosan_dtl_no = models.DecimalField(db_column='TBT1003_YOSAN_DTL_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tbt1004_yosan_utwk_cd = models.CharField(db_column='TBT1004_YOSAN_UTWK_CD', max_length=10)  # Field name made lowercase.
    tbt1004_del_flg = models.CharField(db_column='TBT1004_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt1004_crt_datetime = models.DateTimeField(db_column='TBT1004_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt1004_crt_user_id = models.CharField(db_column='TBT1004_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt1004_crt_prog_nm = models.CharField(db_column='TBT1004_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt1004_upd_datetime = models.DateTimeField(db_column='TBT1004_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt1004_upd_user_id = models.CharField(db_column='TBT1004_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt1004_upd_prog_nm = models.CharField(db_column='TBT1004_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt1004_upd_cnt = models.DecimalField(db_column='TBT1004_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT1004_YOSAN_DTL'
        unique_together = (('tbt1001_nendo', 'tbt1002_yosan_no', 'tbt1003_yosan_dtl_no', 'tbt1004_yosan_utwk_cd'),)


class Tbt1005YosanGetsudo(models.Model):
    tbt1001_nendo = models.SmallIntegerField(db_column='TBT1001_NENDO', primary_key=True)  # Field name made lowercase.
    tbt1002_yosan_no = models.DecimalField(db_column='TBT1002_YOSAN_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tbt1003_yosan_dtl_no = models.DecimalField(db_column='TBT1003_YOSAN_DTL_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tbt1004_yosan_utwk_cd = models.CharField(db_column='TBT1004_YOSAN_UTWK_CD', max_length=10)  # Field name made lowercase.
    tbt1005_getsudo = models.SmallIntegerField(db_column='TBT1005_GETSUDO')  # Field name made lowercase.
    tbt1005_kingaku = models.DecimalField(db_column='TBT1005_KINGAKU', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt1005_del_flg = models.CharField(db_column='TBT1005_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt1005_crt_datetime = models.DateTimeField(db_column='TBT1005_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt1005_crt_user_id = models.CharField(db_column='TBT1005_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt1005_crt_prog_nm = models.CharField(db_column='TBT1005_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt1005_upd_datetime = models.DateTimeField(db_column='TBT1005_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt1005_upd_user_id = models.CharField(db_column='TBT1005_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt1005_upd_prog_nm = models.CharField(db_column='TBT1005_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt1005_upd_cnt = models.DecimalField(db_column='TBT1005_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT1005_YOSAN_GETSUDO'
        unique_together = (('tbt1001_nendo', 'tbt1002_yosan_no', 'tbt1003_yosan_dtl_no', 'tbt1004_yosan_utwk_cd', 'tbt1005_getsudo'),)


class Tbt9005RrekKeiyaku(models.Model):
    tbt9005_keiyaku_no = models.CharField(db_column='TBT9005_KEIYAKU_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt9005_rrek_no = models.DecimalField(db_column='TBT9005_RREK_NO', max_digits=12, decimal_places=0)  # Field name made lowercase.
    tbt9005_nendo = models.SmallIntegerField(db_column='TBT9005_NENDO', blank=True, null=True)  # Field name made lowercase.
    tbt9005_keiyaku_eda_no = models.IntegerField(db_column='TBT9005_KEIYAKU_EDA_NO', blank=True, null=True)  # Field name made lowercase.
    tbt9005_sub_flg = models.CharField(db_column='TBT9005_SUB_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt9005_keiyaku_name = models.CharField(db_column='TBT9005_KEIYAKU_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt9005_tokui_saki_cd = models.CharField(db_column='TBT9005_TOKUI_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbt9005_genba_cd = models.CharField(db_column='TBT9005_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tbt9005_shoku_cd = models.CharField(db_column='TBT9005_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tbt9005_bumon_cd = models.CharField(db_column='TBT9005_BUMON_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbt9005_tanto_cd = models.CharField(db_column='TBT9005_TANTO_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbt9005_keizoku_kbn_cd = models.CharField(db_column='TBT9005_KEIZOKU_KBN_CD', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt9005_keiyaku_str_ym = models.CharField(db_column='TBT9005_KEIYAKU_STR_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tbt9005_keiyaku_end_ym = models.CharField(db_column='TBT9005_KEIYAKU_END_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tbt9005_str_month = models.SmallIntegerField(db_column='TBT9005_STR_MONTH', blank=True, null=True)  # Field name made lowercase.
    tbt9005_cur_str_ym = models.CharField(db_column='TBT9005_CUR_STR_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tbt9005_cur_end_ym = models.CharField(db_column='TBT9005_CUR_END_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tbt9005_mtmr_sho_no = models.CharField(db_column='TBT9005_MTMR_SHO_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt9005_keiyaku_sho_no = models.CharField(db_column='TBT9005_KEIYAKU_SHO_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tbt9005_henk_oboe_gaki = models.CharField(db_column='TBT9005_HENK_OBOE_GAKI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt9005_memo = models.CharField(db_column='TBT9005_MEMO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt9005_omit_flg = models.BooleanField(db_column='TBT9005_OMIT_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt9005_jyu_kihyo_flg = models.BooleanField(db_column='TBT9005_JYU_KIHYO_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt9005_next_year_copy_flg = models.BooleanField(db_column='TBT9005_NEXT_YEAR_COPY_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt9005_tbt0005_del_flg = models.CharField(db_column='TBT9005_TBT0005_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt9005_tbt0005_crt_datetime = models.DateTimeField(db_column='TBT9005_TBT0005_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt9005_tbt0005_crt_user_id = models.CharField(db_column='TBT9005_TBT0005_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt9005_tbt0005_crt_prog_nm = models.CharField(db_column='TBT9005_TBT0005_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt9005_tbt0005_upd_datetime = models.DateTimeField(db_column='TBT9005_TBT0005_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt9005_tbt0005_upd_user_id = models.CharField(db_column='TBT9005_TBT0005_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt9005_tbt0005_upd_prog_nm = models.CharField(db_column='TBT9005_TBT0005_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt9005_tbt0005_upd_cnt = models.DecimalField(db_column='TBT9005_TBT0005_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt9005_del_flg = models.CharField(db_column='TBT9005_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt9005_henk_riyu = models.CharField(db_column='TBT9005_HENK_RIYU', max_length=150, blank=True, null=True)  # Field name made lowercase.
    tbt9005_henk_date = models.DateTimeField(db_column='TBT9005_HENK_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt9005_crt_datetime = models.DateTimeField(db_column='TBT9005_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt9005_crt_user_id = models.CharField(db_column='TBT9005_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt9005_crt_prog_nm = models.CharField(db_column='TBT9005_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT9005_RREK_KEIYAKU'
        unique_together = (('tbt9005_keiyaku_no', 'tbt9005_rrek_no'),)


class Tbt9006RrekKeiyakuDtl(models.Model):
    tbt9005_keiyaku_no = models.CharField(db_column='TBT9005_KEIYAKU_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt9005_rrek_no = models.DecimalField(db_column='TBT9005_RREK_NO', max_digits=12, decimal_places=0)  # Field name made lowercase.
    tbt9006_keiyaku_dtl_no = models.SmallIntegerField(db_column='TBT9006_KEIYAKU_DTL_NO')  # Field name made lowercase.
    tbt9006_seikyu_saki_cd = models.CharField(db_column='TBT9006_SEIKYU_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tbt9006_title = models.CharField(db_column='TBT9006_TITLE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt9006_tekiyo = models.CharField(db_column='TBT9006_TEKIYO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt9006_memo = models.CharField(db_column='TBT9006_MEMO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt9006_tbt0006_del_flg = models.CharField(db_column='TBT9006_TBT0006_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt9006_tbt0006_crt_datetime = models.DateTimeField(db_column='TBT9006_TBT0006_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt9006_tbt0006_crt_user_id = models.CharField(db_column='TBT9006_TBT0006_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt9006_tbt0006_crt_prog_nm = models.CharField(db_column='TBT9006_TBT0006_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt9006_tbt0006_upd_datetime = models.DateTimeField(db_column='TBT9006_TBT0006_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt9006_tbt0006_upd_user_id = models.CharField(db_column='TBT9006_TBT0006_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt9006_tbt0006_upd_prog_nm = models.CharField(db_column='TBT9006_TBT0006_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt9006_tbt0006_upd_cnt = models.DecimalField(db_column='TBT9006_TBT0006_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt9006_del_flg = models.CharField(db_column='TBT9006_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt9006_crt_datetime = models.DateTimeField(db_column='TBT9006_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt9006_crt_user_id = models.CharField(db_column='TBT9006_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt9006_crt_prog_nm = models.CharField(db_column='TBT9006_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT9006_RREK_KEIYAKU_DTL'
        unique_together = (('tbt9005_keiyaku_no', 'tbt9005_rrek_no', 'tbt9006_keiyaku_dtl_no'),)


class Tbt9007RrekKeiyakuUri(models.Model):
    tbt9005_keiyaku_no = models.CharField(db_column='TBT9005_KEIYAKU_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt9005_rrek_no = models.DecimalField(db_column='TBT9005_RREK_NO', max_digits=12, decimal_places=0)  # Field name made lowercase.
    tbt9006_keiyaku_dtl_no = models.SmallIntegerField(db_column='TBT9006_KEIYAKU_DTL_NO')  # Field name made lowercase.
    tbt9007_uri_no = models.SmallIntegerField(db_column='TBT9007_URI_NO')  # Field name made lowercase.
    tbt9007_gyomu_shohin_cd = models.CharField(db_column='TBT9007_GYOMU_SHOHIN_CD', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt9007_tani_nm = models.CharField(db_column='TBT9007_TANI_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tbt9007_tbt0007_del_flg = models.CharField(db_column='TBT9007_TBT0007_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt9007_tbt0007_crt_datetime = models.DateTimeField(db_column='TBT9007_TBT0007_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt9007_tbt0007_crt_user_id = models.CharField(db_column='TBT9007_TBT0007_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt9007_tbt0007_crt_prog_nm = models.CharField(db_column='TBT9007_TBT0007_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt9007_tbt0007_upd_datetime = models.DateTimeField(db_column='TBT9007_TBT0007_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt9007_tbt0007_upd_user_id = models.CharField(db_column='TBT9007_TBT0007_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt9007_tbt0007_upd_prog_nm = models.CharField(db_column='TBT9007_TBT0007_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt9007_tbt0007_upd_cnt = models.DecimalField(db_column='TBT9007_TBT0007_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt9007_del_flg = models.CharField(db_column='TBT9007_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt9007_crt_datetime = models.DateTimeField(db_column='TBT9007_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt9007_crt_user_id = models.CharField(db_column='TBT9007_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt9007_crt_prog_nm = models.CharField(db_column='TBT9007_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt9007_shuka_kbn = models.CharField(db_column='TBT9007_SHUKA_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt9007_soko_cd = models.CharField(db_column='TBT9007_SOKO_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt9007_location_cd = models.CharField(db_column='TBT9007_LOCATION_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT9007_RREK_KEIYAKU_URI'
        unique_together = (('tbt9005_keiyaku_no', 'tbt9005_rrek_no', 'tbt9006_keiyaku_dtl_no', 'tbt9007_uri_no'),)


class Tbt9008RrekKeiyakuUriDtl(models.Model):
    tbt9005_keiyaku_no = models.CharField(db_column='TBT9005_KEIYAKU_NO', primary_key=True, max_length=25)  # Field name made lowercase.
    tbt9005_rrek_no = models.DecimalField(db_column='TBT9005_RREK_NO', max_digits=12, decimal_places=0)  # Field name made lowercase.
    tbt9006_keiyaku_dtl_no = models.SmallIntegerField(db_column='TBT9006_KEIYAKU_DTL_NO')  # Field name made lowercase.
    tbt9007_uri_no = models.SmallIntegerField(db_column='TBT9007_URI_NO')  # Field name made lowercase.
    tbt9008_getsudo = models.SmallIntegerField(db_column='TBT9008_GETSUDO')  # Field name made lowercase.
    tbt9008_yuko_flg = models.BooleanField(db_column='TBT9008_YUKO_FLG', blank=True, null=True)  # Field name made lowercase.
    tbt9008_uri_date = models.DateTimeField(db_column='TBT9008_URI_DATE', blank=True, null=True)  # Field name made lowercase.
    tbt9008_tanka = models.DecimalField(db_column='TBT9008_TANKA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt9008_suryo = models.DecimalField(db_column='TBT9008_SURYO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt9008_kingaku = models.DecimalField(db_column='TBT9008_KINGAKU', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt9008_kazei_kbn = models.CharField(db_column='TBT9008_KAZEI_KBN', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tbt9008_szei_rate = models.DecimalField(db_column='TBT9008_SZEI_RATE', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tbt9008_uchi_zei = models.DecimalField(db_column='TBT9008_UCHI_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt9008_soto_zei = models.DecimalField(db_column='TBT9008_SOTO_ZEI', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt9008_biko = models.CharField(db_column='TBT9008_BIKO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tbt9008_seikyu_yotei_ym = models.CharField(db_column='TBT9008_SEIKYU_YOTEI_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tbt9008_jyuchu_denpyo_no = models.CharField(db_column='TBT9008_JYUCHU_DENPYO_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tbt9008_tbt0008_del_flg = models.CharField(db_column='TBT9008_TBT0008_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt9008_tbt0008_crt_datetime = models.DateTimeField(db_column='TBT9008_TBT0008_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt9008_tbt0008_crt_user_id = models.CharField(db_column='TBT9008_TBT0008_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt9008_tbt0008_crt_prog_nm = models.CharField(db_column='TBT9008_TBT0008_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt9008_tbt0008_upd_datetime = models.DateTimeField(db_column='TBT9008_TBT0008_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt9008_tbt0008_upd_user_id = models.CharField(db_column='TBT9008_TBT0008_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt9008_tbt0008_upd_prog_nm = models.CharField(db_column='TBT9008_TBT0008_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tbt9008_tbt0008_upd_cnt = models.DecimalField(db_column='TBT9008_TBT0008_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tbt9008_del_flg = models.CharField(db_column='TBT9008_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbt9008_crt_datetime = models.DateTimeField(db_column='TBT9008_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tbt9008_crt_user_id = models.CharField(db_column='TBT9008_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tbt9008_crt_prog_nm = models.CharField(db_column='TBT9008_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBT9008_RREK_KEIYAKU_URI_DTL'
        unique_together = (('tbt9005_keiyaku_no', 'tbt9005_rrek_no', 'tbt9006_keiyaku_dtl_no', 'tbt9007_uri_no', 'tbt9008_getsudo'),)


class Tbw0001SdtWork(models.Model):
    tbw0001_session_id = models.CharField(db_column='TBW0001_SESSION_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    tbw0001_app_id = models.CharField(db_column='TBW0001_APP_ID', max_length=20)  # Field name made lowercase.
    tbw0001_datetime = models.DateTimeField(db_column='TBW0001_DATETIME')  # Field name made lowercase.
    tbw0001_sdt_01 = models.TextField(db_column='TBW0001_SDT_01', blank=True, null=True)  # Field name made lowercase.
    tbw0001_sdt_02 = models.TextField(db_column='TBW0001_SDT_02', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBW0001_SDT_WORK'
        unique_together = (('tbw0001_session_id', 'tbw0001_app_id', 'tbw0001_datetime'),)


class Tcm0001SchoolKbn(models.Model):
    tcm0001_school_kbn_cd = models.CharField(db_column='TCM0001_SCHOOL_KBN_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0001_school_kbn_nm = models.CharField(db_column='TCM0001_SCHOOL_KBN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0001_del_flg = models.CharField(db_column='TCM0001_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0001_crt_datetime = models.DateTimeField(db_column='TCM0001_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0001_crt_user_id = models.CharField(db_column='TCM0001_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0001_crt_prog_nm = models.CharField(db_column='TCM0001_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0001_upd_datetime = models.DateTimeField(db_column='TCM0001_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0001_upd_user_id = models.CharField(db_column='TCM0001_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0001_upd_prog_nm = models.CharField(db_column='TCM0001_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0001_upd_cnt = models.DecimalField(db_column='TCM0001_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0001_SCHOOL_KBN'


class Tcm0002KenshuuName(models.Model):
    tcm0002_kenshuu_cd = models.CharField(db_column='TCM0002_KENSHUU_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0002_kenshuu_nm = models.CharField(db_column='TCM0002_KENSHUU_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0002_del_flg = models.CharField(db_column='TCM0002_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0002_crt_datetime = models.DateTimeField(db_column='TCM0002_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0002_crt_user_id = models.CharField(db_column='TCM0002_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0002_crt_prog_nm = models.CharField(db_column='TCM0002_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0002_upd_datetime = models.DateTimeField(db_column='TCM0002_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0002_upd_user_id = models.CharField(db_column='TCM0002_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0002_upd_prog_nm = models.CharField(db_column='TCM0002_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0002_upd_cnt = models.DecimalField(db_column='TCM0002_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0002_KENSHUU_NAME'


class Tcm0004Kokuseki(models.Model):
    tcm0004_kokuseki_cd = models.CharField(db_column='TCM0004_KOKUSEKI_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0004_kokuseki_nm = models.CharField(db_column='TCM0004_KOKUSEKI_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0004_del_flg = models.CharField(db_column='TCM0004_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0004_crt_datetime = models.DateTimeField(db_column='TCM0004_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0004_crt_user_id = models.CharField(db_column='TCM0004_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0004_crt_prog_nm = models.CharField(db_column='TCM0004_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0004_upd_datetime = models.DateTimeField(db_column='TCM0004_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0004_upd_user_id = models.CharField(db_column='TCM0004_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0004_upd_prog_nm = models.CharField(db_column='TCM0004_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0004_upd_cnt = models.DecimalField(db_column='TCM0004_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0004_KOKUSEKI'


class Tcm0005SaiyoKeitai(models.Model):
    tcm0005_saiyo_keitai_cd = models.CharField(db_column='TCM0005_SAIYO_KEITAI_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0005_saiyo_keitai_nm = models.CharField(db_column='TCM0005_SAIYO_KEITAI_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0005_del_flg = models.CharField(db_column='TCM0005_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0005_crt_datetime = models.DateTimeField(db_column='TCM0005_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0005_crt_user_id = models.CharField(db_column='TCM0005_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0005_crt_prog_nm = models.CharField(db_column='TCM0005_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0005_upd_datetime = models.DateTimeField(db_column='TCM0005_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0005_upd_user_id = models.CharField(db_column='TCM0005_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0005_upd_prog_nm = models.CharField(db_column='TCM0005_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0005_upd_cnt = models.DecimalField(db_column='TCM0005_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0005_SAIYO_KEITAI'


class Tcm0006Bunrui(models.Model):
    tcm0006_bunrui_cd = models.CharField(db_column='TCM0006_BUNRUI_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0006_bunrui_nm = models.CharField(db_column='TCM0006_BUNRUI_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0006_del_flg = models.CharField(db_column='TCM0006_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0006_crt_datetime = models.DateTimeField(db_column='TCM0006_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0006_crt_user_id = models.CharField(db_column='TCM0006_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0006_crt_prog_nm = models.CharField(db_column='TCM0006_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0006_upd_datetime = models.DateTimeField(db_column='TCM0006_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0006_upd_user_id = models.CharField(db_column='TCM0006_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0006_upd_prog_nm = models.CharField(db_column='TCM0006_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0006_upd_cnt = models.DecimalField(db_column='TCM0006_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0006_BUNRUI'


class Tcm0010MenkyoShikaku(models.Model):
    tcm0010_menkyo_shikaku_cd = models.CharField(db_column='TCM0010_MENKYO_SHIKAKU_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0010_menkyo_shikaku_nm = models.CharField(db_column='TCM0010_MENKYO_SHIKAKU_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0010_del_flg = models.CharField(db_column='TCM0010_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0010_crt_datetime = models.DateTimeField(db_column='TCM0010_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0010_crt_user_id = models.CharField(db_column='TCM0010_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0010_crt_prog_nm = models.CharField(db_column='TCM0010_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0010_upd_datetime = models.DateTimeField(db_column='TCM0010_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0010_upd_user_id = models.CharField(db_column='TCM0010_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0010_upd_prog_nm = models.CharField(db_column='TCM0010_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0010_upd_cnt = models.DecimalField(db_column='TCM0010_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0010_MENKYO_SHIKAKU'


class Tcm0011Yakushoku(models.Model):
    tcm0011_yakushoku_cd = models.CharField(db_column='TCM0011_YAKUSHOKU_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0011_yakushoku_nm = models.CharField(db_column='TCM0011_YAKUSHOKU_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0011_del_flg = models.CharField(db_column='TCM0011_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0011_crt_datetime = models.DateTimeField(db_column='TCM0011_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0011_crt_user_id = models.CharField(db_column='TCM0011_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0011_crt_prog_nm = models.CharField(db_column='TCM0011_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0011_upd_datetime = models.DateTimeField(db_column='TCM0011_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0011_upd_user_id = models.CharField(db_column='TCM0011_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0011_upd_prog_nm = models.CharField(db_column='TCM0011_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0011_upd_cnt = models.DecimalField(db_column='TCM0011_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0011_YAKUSHOKU'


class Tcm0012KoukaKekka(models.Model):
    tcm0012_kouka_kekka_cd = models.CharField(db_column='TCM0012_KOUKA_KEKKA_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0012_kouka_kekka_nm = models.CharField(db_column='TCM0012_KOUKA_KEKKA_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0012_del_flg = models.CharField(db_column='TCM0012_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0012_crt_datetime = models.DateTimeField(db_column='TCM0012_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0012_crt_user_id = models.CharField(db_column='TCM0012_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0012_crt_prog_nm = models.CharField(db_column='TCM0012_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0012_upd_datetime = models.DateTimeField(db_column='TCM0012_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0012_upd_user_id = models.CharField(db_column='TCM0012_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0012_upd_prog_nm = models.CharField(db_column='TCM0012_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0012_upd_cnt = models.DecimalField(db_column='TCM0012_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0012_KOUKA_KEKKA'


class Tcm0013KoukaShubetsu(models.Model):
    tcm0013_kouka_shubetsu_cd = models.CharField(db_column='TCM0013_KOUKA_SHUBETSU_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0013_kouka_shubetsu_nm = models.CharField(db_column='TCM0013_KOUKA_SHUBETSU_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0013_del_flg = models.CharField(db_column='TCM0013_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0013_crt_datetime = models.DateTimeField(db_column='TCM0013_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0013_crt_user_id = models.CharField(db_column='TCM0013_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0013_crt_prog_nm = models.CharField(db_column='TCM0013_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0013_upd_datetime = models.DateTimeField(db_column='TCM0013_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0013_upd_user_id = models.CharField(db_column='TCM0013_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0013_upd_prog_nm = models.CharField(db_column='TCM0013_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0013_upd_cnt = models.DecimalField(db_column='TCM0013_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0013_KOUKA_SHUBETSU'


class Tcm0014SotsuTaishokuKbn(models.Model):
    tcm0014_sotsu_taishoku_kbn_cd = models.CharField(db_column='TCM0014_SOTSU_TAISHOKU_KBN_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0014_sotsu_taishoku_kbn_nm = models.CharField(db_column='TCM0014_SOTSU_TAISHOKU_KBN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0014_del_flg = models.CharField(db_column='TCM0014_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0014_crt_datetime = models.DateTimeField(db_column='TCM0014_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0014_crt_user_id = models.CharField(db_column='TCM0014_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0014_crt_prog_nm = models.CharField(db_column='TCM0014_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0014_upd_datetime = models.DateTimeField(db_column='TCM0014_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0014_upd_user_id = models.CharField(db_column='TCM0014_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0014_upd_prog_nm = models.CharField(db_column='TCM0014_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0014_upd_cnt = models.DecimalField(db_column='TCM0014_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0014_SOTSU_TAISHOKU_KBN'


class Tcm0015ZaisekiKbn(models.Model):
    tcm0015_zaiseki_kbn_cd = models.CharField(db_column='TCM0015_ZAISEKI_KBN_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0015_zaiseki_kbn_nm = models.CharField(db_column='TCM0015_ZAISEKI_KBN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0015_del_flg = models.CharField(db_column='TCM0015_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0015_crt_datetime = models.DateTimeField(db_column='TCM0015_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0015_crt_user_id = models.CharField(db_column='TCM0015_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0015_crt_prog_nm = models.CharField(db_column='TCM0015_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0015_upd_datetime = models.DateTimeField(db_column='TCM0015_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0015_upd_user_id = models.CharField(db_column='TCM0015_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0015_upd_prog_nm = models.CharField(db_column='TCM0015_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0015_upd_cnt = models.DecimalField(db_column='TCM0015_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tcm0015_kyusyoku_flg = models.CharField(db_column='TCM0015_KYUSYOKU_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0015_ZAISEKI_KBN'


class Tcm0018Zokugara(models.Model):
    tcm0018_zokugara_cd = models.CharField(db_column='TCM0018_ZOKUGARA_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0018_zokugara_nm = models.CharField(db_column='TCM0018_ZOKUGARA_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0018_del_flg = models.CharField(db_column='TCM0018_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0018_crt_datetime = models.DateTimeField(db_column='TCM0018_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0018_crt_user_id = models.CharField(db_column='TCM0018_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0018_crt_prog_nm = models.CharField(db_column='TCM0018_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0018_upd_datetime = models.DateTimeField(db_column='TCM0018_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0018_upd_user_id = models.CharField(db_column='TCM0018_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0018_upd_prog_nm = models.CharField(db_column='TCM0018_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0018_upd_cnt = models.DecimalField(db_column='TCM0018_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0018_ZOKUGARA'


class Tcm0019KsKbn(models.Model):
    tcm0019_ks_kbn_cd = models.CharField(db_column='TCM0019_KS_KBN_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0019_ks_kbn_nm = models.CharField(db_column='TCM0019_KS_KBN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0019_del_flg = models.CharField(db_column='TCM0019_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0019_crt_datetime = models.DateTimeField(db_column='TCM0019_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0019_crt_user_id = models.CharField(db_column='TCM0019_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0019_crt_prog_nm = models.CharField(db_column='TCM0019_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0019_upd_datetime = models.DateTimeField(db_column='TCM0019_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0019_upd_user_id = models.CharField(db_column='TCM0019_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0019_upd_prog_nm = models.CharField(db_column='TCM0019_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0019_upd_cnt = models.DecimalField(db_column='TCM0019_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0019_KS_KBN'


class Tcm0020KsKekka(models.Model):
    tcm0020_ks_kekka_cd = models.CharField(db_column='TCM0020_KS_KEKKA_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0020_ks_kekka_nm = models.CharField(db_column='TCM0020_KS_KEKKA_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0020_del_flg = models.CharField(db_column='TCM0020_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0020_crt_datetime = models.DateTimeField(db_column='TCM0020_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0020_crt_user_id = models.CharField(db_column='TCM0020_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0020_crt_prog_nm = models.CharField(db_column='TCM0020_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0020_upd_datetime = models.DateTimeField(db_column='TCM0020_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0020_upd_user_id = models.CharField(db_column='TCM0020_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0020_upd_prog_nm = models.CharField(db_column='TCM0020_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0020_upd_cnt = models.DecimalField(db_column='TCM0020_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0020_KS_KEKKA'


class Tcm0021RenrakuSakiKbn(models.Model):
    tcm0021_renraku_saki_kbn_cd = models.CharField(db_column='TCM0021_RENRAKU_SAKI_KBN_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0021_renraku_saki_kbn_nm = models.CharField(db_column='TCM0021_RENRAKU_SAKI_KBN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0021_del_flg = models.CharField(db_column='TCM0021_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0021_crt_datetime = models.DateTimeField(db_column='TCM0021_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0021_crt_user_id = models.CharField(db_column='TCM0021_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0021_crt_prog_nm = models.CharField(db_column='TCM0021_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0021_upd_datetime = models.DateTimeField(db_column='TCM0021_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0021_upd_user_id = models.CharField(db_column='TCM0021_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0021_upd_prog_nm = models.CharField(db_column='TCM0021_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0021_upd_cnt = models.DecimalField(db_column='TCM0021_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0021_RENRAKU_SAKI_KBN'


class Tcm0028ShouninKbn(models.Model):
    tcm0028_shounin_kbn_cd = models.CharField(db_column='TCM0028_SHOUNIN_KBN_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0028_shounin_kbn_nm = models.CharField(db_column='TCM0028_SHOUNIN_KBN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0028_del_flg = models.CharField(db_column='TCM0028_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0028_crt_datetime = models.DateTimeField(db_column='TCM0028_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0028_crt_user_id = models.CharField(db_column='TCM0028_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0028_crt_prog_nm = models.CharField(db_column='TCM0028_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0028_upd_datetime = models.DateTimeField(db_column='TCM0028_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0028_upd_user_id = models.CharField(db_column='TCM0028_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0028_upd_prog_nm = models.CharField(db_column='TCM0028_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0028_upd_cnt = models.DecimalField(db_column='TCM0028_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0028_SHOUNIN_KBN'


class Tcm0031ShukkinKyukaKbn(models.Model):
    tcm0031_shukkin_kyuka_id = models.CharField(db_column='TCM0031_SHUKKIN_KYUKA_ID', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0031_shukkin_kyuka_nm = models.CharField(db_column='TCM0031_SHUKKIN_KYUKA_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0031_del_flg = models.CharField(db_column='TCM0031_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0031_crt_datetime = models.DateTimeField(db_column='TCM0031_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0031_crt_user_id = models.CharField(db_column='TCM0031_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0031_crt_prog_nm = models.CharField(db_column='TCM0031_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0031_upd_datetime = models.DateTimeField(db_column='TCM0031_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0031_upd_user_id = models.CharField(db_column='TCM0031_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0031_upd_prog_nm = models.CharField(db_column='TCM0031_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0031_upd_cnt = models.DecimalField(db_column='TCM0031_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tcm0031_yukyu_flg = models.CharField(db_column='TCM0031_YUKYU_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0031_gengaku_flg = models.CharField(db_column='TCM0031_GENGAKU_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0031_shukkin_flg = models.CharField(db_column='TCM0031_SHUKKIN_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0031_kyushutu_flg = models.CharField(db_column='TCM0031_KYUSHUTU_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0031_houkyushutu_flg = models.CharField(db_column='TCM0031_HOUKYUSHUTU_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0031_kyuka_flg = models.CharField(db_column='TCM0031_KYUKA_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0031_ketsujikan_flg = models.CharField(db_column='TCM0031_KETSUJIKAN_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0031_zangyou_flg = models.CharField(db_column='TCM0031_ZANGYOU_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0031_shinya_zangyou_flg = models.CharField(db_column='TCM0031_SHINYA_ZANGYOU_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0031_yobi_flg = models.CharField(db_column='TCM0031_YOBI_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0031_shukkin_kyuka_nm_r = models.CharField(db_column='TCM0031_SHUKKIN_KYUKA_NM_R', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tcm0031_shinsei_kbn = models.CharField(db_column='TCM0031_SHINSEI_KBN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tcm0031_uq_skn_on_flg = models.CharField(db_column='TCM0031_UQ_SKN_ON_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0031_disp_order = models.SmallIntegerField(db_column='TCM0031_DISP_ORDER', blank=True, null=True)  # Field name made lowercase.
    tcm0031_set_time_flg = models.CharField(db_column='TCM0031_SET_TIME_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0031_tokkyu_yukyu_flg = models.CharField(db_column='TCM0031_TOKKYU_YUKYU_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0031_tokkyu_mukyu_flg = models.CharField(db_column='TCM0031_TOKKYU_MUKYU_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0031_SHUKKIN_KYUKA_KBN'


class Tcm0033ZairyuShikakuKbn(models.Model):
    tcm0033_zairyu_shikaku_kbn_cd = models.CharField(db_column='TCM0033_ZAIRYU_SHIKAKU_KBN_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0033_zairyu_shikaku_kbn_nm = models.CharField(db_column='TCM0033_ZAIRYU_SHIKAKU_KBN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0033_del_flg = models.CharField(db_column='TCM0033_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0033_crt_datetime = models.DateTimeField(db_column='TCM0033_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0033_crt_user_id = models.CharField(db_column='TCM0033_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0033_crt_prog_nm = models.CharField(db_column='TCM0033_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0033_upd_datetime = models.DateTimeField(db_column='TCM0033_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0033_upd_user_id = models.CharField(db_column='TCM0033_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0033_upd_prog_nm = models.CharField(db_column='TCM0033_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0033_upd_cnt = models.DecimalField(db_column='TCM0033_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0033_ZAIRYU_SHIKAKU_KBN'


class Tcm0034IdouRirekiKbn(models.Model):
    tcm0034_idou_rireki_kbn_cd = models.CharField(db_column='TCM0034_IDOU_RIREKI_KBN_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0034_idou_rireki_kbn_nm = models.CharField(db_column='TCM0034_IDOU_RIREKI_KBN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0034_del_flg = models.CharField(db_column='TCM0034_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0034_crt_datetime = models.DateTimeField(db_column='TCM0034_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0034_crt_user_id = models.CharField(db_column='TCM0034_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0034_crt_prog_nm = models.CharField(db_column='TCM0034_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0034_upd_datetime = models.DateTimeField(db_column='TCM0034_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0034_upd_user_id = models.CharField(db_column='TCM0034_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0034_upd_prog_nm = models.CharField(db_column='TCM0034_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0034_upd_cnt = models.DecimalField(db_column='TCM0034_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0034_IDOU_RIREKI_KBN'


class Tcm0037KenshuKekkaKbn(models.Model):
    tcm0037_kenshu_kekka_cd = models.CharField(db_column='TCM0037_KENSHU_KEKKA_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0037_kenshu_kekka_nm = models.CharField(db_column='TCM0037_KENSHU_KEKKA_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0037_del_flg = models.CharField(db_column='TCM0037_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0037_crt_datetime = models.DateTimeField(db_column='TCM0037_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0037_crt_user_id = models.CharField(db_column='TCM0037_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0037_crt_prog_nm = models.CharField(db_column='TCM0037_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0037_upd_datetime = models.DateTimeField(db_column='TCM0037_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0037_upd_user_id = models.CharField(db_column='TCM0037_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0037_upd_prog_nm = models.CharField(db_column='TCM0037_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0037_upd_cnt = models.DecimalField(db_column='TCM0037_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0037_KENSHU_KEKKA_KBN'


class Tcm0038KenshuSankaKbn(models.Model):
    tcm0038_kenshu_sanka_kbn_cd = models.CharField(db_column='TCM0038_KENSHU_SANKA_KBN_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0038_kenshu_sanka_kbn_nm = models.CharField(db_column='TCM0038_KENSHU_SANKA_KBN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0038_del_flg = models.CharField(db_column='TCM0038_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0038_crt_datetime = models.DateTimeField(db_column='TCM0038_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0038_crt_user_id = models.CharField(db_column='TCM0038_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0038_crt_prog_nm = models.CharField(db_column='TCM0038_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0038_upd_datetime = models.DateTimeField(db_column='TCM0038_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0038_upd_user_id = models.CharField(db_column='TCM0038_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0038_upd_prog_nm = models.CharField(db_column='TCM0038_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0038_upd_cnt = models.DecimalField(db_column='TCM0038_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0038_KENSHU_SANKA_KBN'


class Tcm0039ShiftCode(models.Model):
    tcm0039_shift_pkey = models.AutoField(db_column='TCM0039_SHIFT_PKEY', primary_key=True)  # Field name made lowercase.
    tcm0039_genba_cd = models.CharField(db_column='TCM0039_GENBA_CD', max_length=5)  # Field name made lowercase.
    tcm0039_shoku_cd = models.CharField(db_column='TCM0039_SHOKU_CD', max_length=2)  # Field name made lowercase.
    tcm0039_shift_code = models.CharField(db_column='TCM0039_SHIFT_CODE', max_length=11)  # Field name made lowercase.
    tcm0039_start_time = models.IntegerField(db_column='TCM0039_START_TIME', blank=True, null=True)  # Field name made lowercase.
    tcm0039_end_time = models.IntegerField(db_column='TCM0039_END_TIME', blank=True, null=True)  # Field name made lowercase.
    tcm0039_break_time = models.DecimalField(db_column='TCM0039_BREAK_TIME', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tcm0039_kosu_time = models.DecimalField(db_column='TCM0039_KOSU_TIME', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tcm0039_shubetsu = models.CharField(db_column='TCM0039_SHUBETSU', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tcm0039_bikou = models.CharField(db_column='TCM0039_BIKOU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tcm0039_del_flg = models.CharField(db_column='TCM0039_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0039_crt_datetime = models.DateTimeField(db_column='TCM0039_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0039_crt_user_id = models.CharField(db_column='TCM0039_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0039_crt_prog_nm = models.CharField(db_column='TCM0039_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0039_upd_datetime = models.DateTimeField(db_column='TCM0039_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0039_upd_user_id = models.CharField(db_column='TCM0039_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0039_upd_prog_nm = models.CharField(db_column='TCM0039_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0039_upd_cnt = models.DecimalField(db_column='TCM0039_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tcm0039_break_time_shinya = models.DecimalField(db_column='TCM0039_BREAK_TIME_SHINYA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0039_SHIFT_CODE'


class Tcm0040DakokuShubetsu(models.Model):
    tcm0040_dakoku_cd = models.CharField(db_column='TCM0040_DAKOKU_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0040_dakoku_nm = models.CharField(db_column='TCM0040_DAKOKU_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0040_del_flg = models.CharField(db_column='TCM0040_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0040_crt_datetime = models.DateTimeField(db_column='TCM0040_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0040_crt_user_id = models.CharField(db_column='TCM0040_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0040_crt_prog_nm = models.CharField(db_column='TCM0040_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0040_upd_datetime = models.DateTimeField(db_column='TCM0040_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0040_upd_user_id = models.CharField(db_column='TCM0040_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0040_upd_prog_nm = models.CharField(db_column='TCM0040_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0040_upd_cnt = models.DecimalField(db_column='TCM0040_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0040_DAKOKU_SHUBETSU'


class Tcm0041SgSystem(models.Model):
    tcm0041_sg_sys_cd = models.CharField(db_column='TCM0041_SG_SYS_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0041_sg_sys_nm = models.CharField(db_column='TCM0041_SG_SYS_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0041_sg_sys_value = models.CharField(db_column='TCM0041_SG_SYS_VALUE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tcm0041_del_flg = models.CharField(db_column='TCM0041_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0041_crt_datetime = models.DateTimeField(db_column='TCM0041_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0041_crt_user_id = models.CharField(db_column='TCM0041_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0041_crt_prog_nm = models.CharField(db_column='TCM0041_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0041_upd_datetime = models.DateTimeField(db_column='TCM0041_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0041_upd_user_id = models.CharField(db_column='TCM0041_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0041_upd_prog_nm = models.CharField(db_column='TCM0041_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0041_upd_cnt = models.DecimalField(db_column='TCM0041_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0041_SG_SYSTEM'


class Tcm0042GetsujiProc(models.Model):
    tcm0042_process_seq_no = models.SmallIntegerField(db_column='TCM0042_PROCESS_SEQ_NO', primary_key=True)  # Field name made lowercase.
    tcm0042_app_id = models.CharField(db_column='TCM0042_APP_ID', max_length=9, blank=True, null=True)  # Field name made lowercase.
    tcm0042_yukou_flg = models.CharField(db_column='TCM0042_YUKOU_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0042_del_flg = models.CharField(db_column='TCM0042_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0042_crt_datetime = models.DateTimeField(db_column='TCM0042_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0042_crt_user_id = models.CharField(db_column='TCM0042_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0042_crt_prog_nm = models.CharField(db_column='TCM0042_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0042_upd_datetime = models.DateTimeField(db_column='TCM0042_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0042_upd_user_id = models.CharField(db_column='TCM0042_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0042_upd_prog_nm = models.CharField(db_column='TCM0042_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0042_upd_cnt = models.DecimalField(db_column='TCM0042_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0042_GETSUJI_PROC'


class Tcm0043OuboShouninUser(models.Model):
    tcm0043_shain_cd = models.CharField(db_column='TCM0043_SHAIN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tcm0043_oubo_shounin_kind = models.CharField(db_column='TCM0043_OUBO_SHOUNIN_KIND', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0043_del_flg = models.CharField(db_column='TCM0043_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0043_crt_datetime = models.DateTimeField(db_column='TCM0043_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0043_crt_user_id = models.CharField(db_column='TCM0043_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0043_crt_prog_nm = models.CharField(db_column='TCM0043_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0043_upd_datetime = models.DateTimeField(db_column='TCM0043_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0043_upd_user_id = models.CharField(db_column='TCM0043_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0043_upd_prog_nm = models.CharField(db_column='TCM0043_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0043_upd_cnt = models.DecimalField(db_column='TCM0043_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0043_OUBO_SHOUNIN_USER'


class Tcm0044CommonSetting(models.Model):
    tcm0044_cm_sys_cd = models.CharField(db_column='TCM0044_CM_SYS_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0044_item_nm = models.CharField(db_column='TCM0044_ITEM_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0044_item_value = models.CharField(db_column='TCM0044_ITEM_VALUE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tcm0044_del_flg = models.CharField(db_column='TCM0044_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0044_crt_datetime = models.DateTimeField(db_column='TCM0044_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0044_crt_user_id = models.CharField(db_column='TCM0044_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0044_crt_prog_nm = models.CharField(db_column='TCM0044_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0044_upd_datetime = models.DateTimeField(db_column='TCM0044_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0044_upd_user_id = models.CharField(db_column='TCM0044_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0044_upd_prog_nm = models.CharField(db_column='TCM0044_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0044_upd_cnt = models.DecimalField(db_column='TCM0044_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0044_COMMON_SETTING'


class Tcm0045Teate(models.Model):
    tcm0045_teate_cd = models.CharField(db_column='TCM0045_TEATE_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0045_teate_nm = models.CharField(db_column='TCM0045_TEATE_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0045_teate_kgk = models.DecimalField(db_column='TCM0045_TEATE_KGK', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tcm0045_del_flg = models.CharField(db_column='TCM0045_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0045_crt_datetime = models.DateTimeField(db_column='TCM0045_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0045_crt_user_id = models.CharField(db_column='TCM0045_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0045_crt_prog_nm = models.CharField(db_column='TCM0045_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0045_upd_datetime = models.DateTimeField(db_column='TCM0045_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0045_upd_user_id = models.CharField(db_column='TCM0045_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0045_upd_prog_nm = models.CharField(db_column='TCM0045_UPD_PROG_NM', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0045_upd_cnt = models.DecimalField(db_column='TCM0045_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0045_TEATE'


class Tcm0046UqSystem(models.Model):
    tcm0046_uq_sys_cd = models.CharField(db_column='TCM0046_UQ_SYS_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tcm0046_uq_sys_nm = models.CharField(db_column='TCM0046_UQ_SYS_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0046_uq_sys_value = models.CharField(db_column='TCM0046_UQ_SYS_VALUE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tcm0046_del_flg = models.CharField(db_column='TCM0046_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0046_crt_datetime = models.DateTimeField(db_column='TCM0046_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0046_crt_user_id = models.CharField(db_column='TCM0046_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0046_crt_prog_nm = models.CharField(db_column='TCM0046_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0046_upd_datetime = models.DateTimeField(db_column='TCM0046_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0046_upd_user_id = models.CharField(db_column='TCM0046_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0046_upd_prog_nm = models.CharField(db_column='TCM0046_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0046_upd_cnt = models.DecimalField(db_column='TCM0046_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0046_UQ_SYSTEM'


class Tcm0047ShinseiKbn(models.Model):
    tcm0047_shinsei_kbn = models.CharField(db_column='TCM0047_SHINSEI_KBN', primary_key=True, max_length=2)  # Field name made lowercase.
    tcm0047_shinsei_kbn_nm = models.CharField(db_column='TCM0047_SHINSEI_KBN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0047_del_flg = models.CharField(db_column='TCM0047_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0047_crt_datetime = models.DateTimeField(db_column='TCM0047_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0047_crt_user_id = models.CharField(db_column='TCM0047_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0047_crt_prog_nm = models.CharField(db_column='TCM0047_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0047_upd_datetime = models.DateTimeField(db_column='TCM0047_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0047_upd_user_id = models.CharField(db_column='TCM0047_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0047_upd_prog_nm = models.CharField(db_column='TCM0047_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0047_upd_cnt = models.DecimalField(db_column='TCM0047_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0047_SHINSEI_KBN'


class Tcm0048JinjiTabCtl(models.Model):
    tcm0048_sys_id = models.CharField(db_column='TCM0048_SYS_ID', primary_key=True, max_length=2)  # Field name made lowercase.
    tcm0048_kihon_tab = models.CharField(db_column='TCM0048_KIHON_TAB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0048_koyou_tab = models.CharField(db_column='TCM0048_KOYOU_TAB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0048_gakusyoku_tab = models.CharField(db_column='TCM0048_GAKUSYOKU_TAB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0048_hosyo_tab = models.CharField(db_column='TCM0048_HOSYO_TAB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0048_shikaku_tab = models.CharField(db_column='TCM0048_SHIKAKU_TAB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0048_kensyu_tab = models.CharField(db_column='TCM0048_KENSYU_TAB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0048_ido_tab = models.CharField(db_column='TCM0048_IDO_TAB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0048_shobatu = models.CharField(db_column='TCM0048_SHOBATU', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0048_kenko_tab = models.CharField(db_column='TCM0048_KENKO_TAB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0048_kouka_tab = models.CharField(db_column='TCM0048_KOUKA_TAB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0048_taishaku_tab = models.CharField(db_column='TCM0048_TAISHAKU_TAB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0048_gkj_tab = models.CharField(db_column='TCM0048_GKJ_TAB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0048_del_flg = models.CharField(db_column='TCM0048_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0048_crt_datetime = models.DateTimeField(db_column='TCM0048_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0048_crt_user_id = models.CharField(db_column='TCM0048_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0048_crt_prog_nm = models.CharField(db_column='TCM0048_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0048_upd_datetime = models.DateTimeField(db_column='TCM0048_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tcm0048_upd_user_id = models.CharField(db_column='TCM0048_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tcm0048_upd_prog_nm = models.CharField(db_column='TCM0048_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tcm0048_upd_cnt = models.DecimalField(db_column='TCM0048_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tcm0048_kyusyoku_tab = models.CharField(db_column='TCM0048_KYUSYOKU_TAB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tcm0048_shain_syokai_tab = models.CharField(db_column='TCM0048_SHAIN_SYOKAI_TAB', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCM0048_JINJI_TAB_CTL'


class Tct0001JobShiji(models.Model):
    tct0001_nendo = models.SmallIntegerField(db_column='TCT0001_NENDO', primary_key=True)  # Field name made lowercase.
    tct0001_getsudo = models.SmallIntegerField(db_column='TCT0001_GETSUDO')  # Field name made lowercase.
    tct0001_kakutei_flg = models.CharField(db_column='TCT0001_KAKUTEI_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tct0001_del_flg = models.CharField(db_column='TCT0001_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tct0001_crt_datetime = models.DateTimeField(db_column='TCT0001_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tct0001_crt_user_id = models.CharField(db_column='TCT0001_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tct0001_crt_prog_nm = models.CharField(db_column='TCT0001_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tct0001_upd_datetime = models.DateTimeField(db_column='TCT0001_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tct0001_upd_user_id = models.CharField(db_column='TCT0001_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tct0001_upd_prog_nm = models.CharField(db_column='TCT0001_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tct0001_upd_cnt = models.DecimalField(db_column='TCT0001_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCT0001_JOB_SHIJI'
        unique_together = (('tct0001_nendo', 'tct0001_getsudo'),)


class Tct0002JobShijiProc(models.Model):
    tct0001_nendo = models.SmallIntegerField(db_column='TCT0001_NENDO', primary_key=True)  # Field name made lowercase.
    tct0001_getsudo = models.SmallIntegerField(db_column='TCT0001_GETSUDO')  # Field name made lowercase.
    tct0002_process_seq_no = models.SmallIntegerField(db_column='TCT0002_PROCESS_SEQ_NO')  # Field name made lowercase.
    tct0002_kakutei_flg = models.CharField(db_column='TCT0002_KAKUTEI_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tct0002_message = models.CharField(db_column='TCT0002_MESSAGE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tct0002_del_flg = models.CharField(db_column='TCT0002_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tct0002_crt_datetime = models.DateTimeField(db_column='TCT0002_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tct0002_crt_user_id = models.CharField(db_column='TCT0002_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tct0002_crt_prog_nm = models.CharField(db_column='TCT0002_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tct0002_upd_datetime = models.DateTimeField(db_column='TCT0002_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tct0002_upd_user_id = models.CharField(db_column='TCT0002_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tct0002_upd_prog_nm = models.CharField(db_column='TCT0002_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tct0002_upd_cnt = models.DecimalField(db_column='TCT0002_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCT0002_JOB_SHIJI_PROC'
        unique_together = (('tct0001_nendo', 'tct0001_getsudo', 'tct0002_process_seq_no'),)


class Tct1000Saiban(models.Model):
    tct1000_kbn_cd = models.CharField(db_column='TCT1000_KBN_CD', primary_key=True, max_length=21)  # Field name made lowercase.
    tct1000_number_cnt = models.DecimalField(db_column='TCT1000_NUMBER_CNT', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tct1000_upd_cnt = models.DecimalField(db_column='TCT1000_UPD_CNT', max_digits=10, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCT1000_SAIBAN'


class Tdm0101Shain(models.Model):
    tdm0101_shain_cd = models.CharField(db_column='TDM0101_SHAIN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tdm0101_shain_nm = models.CharField(db_column='TDM0101_SHAIN_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0101_shain_nm_k = models.CharField(db_column='TDM0101_SHAIN_NM_K', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0101_org_nm = models.CharField(db_column='TDM0101_ORG_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0101_org_nm_k = models.CharField(db_column='TDM0101_ORG_NM_K', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0101_birth_date = models.DateTimeField(db_column='TDM0101_BIRTH_DATE', blank=True, null=True)  # Field name made lowercase.
    tdm0101_gender = models.CharField(db_column='TDM0101_GENDER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0101_blood_type = models.CharField(db_column='TDM0101_BLOOD_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0101_del_flg = models.CharField(db_column='TDM0101_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0101_crt_datetime = models.DateTimeField(db_column='TDM0101_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0101_crt_user_id = models.CharField(db_column='TDM0101_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0101_crt_prog_nm = models.CharField(db_column='TDM0101_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0101_upd_datetime = models.DateTimeField(db_column='TDM0101_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0101_upd_user_id = models.CharField(db_column='TDM0101_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0101_upd_prog_nm = models.CharField(db_column='TDM0101_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0101_upd_cnt = models.DecimalField(db_column='TDM0101_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdm0101_kokuseki_cd = models.CharField(db_column='TDM0101_KOKUSEKI_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0101_is_married = models.CharField(db_column='TDM0101_IS_MARRIED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0101_entry_date = models.DateTimeField(db_column='TDM0101_ENTRY_DATE', blank=True, null=True)  # Field name made lowercase.
    tdm0101_saiyo_kbn_cd = models.CharField(db_column='TDM0101_SAIYO_KBN_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0101_zaiseki_kbn_cd = models.CharField(db_column='TDM0101_ZAISEKI_KBN_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0101_retire_date = models.DateTimeField(db_column='TDM0101_RETIRE_DATE', blank=True, null=True)  # Field name made lowercase.
    tdm0101_retire_riyu = models.CharField(db_column='TDM0101_RETIRE_RIYU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tdm0101_biko = models.CharField(db_column='TDM0101_BIKO', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tdm0101_mail_adrs1 = models.CharField(db_column='TDM0101_MAIL_ADRS1', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tdm0101_mail_adrs2 = models.CharField(db_column='TDM0101_MAIL_ADRS2', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tdm0101_mail_send = models.CharField(db_column='TDM0101_MAIL_SEND', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0101_shakai_hoken_kbn_cd = models.CharField(db_column='TDM0101_SHAKAI_HOKEN_KBN_CD', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0101_koyou_hoken_kbn_cd = models.CharField(db_column='TDM0101_KOYOU_HOKEN_KBN_CD', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0101_shain_kbn_cd1 = models.CharField(db_column='TDM0101_SHAIN_KBN_CD1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0101_shain_kbn1 = models.CharField(db_column='TDM0101_SHAIN_KBN1', max_length=64, blank=True, null=True)  # Field name made lowercase.
    tdm0101_shain_kbn_cd2 = models.CharField(db_column='TDM0101_SHAIN_KBN_CD2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0101_shain_kbn2 = models.CharField(db_column='TDM0101_SHAIN_KBN2', max_length=64, blank=True, null=True)  # Field name made lowercase.
    tdm0101_shain_kbn_cd3 = models.CharField(db_column='TDM0101_SHAIN_KBN_CD3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0101_shain_kbn3 = models.CharField(db_column='TDM0101_SHAIN_KBN3', max_length=64, blank=True, null=True)  # Field name made lowercase.
    tdm0101_in_date = models.DateTimeField(db_column='TDM0101_IN_DATE', blank=True, null=True)  # Field name made lowercase.
    tdm0101_tel1 = models.CharField(db_column='TDM0101_TEL1', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tdm0101_tel2 = models.CharField(db_column='TDM0101_TEL2', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tdm0101_fax = models.CharField(db_column='TDM0101_FAX', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tdm0101_post_no = models.CharField(db_column='TDM0101_POST_NO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    tdm0101_adrs1 = models.CharField(db_column='TDM0101_ADRS1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0101_adrs2 = models.CharField(db_column='TDM0101_ADRS2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0101_renraku_name1 = models.CharField(db_column='TDM0101_RENRAKU_NAME1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0101_renraku_kankei_cd1 = models.CharField(db_column='TDM0101_RENRAKU_KANKEI_CD1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0101_renraku_tel1 = models.CharField(db_column='TDM0101_RENRAKU_TEL1', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tdm0101_renraku_kbn_cd1 = models.CharField(db_column='TDM0101_RENRAKU_KBN_CD1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0101_renraku_post_no1 = models.CharField(db_column='TDM0101_RENRAKU_POST_NO1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    tdm0101_renraku_adrs1_1 = models.CharField(db_column='TDM0101_RENRAKU_ADRS1_1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0101_renraku_adrs2_1 = models.CharField(db_column='TDM0101_RENRAKU_ADRS2_1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0101_renraku_mail1 = models.CharField(db_column='TDM0101_RENRAKU_MAIL1', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tdm0101_renraku_name2 = models.CharField(db_column='TDM0101_RENRAKU_NAME2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0101_renraku_kankei_cd2 = models.CharField(db_column='TDM0101_RENRAKU_KANKEI_CD2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0101_renraku_tel2 = models.CharField(db_column='TDM0101_RENRAKU_TEL2', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tdm0101_renraku_kbn_cd2 = models.CharField(db_column='TDM0101_RENRAKU_KBN_CD2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0101_renraku_post_no2 = models.CharField(db_column='TDM0101_RENRAKU_POST_NO2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    tdm0101_renraku_adrs1_2 = models.CharField(db_column='TDM0101_RENRAKU_ADRS1_2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0101_renraku_adrs2_2 = models.CharField(db_column='TDM0101_RENRAKU_ADRS2_2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0101_renraku_mail2 = models.CharField(db_column='TDM0101_RENRAKU_MAIL2', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tdm0101_kaoshashin = models.BinaryField(db_column='TDM0101_KAOSHASHIN', blank=True, null=True)  # Field name made lowercase.
    tdm0101_tanto_flg = models.BooleanField(db_column='TDM0101_TANTO_FLG', blank=True, null=True)  # Field name made lowercase.
    tdm0101_object_name1 = models.CharField(db_column='TDM0101_OBJECT_NAME1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0101_object1 = models.BinaryField(db_column='TDM0101_OBJECT1', blank=True, null=True)  # Field name made lowercase.
    tdm0101_object_name2 = models.CharField(db_column='TDM0101_OBJECT_NAME2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0101_object2 = models.BinaryField(db_column='TDM0101_OBJECT2', blank=True, null=True)  # Field name made lowercase.
    tdm0101_object_name3 = models.CharField(db_column='TDM0101_OBJECT_NAME3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0101_object3 = models.BinaryField(db_column='TDM0101_OBJECT3', blank=True, null=True)  # Field name made lowercase.
    tdm0101_object_name4 = models.CharField(db_column='TDM0101_OBJECT_NAME4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0101_object4 = models.BinaryField(db_column='TDM0101_OBJECT4', blank=True, null=True)  # Field name made lowercase.
    tdm0101_object_name5 = models.CharField(db_column='TDM0101_OBJECT_NAME5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0101_object5 = models.BinaryField(db_column='TDM0101_OBJECT5', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0101_SHAIN'


class Tdm0102Visa(models.Model):
    tdm0101_shain_cd = models.CharField(db_column='TDM0101_SHAIN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tdm0102_visa_no = models.DecimalField(db_column='TDM0102_VISA_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tdm0102_start_date = models.DateTimeField(db_column='TDM0102_START_DATE', blank=True, null=True)  # Field name made lowercase.
    tdm0102_touroku_kbn = models.CharField(db_column='TDM0102_TOUROKU_KBN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0102_end_date = models.DateTimeField(db_column='TDM0102_END_DATE', blank=True, null=True)  # Field name made lowercase.
    tdm0102_touroku_no = models.CharField(db_column='TDM0102_TOUROKU_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tdm0102_kokuseki_cd = models.CharField(db_column='TDM0102_KOKUSEKI_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0102_next_date = models.DateTimeField(db_column='TDM0102_NEXT_DATE', blank=True, null=True)  # Field name made lowercase.
    tdm0102_next_day = models.CharField(db_column='TDM0102_NEXT_DAY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdm0102_adrs1 = models.CharField(db_column='TDM0102_ADRS1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0102_adrs2 = models.CharField(db_column='TDM0102_ADRS2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0102_cnt_adrs1 = models.CharField(db_column='TDM0102_CNT_ADRS1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0102_cnt_adrs2 = models.CharField(db_column='TDM0102_CNT_ADRS2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0102_send_mail_addr1 = models.CharField(db_column='TDM0102_SEND_MAIL_ADDR1', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tdm0102_send_mail_addr2 = models.CharField(db_column='TDM0102_SEND_MAIL_ADDR2', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tdm0102_del_flg = models.CharField(db_column='TDM0102_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0102_crt_datetime = models.DateTimeField(db_column='TDM0102_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0102_crt_user_id = models.CharField(db_column='TDM0102_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0102_crt_prog_nm = models.CharField(db_column='TDM0102_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0102_upd_datetime = models.DateTimeField(db_column='TDM0102_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0102_upd_user_id = models.CharField(db_column='TDM0102_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0102_upd_prog_nm = models.CharField(db_column='TDM0102_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0102_upd_cnt = models.DecimalField(db_column='TDM0102_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdm0102_send_mail_addr3 = models.CharField(db_column='TDM0102_SEND_MAIL_ADDR3', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tdm0102_send_mail_addr4 = models.CharField(db_column='TDM0102_SEND_MAIL_ADDR4', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tdm0102_send_mail_addr5 = models.CharField(db_column='TDM0102_SEND_MAIL_ADDR5', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tdm0102_file_1 = models.BinaryField(db_column='TDM0102_FILE_1', blank=True, null=True)  # Field name made lowercase.
    tdm0102_file_1_name = models.CharField(db_column='TDM0102_FILE_1_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0102_kakunin_zumi = models.CharField(db_column='TDM0102_KAKUNIN_ZUMI', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0102_VISA'
        unique_together = (('tdm0101_shain_cd', 'tdm0102_visa_no'),)


class Tdm0103GakuReki(models.Model):
    tdm0101_shain_cd = models.CharField(db_column='TDM0101_SHAIN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tdm0103_school_no = models.DecimalField(db_column='TDM0103_SCHOOL_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tdm0103_end_ym = models.CharField(db_column='TDM0103_END_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tdm0103_end_kbn = models.CharField(db_column='TDM0103_END_KBN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0103_cmp_nm = models.CharField(db_column='TDM0103_CMP_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tdm0103_bmn_nm = models.CharField(db_column='TDM0103_BMN_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tdm0103_shoku_nm = models.CharField(db_column='TDM0103_SHOKU_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tdm0103_school_kbn_cd = models.CharField(db_column='TDM0103_SCHOOL_KBN_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0103_is_last = models.CharField(db_column='TDM0103_IS_LAST', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0103_del_flg = models.CharField(db_column='TDM0103_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0103_crt_datetime = models.DateTimeField(db_column='TDM0103_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0103_crt_user_id = models.CharField(db_column='TDM0103_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0103_crt_prog_nm = models.CharField(db_column='TDM0103_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0103_upd_datetime = models.DateTimeField(db_column='TDM0103_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0103_upd_user_id = models.CharField(db_column='TDM0103_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0103_upd_prog_nm = models.CharField(db_column='TDM0103_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0103_upd_cnt = models.DecimalField(db_column='TDM0103_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0103_GAKU_REKI'
        unique_together = (('tdm0101_shain_cd', 'tdm0103_school_no'),)


class Tdm0104HoshoNin(models.Model):
    tdm0101_shain_cd = models.CharField(db_column='TDM0101_SHAIN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tdm0104_hosho_no = models.DecimalField(db_column='TDM0104_HOSHO_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tdm0104_date = models.DateTimeField(db_column='TDM0104_DATE', blank=True, null=True)  # Field name made lowercase.
    tdm0104_hosho_nm = models.CharField(db_column='TDM0104_HOSHO_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0104_kankei_cd = models.CharField(db_column='TDM0104_KANKEI_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0104_yuko_start = models.DateTimeField(db_column='TDM0104_YUKO_START', blank=True, null=True)  # Field name made lowercase.
    tdm0104_yuko_end = models.DateTimeField(db_column='TDM0104_YUKO_END', blank=True, null=True)  # Field name made lowercase.
    tdm0104_biko = models.CharField(db_column='TDM0104_BIKO', max_length=128, blank=True, null=True)  # Field name made lowercase.
    tdm0104_post_no = models.CharField(db_column='TDM0104_POST_NO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    tdm0104_adrs1 = models.CharField(db_column='TDM0104_ADRS1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0104_adrs2 = models.CharField(db_column='TDM0104_ADRS2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0104_tel = models.CharField(db_column='TDM0104_TEL', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tdm0104_del_flg = models.CharField(db_column='TDM0104_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0104_crt_datetime = models.DateTimeField(db_column='TDM0104_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0104_crt_user_id = models.CharField(db_column='TDM0104_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0104_crt_prog_nm = models.CharField(db_column='TDM0104_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0104_upd_datetime = models.DateTimeField(db_column='TDM0104_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0104_upd_user_id = models.CharField(db_column='TDM0104_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0104_upd_prog_nm = models.CharField(db_column='TDM0104_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0104_upd_cnt = models.DecimalField(db_column='TDM0104_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0104_HOSHO_NIN'
        unique_together = (('tdm0101_shain_cd', 'tdm0104_hosho_no'),)


class Tdm0105IdouRireki(models.Model):
    tdm0101_shain_cd = models.CharField(db_column='TDM0101_SHAIN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tdm0105_shozoku_start_date = models.DateTimeField(db_column='TDM0105_SHOZOKU_START_DATE')  # Field name made lowercase.
    tdm0105_idou_kbn_cd = models.CharField(db_column='TDM0105_IDOU_KBN_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0105_bumon_cd = models.CharField(db_column='TDM0105_BUMON_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tdm0105_bumon_name = models.CharField(db_column='TDM0105_BUMON_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0105_yakusyoku_cd = models.CharField(db_column='TDM0105_YAKUSYOKU_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0105_genba_cd = models.CharField(db_column='TDM0105_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0105_shoku_shu_cd = models.CharField(db_column='TDM0105_SHOKU_SHU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdm0105_jirei_zumi_flg = models.CharField(db_column='TDM0105_JIREI_ZUMI_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0105_del_flg = models.CharField(db_column='TDM0105_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0105_crt_datetime = models.DateTimeField(db_column='TDM0105_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0105_crt_user_id = models.CharField(db_column='TDM0105_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0105_crt_prog_nm = models.CharField(db_column='TDM0105_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0105_upd_datetime = models.DateTimeField(db_column='TDM0105_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0105_upd_user_id = models.CharField(db_column='TDM0105_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0105_upd_prog_nm = models.CharField(db_column='TDM0105_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0105_upd_cnt = models.DecimalField(db_column='TDM0105_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdm0105_idou_kbn_cd2 = models.CharField(db_column='TDM0105_IDOU_KBN_CD2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0105_idou_kbn_cd3 = models.CharField(db_column='TDM0105_IDOU_KBN_CD3', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0105_IDOU_RIREKI'
        unique_together = (('tdm0101_shain_cd', 'tdm0105_shozoku_start_date'),)


class Tdm0106Sikaku(models.Model):
    tdm0101_shain_cd = models.CharField(db_column='TDM0101_SHAIN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tdm0106_shikaku_no = models.DecimalField(db_column='TDM0106_SHIKAKU_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tdm0106_shikaku_date = models.DateTimeField(db_column='TDM0106_SHIKAKU_DATE', blank=True, null=True)  # Field name made lowercase.
    tdm0106_shikaku_cd = models.CharField(db_column='TDM0106_SHIKAKU_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0106_nintei_no = models.CharField(db_column='TDM0106_NINTEI_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0106_renew_flg = models.CharField(db_column='TDM0106_RENEW_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0106_renew_date = models.DateTimeField(db_column='TDM0106_RENEW_DATE', blank=True, null=True)  # Field name made lowercase.
    tdm0106_biko = models.CharField(db_column='TDM0106_BIKO', max_length=128, blank=True, null=True)  # Field name made lowercase.
    tdm0106_del_flg = models.CharField(db_column='TDM0106_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0106_crt_datetime = models.DateTimeField(db_column='TDM0106_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0106_crt_user_id = models.CharField(db_column='TDM0106_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0106_crt_prog_nm = models.CharField(db_column='TDM0106_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0106_upd_datetime = models.DateTimeField(db_column='TDM0106_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0106_upd_user_id = models.CharField(db_column='TDM0106_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0106_upd_prog_nm = models.CharField(db_column='TDM0106_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0106_upd_cnt = models.DecimalField(db_column='TDM0106_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0106_SIKAKU'
        unique_together = (('tdm0101_shain_cd', 'tdm0106_shikaku_no'),)


class Tdm0107Kensyu(models.Model):
    tdm0101_shain_cd = models.CharField(db_column='TDM0101_SHAIN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tdm0107_kensyu_no = models.DecimalField(db_column='TDM0107_KENSYU_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tdm0107_jyukou_date = models.DateTimeField(db_column='TDM0107_JYUKOU_DATE', blank=True, null=True)  # Field name made lowercase.
    tdm0107_kensyu_cd = models.CharField(db_column='TDM0107_KENSYU_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0107_shagai_flg = models.CharField(db_column='TDM0107_SHAGAI_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0107_kensyu_end_date = models.DateTimeField(db_column='TDM0107_KENSYU_END_DATE', blank=True, null=True)  # Field name made lowercase.
    tdm0107_jikain_kenshu_ym = models.CharField(db_column='TDM0107_JIKAIN_KENSHU_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tdm0107_hyouten_cd = models.CharField(db_column='TDM0107_HYOUTEN_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0107_sanka_cd = models.CharField(db_column='TDM0107_SANKA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0107_biko = models.CharField(db_column='TDM0107_BIKO', max_length=128, blank=True, null=True)  # Field name made lowercase.
    tdm0107_del_flg = models.CharField(db_column='TDM0107_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0107_crt_datetime = models.DateTimeField(db_column='TDM0107_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0107_crt_user_id = models.CharField(db_column='TDM0107_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0107_crt_prog_nm = models.CharField(db_column='TDM0107_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0107_upd_datetime = models.DateTimeField(db_column='TDM0107_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0107_upd_user_id = models.CharField(db_column='TDM0107_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0107_upd_prog_nm = models.CharField(db_column='TDM0107_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0107_upd_cnt = models.DecimalField(db_column='TDM0107_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0107_KENSYU'
        unique_together = (('tdm0101_shain_cd', 'tdm0107_kensyu_no'),)


class Tdm0108KoyouKeiyaku(models.Model):
    tdm0101_shain_cd = models.CharField(db_column='TDM0101_SHAIN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tdm0108_keiyaku_start_date = models.DateTimeField(db_column='TDM0108_KEIYAKU_START_DATE')  # Field name made lowercase.
    tdm0108_keiyaku_end_date = models.DateTimeField(db_column='TDM0108_KEIYAKU_END_DATE', blank=True, null=True)  # Field name made lowercase.
    tdm0108_syurou_jikan = models.DecimalField(db_column='TDM0108_SYUROU_JIKAN', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_syurou_nissu = models.DecimalField(db_column='TDM0108_SYUROU_NISSU', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_del_flg = models.CharField(db_column='TDM0108_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0108_crt_datetime = models.DateTimeField(db_column='TDM0108_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0108_crt_user_id = models.CharField(db_column='TDM0108_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0108_crt_prog_nm = models.CharField(db_column='TDM0108_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0108_upd_datetime = models.DateTimeField(db_column='TDM0108_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0108_upd_user_id = models.CharField(db_column='TDM0108_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0108_upd_prog_nm = models.CharField(db_column='TDM0108_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0108_upd_cnt = models.DecimalField(db_column='TDM0108_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdm0108_koshin_kbn = models.CharField(db_column='TDM0108_KOSHIN_KBN', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou1_from = models.IntegerField(db_column='TDM0108_SHUGYOU1_FROM', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou1_to = models.IntegerField(db_column='TDM0108_SHUGYOU1_TO', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou1_kosu = models.DecimalField(db_column='TDM0108_SHUGYOU1_KOSU', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou2_from = models.IntegerField(db_column='TDM0108_SHUGYOU2_FROM', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou2_to = models.IntegerField(db_column='TDM0108_SHUGYOU2_TO', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou2_kosu = models.DecimalField(db_column='TDM0108_SHUGYOU2_KOSU', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou3_from = models.IntegerField(db_column='TDM0108_SHUGYOU3_FROM', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou3_to = models.IntegerField(db_column='TDM0108_SHUGYOU3_TO', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou3_kosu = models.DecimalField(db_column='TDM0108_SHUGYOU3_KOSU', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou4_from = models.IntegerField(db_column='TDM0108_SHUGYOU4_FROM', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou4_to = models.IntegerField(db_column='TDM0108_SHUGYOU4_TO', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou4_kosu = models.DecimalField(db_column='TDM0108_SHUGYOU4_KOSU', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_chingin_kbn = models.CharField(db_column='TDM0108_CHINGIN_KBN', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tdm0108_chingin = models.IntegerField(db_column='TDM0108_CHINGIN', blank=True, null=True)  # Field name made lowercase.
    tdm0108_biko = models.CharField(db_column='TDM0108_BIKO', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tdm0108_genba_cd = models.CharField(db_column='TDM0108_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shoku_shu_cd = models.CharField(db_column='TDM0108_SHOKU_SHU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdm0108_genba_cd_2 = models.CharField(db_column='TDM0108_GENBA_CD_2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shoku_shu_cd_2 = models.CharField(db_column='TDM0108_SHOKU_SHU_CD_2', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdm0108_genba_cd_3 = models.CharField(db_column='TDM0108_GENBA_CD_3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shoku_shu_cd_3 = models.CharField(db_column='TDM0108_SHOKU_SHU_CD_3', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdm0108_teate_cd = models.CharField(db_column='TDM0108_TEATE_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0108_teate_kgk = models.DecimalField(db_column='TDM0108_TEATE_KGK', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdm0108_teate_cd_2 = models.CharField(db_column='TDM0108_TEATE_CD_2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0108_teate_kgk_2 = models.DecimalField(db_column='TDM0108_TEATE_KGK_2', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdm0108_teate_cd_3 = models.CharField(db_column='TDM0108_TEATE_CD_3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0108_teate_kgk_3 = models.DecimalField(db_column='TDM0108_TEATE_KGK_3', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdm0108_chingin_dt_1 = models.IntegerField(db_column='TDM0108_CHINGIN_DT_1', blank=True, null=True)  # Field name made lowercase.
    tdm0108_chingin_dt_2 = models.IntegerField(db_column='TDM0108_CHINGIN_DT_2', blank=True, null=True)  # Field name made lowercase.
    tdm0108_chingin_dt_3 = models.IntegerField(db_column='TDM0108_CHINGIN_DT_3', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou1_break = models.DecimalField(db_column='TDM0108_SHUGYOU1_BREAK', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou2_break = models.DecimalField(db_column='TDM0108_SHUGYOU2_BREAK', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou3_break = models.DecimalField(db_column='TDM0108_SHUGYOU3_BREAK', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou4_break = models.DecimalField(db_column='TDM0108_SHUGYOU4_BREAK', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou1_from_2 = models.IntegerField(db_column='TDM0108_SHUGYOU1_FROM_2', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou1_to_2 = models.IntegerField(db_column='TDM0108_SHUGYOU1_TO_2', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou1_break_2 = models.DecimalField(db_column='TDM0108_SHUGYOU1_BREAK_2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou1_kosu_2 = models.DecimalField(db_column='TDM0108_SHUGYOU1_KOSU_2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou2_from_2 = models.IntegerField(db_column='TDM0108_SHUGYOU2_FROM_2', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou2_to_2 = models.IntegerField(db_column='TDM0108_SHUGYOU2_TO_2', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou2_break_2 = models.DecimalField(db_column='TDM0108_SHUGYOU2_BREAK_2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou2_kosu_2 = models.DecimalField(db_column='TDM0108_SHUGYOU2_KOSU_2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou3_from_2 = models.IntegerField(db_column='TDM0108_SHUGYOU3_FROM_2', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou3_to_2 = models.IntegerField(db_column='TDM0108_SHUGYOU3_TO_2', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou3_break_2 = models.DecimalField(db_column='TDM0108_SHUGYOU3_BREAK_2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou3_kosu_2 = models.DecimalField(db_column='TDM0108_SHUGYOU3_KOSU_2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou4_from_2 = models.IntegerField(db_column='TDM0108_SHUGYOU4_FROM_2', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou4_to_2 = models.IntegerField(db_column='TDM0108_SHUGYOU4_TO_2', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou4_break_2 = models.DecimalField(db_column='TDM0108_SHUGYOU4_BREAK_2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou4_kosu_2 = models.DecimalField(db_column='TDM0108_SHUGYOU4_KOSU_2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou1_from_3 = models.IntegerField(db_column='TDM0108_SHUGYOU1_FROM_3', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou1_to_3 = models.IntegerField(db_column='TDM0108_SHUGYOU1_TO_3', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou1_break_3 = models.DecimalField(db_column='TDM0108_SHUGYOU1_BREAK_3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou1_kosu_3 = models.DecimalField(db_column='TDM0108_SHUGYOU1_KOSU_3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou2_from_3 = models.IntegerField(db_column='TDM0108_SHUGYOU2_FROM_3', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou2_to_3 = models.IntegerField(db_column='TDM0108_SHUGYOU2_TO_3', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou2_break_3 = models.DecimalField(db_column='TDM0108_SHUGYOU2_BREAK_3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou2_kosu_3 = models.DecimalField(db_column='TDM0108_SHUGYOU2_KOSU_3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou3_from_3 = models.IntegerField(db_column='TDM0108_SHUGYOU3_FROM_3', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou3_to_3 = models.IntegerField(db_column='TDM0108_SHUGYOU3_TO_3', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou3_break_3 = models.DecimalField(db_column='TDM0108_SHUGYOU3_BREAK_3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou3_kosu_3 = models.DecimalField(db_column='TDM0108_SHUGYOU3_KOSU_3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou4_from_3 = models.IntegerField(db_column='TDM0108_SHUGYOU4_FROM_3', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou4_to_3 = models.IntegerField(db_column='TDM0108_SHUGYOU4_TO_3', blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou4_break_3 = models.DecimalField(db_column='TDM0108_SHUGYOU4_BREAK_3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_shugyou4_kosu_3 = models.DecimalField(db_column='TDM0108_SHUGYOU4_KOSU_3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdm0108_teate_cd_4 = models.CharField(db_column='TDM0108_TEATE_CD_4', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0108_teate_kgk_4 = models.DecimalField(db_column='TDM0108_TEATE_KGK_4', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdm0108_saiyo_kbn_cd = models.CharField(db_column='TDM0108_SAIYO_KBN_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0108_KOYOU_KEIYAKU'
        unique_together = (('tdm0101_shain_cd', 'tdm0108_keiyaku_start_date'),)


class Tdm0109ShouBatsu(models.Model):
    tdm0101_shain_cd = models.CharField(db_column='TDM0101_SHAIN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tdm0109_shoubatsu_no = models.DecimalField(db_column='TDM0109_SHOUBATSU_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tdm0109_shoubatsu_date = models.DateTimeField(db_column='TDM0109_SHOUBATSU_DATE', blank=True, null=True)  # Field name made lowercase.
    tdm0109_shoubatsu_tekiyou = models.CharField(db_column='TDM0109_SHOUBATSU_TEKIYOU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tdm0109_shoubatsu_kbn = models.CharField(db_column='TDM0109_SHOUBATSU_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0109_bikou = models.CharField(db_column='TDM0109_BIKOU', max_length=128, blank=True, null=True)  # Field name made lowercase.
    tdm0109_del_flg = models.CharField(db_column='TDM0109_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0109_crt_datetime = models.DateTimeField(db_column='TDM0109_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0109_crt_user_id = models.CharField(db_column='TDM0109_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0109_crt_prog_nm = models.CharField(db_column='TDM0109_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0109_upd_datetime = models.DateTimeField(db_column='TDM0109_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0109_upd_user_id = models.CharField(db_column='TDM0109_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0109_upd_prog_nm = models.CharField(db_column='TDM0109_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0109_upd_cnt = models.DecimalField(db_column='TDM0109_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0109_SHOU_BATSU'
        unique_together = (('tdm0101_shain_cd', 'tdm0109_shoubatsu_no'),)


class Tdm0110KenkoShindan(models.Model):
    tdm0101_shain_cd = models.CharField(db_column='TDM0101_SHAIN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tdm0110_kenko_shindan_no = models.DecimalField(db_column='TDM0110_KENKO_SHINDAN_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tdm0110_jyushin_date = models.DateTimeField(db_column='TDM0110_JYUSHIN_DATE', blank=True, null=True)  # Field name made lowercase.
    tdm0110_kensa_nm = models.CharField(db_column='TDM0110_KENSA_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tdm0110_kensa_kbn = models.CharField(db_column='TDM0110_KENSA_KBN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0110_kensa_kekka_cd = models.CharField(db_column='TDM0110_KENSA_KEKKA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0110_biko = models.CharField(db_column='TDM0110_BIKO', max_length=128, blank=True, null=True)  # Field name made lowercase.
    tdm0110_del_flg = models.CharField(db_column='TDM0110_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0110_crt_datetime = models.DateTimeField(db_column='TDM0110_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0110_crt_user_id = models.CharField(db_column='TDM0110_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0110_crt_prog_nm = models.CharField(db_column='TDM0110_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0110_upd_datetime = models.DateTimeField(db_column='TDM0110_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0110_upd_user_id = models.CharField(db_column='TDM0110_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0110_upd_prog_nm = models.CharField(db_column='TDM0110_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0110_upd_cnt = models.DecimalField(db_column='TDM0110_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0110_KENKO_SHINDAN'
        unique_together = (('tdm0101_shain_cd', 'tdm0110_kenko_shindan_no'),)


class Tdm0111Kouka(models.Model):
    tdm0101_shain_cd = models.CharField(db_column='TDM0101_SHAIN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tdm0111_kouka_no = models.DecimalField(db_column='TDM0111_KOUKA_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tdm0111_kouka_nendo = models.SmallIntegerField(db_column='TDM0111_KOUKA_NENDO', blank=True, null=True)  # Field name made lowercase.
    tdm0111_kouka_hanki_kbn = models.CharField(db_column='TDM0111_KOUKA_HANKI_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0111_kouka_shbetu_cd = models.CharField(db_column='TDM0111_KOUKA_SHBETU_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0111_kouka_kekka_cd = models.CharField(db_column='TDM0111_KOUKA_KEKKA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0111_hyouten = models.CharField(db_column='TDM0111_HYOUTEN', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tdm0111_biko = models.CharField(db_column='TDM0111_BIKO', max_length=128, blank=True, null=True)  # Field name made lowercase.
    tdm0111_del_flg = models.CharField(db_column='TDM0111_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0111_crt_datetime = models.DateTimeField(db_column='TDM0111_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0111_crt_user_id = models.CharField(db_column='TDM0111_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0111_crt_prog_nm = models.CharField(db_column='TDM0111_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0111_upd_datetime = models.DateTimeField(db_column='TDM0111_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0111_upd_user_id = models.CharField(db_column='TDM0111_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0111_upd_prog_nm = models.CharField(db_column='TDM0111_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0111_upd_cnt = models.DecimalField(db_column='TDM0111_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0111_KOUKA'
        unique_together = (('tdm0101_shain_cd', 'tdm0111_kouka_no'),)


class Tdm0112Taiyo(models.Model):
    tdm0101_shain_cd = models.CharField(db_column='TDM0101_SHAIN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tdm0112_taiyo_no = models.DecimalField(db_column='TDM0112_TAIYO_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tdm0112_taiyo_kbn = models.CharField(db_column='TDM0112_TAIYO_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0112_hinmei = models.CharField(db_column='TDM0112_HINMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tdm0112_start_date = models.DateTimeField(db_column='TDM0112_START_DATE', blank=True, null=True)  # Field name made lowercase.
    tdm0112_henkyaku_date = models.DateTimeField(db_column='TDM0112_HENKYAKU_DATE', blank=True, null=True)  # Field name made lowercase.
    tdm0112_suryou = models.SmallIntegerField(db_column='TDM0112_SURYOU', blank=True, null=True)  # Field name made lowercase.
    tdm0112_biko = models.CharField(db_column='TDM0112_BIKO', max_length=128, blank=True, null=True)  # Field name made lowercase.
    tdm0112_del_flg = models.CharField(db_column='TDM0112_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0112_crt_datetime = models.DateTimeField(db_column='TDM0112_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0112_crt_user_id = models.CharField(db_column='TDM0112_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0112_crt_prog_nm = models.CharField(db_column='TDM0112_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0112_upd_datetime = models.DateTimeField(db_column='TDM0112_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0112_upd_user_id = models.CharField(db_column='TDM0112_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0112_upd_prog_nm = models.CharField(db_column='TDM0112_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0112_upd_cnt = models.DecimalField(db_column='TDM0112_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0112_TAIYO'
        unique_together = (('tdm0101_shain_cd', 'tdm0112_taiyo_no'),)


class Tdm0113Kyusyoku(models.Model):
    tdm0101_shain_cd = models.CharField(db_column='TDM0101_SHAIN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tdm0113_kyusyoku_start_date = models.DateTimeField(db_column='TDM0113_KYUSYOKU_START_DATE')  # Field name made lowercase.
    tdm0113_kyusyoku_end_date = models.DateTimeField(db_column='TDM0113_KYUSYOKU_END_DATE', blank=True, null=True)  # Field name made lowercase.
    tdm0113_kyusyoku_kbn_cd = models.CharField(db_column='TDM0113_KYUSYOKU_KBN_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0113_kyusyoku_riyu = models.CharField(db_column='TDM0113_KYUSYOKU_RIYU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tdm0113_biko = models.CharField(db_column='TDM0113_BIKO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tdm0113_file_1 = models.BinaryField(db_column='TDM0113_FILE_1', blank=True, null=True)  # Field name made lowercase.
    tdm0113_file_1_name = models.CharField(db_column='TDM0113_FILE_1_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0113_file_2 = models.BinaryField(db_column='TDM0113_FILE_2', blank=True, null=True)  # Field name made lowercase.
    tdm0113_file_2_name = models.CharField(db_column='TDM0113_FILE_2_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0113_file_3 = models.BinaryField(db_column='TDM0113_FILE_3', blank=True, null=True)  # Field name made lowercase.
    tdm0113_file_3_name = models.CharField(db_column='TDM0113_FILE_3_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0113_file_4 = models.BinaryField(db_column='TDM0113_FILE_4', blank=True, null=True)  # Field name made lowercase.
    tdm0113_file_4_name = models.CharField(db_column='TDM0113_FILE_4_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0113_file_5 = models.BinaryField(db_column='TDM0113_FILE_5', blank=True, null=True)  # Field name made lowercase.
    tdm0113_file_5_name = models.CharField(db_column='TDM0113_FILE_5_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0113_del_flg = models.CharField(db_column='TDM0113_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0113_crt_datetime = models.DateTimeField(db_column='TDM0113_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0113_crt_user_id = models.CharField(db_column='TDM0113_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0113_crt_prog_nm = models.CharField(db_column='TDM0113_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0113_upd_datetime = models.DateTimeField(db_column='TDM0113_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0113_upd_user_id = models.CharField(db_column='TDM0113_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0113_upd_prog_nm = models.CharField(db_column='TDM0113_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0113_upd_cnt = models.DecimalField(db_column='TDM0113_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0113_KYUSYOKU'
        unique_together = (('tdm0101_shain_cd', 'tdm0113_kyusyoku_start_date'),)


class Tdm0114ShainSyokai(models.Model):
    tdm0101_shain_cd = models.CharField(db_column='TDM0101_SHAIN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tdm0114_no = models.DecimalField(db_column='TDM0114_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tdm0114_syokai_shain_cd = models.CharField(db_column='TDM0114_SYOKAI_SHAIN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tdm0114_mail_date = models.DateTimeField(db_column='TDM0114_MAIL_DATE', blank=True, null=True)  # Field name made lowercase.
    tdm0114_kakunin_zumi = models.CharField(db_column='TDM0114_KAKUNIN_ZUMI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0114_send_mail_addr1 = models.CharField(db_column='TDM0114_SEND_MAIL_ADDR1', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tdm0114_send_mail_addr2 = models.CharField(db_column='TDM0114_SEND_MAIL_ADDR2', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tdm0114_send_mail_addr3 = models.CharField(db_column='TDM0114_SEND_MAIL_ADDR3', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tdm0114_send_mail_addr4 = models.CharField(db_column='TDM0114_SEND_MAIL_ADDR4', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tdm0114_send_mail_addr5 = models.CharField(db_column='TDM0114_SEND_MAIL_ADDR5', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tdm0114_syokai_file = models.BinaryField(db_column='TDM0114_SYOKAI_FILE', blank=True, null=True)  # Field name made lowercase.
    tdm0114_syokai_file_name = models.CharField(db_column='TDM0114_SYOKAI_FILE_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0114_biko = models.CharField(db_column='TDM0114_BIKO', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tdm0114_del_flg = models.CharField(db_column='TDM0114_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0114_crt_datetime = models.DateTimeField(db_column='TDM0114_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0114_crt_user_id = models.CharField(db_column='TDM0114_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0114_crt_prog_nm = models.CharField(db_column='TDM0114_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0114_upd_datetime = models.DateTimeField(db_column='TDM0114_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0114_upd_user_id = models.CharField(db_column='TDM0114_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0114_upd_prog_nm = models.CharField(db_column='TDM0114_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0114_upd_cnt = models.DecimalField(db_column='TDM0114_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0114_SHAIN_SYOKAI'
        unique_together = (('tdm0101_shain_cd', 'tdm0114_no'),)


class Tdm0401SyugyoBase(models.Model):
    tdm0401_nendo = models.SmallIntegerField(db_column='TDM0401_NENDO', primary_key=True)  # Field name made lowercase.
    tdm0401_getsudo = models.SmallIntegerField(db_column='TDM0401_GETSUDO')  # Field name made lowercase.
    tdm0401_del_flg = models.CharField(db_column='TDM0401_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0401_crt_datetime = models.DateTimeField(db_column='TDM0401_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0401_crt_user_id = models.CharField(db_column='TDM0401_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0401_crt_prog_nm = models.CharField(db_column='TDM0401_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0401_upd_datetime = models.DateTimeField(db_column='TDM0401_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0401_upd_user_id = models.CharField(db_column='TDM0401_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0401_upd_prog_nm = models.CharField(db_column='TDM0401_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0401_upd_cnt = models.DecimalField(db_column='TDM0401_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0401_SYUGYO_BASE'


class Tdm0402KinmuShain(models.Model):
    tdm0402_shain_cd = models.CharField(db_column='TDM0402_SHAIN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tdm0402_start_date = models.DateTimeField(db_column='TDM0402_START_DATE', blank=True, null=True)  # Field name made lowercase.
    tdm0402_del_flg = models.CharField(db_column='TDM0402_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0402_crt_datetime = models.DateTimeField(db_column='TDM0402_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0402_crt_user_id = models.CharField(db_column='TDM0402_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0402_crt_prog_nm = models.CharField(db_column='TDM0402_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0402_upd_datetime = models.DateTimeField(db_column='TDM0402_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0402_upd_user_id = models.CharField(db_column='TDM0402_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0402_upd_prog_nm = models.CharField(db_column='TDM0402_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0402_upd_cnt = models.DecimalField(db_column='TDM0402_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0402_KINMU_SHAIN'


class Tdm0403KinmuPtn(models.Model):
    tdm0402_shain_cd = models.CharField(db_column='TDM0402_SHAIN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tdm0403_week_no = models.SmallIntegerField(db_column='TDM0403_WEEK_NO')  # Field name made lowercase.
    tdm0403_day = models.SmallIntegerField(db_column='TDM0403_DAY')  # Field name made lowercase.
    tdm0403_renban = models.SmallIntegerField(db_column='TDM0403_RENBAN')  # Field name made lowercase.
    tdm0403_genba_cd = models.CharField(db_column='TDM0403_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdm0403_shoku_cd = models.CharField(db_column='TDM0403_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdm0403_shift_code = models.CharField(db_column='TDM0403_SHIFT_CODE', max_length=11, blank=True, null=True)  # Field name made lowercase.
    tdm0403_del_flg = models.CharField(db_column='TDM0403_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0403_crt_datetime = models.DateTimeField(db_column='TDM0403_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0403_crt_user_id = models.CharField(db_column='TDM0403_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0403_crt_prog_nm = models.CharField(db_column='TDM0403_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0403_upd_datetime = models.DateTimeField(db_column='TDM0403_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0403_upd_user_id = models.CharField(db_column='TDM0403_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0403_upd_prog_nm = models.CharField(db_column='TDM0403_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0403_upd_cnt = models.DecimalField(db_column='TDM0403_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdm0403_shift_pkey = models.IntegerField(db_column='TDM0403_SHIFT_PKEY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0403_KINMU_PTN'
        unique_together = (('tdm0402_shain_cd', 'tdm0403_week_no', 'tdm0403_day', 'tdm0403_renban'),)


class Tdm0404TanmatuKanri(models.Model):
    tdm0404_shain_cd = models.CharField(db_column='TDM0404_SHAIN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tdm0404_tanmatu_kanri_flg = models.CharField(db_column='TDM0404_TANMATU_KANRI_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0404_del_flg = models.CharField(db_column='TDM0404_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0404_crt_datetime = models.DateTimeField(db_column='TDM0404_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0404_crt_user_id = models.CharField(db_column='TDM0404_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0404_crt_prog_nm = models.CharField(db_column='TDM0404_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0404_upd_datetime = models.DateTimeField(db_column='TDM0404_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0404_upd_user_id = models.CharField(db_column='TDM0404_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0404_upd_prog_nm = models.CharField(db_column='TDM0404_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0404_upd_cnt = models.DecimalField(db_column='TDM0404_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdm0404_pwd = models.CharField(db_column='TDM0404_PWD', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0404_TANMATU_KANRI'


class Tdm0405ShainShoninKngn(models.Model):
    tdm0405_shain_cd = models.CharField(db_column='TDM0405_SHAIN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tdm0405_uketuke_flg = models.CharField(db_column='TDM0405_UKETUKE_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0405_shonin_flg = models.CharField(db_column='TDM0405_SHONIN_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0405_saishu_shonin_flg = models.CharField(db_column='TDM0405_SAISHU_SHONIN_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0405_del_flg = models.CharField(db_column='TDM0405_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0405_crt_datetime = models.DateTimeField(db_column='TDM0405_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0405_crt_user_id = models.CharField(db_column='TDM0405_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0405_crt_prog_nm = models.CharField(db_column='TDM0405_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0405_upd_datetime = models.DateTimeField(db_column='TDM0405_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0405_upd_user_id = models.CharField(db_column='TDM0405_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0405_upd_prog_nm = models.CharField(db_column='TDM0405_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0405_upd_cnt = models.DecimalField(db_column='TDM0405_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0405_SHAIN_SHONIN_KNGN'


class Tdm0406ShainKaoNinsho(models.Model):
    tdm0406_shain_cd = models.CharField(db_column='TDM0406_SHAIN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tdm0406_file_01 = models.BinaryField(db_column='TDM0406_FILE_01', blank=True, null=True)  # Field name made lowercase.
    tdm0406_file_01_nm = models.CharField(db_column='TDM0406_FILE_01_NM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tdm0406_file_01_kak = models.CharField(db_column='TDM0406_FILE_01_KAK', max_length=11, blank=True, null=True)  # Field name made lowercase.
    tdm0406_del_flg = models.CharField(db_column='TDM0406_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0406_crt_datetime = models.DateTimeField(db_column='TDM0406_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0406_crt_user_id = models.CharField(db_column='TDM0406_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0406_crt_prog_nm = models.CharField(db_column='TDM0406_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0406_upd_datetime = models.DateTimeField(db_column='TDM0406_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0406_upd_user_id = models.CharField(db_column='TDM0406_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0406_upd_prog_nm = models.CharField(db_column='TDM0406_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0406_upd_cnt = models.DecimalField(db_column='TDM0406_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdm0406_file_02 = models.BinaryField(db_column='TDM0406_FILE_02', blank=True, null=True)  # Field name made lowercase.
    tdm0406_file_02_nm = models.CharField(db_column='TDM0406_FILE_02_NM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tdm0406_file_02_kak = models.CharField(db_column='TDM0406_FILE_02_KAK', max_length=11, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0406_SHAIN_KAO_NINSHO'


class Tdm0407ShainKaoNinshoLog(models.Model):
    tdm0407_id = models.AutoField(db_column='TDM0407_ID', primary_key=True)  # Field name made lowercase.
    tdm0407_shian_cd = models.CharField(db_column='TDM0407_SHIAN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tdm0407_shian_nm = models.CharField(db_column='TDM0407_SHIAN_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdm0407_auth_per = models.SmallIntegerField(db_column='TDM0407_AUTH_PER', blank=True, null=True)  # Field name made lowercase.
    tdm0407_auth_result = models.CharField(db_column='TDM0407_AUTH_RESULT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0407_auth_time = models.DateTimeField(db_column='TDM0407_AUTH_TIME', blank=True, null=True)  # Field name made lowercase.
    tdm0407_del_flg = models.CharField(db_column='TDM0407_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0407_crt_datetime = models.DateTimeField(db_column='TDM0407_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0407_crt_user_id = models.CharField(db_column='TDM0407_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0407_crt_prog_nm = models.CharField(db_column='TDM0407_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0407_upd_datetime = models.DateTimeField(db_column='TDM0407_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0407_upd_user_id = models.CharField(db_column='TDM0407_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0407_upd_prog_nm = models.CharField(db_column='TDM0407_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0407_upd_cnt = models.DecimalField(db_column='TDM0407_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0407_SHAIN_KAO_NINSHO_LOG'


class Tdm0408ShugyoYoteiSheet(models.Model):
    tdm0408_genba_cd = models.CharField(db_column='TDM0408_GENBA_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tdm0408_shoku_cd = models.CharField(db_column='TDM0408_SHOKU_CD', max_length=2)  # Field name made lowercase.
    tdm0408_sheet_name = models.CharField(db_column='TDM0408_SHEET_NAME', max_length=100)  # Field name made lowercase.
    tdm0408_del_flg = models.CharField(db_column='TDM0408_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdm0408_crt_datetime = models.DateTimeField(db_column='TDM0408_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0408_crt_user_id = models.CharField(db_column='TDM0408_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0408_crt_prog_nm = models.CharField(db_column='TDM0408_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0408_upd_datetime = models.DateTimeField(db_column='TDM0408_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdm0408_upd_user_id = models.CharField(db_column='TDM0408_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdm0408_upd_prog_nm = models.CharField(db_column='TDM0408_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdm0408_upd_cnt = models.DecimalField(db_column='TDM0408_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDM0408_SHUGYO_YOTEI_SHEET'
        unique_together = (('tdm0408_genba_cd', 'tdm0408_shoku_cd', 'tdm0408_sheet_name'),)


class Tdt0101Bosyu(models.Model):
    tdt0101_genba_cd = models.CharField(db_column='TDT0101_GENBA_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tdt0101_shoku_cd = models.CharField(db_column='TDT0101_SHOKU_CD', max_length=2)  # Field name made lowercase.
    tdt0101_boshuu_date_from = models.DateTimeField(db_column='TDT0101_BOSHUU_DATE_FROM')  # Field name made lowercase.
    tdt0101_boshuu_date_to = models.DateTimeField(db_column='TDT0101_BOSHUU_DATE_TO', blank=True, null=True)  # Field name made lowercase.
    tdt0101_boshu_shime_date = models.DateTimeField(db_column='TDT0101_BOSHU_SHIME_DATE', blank=True, null=True)  # Field name made lowercase.
    tdt0101_chingin = models.CharField(db_column='TDT0101_CHINGIN', max_length=48, blank=True, null=True)  # Field name made lowercase.
    tdt0101_kinmu_taikei = models.CharField(db_column='TDT0101_KINMU_TAIKEI', max_length=48, blank=True, null=True)  # Field name made lowercase.
    tdt0101_kinmu_jikan = models.CharField(db_column='TDT0101_KINMU_JIKAN', max_length=48, blank=True, null=True)  # Field name made lowercase.
    tdt0101_bikou = models.CharField(db_column='TDT0101_BIKOU', max_length=128, blank=True, null=True)  # Field name made lowercase.
    tdt0101_del_flg = models.CharField(db_column='TDT0101_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0101_crt_datetime = models.DateTimeField(db_column='TDT0101_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0101_crt_user_id = models.CharField(db_column='TDT0101_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0101_crt_prog_nm = models.CharField(db_column='TDT0101_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0101_upd_datetime = models.DateTimeField(db_column='TDT0101_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0101_upd_user_id = models.CharField(db_column='TDT0101_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0101_upd_prog_nm = models.CharField(db_column='TDT0101_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0101_upd_cnt = models.DecimalField(db_column='TDT0101_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0101_BOSYU'
        unique_together = (('tdt0101_genba_cd', 'tdt0101_shoku_cd', 'tdt0101_boshuu_date_from'),)


class Tdt0102Oubo(models.Model):
    tdt0102_oubousha_no = models.DecimalField(db_column='TDT0102_OUBOUSHA_NO', primary_key=True, max_digits=10, decimal_places=0)  # Field name made lowercase.
    tdt0102_genba_cd = models.CharField(db_column='TDT0102_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0102_shoku_cd = models.CharField(db_column='TDT0102_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdt0102_boshuu_date_from = models.DateTimeField(db_column='TDT0102_BOSHUU_DATE_FROM', blank=True, null=True)  # Field name made lowercase.
    tdt0102_name = models.CharField(db_column='TDT0102_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdt0102_name_k = models.CharField(db_column='TDT0102_NAME_K', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdt0102_nenrei = models.CharField(db_column='TDT0102_NENREI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdt0102_uketsuke_date = models.DateTimeField(db_column='TDT0102_UKETSUKE_DATE', blank=True, null=True)  # Field name made lowercase.
    tdt0102_uketsuke_shain_cd = models.CharField(db_column='TDT0102_UKETSUKE_SHAIN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tdt0102_mensetsu_datetime = models.DateTimeField(db_column='TDT0102_MENSETSU_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0102_mensetsu_shain_cd = models.CharField(db_column='TDT0102_MENSETSU_SHAIN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tdt0102_gender = models.CharField(db_column='TDT0102_GENDER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0102_post = models.CharField(db_column='TDT0102_POST', max_length=8, blank=True, null=True)  # Field name made lowercase.
    tdt0102_address1 = models.CharField(db_column='TDT0102_ADDRESS1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdt0102_address2 = models.CharField(db_column='TDT0102_ADDRESS2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdt0102_tel1 = models.CharField(db_column='TDT0102_TEL1', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tdt0102_tel2 = models.CharField(db_column='TDT0102_TEL2', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tdt0102_fax = models.CharField(db_column='TDT0102_FAX', max_length=13, blank=True, null=True)  # Field name made lowercase.
    tdt0102_is_marred = models.CharField(db_column='TDT0102_IS_MARRED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0102_fuyou_kbn = models.CharField(db_column='TDT0102_FUYOU_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0102_biko = models.CharField(db_column='TDT0102_BIKO', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tdt0102_kokuseki_cd = models.CharField(db_column='TDT0102_KOKUSEKI_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0102_visa_hoyu = models.CharField(db_column='TDT0102_VISA_HOYU', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0102_drv_license_hoyu = models.CharField(db_column='TDT0102_DRV_LICENSE_HOYU', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0102_tsukin_car = models.CharField(db_column='TDT0102_TSUKIN_CAR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0102_tsukin_autobyc = models.CharField(db_column='TDT0102_TSUKIN_AUTOBYC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0102_tsukin_bus = models.CharField(db_column='TDT0102_TSUKIN_BUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0102_tsukin_byc = models.CharField(db_column='TDT0102_TSUKIN_BYC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0102_tsukin_other = models.CharField(db_column='TDT0102_TSUKIN_OTHER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0102_tsukin_other_biko = models.CharField(db_column='TDT0102_TSUKIN_OTHER_BIKO', max_length=48, blank=True, null=True)  # Field name made lowercase.
    tdt0102_shoubatsu1_date = models.DateTimeField(db_column='TDT0102_SHOUBATSU1_DATE', blank=True, null=True)  # Field name made lowercase.
    tdt0102_shoubatsu1_value = models.CharField(db_column='TDT0102_SHOUBATSU1_VALUE', max_length=48, blank=True, null=True)  # Field name made lowercase.
    tdt0102_shoubatsu2_date = models.DateTimeField(db_column='TDT0102_SHOUBATSU2_DATE', blank=True, null=True)  # Field name made lowercase.
    tdt0102_shoubatsu2_value = models.CharField(db_column='TDT0102_SHOUBATSU2_VALUE', max_length=48, blank=True, null=True)  # Field name made lowercase.
    tdt0102_shouninsha1_cd = models.CharField(db_column='TDT0102_SHOUNINSHA1_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tdt0102_shouninsha2_cd = models.CharField(db_column='TDT0102_SHOUNINSHA2_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tdt0102_saiyou_flg = models.CharField(db_column='TDT0102_SAIYOU_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0102_tsuti_date = models.DateTimeField(db_column='TDT0102_TSUTI_DATE', blank=True, null=True)  # Field name made lowercase.
    tdt0102_del_flg = models.CharField(db_column='TDT0102_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0102_crt_datetime = models.DateTimeField(db_column='TDT0102_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0102_crt_user_id = models.CharField(db_column='TDT0102_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0102_crt_prog_nm = models.CharField(db_column='TDT0102_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0102_upd_datetime = models.DateTimeField(db_column='TDT0102_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0102_upd_prog_nm = models.CharField(db_column='TDT0102_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0102_upd_user_id = models.CharField(db_column='TDT0102_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0102_upd_cnt = models.DecimalField(db_column='TDT0102_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0102_OUBO'


class Tdt0201Kanri(models.Model):
    tdt0201_nendo = models.SmallIntegerField(db_column='TDT0201_NENDO', primary_key=True)  # Field name made lowercase.
    tdt0201_getsudo = models.SmallIntegerField(db_column='TDT0201_GETSUDO')  # Field name made lowercase.
    tdt0201_salary_kbn = models.CharField(db_column='TDT0201_SALARY_KBN', max_length=3)  # Field name made lowercase.
    tdt0201_kakutei_flg = models.CharField(db_column='TDT0201_KAKUTEI_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0201_del_flg = models.CharField(db_column='TDT0201_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0201_crt_datetime = models.DateTimeField(db_column='TDT0201_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0201_crt_user_id = models.CharField(db_column='TDT0201_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0201_crt_prog_nm = models.CharField(db_column='TDT0201_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0201_upd_datetime = models.DateTimeField(db_column='TDT0201_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0201_upd_user_id = models.CharField(db_column='TDT0201_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0201_upd_prog_nm = models.CharField(db_column='TDT0201_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0201_upd_cnt = models.DecimalField(db_column='TDT0201_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdt0201_mail_send_flg = models.CharField(db_column='TDT0201_MAIL_SEND_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0201_KANRI'
        unique_together = (('tdt0201_nendo', 'tdt0201_getsudo', 'tdt0201_salary_kbn'),)


class Tdt0202OutputSet(models.Model):
    tdt0202_shikyu_kbn = models.CharField(db_column='TDT0202_SHIKYU_KBN', primary_key=True, max_length=5)  # Field name made lowercase.
    tdt0202_output_iti = models.SmallIntegerField(db_column='TDT0202_OUTPUT_ITI')  # Field name made lowercase.
    tdt0202_salary_kbn = models.CharField(db_column='TDT0202_SALARY_KBN', max_length=3)  # Field name made lowercase.
    tdt0202_kyuyo_output_kbn = models.CharField(db_column='TDT0202_KYUYO_OUTPUT_KBN', max_length=1)  # Field name made lowercase.
    tdt0202_output_column_nm = models.CharField(db_column='TDT0202_OUTPUT_COLUMN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0202_output_display_nm = models.CharField(db_column='TDT0202_OUTPUT_DISPLAY_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0202_del_flg = models.CharField(db_column='TDT0202_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0202_crt_datetime = models.DateTimeField(db_column='TDT0202_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0202_crt_user_id = models.CharField(db_column='TDT0202_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0202_crt_prog_nm = models.CharField(db_column='TDT0202_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0202_upd_datetime = models.DateTimeField(db_column='TDT0202_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0202_upd_user_id = models.CharField(db_column='TDT0202_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0202_upd_prog_nm = models.CharField(db_column='TDT0202_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0202_upd_cnt = models.DecimalField(db_column='TDT0202_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdt0202_mail_output_kind = models.CharField(db_column='TDT0202_MAIL_OUTPUT_KIND', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0202_kihon_kingaku_flg = models.CharField(db_column='TDT0202_KIHON_KINGAKU_FLG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdt0202_tukin_hi_flg = models.CharField(db_column='TDT0202_TUKIN_HI_FLG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdt0202_hotei_fukuri_hi_flg = models.CharField(db_column='TDT0202_HOTEI_FUKURI_HI_FLG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdt0202_teate_kingaku_flg = models.CharField(db_column='TDT0202_TEATE_KINGAKU_FLG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdt0202_zangyo_warimasi_flg = models.CharField(db_column='TDT0202_ZANGYO_WARIMASI_FLG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdt0202_kyusyutu_warimasi_flg = models.CharField(db_column='TDT0202_KYUSYUTU_WARIMASI_FLG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdt0202_yukyu_kingaku_flg = models.CharField(db_column='TDT0202_YUKYU_KINGAKU_FLG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdt0202_syoyo_kingaku_flg = models.CharField(db_column='TDT0202_SYOYO_KINGAKU_FLG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdt0202_hotei_fukuri_calc_ttl_flg = models.CharField(db_column='TDT0202_HOTEI_FUKURI_CALC_TTL_FLG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdt0202_start_ym = models.CharField(db_column='TDT0202_START_YM', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0202_OUTPUT_SET'
        unique_together = (('tdt0202_shikyu_kbn', 'tdt0202_output_iti', 'tdt0202_salary_kbn', 'tdt0202_kyuyo_output_kbn', 'tdt0202_start_ym'),)


class Tdt0203ShainInfo(models.Model):
    tdt0203_nendo = models.SmallIntegerField(db_column='TDT0203_NENDO', primary_key=True)  # Field name made lowercase.
    tdt0203_getsudo = models.SmallIntegerField(db_column='TDT0203_GETSUDO')  # Field name made lowercase.
    tdt0203_salary_kbn = models.CharField(db_column='TDT0203_SALARY_KBN', max_length=3)  # Field name made lowercase.
    tdt0203_shain_cd = models.CharField(db_column='TDT0203_SHAIN_CD', max_length=10)  # Field name made lowercase.
    tdt0203_shikyu_kbn = models.CharField(db_column='TDT0203_SHIKYU_KBN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0203_shain_nm = models.CharField(db_column='TDT0203_SHAIN_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdt0203_mail_send_flg = models.CharField(db_column='TDT0203_MAIL_SEND_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0203_del_flg = models.CharField(db_column='TDT0203_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0203_crt_datetime = models.DateTimeField(db_column='TDT0203_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0203_crt_user_id = models.CharField(db_column='TDT0203_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0203_crt_prog_nm = models.CharField(db_column='TDT0203_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0203_upd_datetime = models.DateTimeField(db_column='TDT0203_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0203_upd_user_id = models.CharField(db_column='TDT0203_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0203_upd_prog_nm = models.CharField(db_column='TDT0203_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0203_upd_cnt = models.DecimalField(db_column='TDT0203_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0203_SHAIN_INFO'
        unique_together = (('tdt0203_nendo', 'tdt0203_getsudo', 'tdt0203_salary_kbn', 'tdt0203_shain_cd'),)


class Tdt0204SalaryTitle(models.Model):
    tdt0203_nendo = models.SmallIntegerField(db_column='TDT0203_NENDO', primary_key=True)  # Field name made lowercase.
    tdt0203_getsudo = models.SmallIntegerField(db_column='TDT0203_GETSUDO')  # Field name made lowercase.
    tdt0203_salary_kbn = models.CharField(db_column='TDT0203_SALARY_KBN', max_length=3)  # Field name made lowercase.
    tdt0204_shikyu_kbn = models.CharField(db_column='TDT0204_SHIKYU_KBN', max_length=5)  # Field name made lowercase.
    tdt0204_column_id = models.SmallIntegerField(db_column='TDT0204_COLUMN_ID')  # Field name made lowercase.
    tdt0204_column_nm = models.CharField(db_column='TDT0204_COLUMN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0204_del_flg = models.CharField(db_column='TDT0204_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0204_crt_datetime = models.DateTimeField(db_column='TDT0204_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0204_crt_user_id = models.CharField(db_column='TDT0204_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0204_crt_prog_nm = models.CharField(db_column='TDT0204_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0204_upd_datetime = models.DateTimeField(db_column='TDT0204_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0204_upd_user_id = models.CharField(db_column='TDT0204_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0204_upd_prog_nm = models.CharField(db_column='TDT0204_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0204_upd_cnt = models.DecimalField(db_column='TDT0204_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0204_SALARY_TITLE'
        unique_together = (('tdt0203_nendo', 'tdt0203_getsudo', 'tdt0203_salary_kbn', 'tdt0204_shikyu_kbn', 'tdt0204_column_id'),)


class Tdt0205SalaryDetails(models.Model):
    tdt0203_nendo = models.SmallIntegerField(db_column='TDT0203_NENDO', primary_key=True)  # Field name made lowercase.
    tdt0203_getsudo = models.SmallIntegerField(db_column='TDT0203_GETSUDO')  # Field name made lowercase.
    tdt0203_salary_kbn = models.CharField(db_column='TDT0203_SALARY_KBN', max_length=3)  # Field name made lowercase.
    tdt0203_shain_cd = models.CharField(db_column='TDT0203_SHAIN_CD', max_length=10)  # Field name made lowercase.
    tdt0204_shikyu_kbn = models.CharField(db_column='TDT0204_SHIKYU_KBN', max_length=5)  # Field name made lowercase.
    tdt0204_column_id = models.SmallIntegerField(db_column='TDT0204_COLUMN_ID')  # Field name made lowercase.
    tdt0205_column_nm = models.CharField(db_column='TDT0205_COLUMN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0205_del_flg = models.CharField(db_column='TDT0205_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0205_crt_datetime = models.DateTimeField(db_column='TDT0205_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0205_crt_user_id = models.CharField(db_column='TDT0205_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0205_crt_prog_nm = models.CharField(db_column='TDT0205_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0205_upd_datetime = models.DateTimeField(db_column='TDT0205_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0205_upd_user_id = models.CharField(db_column='TDT0205_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0205_upd_prog_nm = models.CharField(db_column='TDT0205_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0205_upd_cnt = models.DecimalField(db_column='TDT0205_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0205_SALARY_DETAILS'
        unique_together = (('tdt0203_nendo', 'tdt0203_getsudo', 'tdt0203_salary_kbn', 'tdt0203_shain_cd', 'tdt0204_shikyu_kbn', 'tdt0204_column_id'),)


class Tdt0206SalaryTitleHrzn(models.Model):
    tdt0203_nendo = models.SmallIntegerField(db_column='TDT0203_NENDO', primary_key=True)  # Field name made lowercase.
    tdt0203_getsudo = models.SmallIntegerField(db_column='TDT0203_GETSUDO')  # Field name made lowercase.
    tdt0203_salary_kbn = models.CharField(db_column='TDT0203_SALARY_KBN', max_length=3)  # Field name made lowercase.
    tdt0204_shikyu_kbn = models.CharField(db_column='TDT0204_SHIKYU_KBN', max_length=5)  # Field name made lowercase.
    tdt0206_column_nm_1 = models.CharField(db_column='TDT0206_COLUMN_NM_1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_2 = models.CharField(db_column='TDT0206_COLUMN_NM_2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_3 = models.CharField(db_column='TDT0206_COLUMN_NM_3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_4 = models.CharField(db_column='TDT0206_COLUMN_NM_4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_5 = models.CharField(db_column='TDT0206_COLUMN_NM_5', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_6 = models.CharField(db_column='TDT0206_COLUMN_NM_6', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_7 = models.CharField(db_column='TDT0206_COLUMN_NM_7', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_8 = models.CharField(db_column='TDT0206_COLUMN_NM_8', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_9 = models.CharField(db_column='TDT0206_COLUMN_NM_9', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_10 = models.CharField(db_column='TDT0206_COLUMN_NM_10', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_11 = models.CharField(db_column='TDT0206_COLUMN_NM_11', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_12 = models.CharField(db_column='TDT0206_COLUMN_NM_12', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_13 = models.CharField(db_column='TDT0206_COLUMN_NM_13', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_14 = models.CharField(db_column='TDT0206_COLUMN_NM_14', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_15 = models.CharField(db_column='TDT0206_COLUMN_NM_15', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_16 = models.CharField(db_column='TDT0206_COLUMN_NM_16', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_17 = models.CharField(db_column='TDT0206_COLUMN_NM_17', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_18 = models.CharField(db_column='TDT0206_COLUMN_NM_18', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_19 = models.CharField(db_column='TDT0206_COLUMN_NM_19', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_20 = models.CharField(db_column='TDT0206_COLUMN_NM_20', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_21 = models.CharField(db_column='TDT0206_COLUMN_NM_21', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_22 = models.CharField(db_column='TDT0206_COLUMN_NM_22', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_23 = models.CharField(db_column='TDT0206_COLUMN_NM_23', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_24 = models.CharField(db_column='TDT0206_COLUMN_NM_24', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_25 = models.CharField(db_column='TDT0206_COLUMN_NM_25', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_26 = models.CharField(db_column='TDT0206_COLUMN_NM_26', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_27 = models.CharField(db_column='TDT0206_COLUMN_NM_27', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_28 = models.CharField(db_column='TDT0206_COLUMN_NM_28', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_29 = models.CharField(db_column='TDT0206_COLUMN_NM_29', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_30 = models.CharField(db_column='TDT0206_COLUMN_NM_30', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_31 = models.CharField(db_column='TDT0206_COLUMN_NM_31', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_32 = models.CharField(db_column='TDT0206_COLUMN_NM_32', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_33 = models.CharField(db_column='TDT0206_COLUMN_NM_33', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_34 = models.CharField(db_column='TDT0206_COLUMN_NM_34', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_35 = models.CharField(db_column='TDT0206_COLUMN_NM_35', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_36 = models.CharField(db_column='TDT0206_COLUMN_NM_36', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_37 = models.CharField(db_column='TDT0206_COLUMN_NM_37', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_38 = models.CharField(db_column='TDT0206_COLUMN_NM_38', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_39 = models.CharField(db_column='TDT0206_COLUMN_NM_39', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_40 = models.CharField(db_column='TDT0206_COLUMN_NM_40', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_41 = models.CharField(db_column='TDT0206_COLUMN_NM_41', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_42 = models.CharField(db_column='TDT0206_COLUMN_NM_42', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_43 = models.CharField(db_column='TDT0206_COLUMN_NM_43', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_44 = models.CharField(db_column='TDT0206_COLUMN_NM_44', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_45 = models.CharField(db_column='TDT0206_COLUMN_NM_45', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_46 = models.CharField(db_column='TDT0206_COLUMN_NM_46', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_47 = models.CharField(db_column='TDT0206_COLUMN_NM_47', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_48 = models.CharField(db_column='TDT0206_COLUMN_NM_48', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_49 = models.CharField(db_column='TDT0206_COLUMN_NM_49', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_50 = models.CharField(db_column='TDT0206_COLUMN_NM_50', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_51 = models.CharField(db_column='TDT0206_COLUMN_NM_51', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_52 = models.CharField(db_column='TDT0206_COLUMN_NM_52', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_53 = models.CharField(db_column='TDT0206_COLUMN_NM_53', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_54 = models.CharField(db_column='TDT0206_COLUMN_NM_54', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_55 = models.CharField(db_column='TDT0206_COLUMN_NM_55', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_56 = models.CharField(db_column='TDT0206_COLUMN_NM_56', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_57 = models.CharField(db_column='TDT0206_COLUMN_NM_57', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_58 = models.CharField(db_column='TDT0206_COLUMN_NM_58', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_59 = models.CharField(db_column='TDT0206_COLUMN_NM_59', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_60 = models.CharField(db_column='TDT0206_COLUMN_NM_60', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_61 = models.CharField(db_column='TDT0206_COLUMN_NM_61', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_62 = models.CharField(db_column='TDT0206_COLUMN_NM_62', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_63 = models.CharField(db_column='TDT0206_COLUMN_NM_63', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_64 = models.CharField(db_column='TDT0206_COLUMN_NM_64', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_65 = models.CharField(db_column='TDT0206_COLUMN_NM_65', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_66 = models.CharField(db_column='TDT0206_COLUMN_NM_66', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_67 = models.CharField(db_column='TDT0206_COLUMN_NM_67', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_68 = models.CharField(db_column='TDT0206_COLUMN_NM_68', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_69 = models.CharField(db_column='TDT0206_COLUMN_NM_69', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_70 = models.CharField(db_column='TDT0206_COLUMN_NM_70', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_71 = models.CharField(db_column='TDT0206_COLUMN_NM_71', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_72 = models.CharField(db_column='TDT0206_COLUMN_NM_72', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_73 = models.CharField(db_column='TDT0206_COLUMN_NM_73', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_74 = models.CharField(db_column='TDT0206_COLUMN_NM_74', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_75 = models.CharField(db_column='TDT0206_COLUMN_NM_75', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_76 = models.CharField(db_column='TDT0206_COLUMN_NM_76', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_77 = models.CharField(db_column='TDT0206_COLUMN_NM_77', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_78 = models.CharField(db_column='TDT0206_COLUMN_NM_78', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_79 = models.CharField(db_column='TDT0206_COLUMN_NM_79', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_80 = models.CharField(db_column='TDT0206_COLUMN_NM_80', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_81 = models.CharField(db_column='TDT0206_COLUMN_NM_81', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_82 = models.CharField(db_column='TDT0206_COLUMN_NM_82', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_83 = models.CharField(db_column='TDT0206_COLUMN_NM_83', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_84 = models.CharField(db_column='TDT0206_COLUMN_NM_84', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_85 = models.CharField(db_column='TDT0206_COLUMN_NM_85', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_86 = models.CharField(db_column='TDT0206_COLUMN_NM_86', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_87 = models.CharField(db_column='TDT0206_COLUMN_NM_87', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_88 = models.CharField(db_column='TDT0206_COLUMN_NM_88', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_89 = models.CharField(db_column='TDT0206_COLUMN_NM_89', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_90 = models.CharField(db_column='TDT0206_COLUMN_NM_90', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_91 = models.CharField(db_column='TDT0206_COLUMN_NM_91', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_92 = models.CharField(db_column='TDT0206_COLUMN_NM_92', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_93 = models.CharField(db_column='TDT0206_COLUMN_NM_93', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_94 = models.CharField(db_column='TDT0206_COLUMN_NM_94', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_95 = models.CharField(db_column='TDT0206_COLUMN_NM_95', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_96 = models.CharField(db_column='TDT0206_COLUMN_NM_96', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_97 = models.CharField(db_column='TDT0206_COLUMN_NM_97', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_98 = models.CharField(db_column='TDT0206_COLUMN_NM_98', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_99 = models.CharField(db_column='TDT0206_COLUMN_NM_99', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_100 = models.CharField(db_column='TDT0206_COLUMN_NM_100', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_101 = models.CharField(db_column='TDT0206_COLUMN_NM_101', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_102 = models.CharField(db_column='TDT0206_COLUMN_NM_102', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_103 = models.CharField(db_column='TDT0206_COLUMN_NM_103', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_104 = models.CharField(db_column='TDT0206_COLUMN_NM_104', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_105 = models.CharField(db_column='TDT0206_COLUMN_NM_105', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_106 = models.CharField(db_column='TDT0206_COLUMN_NM_106', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_107 = models.CharField(db_column='TDT0206_COLUMN_NM_107', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_108 = models.CharField(db_column='TDT0206_COLUMN_NM_108', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_109 = models.CharField(db_column='TDT0206_COLUMN_NM_109', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_110 = models.CharField(db_column='TDT0206_COLUMN_NM_110', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_111 = models.CharField(db_column='TDT0206_COLUMN_NM_111', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_112 = models.CharField(db_column='TDT0206_COLUMN_NM_112', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_113 = models.CharField(db_column='TDT0206_COLUMN_NM_113', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_114 = models.CharField(db_column='TDT0206_COLUMN_NM_114', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_115 = models.CharField(db_column='TDT0206_COLUMN_NM_115', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_116 = models.CharField(db_column='TDT0206_COLUMN_NM_116', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_117 = models.CharField(db_column='TDT0206_COLUMN_NM_117', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_118 = models.CharField(db_column='TDT0206_COLUMN_NM_118', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_119 = models.CharField(db_column='TDT0206_COLUMN_NM_119', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_120 = models.CharField(db_column='TDT0206_COLUMN_NM_120', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_121 = models.CharField(db_column='TDT0206_COLUMN_NM_121', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_122 = models.CharField(db_column='TDT0206_COLUMN_NM_122', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_123 = models.CharField(db_column='TDT0206_COLUMN_NM_123', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_124 = models.CharField(db_column='TDT0206_COLUMN_NM_124', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_125 = models.CharField(db_column='TDT0206_COLUMN_NM_125', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_126 = models.CharField(db_column='TDT0206_COLUMN_NM_126', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_127 = models.CharField(db_column='TDT0206_COLUMN_NM_127', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_128 = models.CharField(db_column='TDT0206_COLUMN_NM_128', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_129 = models.CharField(db_column='TDT0206_COLUMN_NM_129', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_130 = models.CharField(db_column='TDT0206_COLUMN_NM_130', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_131 = models.CharField(db_column='TDT0206_COLUMN_NM_131', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_132 = models.CharField(db_column='TDT0206_COLUMN_NM_132', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_133 = models.CharField(db_column='TDT0206_COLUMN_NM_133', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_134 = models.CharField(db_column='TDT0206_COLUMN_NM_134', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_135 = models.CharField(db_column='TDT0206_COLUMN_NM_135', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_136 = models.CharField(db_column='TDT0206_COLUMN_NM_136', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_137 = models.CharField(db_column='TDT0206_COLUMN_NM_137', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_138 = models.CharField(db_column='TDT0206_COLUMN_NM_138', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_139 = models.CharField(db_column='TDT0206_COLUMN_NM_139', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_140 = models.CharField(db_column='TDT0206_COLUMN_NM_140', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_141 = models.CharField(db_column='TDT0206_COLUMN_NM_141', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_142 = models.CharField(db_column='TDT0206_COLUMN_NM_142', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_143 = models.CharField(db_column='TDT0206_COLUMN_NM_143', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_144 = models.CharField(db_column='TDT0206_COLUMN_NM_144', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_145 = models.CharField(db_column='TDT0206_COLUMN_NM_145', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_146 = models.CharField(db_column='TDT0206_COLUMN_NM_146', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_147 = models.CharField(db_column='TDT0206_COLUMN_NM_147', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_148 = models.CharField(db_column='TDT0206_COLUMN_NM_148', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_149 = models.CharField(db_column='TDT0206_COLUMN_NM_149', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_150 = models.CharField(db_column='TDT0206_COLUMN_NM_150', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_151 = models.CharField(db_column='TDT0206_COLUMN_NM_151', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_152 = models.CharField(db_column='TDT0206_COLUMN_NM_152', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_153 = models.CharField(db_column='TDT0206_COLUMN_NM_153', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_154 = models.CharField(db_column='TDT0206_COLUMN_NM_154', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_155 = models.CharField(db_column='TDT0206_COLUMN_NM_155', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_156 = models.CharField(db_column='TDT0206_COLUMN_NM_156', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_157 = models.CharField(db_column='TDT0206_COLUMN_NM_157', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_158 = models.CharField(db_column='TDT0206_COLUMN_NM_158', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_159 = models.CharField(db_column='TDT0206_COLUMN_NM_159', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_160 = models.CharField(db_column='TDT0206_COLUMN_NM_160', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_161 = models.CharField(db_column='TDT0206_COLUMN_NM_161', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_162 = models.CharField(db_column='TDT0206_COLUMN_NM_162', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_163 = models.CharField(db_column='TDT0206_COLUMN_NM_163', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_164 = models.CharField(db_column='TDT0206_COLUMN_NM_164', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_165 = models.CharField(db_column='TDT0206_COLUMN_NM_165', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_166 = models.CharField(db_column='TDT0206_COLUMN_NM_166', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_167 = models.CharField(db_column='TDT0206_COLUMN_NM_167', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_168 = models.CharField(db_column='TDT0206_COLUMN_NM_168', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_169 = models.CharField(db_column='TDT0206_COLUMN_NM_169', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_170 = models.CharField(db_column='TDT0206_COLUMN_NM_170', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_171 = models.CharField(db_column='TDT0206_COLUMN_NM_171', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_172 = models.CharField(db_column='TDT0206_COLUMN_NM_172', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_173 = models.CharField(db_column='TDT0206_COLUMN_NM_173', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_174 = models.CharField(db_column='TDT0206_COLUMN_NM_174', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_175 = models.CharField(db_column='TDT0206_COLUMN_NM_175', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_176 = models.CharField(db_column='TDT0206_COLUMN_NM_176', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_177 = models.CharField(db_column='TDT0206_COLUMN_NM_177', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_178 = models.CharField(db_column='TDT0206_COLUMN_NM_178', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_179 = models.CharField(db_column='TDT0206_COLUMN_NM_179', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_180 = models.CharField(db_column='TDT0206_COLUMN_NM_180', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_181 = models.CharField(db_column='TDT0206_COLUMN_NM_181', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_182 = models.CharField(db_column='TDT0206_COLUMN_NM_182', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_183 = models.CharField(db_column='TDT0206_COLUMN_NM_183', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_184 = models.CharField(db_column='TDT0206_COLUMN_NM_184', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_185 = models.CharField(db_column='TDT0206_COLUMN_NM_185', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_186 = models.CharField(db_column='TDT0206_COLUMN_NM_186', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_187 = models.CharField(db_column='TDT0206_COLUMN_NM_187', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_188 = models.CharField(db_column='TDT0206_COLUMN_NM_188', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_189 = models.CharField(db_column='TDT0206_COLUMN_NM_189', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_190 = models.CharField(db_column='TDT0206_COLUMN_NM_190', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_191 = models.CharField(db_column='TDT0206_COLUMN_NM_191', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_192 = models.CharField(db_column='TDT0206_COLUMN_NM_192', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_193 = models.CharField(db_column='TDT0206_COLUMN_NM_193', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_194 = models.CharField(db_column='TDT0206_COLUMN_NM_194', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_195 = models.CharField(db_column='TDT0206_COLUMN_NM_195', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_196 = models.CharField(db_column='TDT0206_COLUMN_NM_196', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_197 = models.CharField(db_column='TDT0206_COLUMN_NM_197', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_198 = models.CharField(db_column='TDT0206_COLUMN_NM_198', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_199 = models.CharField(db_column='TDT0206_COLUMN_NM_199', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_column_nm_200 = models.CharField(db_column='TDT0206_COLUMN_NM_200', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_del_flg = models.CharField(db_column='TDT0206_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0206_crt_datetime = models.DateTimeField(db_column='TDT0206_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0206_crt_user_id = models.CharField(db_column='TDT0206_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0206_crt_prog_nm = models.CharField(db_column='TDT0206_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_upd_datetime = models.DateTimeField(db_column='TDT0206_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0206_upd_user_id = models.CharField(db_column='TDT0206_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0206_upd_prog_nm = models.CharField(db_column='TDT0206_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0206_upd_cnt = models.DecimalField(db_column='TDT0206_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0206_SALARY_TITLE_HRZN'
        unique_together = (('tdt0203_nendo', 'tdt0203_getsudo', 'tdt0203_salary_kbn', 'tdt0204_shikyu_kbn'),)


class Tdt0207SalaryDetailsHrzn(models.Model):
    tdt0203_nendo = models.SmallIntegerField(db_column='TDT0203_NENDO', primary_key=True)  # Field name made lowercase.
    tdt0203_getsudo = models.SmallIntegerField(db_column='TDT0203_GETSUDO')  # Field name made lowercase.
    tdt0203_salary_kbn = models.CharField(db_column='TDT0203_SALARY_KBN', max_length=3)  # Field name made lowercase.
    tdt0203_shain_cd = models.CharField(db_column='TDT0203_SHAIN_CD', max_length=10)  # Field name made lowercase.
    tdt0204_shikyu_kbn = models.CharField(db_column='TDT0204_SHIKYU_KBN', max_length=5)  # Field name made lowercase.
    tdt0207_column_nm_1 = models.CharField(db_column='TDT0207_COLUMN_NM_1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_2 = models.CharField(db_column='TDT0207_COLUMN_NM_2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_3 = models.CharField(db_column='TDT0207_COLUMN_NM_3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_4 = models.CharField(db_column='TDT0207_COLUMN_NM_4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_5 = models.CharField(db_column='TDT0207_COLUMN_NM_5', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_6 = models.CharField(db_column='TDT0207_COLUMN_NM_6', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_7 = models.CharField(db_column='TDT0207_COLUMN_NM_7', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_8 = models.CharField(db_column='TDT0207_COLUMN_NM_8', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_9 = models.CharField(db_column='TDT0207_COLUMN_NM_9', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_10 = models.CharField(db_column='TDT0207_COLUMN_NM_10', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_11 = models.CharField(db_column='TDT0207_COLUMN_NM_11', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_12 = models.CharField(db_column='TDT0207_COLUMN_NM_12', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_13 = models.CharField(db_column='TDT0207_COLUMN_NM_13', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_14 = models.CharField(db_column='TDT0207_COLUMN_NM_14', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_15 = models.CharField(db_column='TDT0207_COLUMN_NM_15', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_16 = models.CharField(db_column='TDT0207_COLUMN_NM_16', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_17 = models.CharField(db_column='TDT0207_COLUMN_NM_17', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_18 = models.CharField(db_column='TDT0207_COLUMN_NM_18', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_19 = models.CharField(db_column='TDT0207_COLUMN_NM_19', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_20 = models.CharField(db_column='TDT0207_COLUMN_NM_20', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_21 = models.CharField(db_column='TDT0207_COLUMN_NM_21', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_22 = models.CharField(db_column='TDT0207_COLUMN_NM_22', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_23 = models.CharField(db_column='TDT0207_COLUMN_NM_23', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_24 = models.CharField(db_column='TDT0207_COLUMN_NM_24', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_25 = models.CharField(db_column='TDT0207_COLUMN_NM_25', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_26 = models.CharField(db_column='TDT0207_COLUMN_NM_26', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_27 = models.CharField(db_column='TDT0207_COLUMN_NM_27', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_28 = models.CharField(db_column='TDT0207_COLUMN_NM_28', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_29 = models.CharField(db_column='TDT0207_COLUMN_NM_29', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_30 = models.CharField(db_column='TDT0207_COLUMN_NM_30', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_31 = models.CharField(db_column='TDT0207_COLUMN_NM_31', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_32 = models.CharField(db_column='TDT0207_COLUMN_NM_32', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_33 = models.CharField(db_column='TDT0207_COLUMN_NM_33', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_34 = models.CharField(db_column='TDT0207_COLUMN_NM_34', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_35 = models.CharField(db_column='TDT0207_COLUMN_NM_35', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_36 = models.CharField(db_column='TDT0207_COLUMN_NM_36', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_37 = models.CharField(db_column='TDT0207_COLUMN_NM_37', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_38 = models.CharField(db_column='TDT0207_COLUMN_NM_38', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_39 = models.CharField(db_column='TDT0207_COLUMN_NM_39', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_40 = models.CharField(db_column='TDT0207_COLUMN_NM_40', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_41 = models.CharField(db_column='TDT0207_COLUMN_NM_41', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_42 = models.CharField(db_column='TDT0207_COLUMN_NM_42', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_43 = models.CharField(db_column='TDT0207_COLUMN_NM_43', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_44 = models.CharField(db_column='TDT0207_COLUMN_NM_44', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_45 = models.CharField(db_column='TDT0207_COLUMN_NM_45', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_46 = models.CharField(db_column='TDT0207_COLUMN_NM_46', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_47 = models.CharField(db_column='TDT0207_COLUMN_NM_47', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_48 = models.CharField(db_column='TDT0207_COLUMN_NM_48', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_49 = models.CharField(db_column='TDT0207_COLUMN_NM_49', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_50 = models.CharField(db_column='TDT0207_COLUMN_NM_50', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_51 = models.CharField(db_column='TDT0207_COLUMN_NM_51', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_52 = models.CharField(db_column='TDT0207_COLUMN_NM_52', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_53 = models.CharField(db_column='TDT0207_COLUMN_NM_53', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_54 = models.CharField(db_column='TDT0207_COLUMN_NM_54', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_55 = models.CharField(db_column='TDT0207_COLUMN_NM_55', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_56 = models.CharField(db_column='TDT0207_COLUMN_NM_56', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_57 = models.CharField(db_column='TDT0207_COLUMN_NM_57', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_58 = models.CharField(db_column='TDT0207_COLUMN_NM_58', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_59 = models.CharField(db_column='TDT0207_COLUMN_NM_59', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_60 = models.CharField(db_column='TDT0207_COLUMN_NM_60', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_61 = models.CharField(db_column='TDT0207_COLUMN_NM_61', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_62 = models.CharField(db_column='TDT0207_COLUMN_NM_62', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_63 = models.CharField(db_column='TDT0207_COLUMN_NM_63', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_64 = models.CharField(db_column='TDT0207_COLUMN_NM_64', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_65 = models.CharField(db_column='TDT0207_COLUMN_NM_65', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_66 = models.CharField(db_column='TDT0207_COLUMN_NM_66', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_67 = models.CharField(db_column='TDT0207_COLUMN_NM_67', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_68 = models.CharField(db_column='TDT0207_COLUMN_NM_68', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_69 = models.CharField(db_column='TDT0207_COLUMN_NM_69', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_70 = models.CharField(db_column='TDT0207_COLUMN_NM_70', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_71 = models.CharField(db_column='TDT0207_COLUMN_NM_71', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_72 = models.CharField(db_column='TDT0207_COLUMN_NM_72', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_73 = models.CharField(db_column='TDT0207_COLUMN_NM_73', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_74 = models.CharField(db_column='TDT0207_COLUMN_NM_74', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_75 = models.CharField(db_column='TDT0207_COLUMN_NM_75', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_76 = models.CharField(db_column='TDT0207_COLUMN_NM_76', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_77 = models.CharField(db_column='TDT0207_COLUMN_NM_77', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_78 = models.CharField(db_column='TDT0207_COLUMN_NM_78', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_79 = models.CharField(db_column='TDT0207_COLUMN_NM_79', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_80 = models.CharField(db_column='TDT0207_COLUMN_NM_80', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_81 = models.CharField(db_column='TDT0207_COLUMN_NM_81', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_82 = models.CharField(db_column='TDT0207_COLUMN_NM_82', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_83 = models.CharField(db_column='TDT0207_COLUMN_NM_83', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_84 = models.CharField(db_column='TDT0207_COLUMN_NM_84', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_85 = models.CharField(db_column='TDT0207_COLUMN_NM_85', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_86 = models.CharField(db_column='TDT0207_COLUMN_NM_86', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_87 = models.CharField(db_column='TDT0207_COLUMN_NM_87', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_88 = models.CharField(db_column='TDT0207_COLUMN_NM_88', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_89 = models.CharField(db_column='TDT0207_COLUMN_NM_89', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_90 = models.CharField(db_column='TDT0207_COLUMN_NM_90', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_91 = models.CharField(db_column='TDT0207_COLUMN_NM_91', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_92 = models.CharField(db_column='TDT0207_COLUMN_NM_92', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_93 = models.CharField(db_column='TDT0207_COLUMN_NM_93', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_94 = models.CharField(db_column='TDT0207_COLUMN_NM_94', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_95 = models.CharField(db_column='TDT0207_COLUMN_NM_95', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_96 = models.CharField(db_column='TDT0207_COLUMN_NM_96', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_97 = models.CharField(db_column='TDT0207_COLUMN_NM_97', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_98 = models.CharField(db_column='TDT0207_COLUMN_NM_98', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_99 = models.CharField(db_column='TDT0207_COLUMN_NM_99', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_100 = models.CharField(db_column='TDT0207_COLUMN_NM_100', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_101 = models.CharField(db_column='TDT0207_COLUMN_NM_101', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_102 = models.CharField(db_column='TDT0207_COLUMN_NM_102', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_103 = models.CharField(db_column='TDT0207_COLUMN_NM_103', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_104 = models.CharField(db_column='TDT0207_COLUMN_NM_104', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_105 = models.CharField(db_column='TDT0207_COLUMN_NM_105', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_106 = models.CharField(db_column='TDT0207_COLUMN_NM_106', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_107 = models.CharField(db_column='TDT0207_COLUMN_NM_107', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_108 = models.CharField(db_column='TDT0207_COLUMN_NM_108', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_109 = models.CharField(db_column='TDT0207_COLUMN_NM_109', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_110 = models.CharField(db_column='TDT0207_COLUMN_NM_110', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_111 = models.CharField(db_column='TDT0207_COLUMN_NM_111', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_112 = models.CharField(db_column='TDT0207_COLUMN_NM_112', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_113 = models.CharField(db_column='TDT0207_COLUMN_NM_113', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_114 = models.CharField(db_column='TDT0207_COLUMN_NM_114', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_115 = models.CharField(db_column='TDT0207_COLUMN_NM_115', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_116 = models.CharField(db_column='TDT0207_COLUMN_NM_116', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_117 = models.CharField(db_column='TDT0207_COLUMN_NM_117', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_118 = models.CharField(db_column='TDT0207_COLUMN_NM_118', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_119 = models.CharField(db_column='TDT0207_COLUMN_NM_119', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_120 = models.CharField(db_column='TDT0207_COLUMN_NM_120', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_121 = models.CharField(db_column='TDT0207_COLUMN_NM_121', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_122 = models.CharField(db_column='TDT0207_COLUMN_NM_122', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_123 = models.CharField(db_column='TDT0207_COLUMN_NM_123', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_124 = models.CharField(db_column='TDT0207_COLUMN_NM_124', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_125 = models.CharField(db_column='TDT0207_COLUMN_NM_125', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_126 = models.CharField(db_column='TDT0207_COLUMN_NM_126', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_127 = models.CharField(db_column='TDT0207_COLUMN_NM_127', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_128 = models.CharField(db_column='TDT0207_COLUMN_NM_128', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_129 = models.CharField(db_column='TDT0207_COLUMN_NM_129', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_130 = models.CharField(db_column='TDT0207_COLUMN_NM_130', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_131 = models.CharField(db_column='TDT0207_COLUMN_NM_131', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_132 = models.CharField(db_column='TDT0207_COLUMN_NM_132', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_133 = models.CharField(db_column='TDT0207_COLUMN_NM_133', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_134 = models.CharField(db_column='TDT0207_COLUMN_NM_134', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_135 = models.CharField(db_column='TDT0207_COLUMN_NM_135', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_136 = models.CharField(db_column='TDT0207_COLUMN_NM_136', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_137 = models.CharField(db_column='TDT0207_COLUMN_NM_137', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_138 = models.CharField(db_column='TDT0207_COLUMN_NM_138', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_139 = models.CharField(db_column='TDT0207_COLUMN_NM_139', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_140 = models.CharField(db_column='TDT0207_COLUMN_NM_140', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_141 = models.CharField(db_column='TDT0207_COLUMN_NM_141', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_142 = models.CharField(db_column='TDT0207_COLUMN_NM_142', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_143 = models.CharField(db_column='TDT0207_COLUMN_NM_143', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_144 = models.CharField(db_column='TDT0207_COLUMN_NM_144', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_145 = models.CharField(db_column='TDT0207_COLUMN_NM_145', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_146 = models.CharField(db_column='TDT0207_COLUMN_NM_146', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_147 = models.CharField(db_column='TDT0207_COLUMN_NM_147', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_148 = models.CharField(db_column='TDT0207_COLUMN_NM_148', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_149 = models.CharField(db_column='TDT0207_COLUMN_NM_149', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_150 = models.CharField(db_column='TDT0207_COLUMN_NM_150', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_151 = models.CharField(db_column='TDT0207_COLUMN_NM_151', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_152 = models.CharField(db_column='TDT0207_COLUMN_NM_152', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_153 = models.CharField(db_column='TDT0207_COLUMN_NM_153', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_154 = models.CharField(db_column='TDT0207_COLUMN_NM_154', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_155 = models.CharField(db_column='TDT0207_COLUMN_NM_155', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_156 = models.CharField(db_column='TDT0207_COLUMN_NM_156', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_157 = models.CharField(db_column='TDT0207_COLUMN_NM_157', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_158 = models.CharField(db_column='TDT0207_COLUMN_NM_158', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_159 = models.CharField(db_column='TDT0207_COLUMN_NM_159', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_160 = models.CharField(db_column='TDT0207_COLUMN_NM_160', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_161 = models.CharField(db_column='TDT0207_COLUMN_NM_161', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_162 = models.CharField(db_column='TDT0207_COLUMN_NM_162', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_163 = models.CharField(db_column='TDT0207_COLUMN_NM_163', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_164 = models.CharField(db_column='TDT0207_COLUMN_NM_164', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_165 = models.CharField(db_column='TDT0207_COLUMN_NM_165', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_166 = models.CharField(db_column='TDT0207_COLUMN_NM_166', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_167 = models.CharField(db_column='TDT0207_COLUMN_NM_167', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_168 = models.CharField(db_column='TDT0207_COLUMN_NM_168', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_169 = models.CharField(db_column='TDT0207_COLUMN_NM_169', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_170 = models.CharField(db_column='TDT0207_COLUMN_NM_170', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_171 = models.CharField(db_column='TDT0207_COLUMN_NM_171', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_172 = models.CharField(db_column='TDT0207_COLUMN_NM_172', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_173 = models.CharField(db_column='TDT0207_COLUMN_NM_173', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_174 = models.CharField(db_column='TDT0207_COLUMN_NM_174', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_175 = models.CharField(db_column='TDT0207_COLUMN_NM_175', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_176 = models.CharField(db_column='TDT0207_COLUMN_NM_176', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_177 = models.CharField(db_column='TDT0207_COLUMN_NM_177', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_178 = models.CharField(db_column='TDT0207_COLUMN_NM_178', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_179 = models.CharField(db_column='TDT0207_COLUMN_NM_179', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_180 = models.CharField(db_column='TDT0207_COLUMN_NM_180', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_181 = models.CharField(db_column='TDT0207_COLUMN_NM_181', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_182 = models.CharField(db_column='TDT0207_COLUMN_NM_182', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_183 = models.CharField(db_column='TDT0207_COLUMN_NM_183', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_184 = models.CharField(db_column='TDT0207_COLUMN_NM_184', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_185 = models.CharField(db_column='TDT0207_COLUMN_NM_185', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_186 = models.CharField(db_column='TDT0207_COLUMN_NM_186', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_187 = models.CharField(db_column='TDT0207_COLUMN_NM_187', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_188 = models.CharField(db_column='TDT0207_COLUMN_NM_188', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_189 = models.CharField(db_column='TDT0207_COLUMN_NM_189', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_190 = models.CharField(db_column='TDT0207_COLUMN_NM_190', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_191 = models.CharField(db_column='TDT0207_COLUMN_NM_191', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_192 = models.CharField(db_column='TDT0207_COLUMN_NM_192', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_193 = models.CharField(db_column='TDT0207_COLUMN_NM_193', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_194 = models.CharField(db_column='TDT0207_COLUMN_NM_194', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_195 = models.CharField(db_column='TDT0207_COLUMN_NM_195', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_196 = models.CharField(db_column='TDT0207_COLUMN_NM_196', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_197 = models.CharField(db_column='TDT0207_COLUMN_NM_197', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_198 = models.CharField(db_column='TDT0207_COLUMN_NM_198', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_199 = models.CharField(db_column='TDT0207_COLUMN_NM_199', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_column_nm_200 = models.CharField(db_column='TDT0207_COLUMN_NM_200', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_del_flg = models.CharField(db_column='TDT0207_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0207_crt_datetime = models.DateTimeField(db_column='TDT0207_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0207_crt_user_id = models.CharField(db_column='TDT0207_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0207_crt_prog_nm = models.CharField(db_column='TDT0207_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_upd_datetime = models.DateTimeField(db_column='TDT0207_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0207_upd_user_id = models.CharField(db_column='TDT0207_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0207_upd_prog_nm = models.CharField(db_column='TDT0207_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0207_upd_cnt = models.DecimalField(db_column='TDT0207_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0207_SALARY_DETAILS_HRZN'
        unique_together = (('tdt0203_nendo', 'tdt0203_getsudo', 'tdt0203_salary_kbn', 'tdt0203_shain_cd', 'tdt0204_shikyu_kbn'),)


class Tdt0301UqShainKihon(models.Model):
    tdt0301_shain_cd = models.CharField(db_column='TDT0301_SHAIN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    tdt0301_work_day_num = models.SmallIntegerField(db_column='TDT0301_WORK_DAY_NUM', blank=True, null=True)  # Field name made lowercase.
    tdt0301_base_rate = models.DecimalField(db_column='TDT0301_BASE_RATE', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0301_initial_date = models.DateTimeField(db_column='TDT0301_INITIAL_DATE', blank=True, null=True)  # Field name made lowercase.
    tdt0301_del_flg = models.CharField(db_column='TDT0301_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0301_crt_datetime = models.DateTimeField(db_column='TDT0301_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0301_crt_user_id = models.CharField(db_column='TDT0301_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0301_crt_prog_nm = models.CharField(db_column='TDT0301_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0301_upd_datetime = models.DateTimeField(db_column='TDT0301_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0301_upd_user_id = models.CharField(db_column='TDT0301_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0301_upd_prog_nm = models.CharField(db_column='TDT0301_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0301_upd_cnt = models.DecimalField(db_column='TDT0301_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdt0301_uq_no_fuyo_flg = models.CharField(db_column='TDT0301_UQ_NO_FUYO_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0301_first_work_day_num = models.SmallIntegerField(db_column='TDT0301_FIRST_WORK_DAY_NUM', blank=True, null=True)  # Field name made lowercase.
    tdt0301_uq_jikan_day = models.SmallIntegerField(db_column='TDT0301_UQ_JIKAN_DAY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0301_UQ_SHAIN_KIHON'


class Tdt0303UqShainFuyo(models.Model):
    tdt0303_shain_kbn_cd = models.CharField(db_column='TDT0303_SHAIN_KBN_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tdt0303_kinzoku_month_num = models.SmallIntegerField(db_column='TDT0303_KINZOKU_MONTH_NUM')  # Field name made lowercase.
    tdt0303_work_day_num_by_week = models.DecimalField(db_column='TDT0303_WORK_DAY_NUM_BY_WEEK', max_digits=10, decimal_places=4)  # Field name made lowercase.
    tdt0303_low_work_day_num = models.SmallIntegerField(db_column='TDT0303_LOW_WORK_DAY_NUM', blank=True, null=True)  # Field name made lowercase.
    tdt0303_high_work_day_num = models.SmallIntegerField(db_column='TDT0303_HIGH_WORK_DAY_NUM', blank=True, null=True)  # Field name made lowercase.
    tdt0303_uq_day_num = models.DecimalField(db_column='TDT0303_UQ_DAY_NUM', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0303_del_flg = models.CharField(db_column='TDT0303_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0303_crt_datetime = models.DateTimeField(db_column='TDT0303_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0303_crt_user_id = models.CharField(db_column='TDT0303_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0303_crt_prog_nm = models.CharField(db_column='TDT0303_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0303_upd_datetime = models.DateTimeField(db_column='TDT0303_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0303_upd_user_id = models.CharField(db_column='TDT0303_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0303_upd_prog_nm = models.CharField(db_column='TDT0303_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0303_upd_cnt = models.DecimalField(db_column='TDT0303_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0303_UQ_SHAIN_FUYO'
        unique_together = (('tdt0303_shain_kbn_cd', 'tdt0303_kinzoku_month_num', 'tdt0303_work_day_num_by_week'),)


class Tdt0305UqFuyoKanri(models.Model):
    tdt0305_nendo = models.SmallIntegerField(db_column='TDT0305_NENDO', primary_key=True)  # Field name made lowercase.
    tdt0305_getsudo = models.SmallIntegerField(db_column='TDT0305_GETSUDO')  # Field name made lowercase.
    tdt0305_fuyo_flg = models.CharField(db_column='TDT0305_FUYO_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0305_del_flg = models.CharField(db_column='TDT0305_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0305_crt_datetime = models.DateTimeField(db_column='TDT0305_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0305_crt_user_id = models.CharField(db_column='TDT0305_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0305_crt_prog_nm = models.CharField(db_column='TDT0305_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0305_upd_datetime = models.DateTimeField(db_column='TDT0305_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0305_upd_user_id = models.CharField(db_column='TDT0305_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0305_upd_prog_nm = models.CharField(db_column='TDT0305_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0305_upd_cnt = models.DecimalField(db_column='TDT0305_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdt0305_kakutei_flg = models.CharField(db_column='TDT0305_KAKUTEI_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0305_UQ_FUYO_KANRI'
        unique_together = (('tdt0305_nendo', 'tdt0305_getsudo'),)


class Tdt0306UqInfo(models.Model):
    tdt0306_nendo = models.SmallIntegerField(db_column='TDT0306_NENDO', primary_key=True)  # Field name made lowercase.
    tdt0306_getsudo = models.SmallIntegerField(db_column='TDT0306_GETSUDO')  # Field name made lowercase.
    tdt0306_shain_cd = models.CharField(db_column='TDT0306_SHAIN_CD', max_length=10)  # Field name made lowercase.
    tdt0306_kinzoku_nen = models.SmallIntegerField(db_column='TDT0306_KINZOKU_NEN', blank=True, null=True)  # Field name made lowercase.
    tdt0306_kinzoku_getsu = models.SmallIntegerField(db_column='TDT0306_KINZOKU_GETSU', blank=True, null=True)  # Field name made lowercase.
    tdt0306_shain_kbn_cd = models.CharField(db_column='TDT0306_SHAIN_KBN_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0306_work_day_num = models.SmallIntegerField(db_column='TDT0306_WORK_DAY_NUM', blank=True, null=True)  # Field name made lowercase.
    tdt0306_zen_uq_day_num = models.DecimalField(db_column='TDT0306_ZEN_UQ_DAY_NUM', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0306_zen_uq_date = models.DateTimeField(db_column='TDT0306_ZEN_UQ_DATE', blank=True, null=True)  # Field name made lowercase.
    tdt0306_nen_ttl_day_num = models.SmallIntegerField(db_column='TDT0306_NEN_TTL_DAY_NUM', blank=True, null=True)  # Field name made lowercase.
    tdt0306_nen_ttl_day_rate = models.DecimalField(db_column='TDT0306_NEN_TTL_DAY_RATE', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0306_zen_uq_kurikoshi = models.DecimalField(db_column='TDT0306_ZEN_UQ_KURIKOSHI', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0306_tou_str_uq_num = models.DecimalField(db_column='TDT0306_TOU_STR_UQ_NUM', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0306_tou_uq_kurikoshi_num = models.DecimalField(db_column='TDT0306_TOU_UQ_KURIKOSHI_NUM', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0306_tou_str_uq_zan_num = models.DecimalField(db_column='TDT0306_TOU_STR_UQ_ZAN_NUM', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0306_next_uq_date = models.DateTimeField(db_column='TDT0306_NEXT_UQ_DATE', blank=True, null=True)  # Field name made lowercase.
    tdt0306_next_uq_day_num = models.DecimalField(db_column='TDT0306_NEXT_UQ_DAY_NUM', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0306_zen_zen_uq_day_num = models.DecimalField(db_column='TDT0306_ZEN_ZEN_UQ_DAY_NUM', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0306_zen_zen_uq_date = models.DateTimeField(db_column='TDT0306_ZEN_ZEN_UQ_DATE', blank=True, null=True)  # Field name made lowercase.
    tdt0306_uq_tokubetsu_fuyo = models.DecimalField(db_column='TDT0306_UQ_TOKUBETSU_FUYO', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0306_uq_fuyo_month_flg = models.CharField(db_column='TDT0306_UQ_FUYO_MONTH_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0306_del_flg = models.CharField(db_column='TDT0306_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0306_crt_datetime = models.DateTimeField(db_column='TDT0306_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0306_crt_user_id = models.CharField(db_column='TDT0306_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0306_crt_prog_nm = models.CharField(db_column='TDT0306_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0306_upd_datetime = models.DateTimeField(db_column='TDT0306_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0306_upd_user_id = models.CharField(db_column='TDT0306_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0306_upd_prog_nm = models.CharField(db_column='TDT0306_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0306_upd_cnt = models.DecimalField(db_column='TDT0306_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdt0306_initial_date = models.DateTimeField(db_column='TDT0306_INITIAL_DATE', blank=True, null=True)  # Field name made lowercase.
    tdt0306_uq_no_fuyo_flg = models.CharField(db_column='TDT0306_UQ_NO_FUYO_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0306_tm_work_day_num = models.SmallIntegerField(db_column='TDT0306_TM_WORK_DAY_NUM', blank=True, null=True)  # Field name made lowercase.
    tdt0306_tm_ttl_day_num = models.SmallIntegerField(db_column='TDT0306_TM_TTL_DAY_NUM', blank=True, null=True)  # Field name made lowercase.
    tdt0306_tm_ttl_day_rate = models.DecimalField(db_column='TDT0306_TM_TTL_DAY_RATE', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0306_nm_uq_day_num = models.DecimalField(db_column='TDT0306_NM_UQ_DAY_NUM', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0306_base_rate = models.DecimalField(db_column='TDT0306_BASE_RATE', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0306_zen_jikan_uq_syouka = models.SmallIntegerField(db_column='TDT0306_ZEN_JIKAN_UQ_SYOUKA', blank=True, null=True)  # Field name made lowercase.
    tdt0306_tou_jikan_uq_syouka = models.SmallIntegerField(db_column='TDT0306_TOU_JIKAN_UQ_SYOUKA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0306_UQ_INFO'
        unique_together = (('tdt0306_nendo', 'tdt0306_getsudo', 'tdt0306_shain_cd'),)


class Tdt0308UqFuyoControl(models.Model):
    tdt0308_uq_fuyo_control_no = models.SmallIntegerField(db_column='TDT0308_UQ_FUYO_CONTROL_NO', primary_key=True)  # Field name made lowercase.
    tdt0308_uq_fuyo_control_flg = models.CharField(db_column='TDT0308_UQ_FUYO_CONTROL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0308_UQ_FUYO_CONTROL'


class Tdt0309PlanUqYotei(models.Model):
    tdt0309_nendo = models.SmallIntegerField(db_column='TDT0309_NENDO', primary_key=True)  # Field name made lowercase.
    tdt0309_shain_cd = models.CharField(db_column='TDT0309_SHAIN_CD', max_length=10)  # Field name made lowercase.
    tdt0309_no = models.DecimalField(db_column='TDT0309_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tdt0309_yotei_date = models.CharField(db_column='TDT0309_YOTEI_DATE', max_length=10)  # Field name made lowercase.
    tdt0309_del_flg = models.CharField(db_column='TDT0309_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0309_crt_datetime = models.DateTimeField(db_column='TDT0309_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0309_crt_user_id = models.CharField(db_column='TDT0309_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0309_crt_prog_nm = models.CharField(db_column='TDT0309_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0309_upd_datetime = models.DateTimeField(db_column='TDT0309_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0309_upd_user_id = models.CharField(db_column='TDT0309_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0309_upd_prog_nm = models.CharField(db_column='TDT0309_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0309_upd_cnt = models.DecimalField(db_column='TDT0309_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0309_PLAN_UQ_YOTEI'
        unique_together = (('tdt0309_nendo', 'tdt0309_shain_cd', 'tdt0309_no'),)


class Tdt0400Syugyo(models.Model):
    tdt0400_nendo = models.SmallIntegerField(db_column='TDT0400_NENDO', primary_key=True)  # Field name made lowercase.
    tdt0400_getsudo = models.SmallIntegerField(db_column='TDT0400_GETSUDO')  # Field name made lowercase.
    tdt0400_status = models.CharField(db_column='TDT0400_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0400_del_flg = models.CharField(db_column='TDT0400_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0400_crt_datetime = models.DateTimeField(db_column='TDT0400_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0400_crt_user_id = models.CharField(db_column='TDT0400_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0400_crt_prog_nm = models.CharField(db_column='TDT0400_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0400_upd_datetime = models.DateTimeField(db_column='TDT0400_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0400_upd_user_id = models.CharField(db_column='TDT0400_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0400_upd_prog_nm = models.CharField(db_column='TDT0400_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0400_upd_cnt = models.DecimalField(db_column='TDT0400_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdt0400_jisseki_status = models.CharField(db_column='TDT0400_JISSEKI_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0400_chk_flg = models.CharField(db_column='TDT0400_CHK_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0400_SYUGYO'
        unique_together = (('tdt0400_nendo', 'tdt0400_getsudo'),)


class Tdt0401SyugyoShain(models.Model):
    tdt0400_nendo = models.SmallIntegerField(db_column='TDT0400_NENDO', primary_key=True)  # Field name made lowercase.
    tdt0400_getsudo = models.SmallIntegerField(db_column='TDT0400_GETSUDO')  # Field name made lowercase.
    tdt0401_shain_no = models.CharField(db_column='TDT0401_SHAIN_NO', max_length=10)  # Field name made lowercase.
    tdt0401_del_flg = models.CharField(db_column='TDT0401_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0401_crt_datetime = models.DateTimeField(db_column='TDT0401_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0401_crt_user_id = models.CharField(db_column='TDT0401_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0401_crt_prog_nm = models.CharField(db_column='TDT0401_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0401_upd_datetime = models.DateTimeField(db_column='TDT0401_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0401_upd_user_id = models.CharField(db_column='TDT0401_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0401_upd_prog_nm = models.CharField(db_column='TDT0401_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0401_upd_cnt = models.DecimalField(db_column='TDT0401_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdt0401_geppou_syuturyoku_date = models.DateTimeField(db_column='TDT0401_GEPPOU_SYUTURYOKU_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0401_SYUGYO_SHAIN'
        unique_together = (('tdt0400_nendo', 'tdt0400_getsudo', 'tdt0401_shain_no'),)


class Tdt0402SyugyoYotei(models.Model):
    tdt0400_nendo = models.SmallIntegerField(db_column='TDT0400_NENDO', primary_key=True)  # Field name made lowercase.
    tdt0400_getsudo = models.SmallIntegerField(db_column='TDT0400_GETSUDO')  # Field name made lowercase.
    tdt0401_shain_no = models.CharField(db_column='TDT0401_SHAIN_NO', max_length=10)  # Field name made lowercase.
    tdt0402_renban = models.SmallIntegerField(db_column='TDT0402_RENBAN')  # Field name made lowercase.
    tdt0402_day_num = models.SmallIntegerField(db_column='TDT0402_DAY_NUM')  # Field name made lowercase.
    tdt0402_genba_cd = models.CharField(db_column='TDT0402_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0402_shoku_cd = models.CharField(db_column='TDT0402_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdt0402_start_time = models.IntegerField(db_column='TDT0402_START_TIME', blank=True, null=True)  # Field name made lowercase.
    tdt0402_end_time = models.IntegerField(db_column='TDT0402_END_TIME', blank=True, null=True)  # Field name made lowercase.
    tdt0402_kosu_time = models.DecimalField(db_column='TDT0402_KOSU_TIME', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0402_shukkin_kyuka_id = models.CharField(db_column='TDT0402_SHUKKIN_KYUKA_ID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0402_del_flg = models.CharField(db_column='TDT0402_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0402_crt_datetime = models.DateTimeField(db_column='TDT0402_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0402_crt_user_id = models.CharField(db_column='TDT0402_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0402_crt_prog_nm = models.CharField(db_column='TDT0402_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0402_upd_datetime = models.DateTimeField(db_column='TDT0402_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0402_upd_user_id = models.CharField(db_column='TDT0402_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0402_upd_prog_nm = models.CharField(db_column='TDT0402_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0402_upd_cnt = models.DecimalField(db_column='TDT0402_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdt0402_week_no = models.SmallIntegerField(db_column='TDT0402_WEEK_NO', blank=True, null=True)  # Field name made lowercase.
    tdt0402_break_time = models.DecimalField(db_column='TDT0402_BREAK_TIME', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0402_shift_code = models.CharField(db_column='TDT0402_SHIFT_CODE', max_length=11, blank=True, null=True)  # Field name made lowercase.
    tdt0402_shift_pkey = models.IntegerField(db_column='TDT0402_SHIFT_PKEY', blank=True, null=True)  # Field name made lowercase.
    tdt0402_break_time_shinya = models.DecimalField(db_column='TDT0402_BREAK_TIME_SHINYA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0402_crt_sheet_nm = models.CharField(db_column='TDT0402_CRT_SHEET_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0402_SYUGYO_YOTEI'
        unique_together = (('tdt0400_nendo', 'tdt0400_getsudo', 'tdt0401_shain_no', 'tdt0402_renban', 'tdt0402_day_num'),)


class Tdt0403SyugyoJisseki(models.Model):
    tdt0400_nendo = models.SmallIntegerField(db_column='TDT0400_NENDO', primary_key=True)  # Field name made lowercase.
    tdt0400_getsudo = models.SmallIntegerField(db_column='TDT0400_GETSUDO')  # Field name made lowercase.
    tdt0401_shain_no = models.CharField(db_column='TDT0401_SHAIN_NO', max_length=10)  # Field name made lowercase.
    tdt0403_day = models.SmallIntegerField(db_column='TDT0403_DAY')  # Field name made lowercase.
    tdt0403_renban = models.SmallIntegerField(db_column='TDT0403_RENBAN')  # Field name made lowercase.
    tdt0403_genba_cd = models.CharField(db_column='TDT0403_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0403_shoku_cd = models.CharField(db_column='TDT0403_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdt0403_dakoku_start_time = models.IntegerField(db_column='TDT0403_DAKOKU_START_TIME', blank=True, null=True)  # Field name made lowercase.
    tdt0403_dakoku_end_time = models.IntegerField(db_column='TDT0403_DAKOKU_END_TIME', blank=True, null=True)  # Field name made lowercase.
    tdt0403_start_time = models.IntegerField(db_column='TDT0403_START_TIME', blank=True, null=True)  # Field name made lowercase.
    tdt0403_end_time = models.IntegerField(db_column='TDT0403_END_TIME', blank=True, null=True)  # Field name made lowercase.
    tdt0403_break_time = models.DecimalField(db_column='TDT0403_BREAK_TIME', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0403_kosu_time = models.DecimalField(db_column='TDT0403_KOSU_TIME', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0403_shukkin_kyuka_id = models.CharField(db_column='TDT0403_SHUKKIN_KYUKA_ID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0403_uq_kosu_time = models.DecimalField(db_column='TDT0403_UQ_KOSU_TIME', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0403_del_flg = models.CharField(db_column='TDT0403_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0403_crt_datetime = models.DateTimeField(db_column='TDT0403_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0403_crt_user_id = models.CharField(db_column='TDT0403_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0403_crt_prog_nm = models.CharField(db_column='TDT0403_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0403_upd_datetime = models.DateTimeField(db_column='TDT0403_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0403_upd_user_id = models.CharField(db_column='TDT0403_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0403_upd_prog_nm = models.CharField(db_column='TDT0403_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0403_upd_cnt = models.DecimalField(db_column='TDT0403_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdt0403_from_dakoku_kbn_cd = models.CharField(db_column='TDT0403_FROM_DAKOKU_KBN_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0403_to_dakoku_kbn_cd = models.CharField(db_column='TDT0403_TO_DAKOKU_KBN_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0403_jisseki_from_dakoku_kbn_cd = models.CharField(db_column='TDT0403_JISSEKI_FROM_DAKOKU_KBN_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0403_jisseki_to_dakoku_kbn_cd = models.CharField(db_column='TDT0403_JISSEKI_TO_DAKOKU_KBN_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0403_break_time_jit = models.DecimalField(db_column='TDT0403_BREAK_TIME_JIT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0403_out_of_error_flg = models.CharField(db_column='TDT0403_OUT_OF_ERROR_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0403_dakoku_genba_cd = models.CharField(db_column='TDT0403_DAKOKU_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0403_dakoku_shoku_cd = models.CharField(db_column='TDT0403_DAKOKU_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdt0403_dakoku_start_timestamp = models.DateTimeField(db_column='TDT0403_DAKOKU_START_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    tdt0403_dakoku_end_timestamp = models.DateTimeField(db_column='TDT0403_DAKOKU_END_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    tdt0403_correct_flg = models.CharField(db_column='TDT0403_CORRECT_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0403_check_flg = models.CharField(db_column='TDT0403_CHECK_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0403_mae_idou_kosu = models.IntegerField(db_column='TDT0403_MAE_IDOU_KOSU', blank=True, null=True)  # Field name made lowercase.
    tdt0403_ato_idou_kosu = models.IntegerField(db_column='TDT0403_ATO_IDOU_KOSU', blank=True, null=True)  # Field name made lowercase.
    tdt0403_device_id = models.CharField(db_column='TDT0403_DEVICE_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tdt0403_break_time_shinya = models.DecimalField(db_column='TDT0403_BREAK_TIME_SHINYA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0403_start_set_flg = models.CharField(db_column='TDT0403_START_SET_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0403_end_set_flg = models.CharField(db_column='TDT0403_END_SET_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0403_todokede_renban = models.SmallIntegerField(db_column='TDT0403_TODOKEDE_RENBAN', blank=True, null=True)  # Field name made lowercase.
    tdt0403_dakoku_start_timestamp_ipad = models.DateTimeField(db_column='TDT0403_DAKOKU_START_TIMESTAMP_iPad', blank=True, null=True)  # Field name made lowercase.
    tdt0403_dakoku_end_timestamp_ipad = models.DateTimeField(db_column='TDT0403_DAKOKU_END_TIMESTAMP_iPad', blank=True, null=True)  # Field name made lowercase.
    tdt0403_half_day_yukyu_flg = models.CharField(db_column='TDT0403_HALF_DAY_YUKYU_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0403_SYUGYO_JISSEKI'
        unique_together = (('tdt0400_nendo', 'tdt0400_getsudo', 'tdt0401_shain_no', 'tdt0403_day', 'tdt0403_renban'),)


class Tdt0404SyugyoShinsei(models.Model):
    tdt0400_nendo = models.SmallIntegerField(db_column='TDT0400_NENDO', primary_key=True)  # Field name made lowercase.
    tdt0400_getsudo = models.SmallIntegerField(db_column='TDT0400_GETSUDO')  # Field name made lowercase.
    tdt0401_shain_no = models.CharField(db_column='TDT0401_SHAIN_NO', max_length=10)  # Field name made lowercase.
    tdt0404_day = models.SmallIntegerField(db_column='TDT0404_DAY')  # Field name made lowercase.
    tdt0404_renban = models.SmallIntegerField(db_column='TDT0404_RENBAN')  # Field name made lowercase.
    tdt0404_start_time = models.IntegerField(db_column='TDT0404_START_TIME', blank=True, null=True)  # Field name made lowercase.
    tdt0404_end_time = models.IntegerField(db_column='TDT0404_END_TIME', blank=True, null=True)  # Field name made lowercase.
    tdt0404_kosu_time = models.DecimalField(db_column='TDT0404_KOSU_TIME', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0404_shukkin_kyuka_id = models.CharField(db_column='TDT0404_SHUKKIN_KYUKA_ID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0404_shinsei_riyu = models.CharField(db_column='TDT0404_SHINSEI_RIYU', max_length=64, blank=True, null=True)  # Field name made lowercase.
    tdt0404_shounin_kbn_cd = models.CharField(db_column='TDT0404_SHOUNIN_KBN_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0404_hinin_riyu = models.CharField(db_column='TDT0404_HININ_RIYU', max_length=64, blank=True, null=True)  # Field name made lowercase.
    tdt0404_del_flg = models.CharField(db_column='TDT0404_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0404_crt_datetime = models.DateTimeField(db_column='TDT0404_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0404_crt_user_id = models.CharField(db_column='TDT0404_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0404_crt_prog_nm = models.CharField(db_column='TDT0404_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0404_upd_datetime = models.DateTimeField(db_column='TDT0404_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0404_upd_user_id = models.CharField(db_column='TDT0404_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0404_upd_prog_nm = models.CharField(db_column='TDT0404_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0404_upd_cnt = models.DecimalField(db_column='TDT0404_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdt0404_shinsei_date = models.DateTimeField(db_column='TDT0404_SHINSEI_DATE', blank=True, null=True)  # Field name made lowercase.
    tdt0404_genba_cd = models.CharField(db_column='TDT0404_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0404_shoku_cd = models.CharField(db_column='TDT0404_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdt0404_shouninsha1_cd = models.CharField(db_column='TDT0404_SHOUNINSHA1_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tdt0404_shouninsha2_cd = models.CharField(db_column='TDT0404_SHOUNINSHA2_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tdt0404_last_shounin_cd = models.CharField(db_column='TDT0404_LAST_SHOUNIN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tdt0404_kairansha_cd = models.CharField(db_column='TDT0404_KAIRANSHA_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tdt0404_s1_shounin_kbn_cd = models.CharField(db_column='TDT0404_S1_SHOUNIN_KBN_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0404_s2_shounin_kbn_cd = models.CharField(db_column='TDT0404_S2_SHOUNIN_KBN_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0404_uketukesha_cd = models.CharField(db_column='TDT0404_UKETUKESHA_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tdt0404_uketuke_date = models.DateTimeField(db_column='TDT0404_UKETUKE_DATE', blank=True, null=True)  # Field name made lowercase.
    tdt0404_break_time = models.DecimalField(db_column='TDT0404_BREAK_TIME', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0404_break_time_shinya = models.DecimalField(db_column='TDT0404_BREAK_TIME_SHINYA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tdt0404_crt_sheet_nm = models.CharField(db_column='TDT0404_CRT_SHEET_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tdt0404_half_day_yukyu_flg = models.CharField(db_column='TDT0404_HALF_DAY_YUKYU_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0404_SYUGYO_SHINSEI'
        unique_together = (('tdt0400_nendo', 'tdt0400_getsudo', 'tdt0401_shain_no', 'tdt0404_day', 'tdt0404_renban'),)


class Tdt0405SyugyoDakokuError(models.Model):
    tdt0400_nendo = models.SmallIntegerField(db_column='TDT0400_NENDO', primary_key=True)  # Field name made lowercase.
    tdt0400_getsudo = models.SmallIntegerField(db_column='TDT0400_GETSUDO')  # Field name made lowercase.
    tdt0401_shain_no = models.CharField(db_column='TDT0401_SHAIN_NO', max_length=10)  # Field name made lowercase.
    tdt0405_day = models.SmallIntegerField(db_column='TDT0405_DAY')  # Field name made lowercase.
    tdt0405_renban = models.SmallIntegerField(db_column='TDT0405_RENBAN')  # Field name made lowercase.
    tdt0405_ganba_cd_yotei = models.CharField(db_column='TDT0405_GANBA_CD_YOTEI', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0405_shoku_cd_yotei = models.CharField(db_column='TDT0405_SHOKU_CD_YOTEI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdt0405_start_time_yotei = models.IntegerField(db_column='TDT0405_START_TIME_YOTEI', blank=True, null=True)  # Field name made lowercase.
    tdt0405_end_time_yotei = models.IntegerField(db_column='TDT0405_END_TIME_YOTEI', blank=True, null=True)  # Field name made lowercase.
    tdt0405_shukkin_kyuka_id_yotei = models.CharField(db_column='TDT0405_SHUKKIN_KYUKA_ID_YOTEI', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0405_ganba_cd_jitu = models.CharField(db_column='TDT0405_GANBA_CD_JITU', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0405_shoku_cd_jitu = models.CharField(db_column='TDT0405_SHOKU_CD_JITU', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tdt0405_start_time_jitu = models.IntegerField(db_column='TDT0405_START_TIME_JITU', blank=True, null=True)  # Field name made lowercase.
    tdt0405_end_time_jitu = models.IntegerField(db_column='TDT0405_END_TIME_JITU', blank=True, null=True)  # Field name made lowercase.
    tdt0405_from_dakoku_kbn_cd_jitu = models.CharField(db_column='TDT0405_FROM_DAKOKU_KBN_CD_JITU', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0405_to_dakoku_kbn_cd_jitu = models.CharField(db_column='TDT0405_TO_DAKOKU_KBN_CD_JITU', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tdt0405_del_flg = models.CharField(db_column='TDT0405_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0405_crt_datetime = models.DateTimeField(db_column='TDT0405_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0405_crt_user_id = models.CharField(db_column='TDT0405_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0405_crt_prog_nm = models.CharField(db_column='TDT0405_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0405_upd_datetime = models.DateTimeField(db_column='TDT0405_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0405_upd_user_id = models.CharField(db_column='TDT0405_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0405_upd_prog_nm = models.CharField(db_column='TDT0405_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0405_upd_cnt = models.DecimalField(db_column='TDT0405_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdt0405_renban_jitu = models.SmallIntegerField(db_column='TDT0405_RENBAN_JITU', blank=True, null=True)  # Field name made lowercase.
    tdt0405_out_of_error_flg = models.CharField(db_column='TDT0405_OUT_OF_ERROR_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0405_err_msg_r = models.CharField(db_column='TDT0405_ERR_MSG_R', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0405_err_msg_01 = models.CharField(db_column='TDT0405_ERR_MSG_01', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0405_err_msg_02 = models.CharField(db_column='TDT0405_ERR_MSG_02', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0405_err_msg_03 = models.CharField(db_column='TDT0405_ERR_MSG_03', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0405_err_msg_04 = models.CharField(db_column='TDT0405_ERR_MSG_04', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0405_err_msg_05 = models.CharField(db_column='TDT0405_ERR_MSG_05', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0405_err_msg_06 = models.CharField(db_column='TDT0405_ERR_MSG_06', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0405_err_msg_07 = models.CharField(db_column='TDT0405_ERR_MSG_07', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0405_err_msg_08 = models.CharField(db_column='TDT0405_ERR_MSG_08', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0405_err_msg_09 = models.CharField(db_column='TDT0405_ERR_MSG_09', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0405_err_msg_10 = models.CharField(db_column='TDT0405_ERR_MSG_10', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0405_start_set_flg = models.CharField(db_column='TDT0405_START_SET_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0405_end_set_flg = models.CharField(db_column='TDT0405_END_SET_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0405_SYUGYO_DAKOKU_ERROR'
        unique_together = (('tdt0400_nendo', 'tdt0400_getsudo', 'tdt0401_shain_no', 'tdt0405_day', 'tdt0405_renban'),)


class Tdt0406SgJobControl(models.Model):
    tdt0406_job_no = models.SmallIntegerField(db_column='TDT0406_JOB_NO', primary_key=True)  # Field name made lowercase.
    tdt0406_control_flg = models.CharField(db_column='TDT0406_CONTROL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0406_SG_JOB_CONTROL'


class Tdt0407SyugyoShainDayError(models.Model):
    tdt0400_nendo = models.SmallIntegerField(db_column='TDT0400_NENDO', primary_key=True)  # Field name made lowercase.
    tdt0400_getsudo = models.SmallIntegerField(db_column='TDT0400_GETSUDO')  # Field name made lowercase.
    tdt0401_shain_no = models.CharField(db_column='TDT0401_SHAIN_NO', max_length=10)  # Field name made lowercase.
    tdt0407_day = models.SmallIntegerField(db_column='TDT0407_DAY')  # Field name made lowercase.
    tdt0407_out_of_error_flg = models.CharField(db_column='TDT0407_OUT_OF_ERROR_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0407_serious_flg = models.CharField(db_column='TDT0407_SERIOUS_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0407_del_flg = models.CharField(db_column='TDT0407_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tdt0407_crt_datetime = models.DateTimeField(db_column='TDT0407_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0407_crt_user_id = models.CharField(db_column='TDT0407_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0407_crt_prog_nm = models.CharField(db_column='TDT0407_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0407_upd_datetime = models.DateTimeField(db_column='TDT0407_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tdt0407_upd_user_id = models.CharField(db_column='TDT0407_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tdt0407_upd_prog_nm = models.CharField(db_column='TDT0407_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tdt0407_upd_cnt = models.DecimalField(db_column='TDT0407_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tdt0407_err_msg_r = models.CharField(db_column='TDT0407_ERR_MSG_R', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0407_err_msg_01 = models.CharField(db_column='TDT0407_ERR_MSG_01', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0407_err_msg_02 = models.CharField(db_column='TDT0407_ERR_MSG_02', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0407_err_msg_03 = models.CharField(db_column='TDT0407_ERR_MSG_03', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0407_err_msg_04 = models.CharField(db_column='TDT0407_ERR_MSG_04', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0407_err_msg_05 = models.CharField(db_column='TDT0407_ERR_MSG_05', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0407_err_msg_06 = models.CharField(db_column='TDT0407_ERR_MSG_06', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0407_err_msg_07 = models.CharField(db_column='TDT0407_ERR_MSG_07', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0407_err_msg_08 = models.CharField(db_column='TDT0407_ERR_MSG_08', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0407_err_msg_09 = models.CharField(db_column='TDT0407_ERR_MSG_09', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0407_err_msg_10 = models.CharField(db_column='TDT0407_ERR_MSG_10', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tdt0407_dakoku_err_exist_flg = models.CharField(db_column='TDT0407_DAKOKU_ERR_EXIST_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TDT0407_SYUGYO_SHAIN_DAY_ERROR'
        unique_together = (('tdt0400_nendo', 'tdt0400_getsudo', 'tdt0401_shain_no', 'tdt0407_day'),)


class Tem0101Shitushu(models.Model):
    tem0101_insp_kbn = models.CharField(db_column='TEM0101_INSP_KBN', max_length=1)  # Field name made lowercase.
    tem0101_genba_cd = models.CharField(db_column='TEM0101_GENBA_CD', max_length=5)  # Field name made lowercase.
    tem0101_shitushu_cd = models.CharField(db_column='TEM0101_SHITUSHU_CD', max_length=10)  # Field name made lowercase.
    tem0101_shitushu_nm = models.CharField(db_column='TEM0101_SHITUSHU_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tem0101_tou_nm = models.CharField(db_column='TEM0101_TOU_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0101_kaisho_nm = models.CharField(db_column='TEM0101_KAISHO_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0101_del_flg = models.CharField(db_column='TEM0101_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0101_crt_datetime = models.DateTimeField(db_column='TEM0101_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0101_crt_user_id = models.CharField(db_column='TEM0101_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0101_crt_prog_nm = models.CharField(db_column='TEM0101_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0101_upd_datetime = models.DateTimeField(db_column='TEM0101_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0101_upd_user_id = models.CharField(db_column='TEM0101_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0101_upd_prog_nm = models.CharField(db_column='TEM0101_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0101_upd_cnt = models.DecimalField(db_column='TEM0101_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0101_SHITUSHU'


class Tem0101ShitushuLv1(models.Model):
    tem0101_shitushu_lv_1_seq_no = models.AutoField(db_column='TEM0101_SHITUSHU_LV_1_SEQ_NO', primary_key=True)  # Field name made lowercase.
    tem0101_shitushu_lv_1_cd = models.CharField(db_column='TEM0101_SHITUSHU_LV_1_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tem0101_genba_cd = models.CharField(db_column='TEM0101_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tem0101_shoku_cd = models.CharField(db_column='TEM0101_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tem0101_del_flg = models.CharField(db_column='TEM0101_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0101_crt_datetime = models.DateTimeField(db_column='TEM0101_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0101_crt_user_id = models.CharField(db_column='TEM0101_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0101_crt_prog_nm = models.CharField(db_column='TEM0101_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0101_upd_datetime = models.DateTimeField(db_column='TEM0101_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0101_upd_user_id = models.CharField(db_column='TEM0101_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0101_upd_prog_nm = models.CharField(db_column='TEM0101_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0101_upd_cnt = models.DecimalField(db_column='TEM0101_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tem0101_shitushu_lv_1_nm = models.CharField(db_column='TEM0101_SHITUSHU_LV_1_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0101_SHITUSHU_LV_1'


class Tem0102ShitushuLv2(models.Model):
    tem0102_shitushu_lv_2_seq_no = models.AutoField(db_column='TEM0102_SHITUSHU_LV_2_SEQ_NO', primary_key=True)  # Field name made lowercase.
    tem0102_shitushu_lv_2_cd = models.CharField(db_column='TEM0102_SHITUSHU_LV_2_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tem0102_shitushu_lv_2_nm = models.CharField(db_column='TEM0102_SHITUSHU_LV_2_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0102_genba_cd = models.CharField(db_column='TEM0102_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tem0102_shoku_cd = models.CharField(db_column='TEM0102_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tem0102_del_flg = models.CharField(db_column='TEM0102_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0102_crt_datetime = models.DateTimeField(db_column='TEM0102_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0102_crt_user_id = models.CharField(db_column='TEM0102_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0102_crt_prog_nm = models.CharField(db_column='TEM0102_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0102_upd_datetime = models.DateTimeField(db_column='TEM0102_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0102_upd_user_id = models.CharField(db_column='TEM0102_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0102_upd_prog_nm = models.CharField(db_column='TEM0102_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0102_upd_cnt = models.DecimalField(db_column='TEM0102_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0102_SHITUSHU_LV_2'


class Tem0102Taisho(models.Model):
    tem0102_insp_kbn = models.CharField(db_column='TEM0102_INSP_KBN', max_length=1)  # Field name made lowercase.
    tem0102_taisho_cd = models.CharField(db_column='TEM0102_TAISHO_CD', max_length=10)  # Field name made lowercase.
    tem0102_taisho_nm = models.CharField(db_column='TEM0102_TAISHO_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0102_zaishitu = models.CharField(db_column='TEM0102_ZAISHITU', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0102_del_flg = models.CharField(db_column='TEM0102_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0102_crt_datetime = models.DateTimeField(db_column='TEM0102_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0102_crt_user_id = models.CharField(db_column='TEM0102_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0102_crt_prog_nm = models.CharField(db_column='TEM0102_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0102_upd_datetime = models.DateTimeField(db_column='TEM0102_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0102_upd_user_id = models.CharField(db_column='TEM0102_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0102_upd_prog_nm = models.CharField(db_column='TEM0102_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0102_upd_cnt = models.DecimalField(db_column='TEM0102_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0102_TAISHO'


class Tem0103Shitushu(models.Model):
    tem0103_shitushu_seq_no = models.AutoField(db_column='TEM0103_SHITUSHU_SEQ_NO', primary_key=True)  # Field name made lowercase.
    tem0103_shitushu_cd = models.CharField(db_column='TEM0103_SHITUSHU_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tem0103_shitushu_nm = models.CharField(db_column='TEM0103_SHITUSHU_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0103_genba_cd = models.CharField(db_column='TEM0103_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tem0103_shoku_cd = models.CharField(db_column='TEM0103_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tem0103_del_flg = models.CharField(db_column='TEM0103_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0103_crt_datetime = models.DateTimeField(db_column='TEM0103_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0103_crt_user_id = models.CharField(db_column='TEM0103_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0103_crt_prog_nm = models.CharField(db_column='TEM0103_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0103_upd_datetime = models.DateTimeField(db_column='TEM0103_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0103_upd_user_id = models.CharField(db_column='TEM0103_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0103_upd_prog_nm = models.CharField(db_column='TEM0103_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0103_upd_cnt = models.DecimalField(db_column='TEM0103_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0103_SHITUSHU'


class Tem0104SeisoSagyoShiyo(models.Model):
    tem0104_insp_kbn = models.CharField(db_column='TEM0104_INSP_KBN', max_length=1)  # Field name made lowercase.
    tem0104_sagyo_plan_cd = models.CharField(db_column='TEM0104_SAGYO_PLAN_CD', max_length=10)  # Field name made lowercase.
    tem0104_genba_cd = models.CharField(db_column='TEM0104_GENBA_CD', max_length=5)  # Field name made lowercase.
    tem0104_shoku_cd = models.CharField(db_column='TEM0104_SHOKU_CD', max_length=2)  # Field name made lowercase.
    tem0104_sagyo_plan_nm = models.CharField(db_column='TEM0104_SAGYO_PLAN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0104_sagyo_plan_from = models.DateTimeField(db_column='TEM0104_SAGYO_PLAN_FROM', blank=True, null=True)  # Field name made lowercase.
    tem0104_sagyo_plan_to = models.DateTimeField(db_column='TEM0104_SAGYO_PLAN_TO', blank=True, null=True)  # Field name made lowercase.
    tem0104_del_flg = models.CharField(db_column='TEM0104_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0104_crt_datetime = models.DateTimeField(db_column='TEM0104_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0104_crt_user_id = models.CharField(db_column='TEM0104_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0104_crt_prog_nm = models.CharField(db_column='TEM0104_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0104_upd_datetime = models.DateTimeField(db_column='TEM0104_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0104_upd_user_id = models.CharField(db_column='TEM0104_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0104_upd_prog_nm = models.CharField(db_column='TEM0104_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0104_upd_cnt = models.DecimalField(db_column='TEM0104_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0104_SEISO_SAGYO_SHIYO'


class Tem0104Taisho(models.Model):
    tem0104_taisho_seq_no = models.AutoField(db_column='TEM0104_TAISHO_SEQ_NO', primary_key=True)  # Field name made lowercase.
    tem0104_taisho_cd = models.CharField(db_column='TEM0104_TAISHO_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tem0104_taisho_nm = models.CharField(db_column='TEM0104_TAISHO_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0104_genba_cd = models.CharField(db_column='TEM0104_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tem0104_shoku_cd = models.CharField(db_column='TEM0104_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tem0104_del_flg = models.CharField(db_column='TEM0104_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0104_crt_datetime = models.DateTimeField(db_column='TEM0104_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0104_crt_user_id = models.CharField(db_column='TEM0104_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0104_crt_prog_nm = models.CharField(db_column='TEM0104_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0104_upd_datetime = models.DateTimeField(db_column='TEM0104_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0104_upd_user_id = models.CharField(db_column='TEM0104_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0104_upd_prog_nm = models.CharField(db_column='TEM0104_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0104_upd_cnt = models.DecimalField(db_column='TEM0104_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tem0104_init_naiyo_ptn_cd = models.CharField(db_column='TEM0104_INIT_NAIYO_PTN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0104_TAISHO'


class Tem0105HyokaPointSgy(models.Model):
    tem0104_taisho_seq_no = models.DecimalField(db_column='TEM0104_TAISHO_SEQ_NO', primary_key=True, max_digits=10, decimal_places=0)  # Field name made lowercase.
    tem0105_dtl_no = models.SmallIntegerField(db_column='TEM0105_DTL_NO')  # Field name made lowercase.
    tem0105_sg_hyoka_point = models.CharField(db_column='TEM0105_SG_HYOKA_POINT', max_length=150, blank=True, null=True)  # Field name made lowercase.
    tem0105_hyoji_no = models.SmallIntegerField(db_column='TEM0105_HYOJI_NO', blank=True, null=True)  # Field name made lowercase.
    tem0105_del_flg = models.CharField(db_column='TEM0105_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0105_crt_datetime = models.DateTimeField(db_column='TEM0105_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0105_crt_user_id = models.CharField(db_column='TEM0105_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0105_crt_prog_nm = models.CharField(db_column='TEM0105_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0105_upd_datetime = models.DateTimeField(db_column='TEM0105_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0105_upd_user_id = models.CharField(db_column='TEM0105_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0105_upd_prog_nm = models.CharField(db_column='TEM0105_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0105_upd_cnt = models.DecimalField(db_column='TEM0105_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tem0105_seiso_kbn = models.CharField(db_column='TEM0105_SEISO_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0105_HYOKA_POINT_SGY'
        unique_together = (('tem0104_taisho_seq_no', 'tem0105_dtl_no'),)


class Tem0105SeisoSagyoShiyoDtl(models.Model):
    tem0104_insp_kbn = models.CharField(db_column='TEM0104_INSP_KBN', max_length=1)  # Field name made lowercase.
    tem0104_sagyo_plan_cd = models.CharField(db_column='TEM0104_SAGYO_PLAN_CD', max_length=10)  # Field name made lowercase.
    tem0104_genba_cd = models.CharField(db_column='TEM0104_GENBA_CD', max_length=5)  # Field name made lowercase.
    tem0104_shoku_cd = models.CharField(db_column='TEM0104_SHOKU_CD', max_length=2)  # Field name made lowercase.
    tem0105_shitushu_cd = models.CharField(db_column='TEM0105_SHITUSHU_CD', max_length=10)  # Field name made lowercase.
    tem0105_taisho_cd = models.CharField(db_column='TEM0105_TAISHO_CD', max_length=10)  # Field name made lowercase.
    tem0105_kosu = models.IntegerField(db_column='TEM0105_KOSU', blank=True, null=True)  # Field name made lowercase.
    tem0105_menseki = models.IntegerField(db_column='TEM0105_MENSEKI', blank=True, null=True)  # Field name made lowercase.
    tem0105_sagyo_naiyo_dtl_no = models.SmallIntegerField(db_column='TEM0105_SAGYO_NAIYO_DTL_NO', blank=True, null=True)  # Field name made lowercase.
    tem0105_seiso_kbn = models.CharField(db_column='TEM0105_SEISO_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0105_kaisu = models.SmallIntegerField(db_column='TEM0105_KAISU', blank=True, null=True)  # Field name made lowercase.
    tem0105_shuki = models.CharField(db_column='TEM0105_SHUKI', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0105_del_flg = models.CharField(db_column='TEM0105_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0105_crt_datetime = models.DateTimeField(db_column='TEM0105_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0105_crt_user_id = models.CharField(db_column='TEM0105_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0105_crt_prog_nm = models.CharField(db_column='TEM0105_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0105_upd_datetime = models.DateTimeField(db_column='TEM0105_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0105_upd_user_id = models.CharField(db_column='TEM0105_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0105_upd_prog_nm = models.CharField(db_column='TEM0105_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0105_upd_cnt = models.DecimalField(db_column='TEM0105_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0105_SEISO_SAGYO_SHIYO_DTL'


class Tem0106NaiyoPtn(models.Model):
    tem0104_taisho_seq_no = models.DecimalField(db_column='TEM0104_TAISHO_SEQ_NO', primary_key=True, max_digits=10, decimal_places=0)  # Field name made lowercase.
    tem0106_naiyo_ptn_cd = models.CharField(db_column='TEM0106_NAIYO_PTN_CD', max_length=10)  # Field name made lowercase.
    tem0106_naiyo_ptn_nm = models.CharField(db_column='TEM0106_NAIYO_PTN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0106_del_flg = models.CharField(db_column='TEM0106_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0106_crt_datetime = models.DateTimeField(db_column='TEM0106_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0106_crt_user_id = models.CharField(db_column='TEM0106_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0106_crt_prog_nm = models.CharField(db_column='TEM0106_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0106_upd_datetime = models.DateTimeField(db_column='TEM0106_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0106_upd_user_id = models.CharField(db_column='TEM0106_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0106_upd_prog_nm = models.CharField(db_column='TEM0106_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0106_upd_cnt = models.DecimalField(db_column='TEM0106_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tem0106_set_dtl_no = models.SmallIntegerField(db_column='TEM0106_SET_DTL_NO', blank=True, null=True)  # Field name made lowercase.
    tem0106_seiso_kbn = models.CharField(db_column='TEM0106_SEISO_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0106_memo = models.CharField(db_column='TEM0106_MEMO', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0106_NAIYO_PTN'
        unique_together = (('tem0104_taisho_seq_no', 'tem0106_naiyo_ptn_cd'),)


class Tem0107HyokaKmk(models.Model):
    tem0107_sk_hyoka_seq_no = models.AutoField(db_column='TEM0107_SK_HYOKA_SEQ_NO', primary_key=True)  # Field name made lowercase.
    tem0107_sk_hyoka_cd = models.CharField(db_column='TEM0107_SK_HYOKA_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tem0107_sk_hyoka_nm = models.CharField(db_column='TEM0107_SK_HYOKA_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0107_genba_cd = models.CharField(db_column='TEM0107_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tem0107_shoku_cd = models.CharField(db_column='TEM0107_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tem0107_del_flg = models.CharField(db_column='TEM0107_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0107_crt_datetime = models.DateTimeField(db_column='TEM0107_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0107_crt_user_id = models.CharField(db_column='TEM0107_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0107_crt_prog_nm = models.CharField(db_column='TEM0107_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0107_upd_datetime = models.DateTimeField(db_column='TEM0107_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0107_upd_user_id = models.CharField(db_column='TEM0107_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0107_upd_prog_nm = models.CharField(db_column='TEM0107_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0107_upd_cnt = models.DecimalField(db_column='TEM0107_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tem0107_insp_term_tanni = models.CharField(db_column='TEM0107_INSP_TERM_TANNI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0107_insp_start_ym = models.CharField(db_column='TEM0107_INSP_START_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tem0107_insp_term_kaisu = models.SmallIntegerField(db_column='TEM0107_INSP_TERM_KAISU', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0107_HYOKA_KMK'


class Tem0108TenkenKmk(models.Model):
    tem0107_sk_hyoka_seq_no = models.DecimalField(db_column='TEM0107_SK_HYOKA_SEQ_NO', primary_key=True, max_digits=10, decimal_places=0)  # Field name made lowercase.
    tem0108_sk_tenken_seq_no = models.DecimalField(db_column='TEM0108_SK_TENKEN_SEQ_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tem0108_sk_tenken_cd = models.CharField(db_column='TEM0108_SK_TENKEN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tem0108_sk_tenken_nm = models.CharField(db_column='TEM0108_SK_TENKEN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0108_del_flg = models.CharField(db_column='TEM0108_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0108_crt_datetime = models.DateTimeField(db_column='TEM0108_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0108_crt_user_id = models.CharField(db_column='TEM0108_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0108_crt_prog_nm = models.CharField(db_column='TEM0108_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0108_upd_datetime = models.DateTimeField(db_column='TEM0108_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0108_upd_user_id = models.CharField(db_column='TEM0108_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0108_upd_prog_nm = models.CharField(db_column='TEM0108_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0108_upd_cnt = models.DecimalField(db_column='TEM0108_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0108_TENKEN_KMK'
        unique_together = (('tem0107_sk_hyoka_seq_no', 'tem0108_sk_tenken_seq_no'),)


class Tem0109HyokaPointSsk(models.Model):
    tem0107_sk_hyoka_seq_no = models.DecimalField(db_column='TEM0107_SK_HYOKA_SEQ_NO', primary_key=True, max_digits=10, decimal_places=0)  # Field name made lowercase.
    tem0108_sk_tenken_seq_no = models.DecimalField(db_column='TEM0108_SK_TENKEN_SEQ_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tem0109_dtl_no = models.SmallIntegerField(db_column='TEM0109_DTL_NO')  # Field name made lowercase.
    tem0109_sk_hyoka_point = models.CharField(db_column='TEM0109_SK_HYOKA_POINT', max_length=150, blank=True, null=True)  # Field name made lowercase.
    tem0109_hyoji_no = models.SmallIntegerField(db_column='TEM0109_HYOJI_NO', blank=True, null=True)  # Field name made lowercase.
    tem0109_del_flg = models.CharField(db_column='TEM0109_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0109_crt_datetime = models.DateTimeField(db_column='TEM0109_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0109_crt_user_id = models.CharField(db_column='TEM0109_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0109_crt_prog_nm = models.CharField(db_column='TEM0109_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0109_upd_datetime = models.DateTimeField(db_column='TEM0109_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0109_upd_user_id = models.CharField(db_column='TEM0109_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0109_upd_prog_nm = models.CharField(db_column='TEM0109_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0109_upd_cnt = models.DecimalField(db_column='TEM0109_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0109_HYOKA_POINT_SSK'
        unique_together = (('tem0107_sk_hyoka_seq_no', 'tem0108_sk_tenken_seq_no', 'tem0109_dtl_no'),)


class Tem0110Category(models.Model):
    tem0110_insp_kbn = models.CharField(db_column='TEM0110_INSP_KBN', primary_key=True, max_length=1)  # Field name made lowercase.
    tem0110_doc_kbn = models.CharField(db_column='TEM0110_DOC_KBN', max_length=1)  # Field name made lowercase.
    tem0110_category_cd = models.CharField(db_column='TEM0110_CATEGORY_CD', max_length=2)  # Field name made lowercase.
    tem0110_category_nm = models.CharField(db_column='TEM0110_CATEGORY_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0110_del_flg = models.CharField(db_column='TEM0110_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0110_crt_datetime = models.DateTimeField(db_column='TEM0110_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0110_crt_user_id = models.CharField(db_column='TEM0110_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0110_crt_prog_nm = models.CharField(db_column='TEM0110_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0110_upd_datetime = models.DateTimeField(db_column='TEM0110_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0110_upd_user_id = models.CharField(db_column='TEM0110_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0110_upd_prog_nm = models.CharField(db_column='TEM0110_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0110_upd_cnt = models.DecimalField(db_column='TEM0110_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0110_CATEGORY'
        unique_together = (('tem0110_insp_kbn', 'tem0110_doc_kbn', 'tem0110_category_cd'),)


class Tem0111Tenko(models.Model):
    tem0111_tenko_cd = models.CharField(db_column='TEM0111_TENKO_CD', primary_key=True, max_length=2)  # Field name made lowercase.
    tem0111_tenko_nm = models.CharField(db_column='TEM0111_TENKO_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0111_del_flg = models.CharField(db_column='TEM0111_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0111_crt_datetime = models.DateTimeField(db_column='TEM0111_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0111_crt_user_id = models.CharField(db_column='TEM0111_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0111_crt_prog_nm = models.CharField(db_column='TEM0111_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0111_upd_datetime = models.DateTimeField(db_column='TEM0111_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0111_upd_user_id = models.CharField(db_column='TEM0111_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0111_upd_prog_nm = models.CharField(db_column='TEM0111_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0111_upd_cnt = models.DecimalField(db_column='TEM0111_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0111_TENKO'


class Tem0112InspUser(models.Model):
    tem0112_insp_user_seq_no = models.AutoField(db_column='TEM0112_INSP_USER_SEQ_NO', primary_key=True)  # Field name made lowercase.
    tem0112_shain_cd = models.CharField(db_column='TEM0112_SHAIN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tem0112_guest_nm = models.CharField(db_column='TEM0112_GUEST_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tem0112_sagyo_kngn_flg = models.CharField(db_column='TEM0112_SAGYO_KNGN_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0112_sosiki_kngn_flg = models.CharField(db_column='TEM0112_SOSIKI_KNGN_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0112_kanri_kngn_flg = models.CharField(db_column='TEM0112_KANRI_KNGN_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0112_guest_flg = models.CharField(db_column='TEM0112_GUEST_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0112_insp_pwd = models.CharField(db_column='TEM0112_INSP_PWD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tem0112_del_flg = models.CharField(db_column='TEM0112_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0112_crt_datetime = models.DateTimeField(db_column='TEM0112_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0112_crt_user_id = models.CharField(db_column='TEM0112_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0112_crt_prog_nm = models.CharField(db_column='TEM0112_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0112_upd_datetime = models.DateTimeField(db_column='TEM0112_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0112_upd_user_id = models.CharField(db_column='TEM0112_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0112_upd_prog_nm = models.CharField(db_column='TEM0112_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0112_upd_cnt = models.DecimalField(db_column='TEM0112_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tem0112_insp_user_kb = models.CharField(db_column='TEM0112_INSP_USER_KB', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0112_INSP_USER'


class Tem0113ShitushuLv3(models.Model):
    tem0113_shitushu_lv_3_seq_no = models.AutoField(db_column='TEM0113_SHITUSHU_LV_3_SEQ_NO', primary_key=True)  # Field name made lowercase.
    tem0113_shitushu_lv_3_cd = models.CharField(db_column='TEM0113_SHITUSHU_LV_3_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tem0113_shitushu_lv_3_nm = models.CharField(db_column='TEM0113_SHITUSHU_LV_3_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0113_genba_cd = models.CharField(db_column='TEM0113_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tem0113_shoku_cd = models.CharField(db_column='TEM0113_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tem0113_del_flg = models.CharField(db_column='TEM0113_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0113_crt_datetime = models.DateTimeField(db_column='TEM0113_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0113_crt_user_id = models.CharField(db_column='TEM0113_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0113_crt_prog_nm = models.CharField(db_column='TEM0113_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0113_upd_datetime = models.DateTimeField(db_column='TEM0113_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0113_upd_user_id = models.CharField(db_column='TEM0113_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0113_upd_prog_nm = models.CharField(db_column='TEM0113_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0113_upd_cnt = models.DecimalField(db_column='TEM0113_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0113_SHITUSHU_LV_3'


class Tem0114Tensu(models.Model):
    tem0114_insp_kbn = models.CharField(db_column='TEM0114_INSP_KBN', primary_key=True, max_length=1)  # Field name made lowercase.
    tem0114_insp_siyo_kbn = models.CharField(db_column='TEM0114_INSP_SIYO_KBN', max_length=1)  # Field name made lowercase.
    tem0114_dtl_no = models.SmallIntegerField(db_column='TEM0114_DTL_NO')  # Field name made lowercase.
    tem0114_disp_nm = models.CharField(db_column='TEM0114_DISP_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tem0114_haiten = models.SmallIntegerField(db_column='TEM0114_HAITEN', blank=True, null=True)  # Field name made lowercase.
    tem0114_hanrei = models.CharField(db_column='TEM0114_HANREI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tem0114_kaizen_flg = models.CharField(db_column='TEM0114_KAIZEN_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0114_invalid_flg = models.CharField(db_column='TEM0114_INVALID_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0114_del_flg = models.CharField(db_column='TEM0114_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0114_crt_datetime = models.DateTimeField(db_column='TEM0114_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0114_crt_user_id = models.CharField(db_column='TEM0114_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0114_crt_prog_nm = models.CharField(db_column='TEM0114_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0114_upd_datetime = models.DateTimeField(db_column='TEM0114_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0114_upd_user_id = models.CharField(db_column='TEM0114_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0114_upd_prog_nm = models.CharField(db_column='TEM0114_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0114_upd_cnt = models.DecimalField(db_column='TEM0114_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0114_TENSU'
        unique_together = (('tem0114_insp_kbn', 'tem0114_insp_siyo_kbn', 'tem0114_dtl_no'),)


class Tem0115Naiyo(models.Model):
    tem0104_taisho_seq_no = models.DecimalField(db_column='TEM0104_TAISHO_SEQ_NO', primary_key=True, max_digits=10, decimal_places=0)  # Field name made lowercase.
    tem0106_naiyo_ptn_cd = models.CharField(db_column='TEM0106_NAIYO_PTN_CD', max_length=10)  # Field name made lowercase.
    tem0115_dtl_no = models.SmallIntegerField(db_column='TEM0115_DTL_NO')  # Field name made lowercase.
    tem0115_naiyo_nm = models.CharField(db_column='TEM0115_NAIYO_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0115_del_flg = models.CharField(db_column='TEM0115_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0115_crt_datetime = models.DateTimeField(db_column='TEM0115_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0115_crt_user_id = models.CharField(db_column='TEM0115_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0115_crt_prog_nm = models.CharField(db_column='TEM0115_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0115_upd_datetime = models.DateTimeField(db_column='TEM0115_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0115_upd_user_id = models.CharField(db_column='TEM0115_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0115_upd_prog_nm = models.CharField(db_column='TEM0115_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0115_upd_cnt = models.DecimalField(db_column='TEM0115_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tem0115_seiso_term_kaisu = models.SmallIntegerField(db_column='TEM0115_SEISO_TERM_KAISU', blank=True, null=True)  # Field name made lowercase.
    tem0115_seiso_term_tanni = models.CharField(db_column='TEM0115_SEISO_TERM_TANNI', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0115_NAIYO'
        unique_together = (('tem0104_taisho_seq_no', 'tem0106_naiyo_ptn_cd', 'tem0115_dtl_no'),)


class Tem0301InspShain(models.Model):
    tem0301_shain_cd = models.CharField(db_column='TEM0301_SHAIN_CD', max_length=10)  # Field name made lowercase.
    tem0301_sagyo_hinshitu_flg = models.CharField(db_column='TEM0301_SAGYO_HINSHITU_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0301_sosiki_hinshitu_flg = models.CharField(db_column='TEM0301_SOSIKI_HINSHITU_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0301_del_flg = models.CharField(db_column='TEM0301_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0301_crt_datetime = models.DateTimeField(db_column='TEM0301_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0301_crt_user_id = models.CharField(db_column='TEM0301_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0301_crt_prog_nm = models.CharField(db_column='TEM0301_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0301_upd_datetime = models.DateTimeField(db_column='TEM0301_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0301_upd_user_id = models.CharField(db_column='TEM0301_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0301_upd_prog_nm = models.CharField(db_column='TEM0301_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0301_upd_cnt = models.DecimalField(db_column='TEM0301_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tem0301_insp_pwd = models.CharField(db_column='TEM0301_INSP_PWD', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0301_INSP_SHAIN'


class Tem0302HyokaTensu(models.Model):
    tem0302_insp_kbn = models.CharField(db_column='TEM0302_INSP_KBN', max_length=1)  # Field name made lowercase.
    tem0302_dtl_no = models.SmallIntegerField(db_column='TEM0302_DTL_NO')  # Field name made lowercase.
    tem0302_disp_nm = models.CharField(db_column='TEM0302_DISP_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0302_haiten = models.SmallIntegerField(db_column='TEM0302_HAITEN', blank=True, null=True)  # Field name made lowercase.
    tem0302_comment_flg = models.CharField(db_column='TEM0302_COMMENT_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0302_invalid_flg = models.CharField(db_column='TEM0302_INVALID_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0302_upper_jogai1 = models.SmallIntegerField(db_column='TEM0302_UPPER_JOGAI1', blank=True, null=True)  # Field name made lowercase.
    tem0302_upper_jogai2 = models.SmallIntegerField(db_column='TEM0302_UPPER_JOGAI2', blank=True, null=True)  # Field name made lowercase.
    tem0302_upper_jogai3 = models.SmallIntegerField(db_column='TEM0302_UPPER_JOGAI3', blank=True, null=True)  # Field name made lowercase.
    tem0302_upper_taisho1 = models.SmallIntegerField(db_column='TEM0302_UPPER_TAISHO1', blank=True, null=True)  # Field name made lowercase.
    tem0302_upper_taisho2 = models.SmallIntegerField(db_column='TEM0302_UPPER_TAISHO2', blank=True, null=True)  # Field name made lowercase.
    tem0302_upper_taisho3 = models.SmallIntegerField(db_column='TEM0302_UPPER_TAISHO3', blank=True, null=True)  # Field name made lowercase.
    tem0302_upper_hiritu = models.SmallIntegerField(db_column='TEM0302_UPPER_HIRITU', blank=True, null=True)  # Field name made lowercase.
    tem0302_upper_haiten = models.SmallIntegerField(db_column='TEM0302_UPPER_HAITEN', blank=True, null=True)  # Field name made lowercase.
    tem0302_lower_jogai1 = models.SmallIntegerField(db_column='TEM0302_LOWER_JOGAI1', blank=True, null=True)  # Field name made lowercase.
    tem0302_lower_jogai2 = models.SmallIntegerField(db_column='TEM0302_LOWER_JOGAI2', blank=True, null=True)  # Field name made lowercase.
    tem0302_lower_jogai3 = models.SmallIntegerField(db_column='TEM0302_LOWER_JOGAI3', blank=True, null=True)  # Field name made lowercase.
    tem0302_lower_taisho1 = models.SmallIntegerField(db_column='TEM0302_LOWER_TAISHO1', blank=True, null=True)  # Field name made lowercase.
    tem0302_lower_taisho2 = models.SmallIntegerField(db_column='TEM0302_LOWER_TAISHO2', blank=True, null=True)  # Field name made lowercase.
    tem0302_lower_taisho3 = models.SmallIntegerField(db_column='TEM0302_LOWER_TAISHO3', blank=True, null=True)  # Field name made lowercase.
    tem0302_lower_hiritu = models.SmallIntegerField(db_column='TEM0302_LOWER_HIRITU', blank=True, null=True)  # Field name made lowercase.
    tem0302_lower_haiten = models.SmallIntegerField(db_column='TEM0302_LOWER_HAITEN', blank=True, null=True)  # Field name made lowercase.
    tem0302_other_haiten = models.SmallIntegerField(db_column='TEM0302_OTHER_HAITEN', blank=True, null=True)  # Field name made lowercase.
    tem0302_del_flg = models.CharField(db_column='TEM0302_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0302_crt_datetime = models.DateTimeField(db_column='TEM0302_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0302_crt_user_id = models.CharField(db_column='TEM0302_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0302_crt_prog_nm = models.CharField(db_column='TEM0302_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0302_upd_datetime = models.DateTimeField(db_column='TEM0302_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0302_upd_user_id = models.CharField(db_column='TEM0302_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0302_upd_prog_nm = models.CharField(db_column='TEM0302_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0302_upd_cnt = models.DecimalField(db_column='TEM0302_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0302_HYOKA_TENSU'


class Tem0303Category(models.Model):
    tem0303_insp_kbn = models.CharField(db_column='TEM0303_INSP_KBN', max_length=1)  # Field name made lowercase.
    tem0303_doc_kbn = models.CharField(db_column='TEM0303_DOC_KBN', max_length=1)  # Field name made lowercase.
    tem0303_category_cd = models.CharField(db_column='TEM0303_CATEGORY_CD', max_length=2)  # Field name made lowercase.
    tem0303_category_nm = models.CharField(db_column='TEM0303_CATEGORY_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0303_del_flg = models.CharField(db_column='TEM0303_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0303_crt_datetime = models.DateTimeField(db_column='TEM0303_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0303_crt_user_id = models.CharField(db_column='TEM0303_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0303_crt_prog_nm = models.CharField(db_column='TEM0303_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0303_upd_datetime = models.DateTimeField(db_column='TEM0303_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0303_upd_user_id = models.CharField(db_column='TEM0303_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0303_upd_prog_nm = models.CharField(db_column='TEM0303_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0303_upd_cnt = models.DecimalField(db_column='TEM0303_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0303_CATEGORY'


class Tem0304Tenko(models.Model):
    tem0304_tenko_cd = models.CharField(db_column='TEM0304_TENKO_CD', max_length=2)  # Field name made lowercase.
    tem0304_tenko_nm = models.CharField(db_column='TEM0304_TENKO_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0304_del_flg = models.CharField(db_column='TEM0304_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0304_crt_datetime = models.DateTimeField(db_column='TEM0304_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0304_crt_user_id = models.CharField(db_column='TEM0304_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0304_crt_prog_nm = models.CharField(db_column='TEM0304_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0304_upd_datetime = models.DateTimeField(db_column='TEM0304_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0304_upd_user_id = models.CharField(db_column='TEM0304_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0304_upd_prog_nm = models.CharField(db_column='TEM0304_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0304_upd_cnt = models.DecimalField(db_column='TEM0304_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0304_TENKO'


class Tem0305HyokaPoint(models.Model):
    tem0305_insp_kbn = models.CharField(db_column='TEM0305_INSP_KBN', max_length=1)  # Field name made lowercase.
    tem0305_taisho_cd = models.CharField(db_column='TEM0305_TAISHO_CD', max_length=10)  # Field name made lowercase.
    tem0305_del_flg = models.CharField(db_column='TEM0305_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0305_crt_datetime = models.DateTimeField(db_column='TEM0305_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0305_crt_user_id = models.CharField(db_column='TEM0305_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0305_crt_prog_nm = models.CharField(db_column='TEM0305_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0305_upd_datetime = models.DateTimeField(db_column='TEM0305_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0305_upd_user_id = models.CharField(db_column='TEM0305_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0305_upd_prog_nm = models.CharField(db_column='TEM0305_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0305_upd_cnt = models.DecimalField(db_column='TEM0305_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0305_HYOKA_POINT'


class Tem0306HyokaPointDtl(models.Model):
    tem0305_insp_kbn = models.CharField(db_column='TEM0305_INSP_KBN', max_length=1)  # Field name made lowercase.
    tem0305_taisho_cd = models.CharField(db_column='TEM0305_TAISHO_CD', max_length=10)  # Field name made lowercase.
    tem0306_dtl_no = models.SmallIntegerField(db_column='TEM0306_DTL_NO')  # Field name made lowercase.
    tem0306_seiso_kbn = models.CharField(db_column='TEM0306_SEISO_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0306_hyoka_point = models.CharField(db_column='TEM0306_HYOKA_POINT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tem0306_del_flg = models.CharField(db_column='TEM0306_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0306_crt_datetime = models.DateTimeField(db_column='TEM0306_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0306_crt_user_id = models.CharField(db_column='TEM0306_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0306_crt_prog_nm = models.CharField(db_column='TEM0306_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0306_upd_datetime = models.DateTimeField(db_column='TEM0306_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0306_upd_user_id = models.CharField(db_column='TEM0306_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0306_upd_prog_nm = models.CharField(db_column='TEM0306_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0306_upd_cnt = models.DecimalField(db_column='TEM0306_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0306_HYOKA_POINT_DTL'


class Tem0901YukaZai(models.Model):
    tem0901_yuka_zai_cd = models.DecimalField(db_column='TEM0901_YUKA_ZAI_CD', primary_key=True, max_digits=10, decimal_places=0)  # Field name made lowercase.
    tem0901_yuka_zai_nm = models.CharField(db_column='TEM0901_YUKA_ZAI_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0901_del_flg = models.CharField(db_column='TEM0901_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0901_crt_datetime = models.DateTimeField(db_column='TEM0901_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0901_crt_user_id = models.CharField(db_column='TEM0901_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0901_crt_prog_nm = models.CharField(db_column='TEM0901_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0901_upd_datetime = models.DateTimeField(db_column='TEM0901_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0901_upd_user_id = models.CharField(db_column='TEM0901_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0901_upd_prog_nm = models.CharField(db_column='TEM0901_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0901_upd_cnt = models.DecimalField(db_column='TEM0901_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0901_YUKA_ZAI'


class Tem0902KosuTanni(models.Model):
    tem0902_kosu_tanni_cd = models.DecimalField(db_column='TEM0902_KOSU_TANNI_CD', primary_key=True, max_digits=10, decimal_places=0)  # Field name made lowercase.
    tem0902_kosu_tanni_nm = models.CharField(db_column='TEM0902_KOSU_TANNI_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tem0902_del_flg = models.CharField(db_column='TEM0902_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tem0902_crt_datetime = models.DateTimeField(db_column='TEM0902_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0902_crt_user_id = models.CharField(db_column='TEM0902_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0902_crt_prog_nm = models.CharField(db_column='TEM0902_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0902_upd_datetime = models.DateTimeField(db_column='TEM0902_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tem0902_upd_user_id = models.CharField(db_column='TEM0902_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tem0902_upd_prog_nm = models.CharField(db_column='TEM0902_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem0902_upd_cnt = models.DecimalField(db_column='TEM0902_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEM0902_KOSU_TANNI'


class Tet0201SeisoSagyoBase(models.Model):
    tet0201_genba_cd = models.CharField(db_column='TET0201_GENBA_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tet0201_shoku_cd = models.CharField(db_column='TET0201_SHOKU_CD', max_length=2)  # Field name made lowercase.
    tet0201_tokui_saki_cd = models.CharField(db_column='TET0201_TOKUI_SAKI_CD', max_length=4)  # Field name made lowercase.
    tet0201_kenmei = models.CharField(db_column='TET0201_KENMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tet0201_del_flg = models.CharField(db_column='TET0201_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0201_crt_datetime = models.DateTimeField(db_column='TET0201_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0201_crt_user_id = models.CharField(db_column='TET0201_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0201_crt_prog_nm = models.CharField(db_column='TET0201_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0201_upd_datetime = models.DateTimeField(db_column='TET0201_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0201_upd_user_id = models.CharField(db_column='TET0201_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0201_upd_prog_nm = models.CharField(db_column='TET0201_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0201_upd_cnt = models.DecimalField(db_column='TET0201_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0201_sla_tekiyo_flg = models.CharField(db_column='TET0201_SLA_TEKIYO_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0201_SEISO_SAGYO_BASE'
        unique_together = (('tet0201_genba_cd', 'tet0201_shoku_cd', 'tet0201_tokui_saki_cd'),)


class Tet0202SeisoSagyoShitushu(models.Model):
    tet0201_genba_cd = models.CharField(db_column='TET0201_GENBA_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tet0201_shoku_cd = models.CharField(db_column='TET0201_SHOKU_CD', max_length=2)  # Field name made lowercase.
    tet0201_tokui_saki_cd = models.CharField(db_column='TET0201_TOKUI_SAKI_CD', max_length=4)  # Field name made lowercase.
    tet0202_seiso_shitushu_seq_no = models.DecimalField(db_column='TET0202_SEISO_SHITUSHU_SEQ_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0202_shitushu_lv_1_seq_no = models.DecimalField(db_column='TET0202_SHITUSHU_LV_1_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0202_shitushu_lv_2_seq_no = models.DecimalField(db_column='TET0202_SHITUSHU_LV_2_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0202_del_flg = models.CharField(db_column='TET0202_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0202_crt_datetime = models.DateTimeField(db_column='TET0202_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0202_crt_user_id = models.CharField(db_column='TET0202_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0202_crt_prog_nm = models.CharField(db_column='TET0202_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0202_upd_datetime = models.DateTimeField(db_column='TET0202_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0202_upd_user_id = models.CharField(db_column='TET0202_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0202_upd_prog_nm = models.CharField(db_column='TET0202_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0202_upd_cnt = models.DecimalField(db_column='TET0202_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0202_shitushu_lv_3_seq_no = models.DecimalField(db_column='TET0202_SHITUSHU_LV_3_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0202_shitushu_lv_1_cd = models.CharField(db_column='TET0202_SHITUSHU_LV_1_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tet0202_shitushu_lv_1_nm = models.CharField(db_column='TET0202_SHITUSHU_LV_1_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0202_shitushu_lv_2_cd = models.CharField(db_column='TET0202_SHITUSHU_LV_2_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tet0202_shitushu_lv_2_nm = models.CharField(db_column='TET0202_SHITUSHU_LV_2_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0202_shitushu_lv_3_cd = models.CharField(db_column='TET0202_SHITUSHU_LV_3_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tet0202_shitushu_lv_3_nm = models.CharField(db_column='TET0202_SHITUSHU_LV_3_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0202_shitushu_seq_no = models.DecimalField(db_column='TET0202_SHITUSHU_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0202_shitushu_cd = models.CharField(db_column='TET0202_SHITUSHU_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0202_shitushu_nm = models.CharField(db_column='TET0202_SHITUSHU_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0202_insp_term_kaisu = models.SmallIntegerField(db_column='TET0202_INSP_TERM_KAISU', blank=True, null=True)  # Field name made lowercase.
    tet0202_insp_term_tanni = models.CharField(db_column='TET0202_INSP_TERM_TANNI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0202_insp_start_ym = models.CharField(db_column='TET0202_INSP_START_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tet0202_menseki = models.DecimalField(db_column='TET0202_MENSEKI', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tet0202_yuka_zai_cd = models.DecimalField(db_column='TET0202_YUKA_ZAI_CD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0202_SEISO_SAGYO_SHITUSHU'
        unique_together = (('tet0201_genba_cd', 'tet0201_shoku_cd', 'tet0201_tokui_saki_cd', 'tet0202_seiso_shitushu_seq_no'),)


class Tet0203SeisoSagyoTaisho(models.Model):
    tet0201_genba_cd = models.CharField(db_column='TET0201_GENBA_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tet0201_shoku_cd = models.CharField(db_column='TET0201_SHOKU_CD', max_length=2)  # Field name made lowercase.
    tet0201_tokui_saki_cd = models.CharField(db_column='TET0201_TOKUI_SAKI_CD', max_length=4)  # Field name made lowercase.
    tet0202_seiso_shitushu_seq_no = models.DecimalField(db_column='TET0202_SEISO_SHITUSHU_SEQ_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0203_seiso_taisho_seq_no = models.DecimalField(db_column='TET0203_SEISO_TAISHO_SEQ_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0203_del_flg = models.CharField(db_column='TET0203_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0203_crt_datetime = models.DateTimeField(db_column='TET0203_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0203_crt_user_id = models.CharField(db_column='TET0203_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0203_crt_prog_nm = models.CharField(db_column='TET0203_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0203_upd_datetime = models.DateTimeField(db_column='TET0203_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0203_upd_user_id = models.CharField(db_column='TET0203_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0203_upd_prog_nm = models.CharField(db_column='TET0203_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0203_upd_cnt = models.DecimalField(db_column='TET0203_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0203_taisho_cd = models.CharField(db_column='TET0203_TAISHO_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0203_taisho_nm = models.CharField(db_column='TET0203_TAISHO_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0203_sla_kijyun = models.DecimalField(db_column='TET0203_SLA_KIJYUN', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tet0203_naiyo_ptn_cd = models.CharField(db_column='TET0203_NAIYO_PTN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0203_naiyo_ptn_seiso_kbn = models.CharField(db_column='TET0203_NAIYO_PTN_SEISO_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0203_naiyo_ptn_nm = models.CharField(db_column='TET0203_NAIYO_PTN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0203_kosu_suryo = models.DecimalField(db_column='TET0203_KOSU_SURYO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0203_kosu_tanni_cd = models.DecimalField(db_column='TET0203_KOSU_TANNI_CD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0203_set_dtl_no = models.SmallIntegerField(db_column='TET0203_SET_DTL_NO', blank=True, null=True)  # Field name made lowercase.
    tet0203_naiyo_ptn_edit_flg = models.CharField(db_column='TET0203_NAIYO_PTN_EDIT_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0203_SEISO_SAGYO_TAISHO'
        unique_together = (('tet0201_genba_cd', 'tet0201_shoku_cd', 'tet0201_tokui_saki_cd', 'tet0202_seiso_shitushu_seq_no', 'tet0203_seiso_taisho_seq_no'),)


class Tet0204SeisoSagyoNaiyo(models.Model):
    tet0201_genba_cd = models.CharField(db_column='TET0201_GENBA_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tet0201_shoku_cd = models.CharField(db_column='TET0201_SHOKU_CD', max_length=2)  # Field name made lowercase.
    tet0201_tokui_saki_cd = models.CharField(db_column='TET0201_TOKUI_SAKI_CD', max_length=4)  # Field name made lowercase.
    tet0202_seiso_shitushu_seq_no = models.DecimalField(db_column='TET0202_SEISO_SHITUSHU_SEQ_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0203_seiso_taisho_seq_no = models.DecimalField(db_column='TET0203_SEISO_TAISHO_SEQ_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0204_naiyo_ptn_cd = models.CharField(db_column='TET0204_NAIYO_PTN_CD', max_length=10)  # Field name made lowercase.
    tet0204_dtl_no = models.SmallIntegerField(db_column='TET0204_DTL_NO')  # Field name made lowercase.
    tet0204_del_flg = models.CharField(db_column='TET0204_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0204_crt_datetime = models.DateTimeField(db_column='TET0204_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0204_crt_user_id = models.CharField(db_column='TET0204_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0204_crt_prog_nm = models.CharField(db_column='TET0204_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0204_upd_datetime = models.DateTimeField(db_column='TET0204_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0204_upd_user_id = models.CharField(db_column='TET0204_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0204_upd_prog_nm = models.CharField(db_column='TET0204_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0204_upd_cnt = models.DecimalField(db_column='TET0204_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0204_naiyo_nm = models.CharField(db_column='TET0204_NAIYO_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0204_seiso_term_tanni = models.CharField(db_column='TET0204_SEISO_TERM_TANNI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0204_seiso_term_kaisu = models.SmallIntegerField(db_column='TET0204_SEISO_TERM_KAISU', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0204_SEISO_SAGYO_NAIYO'
        unique_together = (('tet0201_genba_cd', 'tet0201_shoku_cd', 'tet0201_tokui_saki_cd', 'tet0202_seiso_shitushu_seq_no', 'tet0203_seiso_taisho_seq_no', 'tet0204_naiyo_ptn_cd', 'tet0204_dtl_no'),)


class Tet0205SeisoSagyoControl(models.Model):
    tet0205_haita_control_no = models.SmallIntegerField(db_column='TET0205_HAITA_CONTROL_NO', primary_key=True)  # Field name made lowercase.
    tet0205_haita_flg = models.CharField(db_column='TET0205_HAITA_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0205_SEISO_SAGYO_CONTROL'


class Tet0301InspInfo(models.Model):
    tet0301_insp_cd = models.CharField(db_column='TET0301_INSP_CD', max_length=25)  # Field name made lowercase.
    tet0301_insp_ed_no = models.SmallIntegerField(db_column='TET0301_INSP_ED_NO')  # Field name made lowercase.
    tet0301_sagyo_plan_cd = models.CharField(db_column='TET0301_SAGYO_PLAN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0301_genba_cd = models.CharField(db_column='TET0301_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tet0301_shoku_cd = models.CharField(db_column='TET0301_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tet0301_insp_kbn = models.CharField(db_column='TET0301_INSP_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0301_yotei_date = models.DateTimeField(db_column='TET0301_YOTEI_DATE', blank=True, null=True)  # Field name made lowercase.
    tet0301_shain_cd = models.CharField(db_column='TET0301_SHAIN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0301_insp_sts = models.CharField(db_column='TET0301_INSP_STS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0301_hyoka = models.SmallIntegerField(db_column='TET0301_HYOKA', blank=True, null=True)  # Field name made lowercase.
    tet0301_start_datetime = models.DateTimeField(db_column='TET0301_START_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0301_end_datetime = models.DateTimeField(db_column='TET0301_END_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0301_del_flg = models.CharField(db_column='TET0301_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0301_crt_datetime = models.DateTimeField(db_column='TET0301_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0301_crt_user_id = models.CharField(db_column='TET0301_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0301_crt_prog_nm = models.CharField(db_column='TET0301_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0301_upd_datetime = models.DateTimeField(db_column='TET0301_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0301_upd_user_id = models.CharField(db_column='TET0301_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0301_upd_prog_nm = models.CharField(db_column='TET0301_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0301_upd_cnt = models.DecimalField(db_column='TET0301_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0301_genba_jogai_flg = models.CharField(db_column='TET0301_GENBA_JOGAI_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0301_INSP_INFO'


class Tet0301InspPlanBase(models.Model):
    tet0301_insp_plan_seq_no = models.AutoField(db_column='TET0301_INSP_PLAN_SEQ_NO', primary_key=True)  # Field name made lowercase.
    tet0301_kenmei = models.CharField(db_column='TET0301_KENMEI', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tet0301_genba_cd = models.CharField(db_column='TET0301_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tet0301_shoku_cd = models.CharField(db_column='TET0301_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tet0301_insp_kbn = models.CharField(db_column='TET0301_INSP_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0301_keikaku_kbn = models.CharField(db_column='TET0301_KEIKAKU_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0301_term_start_ym = models.CharField(db_column='TET0301_TERM_START_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tet0301_term_end_ym = models.CharField(db_column='TET0301_TERM_END_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tet0301_yotei_ym = models.CharField(db_column='TET0301_YOTEI_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tet0301_kaisu = models.SmallIntegerField(db_column='TET0301_KAISU', blank=True, null=True)  # Field name made lowercase.
    tet0301_del_flg = models.CharField(db_column='TET0301_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0301_crt_datetime = models.DateTimeField(db_column='TET0301_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0301_crt_user_id = models.CharField(db_column='TET0301_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0301_crt_prog_nm = models.CharField(db_column='TET0301_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0301_upd_datetime = models.DateTimeField(db_column='TET0301_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0301_upd_user_id = models.CharField(db_column='TET0301_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0301_upd_prog_nm = models.CharField(db_column='TET0301_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0301_upd_cnt = models.DecimalField(db_column='TET0301_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0301_tokui_saki_cd = models.CharField(db_column='TET0301_TOKUI_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tet0301_hyoten_kbn = models.CharField(db_column='TET0301_HYOTEN_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0301_moto_mst_plan_seq_no = models.DecimalField(db_column='TET0301_MOTO_MST_PLAN_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0301_last_mst_plan_date = models.DateTimeField(db_column='TET0301_LAST_MST_PLAN_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0301_INSP_PLAN_BASE'


class Tet0302InspKoumoku1Info(models.Model):
    tet0301_insp_cd = models.CharField(db_column='TET0301_INSP_CD', max_length=25)  # Field name made lowercase.
    tet0301_insp_ed_no = models.SmallIntegerField(db_column='TET0301_INSP_ED_NO')  # Field name made lowercase.
    tet0302_koumoku1_cd = models.CharField(db_column='TET0302_KOUMOKU1_CD', max_length=10)  # Field name made lowercase.
    tet0302_hyoka = models.SmallIntegerField(db_column='TET0302_HYOKA', blank=True, null=True)  # Field name made lowercase.
    tet0302_start_datetime = models.DateTimeField(db_column='TET0302_START_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0302_end_datetime = models.DateTimeField(db_column='TET0302_END_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0302_jogai_flg = models.CharField(db_column='TET0302_JOGAI_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0302_img1 = models.BinaryField(db_column='TET0302_IMG1', blank=True, null=True)  # Field name made lowercase.
    tet0302_img1_nm = models.CharField(db_column='TET0302_IMG1_NM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tet0302_img1_kak = models.CharField(db_column='TET0302_IMG1_KAK', max_length=11, blank=True, null=True)  # Field name made lowercase.
    tet0302_img2 = models.BinaryField(db_column='TET0302_IMG2', blank=True, null=True)  # Field name made lowercase.
    tet0302_img2_nm = models.CharField(db_column='TET0302_IMG2_NM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tet0302_img2_kak = models.CharField(db_column='TET0302_IMG2_KAK', max_length=11, blank=True, null=True)  # Field name made lowercase.
    tet0302_img3 = models.BinaryField(db_column='TET0302_IMG3', blank=True, null=True)  # Field name made lowercase.
    tet0302_img3_nm = models.CharField(db_column='TET0302_IMG3_NM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tet0302_img3_kak = models.CharField(db_column='TET0302_IMG3_KAK', max_length=11, blank=True, null=True)  # Field name made lowercase.
    tet0302_img4 = models.BinaryField(db_column='TET0302_IMG4', blank=True, null=True)  # Field name made lowercase.
    tet0302_img4_nm = models.CharField(db_column='TET0302_IMG4_NM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tet0302_img4_kak = models.CharField(db_column='TET0302_IMG4_KAK', max_length=11, blank=True, null=True)  # Field name made lowercase.
    tet0302_img5 = models.BinaryField(db_column='TET0302_IMG5', blank=True, null=True)  # Field name made lowercase.
    tet0302_img5_nm = models.CharField(db_column='TET0302_IMG5_NM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tet0302_img5_kak = models.CharField(db_column='TET0302_IMG5_KAK', max_length=11, blank=True, null=True)  # Field name made lowercase.
    tet0302_del_flg = models.CharField(db_column='TET0302_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0302_crt_datetime = models.DateTimeField(db_column='TET0302_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0302_crt_user_id = models.CharField(db_column='TET0302_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0302_crt_prog_nm = models.CharField(db_column='TET0302_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0302_upd_datetime = models.DateTimeField(db_column='TET0302_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0302_upd_user_id = models.CharField(db_column='TET0302_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0302_upd_prog_nm = models.CharField(db_column='TET0302_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0302_upd_cnt = models.DecimalField(db_column='TET0302_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0302_genba_jogai_flg = models.CharField(db_column='TET0302_GENBA_JOGAI_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0302_INSP_KOUMOKU1_INFO'


class Tet0302InspPlanShitushu(models.Model):
    tet0301_insp_plan_seq_no = models.DecimalField(db_column='TET0301_INSP_PLAN_SEQ_NO', primary_key=True, max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0302_insp_shitushu_seq_no = models.DecimalField(db_column='TET0302_INSP_SHITUSHU_SEQ_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0302_shitushu_lv_1_seq_no = models.DecimalField(db_column='TET0302_SHITUSHU_LV_1_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0302_shitushu_lv_1_cd = models.CharField(db_column='TET0302_SHITUSHU_LV_1_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tet0302_shitushu_lv_1_nm = models.CharField(db_column='TET0302_SHITUSHU_LV_1_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0302_shitushu_lv_2_seq_no = models.DecimalField(db_column='TET0302_SHITUSHU_LV_2_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0302_shitushu_lv_2_cd = models.CharField(db_column='TET0302_SHITUSHU_LV_2_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tet0302_shitushu_lv_2_nm = models.CharField(db_column='TET0302_SHITUSHU_LV_2_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0302_shitushu_lv_3_seq_no = models.DecimalField(db_column='TET0302_SHITUSHU_LV_3_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0302_shitushu_lv_3_cd = models.CharField(db_column='TET0302_SHITUSHU_LV_3_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tet0302_shitushu_lv_3_nm = models.CharField(db_column='TET0302_SHITUSHU_LV_3_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0302_shitushu_seq_no = models.DecimalField(db_column='TET0302_SHITUSHU_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0302_shitushu_cd = models.CharField(db_column='TET0302_SHITUSHU_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0302_shitushu_nm = models.CharField(db_column='TET0302_SHITUSHU_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0302_hyoji_no = models.SmallIntegerField(db_column='TET0302_HYOJI_NO', blank=True, null=True)  # Field name made lowercase.
    tet0302_del_flg = models.CharField(db_column='TET0302_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0302_crt_datetime = models.DateTimeField(db_column='TET0302_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0302_crt_user_id = models.CharField(db_column='TET0302_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0302_crt_prog_nm = models.CharField(db_column='TET0302_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0302_upd_datetime = models.DateTimeField(db_column='TET0302_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0302_upd_user_id = models.CharField(db_column='TET0302_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0302_upd_prog_nm = models.CharField(db_column='TET0302_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0302_upd_cnt = models.DecimalField(db_column='TET0302_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0302_taisho_flg = models.CharField(db_column='TET0302_TAISHO_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0302_sk_hyoka_seq_no = models.DecimalField(db_column='TET0302_SK_HYOKA_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0302_sk_hyoka_cd = models.CharField(db_column='TET0302_SK_HYOKA_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0302_sk_hyoka_nm = models.CharField(db_column='TET0302_SK_HYOKA_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0302_tokui_saki_cd = models.CharField(db_column='TET0302_TOKUI_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tet0302_insp_term_kaisu = models.SmallIntegerField(db_column='TET0302_INSP_TERM_KAISU', blank=True, null=True)  # Field name made lowercase.
    tet0302_insp_term_tanni = models.CharField(db_column='TET0302_INSP_TERM_TANNI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0302_insp_start_ym = models.CharField(db_column='TET0302_INSP_START_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0302_INSP_PLAN_SHITUSHU'
        unique_together = (('tet0301_insp_plan_seq_no', 'tet0302_insp_shitushu_seq_no'),)


class Tet0303InspKoumoku2Info(models.Model):
    tet0301_insp_cd = models.CharField(db_column='TET0301_INSP_CD', max_length=25)  # Field name made lowercase.
    tet0301_insp_ed_no = models.SmallIntegerField(db_column='TET0301_INSP_ED_NO')  # Field name made lowercase.
    tet0302_koumoku1_cd = models.CharField(db_column='TET0302_KOUMOKU1_CD', max_length=10)  # Field name made lowercase.
    tet0303_koumoku2_cd = models.CharField(db_column='TET0303_KOUMOKU2_CD', max_length=10)  # Field name made lowercase.
    tet0303_hyoka_point_dtl_no = models.SmallIntegerField(db_column='TET0303_HYOKA_POINT_DTL_NO')  # Field name made lowercase.
    tet0303_seiso_kbn = models.CharField(db_column='TET0303_SEISO_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0303_kaisu = models.SmallIntegerField(db_column='TET0303_KAISU', blank=True, null=True)  # Field name made lowercase.
    tet0303_syuki = models.CharField(db_column='TET0303_SYUKI', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0303_hyoka = models.SmallIntegerField(db_column='TET0303_HYOKA', blank=True, null=True)  # Field name made lowercase.
    tet0303_start_datetime = models.DateTimeField(db_column='TET0303_START_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0303_end_datetime = models.DateTimeField(db_column='TET0303_END_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0303_jogai_flg = models.CharField(db_column='TET0303_JOGAI_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0303_comment = models.CharField(db_column='TET0303_COMMENT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tet0303_img1 = models.BinaryField(db_column='TET0303_IMG1', blank=True, null=True)  # Field name made lowercase.
    tet0303_img1_nm = models.CharField(db_column='TET0303_IMG1_NM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tet0303_img1_kak = models.CharField(db_column='TET0303_IMG1_KAK', max_length=11, blank=True, null=True)  # Field name made lowercase.
    tet0303_img2 = models.BinaryField(db_column='TET0303_IMG2', blank=True, null=True)  # Field name made lowercase.
    tet0303_img2_nm = models.CharField(db_column='TET0303_IMG2_NM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tet0303_img2_kak = models.CharField(db_column='TET0303_IMG2_KAK', max_length=11, blank=True, null=True)  # Field name made lowercase.
    tet0303_kaizen_shiji_no = models.SmallIntegerField(db_column='TET0303_KAIZEN_SHIJI_NO', blank=True, null=True)  # Field name made lowercase.
    tet0303_del_flg = models.CharField(db_column='TET0303_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0303_crt_datetime = models.DateTimeField(db_column='TET0303_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0303_crt_user_id = models.CharField(db_column='TET0303_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0303_crt_prog_nm = models.CharField(db_column='TET0303_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0303_upd_datetime = models.DateTimeField(db_column='TET0303_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0303_upd_user_id = models.CharField(db_column='TET0303_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0303_upd_prog_nm = models.CharField(db_column='TET0303_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0303_upd_cnt = models.DecimalField(db_column='TET0303_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0303_genba_jogai_flg = models.CharField(db_column='TET0303_GENBA_JOGAI_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0303_INSP_KOUMOKU2_INFO'


class Tet0303InspPlanTaisho(models.Model):
    tet0301_insp_plan_seq_no = models.DecimalField(db_column='TET0301_INSP_PLAN_SEQ_NO', primary_key=True, max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0302_insp_shitushu_seq_no = models.DecimalField(db_column='TET0302_INSP_SHITUSHU_SEQ_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0303_taisho_seq_no = models.DecimalField(db_column='TET0303_TAISHO_SEQ_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0303_taisho_cd = models.CharField(db_column='TET0303_TAISHO_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0303_taisho_nm = models.CharField(db_column='TET0303_TAISHO_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0303_del_flg = models.CharField(db_column='TET0303_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0303_crt_datetime = models.DateTimeField(db_column='TET0303_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0303_crt_user_id = models.CharField(db_column='TET0303_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0303_crt_prog_nm = models.CharField(db_column='TET0303_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0303_upd_datetime = models.DateTimeField(db_column='TET0303_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0303_upd_user_id = models.CharField(db_column='TET0303_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0303_upd_prog_nm = models.CharField(db_column='TET0303_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0303_upd_cnt = models.DecimalField(db_column='TET0303_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0303_sla_kijyun = models.DecimalField(db_column='TET0303_SLA_KIJYUN', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0303_INSP_PLAN_TAISHO'
        unique_together = (('tet0301_insp_plan_seq_no', 'tet0302_insp_shitushu_seq_no', 'tet0303_taisho_seq_no'),)


class Tet0304InspPlanHyoka(models.Model):
    tet0301_insp_plan_seq_no = models.DecimalField(db_column='TET0301_INSP_PLAN_SEQ_NO', primary_key=True, max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0302_insp_shitushu_seq_no = models.DecimalField(db_column='TET0302_INSP_SHITUSHU_SEQ_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0303_taisho_seq_no = models.DecimalField(db_column='TET0303_TAISHO_SEQ_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0304_dtl_no = models.SmallIntegerField(db_column='TET0304_DTL_NO')  # Field name made lowercase.
    tet0304_seiso_kbn = models.CharField(db_column='TET0304_SEISO_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0304_seiso_term_kaisu = models.SmallIntegerField(db_column='TET0304_SEISO_TERM_KAISU', blank=True, null=True)  # Field name made lowercase.
    tet0304_seiso_term_tanni = models.CharField(db_column='TET0304_SEISO_TERM_TANNI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0304_hyoji_no = models.SmallIntegerField(db_column='TET0304_HYOJI_NO', blank=True, null=True)  # Field name made lowercase.
    tet0304_del_flg = models.CharField(db_column='TET0304_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0304_crt_datetime = models.DateTimeField(db_column='TET0304_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0304_crt_user_id = models.CharField(db_column='TET0304_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0304_crt_prog_nm = models.CharField(db_column='TET0304_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0304_upd_datetime = models.DateTimeField(db_column='TET0304_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0304_upd_user_id = models.CharField(db_column='TET0304_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0304_upd_prog_nm = models.CharField(db_column='TET0304_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0304_upd_cnt = models.DecimalField(db_column='TET0304_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0304_hyoka_point = models.CharField(db_column='TET0304_HYOKA_POINT', max_length=150, blank=True, null=True)  # Field name made lowercase.
    tet0304_taisho_flg = models.CharField(db_column='TET0304_TAISHO_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0304_INSP_PLAN_HYOKA'
        unique_together = (('tet0301_insp_plan_seq_no', 'tet0302_insp_shitushu_seq_no', 'tet0303_taisho_seq_no', 'tet0304_dtl_no'),)


class Tet0304KaizenShiji(models.Model):
    tet0301_insp_cd = models.CharField(db_column='TET0301_INSP_CD', max_length=25)  # Field name made lowercase.
    tet0301_insp_ed_no = models.SmallIntegerField(db_column='TET0301_INSP_ED_NO')  # Field name made lowercase.
    tet0304_kaizen_shiji_no = models.SmallIntegerField(db_column='TET0304_KAIZEN_SHIJI_NO')  # Field name made lowercase.
    tet0304_sakusei_date = models.DateTimeField(db_column='TET0304_SAKUSEI_DATE', blank=True, null=True)  # Field name made lowercase.
    tet0304_tenko_cd = models.CharField(db_column='TET0304_TENKO_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tet0304_category_cd = models.CharField(db_column='TET0304_CATEGORY_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tet0304_koumoku1_cd = models.CharField(db_column='TET0304_KOUMOKU1_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0304_koumoku2_cd = models.CharField(db_column='TET0304_KOUMOKU2_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0304_hyoka_point_dtl_no = models.SmallIntegerField(db_column='TET0304_HYOKA_POINT_DTL_NO', blank=True, null=True)  # Field name made lowercase.
    tet0304_kaizen_sts = models.CharField(db_column='TET0304_KAIZEN_STS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0304_kaizen_shiji_naiyo = models.CharField(db_column='TET0304_KAIZEN_SHIJI_NAIYO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tet0304_genin = models.CharField(db_column='TET0304_GENIN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tet0304_kaizen_hoho = models.CharField(db_column='TET0304_KAIZEN_HOHO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tet0304_kaizen_kigen = models.DateTimeField(db_column='TET0304_KAIZEN_KIGEN', blank=True, null=True)  # Field name made lowercase.
    tet0304_kanryo_date = models.DateTimeField(db_column='TET0304_KANRYO_DATE', blank=True, null=True)  # Field name made lowercase.
    tet0304_hokoku_saki_nm = models.CharField(db_column='TET0304_HOKOKU_SAKI_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tet0304_hokoku_saki_email = models.CharField(db_column='TET0304_HOKOKU_SAKI_EMAIL', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tet0304_saitenken_yotei1 = models.DateTimeField(db_column='TET0304_SAITENKEN_YOTEI1', blank=True, null=True)  # Field name made lowercase.
    tet0304_saitenken_yotei2 = models.DateTimeField(db_column='TET0304_SAITENKEN_YOTEI2', blank=True, null=True)  # Field name made lowercase.
    tet0304_img1 = models.BinaryField(db_column='TET0304_IMG1', blank=True, null=True)  # Field name made lowercase.
    tet0304_img1_nm = models.CharField(db_column='TET0304_IMG1_NM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tet0304_img1_kak = models.CharField(db_column='TET0304_IMG1_KAK', max_length=11, blank=True, null=True)  # Field name made lowercase.
    tet0304_img2 = models.BinaryField(db_column='TET0304_IMG2', blank=True, null=True)  # Field name made lowercase.
    tet0304_img2_nm = models.CharField(db_column='TET0304_IMG2_NM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tet0304_img2_kak = models.CharField(db_column='TET0304_IMG2_KAK', max_length=11, blank=True, null=True)  # Field name made lowercase.
    tet0304_img3 = models.BinaryField(db_column='TET0304_IMG3', blank=True, null=True)  # Field name made lowercase.
    tet0304_img3_nm = models.CharField(db_column='TET0304_IMG3_NM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tet0304_img3_kak = models.CharField(db_column='TET0304_IMG3_KAK', max_length=11, blank=True, null=True)  # Field name made lowercase.
    tet0304_img4 = models.BinaryField(db_column='TET0304_IMG4', blank=True, null=True)  # Field name made lowercase.
    tet0304_img4_nm = models.CharField(db_column='TET0304_IMG4_NM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tet0304_img4_kak = models.CharField(db_column='TET0304_IMG4_KAK', max_length=11, blank=True, null=True)  # Field name made lowercase.
    tet0304_del_flg = models.CharField(db_column='TET0304_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0304_crt_datetime = models.DateTimeField(db_column='TET0304_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0304_crt_user_id = models.CharField(db_column='TET0304_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0304_crt_prog_nm = models.CharField(db_column='TET0304_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0304_upd_datetime = models.DateTimeField(db_column='TET0304_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0304_upd_user_id = models.CharField(db_column='TET0304_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0304_upd_prog_nm = models.CharField(db_column='TET0304_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0304_upd_cnt = models.DecimalField(db_column='TET0304_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0304_KAIZEN_SHIJI'


class Tet0305IjoHokoku(models.Model):
    tet0301_insp_cd = models.CharField(db_column='TET0301_INSP_CD', max_length=25)  # Field name made lowercase.
    tet0301_insp_ed_no = models.SmallIntegerField(db_column='TET0301_INSP_ED_NO')  # Field name made lowercase.
    tet0305_ijo_hokoku_no = models.SmallIntegerField(db_column='TET0305_IJO_HOKOKU_NO')  # Field name made lowercase.
    tet0305_sakusei_date = models.DateTimeField(db_column='TET0305_SAKUSEI_DATE', blank=True, null=True)  # Field name made lowercase.
    tet0305_category_cd = models.CharField(db_column='TET0305_CATEGORY_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tet0305_shitushu_cd = models.CharField(db_column='TET0305_SHITUSHU_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0305_taisho_cd = models.CharField(db_column='TET0305_TAISHO_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0305_kenmei = models.CharField(db_column='TET0305_KENMEI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tet0305_ijo_naiyo = models.CharField(db_column='TET0305_IJO_NAIYO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tet0305_img1 = models.BinaryField(db_column='TET0305_IMG1', blank=True, null=True)  # Field name made lowercase.
    tet0305_img1_nm = models.CharField(db_column='TET0305_IMG1_NM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tet0305_img1_kak = models.CharField(db_column='TET0305_IMG1_KAK', max_length=11, blank=True, null=True)  # Field name made lowercase.
    tet0305_img2 = models.BinaryField(db_column='TET0305_IMG2', blank=True, null=True)  # Field name made lowercase.
    tet0305_img2_nm = models.CharField(db_column='TET0305_IMG2_NM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tet0305_img2_kak = models.CharField(db_column='TET0305_IMG2_KAK', max_length=11, blank=True, null=True)  # Field name made lowercase.
    tet0305_del_flg = models.CharField(db_column='TET0305_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0305_crt_datetime = models.DateTimeField(db_column='TET0305_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0305_crt_user_id = models.CharField(db_column='TET0305_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0305_crt_prog_nm = models.CharField(db_column='TET0305_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0305_upd_datetime = models.DateTimeField(db_column='TET0305_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0305_upd_user_id = models.CharField(db_column='TET0305_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0305_upd_prog_nm = models.CharField(db_column='TET0305_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0305_upd_cnt = models.DecimalField(db_column='TET0305_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0305_IJO_HOKOKU'


class Tet0305InspPlanSeisoSagyoNaiyo(models.Model):
    tet0301_insp_plan_seq_no = models.DecimalField(db_column='TET0301_INSP_PLAN_SEQ_NO', primary_key=True, max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0302_insp_shitushu_seq_no = models.DecimalField(db_column='TET0302_INSP_SHITUSHU_SEQ_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0303_taisho_seq_no = models.DecimalField(db_column='TET0303_TAISHO_SEQ_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0305_dtl_no = models.SmallIntegerField(db_column='TET0305_DTL_NO')  # Field name made lowercase.
    tet0305_naiyo_ptn_cd = models.CharField(db_column='TET0305_NAIYO_PTN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0305_naiyo_ptn_seiso_kbn = models.CharField(db_column='TET0305_NAIYO_PTN_SEISO_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0305_naiyo_nm = models.CharField(db_column='TET0305_NAIYO_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0305_seiso_term_tanni = models.CharField(db_column='TET0305_SEISO_TERM_TANNI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0305_seiso_term_kaisu = models.SmallIntegerField(db_column='TET0305_SEISO_TERM_KAISU', blank=True, null=True)  # Field name made lowercase.
    tet0305_del_flg = models.CharField(db_column='TET0305_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0305_crt_datetime = models.DateTimeField(db_column='TET0305_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0305_crt_user_id = models.CharField(db_column='TET0305_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0305_crt_prog_nm = models.CharField(db_column='TET0305_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0305_upd_datetime = models.DateTimeField(db_column='TET0305_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0305_upd_user_id = models.CharField(db_column='TET0305_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0305_upd_prog_nm = models.CharField(db_column='TET0305_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0305_upd_cnt = models.DecimalField(db_column='TET0305_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0305_INSP_PLAN_SEISO_SAGYO_NAIYO'
        unique_together = (('tet0301_insp_plan_seq_no', 'tet0302_insp_shitushu_seq_no', 'tet0303_taisho_seq_no', 'tet0305_dtl_no'),)


class Tet0401InspBox(models.Model):
    tet0401_insp_box_seq_no = models.AutoField(db_column='TET0401_INSP_BOX_SEQ_NO', primary_key=True)  # Field name made lowercase.
    tet0401_insp_kbn = models.CharField(db_column='TET0401_INSP_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0401_insp_box_nm = models.CharField(db_column='TET0401_INSP_BOX_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tet0401_keikaku_send_flg = models.CharField(db_column='TET0401_KEIKAKU_SEND_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0401_keikaku_pre_mnth = models.SmallIntegerField(db_column='TET0401_KEIKAKU_PRE_MNTH', blank=True, null=True)  # Field name made lowercase.
    tet0401_keikaku_period_mnth = models.SmallIntegerField(db_column='TET0401_KEIKAKU_PERIOD_MNTH', blank=True, null=True)  # Field name made lowercase.
    tet0401_kaizen_send_flg = models.CharField(db_column='TET0401_KAIZEN_SEND_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0401_kaizen_pre_mnth = models.SmallIntegerField(db_column='TET0401_KAIZEN_PRE_MNTH', blank=True, null=True)  # Field name made lowercase.
    tet0401_del_flg = models.CharField(db_column='TET0401_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0401_crt_datetime = models.DateTimeField(db_column='TET0401_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0401_crt_user_id = models.CharField(db_column='TET0401_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0401_crt_prog_nm = models.CharField(db_column='TET0401_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0401_upd_datetime = models.DateTimeField(db_column='TET0401_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0401_upd_user_id = models.CharField(db_column='TET0401_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0401_upd_prog_nm = models.CharField(db_column='TET0401_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0401_upd_cnt = models.DecimalField(db_column='TET0401_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0401_kaizen_send_sts = models.CharField(db_column='TET0401_KAIZEN_SEND_STS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0401_insp_send_sts = models.CharField(db_column='TET0401_INSP_SEND_STS', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0401_INSP_BOX'


class Tet0402InspBoxGenbaDtl(models.Model):
    tet0401_insp_box_seq_no = models.DecimalField(db_column='TET0401_INSP_BOX_SEQ_NO', primary_key=True, max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0402_dtl_no = models.SmallIntegerField(db_column='TET0402_DTL_NO')  # Field name made lowercase.
    tet0402_genba_cd = models.CharField(db_column='TET0402_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tet0402_shoku_cd = models.CharField(db_column='TET0402_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tet0402_del_flg = models.CharField(db_column='TET0402_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0402_crt_datetime = models.DateTimeField(db_column='TET0402_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0402_crt_user_id = models.CharField(db_column='TET0402_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0402_crt_prog_nm = models.CharField(db_column='TET0402_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0402_upd_datetime = models.DateTimeField(db_column='TET0402_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0402_upd_user_id = models.CharField(db_column='TET0402_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0402_upd_prog_nm = models.CharField(db_column='TET0402_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0402_upd_cnt = models.DecimalField(db_column='TET0402_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0402_INSP_BOX_GENBA_DTL'
        unique_together = (('tet0401_insp_box_seq_no', 'tet0402_dtl_no'),)


class Tet0501InspRsltBase(models.Model):
    tet0501_insp_rslt_seq_no = models.AutoField(db_column='TET0501_INSP_RSLT_SEQ_NO', primary_key=True)  # Field name made lowercase.
    tet0501_insp_rslt_no = models.CharField(db_column='TET0501_INSP_RSLT_NO', max_length=25)  # Field name made lowercase.
    tet0501_insp_plan_seq_no = models.DecimalField(db_column='TET0501_INSP_PLAN_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0501_kenmei = models.CharField(db_column='TET0501_KENMEI', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tet0501_genba_cd = models.CharField(db_column='TET0501_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tet0501_shoku_cd = models.CharField(db_column='TET0501_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tet0501_insp_kbn = models.CharField(db_column='TET0501_INSP_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0501_insp_shain_cd = models.CharField(db_column='TET0501_INSP_SHAIN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0501_insp_shain_nm = models.CharField(db_column='TET0501_INSP_SHAIN_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tet0501_device_id = models.CharField(db_column='TET0501_DEVICE_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tet0501_tanmatu_crt_timestamp = models.CharField(db_column='TET0501_TANMATU_CRT_TIMESTAMP', max_length=17, blank=True, null=True)  # Field name made lowercase.
    tet0501_tanmatu_upd_timestamp = models.CharField(db_column='TET0501_TANMATU_UPD_TIMESTAMP', max_length=17, blank=True, null=True)  # Field name made lowercase.
    tet0501_yotei_ym = models.CharField(db_column='TET0501_YOTEI_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tet0501_kaisu = models.SmallIntegerField(db_column='TET0501_KAISU', blank=True, null=True)  # Field name made lowercase.
    tet0501_del_flg = models.CharField(db_column='TET0501_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0501_crt_datetime = models.DateTimeField(db_column='TET0501_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0501_crt_user_id = models.CharField(db_column='TET0501_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0501_crt_prog_nm = models.CharField(db_column='TET0501_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0501_upd_datetime = models.DateTimeField(db_column='TET0501_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0501_upd_user_id = models.CharField(db_column='TET0501_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0501_upd_prog_nm = models.CharField(db_column='TET0501_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0501_upd_cnt = models.DecimalField(db_column='TET0501_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0501_insp_user_seq_no = models.DecimalField(db_column='TET0501_INSP_USER_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0501_jisseki_ymd = models.DateTimeField(db_column='TET0501_JISSEKI_YMD', blank=True, null=True)  # Field name made lowercase.
    tet0501_insp_sts = models.CharField(db_column='TET0501_INSP_STS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0501_insp_rslt_hyoka = models.DecimalField(db_column='TET0501_INSP_RSLT_HYOKA', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tet0501_hyoten_kbn = models.CharField(db_column='TET0501_HYOTEN_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0501_max_haiten = models.SmallIntegerField(db_column='TET0501_MAX_HAITEN', blank=True, null=True)  # Field name made lowercase.
    tet0501_insp_siyo_kbn = models.CharField(db_column='TET0501_INSP_SIYO_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0501_tokui_saki_cd = models.CharField(db_column='TET0501_TOKUI_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tet0501_srv_upd_flg = models.CharField(db_column='TET0501_SRV_UPD_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0501_INSP_RSLT_BASE'


class Tet0502InspRsltShitushu(models.Model):
    tet0501_insp_rslt_seq_no = models.DecimalField(db_column='TET0501_INSP_RSLT_SEQ_NO', primary_key=True, max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0502_insp_shitushu_seq_no = models.DecimalField(db_column='TET0502_INSP_SHITUSHU_SEQ_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0502_shitushu_lv_1_seq_no = models.DecimalField(db_column='TET0502_SHITUSHU_LV_1_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0502_shitushu_lv_1_cd = models.CharField(db_column='TET0502_SHITUSHU_LV_1_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tet0502_shitushu_lv_1_nm = models.CharField(db_column='TET0502_SHITUSHU_LV_1_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0502_shitushu_lv_2_seq_no = models.DecimalField(db_column='TET0502_SHITUSHU_LV_2_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0502_shitushu_lv_2_cd = models.CharField(db_column='TET0502_SHITUSHU_LV_2_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tet0502_shitushu_lv_2_nm = models.CharField(db_column='TET0502_SHITUSHU_LV_2_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0502_shitushu_lv_3_seq_no = models.DecimalField(db_column='TET0502_SHITUSHU_LV_3_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0502_shitushu_lv_3_cd = models.CharField(db_column='TET0502_SHITUSHU_LV_3_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tet0502_shitushu_lv_3_nm = models.CharField(db_column='TET0502_SHITUSHU_LV_3_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0502_shitushu_seq_no = models.DecimalField(db_column='TET0502_SHITUSHU_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0502_shitushu_cd = models.CharField(db_column='TET0502_SHITUSHU_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0502_shitushu_nm = models.CharField(db_column='TET0502_SHITUSHU_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0502_sk_hyoka_seq_no = models.DecimalField(db_column='TET0502_SK_HYOKA_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0502_hyoji_no = models.SmallIntegerField(db_column='TET0502_HYOJI_NO', blank=True, null=True)  # Field name made lowercase.
    tet0502_start_datetime = models.DateTimeField(db_column='TET0502_START_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0502_end_datetime = models.DateTimeField(db_column='TET0502_END_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0502_taishogai_flg = models.CharField(db_column='TET0502_TAISHOGAI_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0502_cmt_comment_seq_no = models.DecimalField(db_column='TET0502_CMT_COMMENT_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0502_ijo_comment_seq_no = models.DecimalField(db_column='TET0502_IJO_COMMENT_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0502_del_flg = models.CharField(db_column='TET0502_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0502_crt_datetime = models.DateTimeField(db_column='TET0502_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0502_crt_user_id = models.CharField(db_column='TET0502_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0502_crt_prog_nm = models.CharField(db_column='TET0502_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0502_upd_datetime = models.DateTimeField(db_column='TET0502_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0502_upd_user_id = models.CharField(db_column='TET0502_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0502_upd_prog_nm = models.CharField(db_column='TET0502_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0502_upd_cnt = models.DecimalField(db_column='TET0502_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0502_tokui_saki_cd = models.CharField(db_column='TET0502_TOKUI_SAKI_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tet0502_sk_hyoka_cd = models.CharField(db_column='TET0502_SK_HYOKA_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0502_sk_hyoka_nm = models.CharField(db_column='TET0502_SK_HYOKA_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0502_insp_term_kaisu = models.SmallIntegerField(db_column='TET0502_INSP_TERM_KAISU', blank=True, null=True)  # Field name made lowercase.
    tet0502_insp_term_tanni = models.CharField(db_column='TET0502_INSP_TERM_TANNI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0502_insp_start_ym = models.CharField(db_column='TET0502_INSP_START_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tet0502_shitushu_hyoka = models.DecimalField(db_column='TET0502_SHITUSHU_HYOKA', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tet0502_shitushu_ttl_tensu = models.DecimalField(db_column='TET0502_SHITUSHU_TTL_TENSU', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tet0502_shitushu_max_tensu = models.DecimalField(db_column='TET0502_SHITUSHU_MAX_TENSU', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0502_INSP_RSLT_SHITUSHU'
        unique_together = (('tet0501_insp_rslt_seq_no', 'tet0502_insp_shitushu_seq_no'),)


class Tet0503InspRsltTaisho(models.Model):
    tet0501_insp_rslt_seq_no = models.DecimalField(db_column='TET0501_INSP_RSLT_SEQ_NO', primary_key=True, max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0502_insp_shitushu_seq_no = models.DecimalField(db_column='TET0502_INSP_SHITUSHU_SEQ_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0503_taisho_seq_no = models.DecimalField(db_column='TET0503_TAISHO_SEQ_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0503_taisho_cd = models.CharField(db_column='TET0503_TAISHO_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0503_taisho_nm = models.CharField(db_column='TET0503_TAISHO_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0503_start_datetime = models.DateTimeField(db_column='TET0503_START_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0503_end_datetime = models.DateTimeField(db_column='TET0503_END_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0503_cmt_comment_seq_no = models.DecimalField(db_column='TET0503_CMT_COMMENT_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0503_ijo_comment_seq_no = models.DecimalField(db_column='TET0503_IJO_COMMENT_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0503_del_flg = models.CharField(db_column='TET0503_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0503_crt_datetime = models.DateTimeField(db_column='TET0503_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0503_crt_user_id = models.CharField(db_column='TET0503_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0503_crt_prog_nm = models.CharField(db_column='TET0503_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0503_upd_datetime = models.DateTimeField(db_column='TET0503_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0503_upd_user_id = models.CharField(db_column='TET0503_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0503_upd_prog_nm = models.CharField(db_column='TET0503_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0503_upd_cnt = models.DecimalField(db_column='TET0503_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0503_taisho_hyoka = models.DecimalField(db_column='TET0503_TAISHO_HYOKA', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tet0503_sla_kijyun = models.DecimalField(db_column='TET0503_SLA_KIJYUN', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0503_INSP_RSLT_TAISHO'
        unique_together = (('tet0501_insp_rslt_seq_no', 'tet0502_insp_shitushu_seq_no', 'tet0503_taisho_seq_no'),)


class Tet0504InspRsltHyoka(models.Model):
    tet0501_insp_rslt_seq_no = models.DecimalField(db_column='TET0501_INSP_RSLT_SEQ_NO', primary_key=True, max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0502_insp_shitushu_seq_no = models.DecimalField(db_column='TET0502_INSP_SHITUSHU_SEQ_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0503_taisho_seq_no = models.DecimalField(db_column='TET0503_TAISHO_SEQ_NO', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0504_dtl_no = models.SmallIntegerField(db_column='TET0504_DTL_NO')  # Field name made lowercase.
    tet0504_seiso_kbn = models.CharField(db_column='TET0504_SEISO_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0504_hyoka_point = models.CharField(db_column='TET0504_HYOKA_POINT', max_length=150, blank=True, null=True)  # Field name made lowercase.
    tet0504_seiso_term_kaisu = models.SmallIntegerField(db_column='TET0504_SEISO_TERM_KAISU', blank=True, null=True)  # Field name made lowercase.
    tet0504_hyoji_no = models.SmallIntegerField(db_column='TET0504_HYOJI_NO', blank=True, null=True)  # Field name made lowercase.
    tet0504_hyoka = models.SmallIntegerField(db_column='TET0504_HYOKA', blank=True, null=True)  # Field name made lowercase.
    tet0504_start_datetime = models.DateTimeField(db_column='TET0504_START_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0504_end_datetime = models.DateTimeField(db_column='TET0504_END_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0504_taishogai_flg = models.CharField(db_column='TET0504_TAISHOGAI_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0504_del_flg = models.CharField(db_column='TET0504_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0504_crt_datetime = models.DateTimeField(db_column='TET0504_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0504_crt_user_id = models.CharField(db_column='TET0504_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0504_crt_prog_nm = models.CharField(db_column='TET0504_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0504_upd_datetime = models.DateTimeField(db_column='TET0504_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0504_upd_user_id = models.CharField(db_column='TET0504_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0504_upd_prog_nm = models.CharField(db_column='TET0504_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0504_upd_cnt = models.DecimalField(db_column='TET0504_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0504_seiso_term_tanni = models.CharField(db_column='TET0504_SEISO_TERM_TANNI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0504_hyoka_label = models.CharField(db_column='TET0504_HYOKA_LABEL', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0504_INSP_RSLT_HYOKA'
        unique_together = (('tet0501_insp_rslt_seq_no', 'tet0502_insp_shitushu_seq_no', 'tet0503_taisho_seq_no', 'tet0504_dtl_no'),)


class Tet0505Comment(models.Model):
    tet0505_comment_seq_no = models.AutoField(db_column='TET0505_COMMENT_SEQ_NO', primary_key=True)  # Field name made lowercase.
    tet0505_insp_rslt_seq_no = models.DecimalField(db_column='TET0505_INSP_RSLT_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0505_taisho_seq_no = models.DecimalField(db_column='TET0505_TAISHO_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0505_category_cd = models.CharField(db_column='TET0505_CATEGORY_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tet0505_insp_kbn = models.CharField(db_column='TET0505_INSP_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0505_doc_kbn = models.CharField(db_column='TET0505_DOC_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0505_comment = models.CharField(db_column='TET0505_COMMENT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tet0505_img1 = models.BinaryField(db_column='TET0505_IMG1', blank=True, null=True)  # Field name made lowercase.
    tet0505_img2 = models.BinaryField(db_column='TET0505_IMG2', blank=True, null=True)  # Field name made lowercase.
    tet0505_del_flg = models.CharField(db_column='TET0505_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0505_crt_datetime = models.DateTimeField(db_column='TET0505_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0505_crt_user_id = models.CharField(db_column='TET0505_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0505_crt_prog_nm = models.CharField(db_column='TET0505_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0505_upd_datetime = models.DateTimeField(db_column='TET0505_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0505_upd_user_id = models.CharField(db_column='TET0505_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0505_upd_prog_nm = models.CharField(db_column='TET0505_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0505_upd_cnt = models.DecimalField(db_column='TET0505_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0505_insp_shitushu_seq_no = models.DecimalField(db_column='TET0505_INSP_SHITUSHU_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0505_COMMENT'


class Tet0601KaizenBase(models.Model):
    tet0601_kaizen_seq_no = models.AutoField(db_column='TET0601_KAIZEN_SEQ_NO', primary_key=True)  # Field name made lowercase.
    tet0601_insp_rslt_seq_no = models.DecimalField(db_column='TET0601_INSP_RSLT_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0601_insp_rslt_no = models.CharField(db_column='TET0601_INSP_RSLT_NO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tet0601_insp_plan_seq_no = models.DecimalField(db_column='TET0601_INSP_PLAN_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0601_kenmei = models.CharField(db_column='TET0601_KENMEI', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tet0601_genba_cd = models.CharField(db_column='TET0601_GENBA_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tet0601_shoku_cd = models.CharField(db_column='TET0601_SHOKU_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tet0601_insp_kbn = models.CharField(db_column='TET0601_INSP_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0601_insp_shain_cd = models.CharField(db_column='TET0601_INSP_SHAIN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0601_insp_shain_nm = models.CharField(db_column='TET0601_INSP_SHAIN_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tet0601_device_id = models.CharField(db_column='TET0601_DEVICE_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tet0601_tanmatu_crt_timestamp = models.CharField(db_column='TET0601_TANMATU_CRT_TIMESTAMP', max_length=17, blank=True, null=True)  # Field name made lowercase.
    tet0601_tanmatu_upd_timestamp = models.CharField(db_column='TET0601_TANMATU_UPD_TIMESTAMP', max_length=17, blank=True, null=True)  # Field name made lowercase.
    tet0601_server_upd_timestamp = models.CharField(db_column='TET0601_SERVER_UPD_TIMESTAMP', max_length=17, blank=True, null=True)  # Field name made lowercase.
    tet0601_kaizen_sts = models.CharField(db_column='TET0601_KAIZEN_STS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0601_sakusei_date = models.DateTimeField(db_column='TET0601_SAKUSEI_DATE', blank=True, null=True)  # Field name made lowercase.
    tet0601_sakusei_kigen = models.DateTimeField(db_column='TET0601_SAKUSEI_KIGEN', blank=True, null=True)  # Field name made lowercase.
    tet0601_mng_nm = models.CharField(db_column='TET0601_MNG_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tet0601_tenko_cd = models.CharField(db_column='TET0601_TENKO_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tet0601_category_cd_1 = models.CharField(db_column='TET0601_CATEGORY_CD_1', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tet0601_category_cd_2 = models.CharField(db_column='TET0601_CATEGORY_CD_2', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tet0601_shitushu_lv_1_seq_no = models.DecimalField(db_column='TET0601_SHITUSHU_LV_1_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0601_shitushu_lv_1_cd = models.CharField(db_column='TET0601_SHITUSHU_LV_1_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tet0601_shitushu_lv_1_nm = models.CharField(db_column='TET0601_SHITUSHU_LV_1_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0601_shitushu_lv_2_seq_no = models.DecimalField(db_column='TET0601_SHITUSHU_LV_2_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0601_shitushu_lv_2_cd = models.CharField(db_column='TET0601_SHITUSHU_LV_2_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tet0601_shitushu_lv_2_nm = models.CharField(db_column='TET0601_SHITUSHU_LV_2_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0601_shitushu_lv_3_seq_no = models.DecimalField(db_column='TET0601_SHITUSHU_LV_3_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0601_shitushu_lv_3_cd = models.CharField(db_column='TET0601_SHITUSHU_LV_3_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tet0601_shitushu_lv_3_nm = models.CharField(db_column='TET0601_SHITUSHU_LV_3_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0601_shitushu_seq_no = models.DecimalField(db_column='TET0601_SHITUSHU_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0601_shitushu_cd = models.CharField(db_column='TET0601_SHITUSHU_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0601_shitushu_nm = models.CharField(db_column='TET0601_SHITUSHU_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0601_taisho_seq_no = models.DecimalField(db_column='TET0601_TAISHO_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0601_taisho_cd = models.CharField(db_column='TET0601_TAISHO_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0601_taisho_nm = models.CharField(db_column='TET0601_TAISHO_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0601_del_flg = models.CharField(db_column='TET0601_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0601_crt_datetime = models.DateTimeField(db_column='TET0601_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0601_crt_user_id = models.CharField(db_column='TET0601_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0601_crt_prog_nm = models.CharField(db_column='TET0601_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0601_upd_datetime = models.DateTimeField(db_column='TET0601_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0601_upd_user_id = models.CharField(db_column='TET0601_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0601_upd_prog_nm = models.CharField(db_column='TET0601_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0601_upd_cnt = models.DecimalField(db_column='TET0601_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0601_img1 = models.BinaryField(db_column='TET0601_IMG1', blank=True, null=True)  # Field name made lowercase.
    tet0601_img2 = models.BinaryField(db_column='TET0601_IMG2', blank=True, null=True)  # Field name made lowercase.
    tet0601_img3 = models.BinaryField(db_column='TET0601_IMG3', blank=True, null=True)  # Field name made lowercase.
    tet0601_img4 = models.BinaryField(db_column='TET0601_IMG4', blank=True, null=True)  # Field name made lowercase.
    tet0601_img5 = models.BinaryField(db_column='TET0601_IMG5', blank=True, null=True)  # Field name made lowercase.
    tet0601_mng_cd = models.CharField(db_column='TET0601_MNG_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0601_sk_hyoka_seq_no = models.DecimalField(db_column='TET0601_SK_HYOKA_SEQ_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0601_sk_hyoka_cd = models.CharField(db_column='TET0601_SK_HYOKA_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0601_sk_hyoka_nm = models.CharField(db_column='TET0601_SK_HYOKA_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0601_tenko_nm = models.CharField(db_column='TET0601_TENKO_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0601_category_nm_1 = models.CharField(db_column='TET0601_CATEGORY_NM_1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0601_category_nm_2 = models.CharField(db_column='TET0601_CATEGORY_NM_2', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0601_KAIZEN_BASE'


class Tet0602KaizenDtl(models.Model):
    tet0601_kaizen_seq_no = models.DecimalField(db_column='TET0601_KAIZEN_SEQ_NO', primary_key=True, max_digits=10, decimal_places=0)  # Field name made lowercase.
    tet0602_dtl_no = models.SmallIntegerField(db_column='TET0602_DTL_NO')  # Field name made lowercase.
    tet0602_genin = models.TextField(db_column='TET0602_GENIN', blank=True, null=True)  # Field name made lowercase.
    tet0602_kaizen_hoho = models.TextField(db_column='TET0602_KAIZEN_HOHO', blank=True, null=True)  # Field name made lowercase.
    tet0602_kaizen_kigen = models.DateTimeField(db_column='TET0602_KAIZEN_KIGEN', blank=True, null=True)  # Field name made lowercase.
    tet0602_saitenken_yotei = models.DateTimeField(db_column='TET0602_SAITENKEN_YOTEI', blank=True, null=True)  # Field name made lowercase.
    tet0602_jissi_date = models.DateTimeField(db_column='TET0602_JISSI_DATE', blank=True, null=True)  # Field name made lowercase.
    tet0602_iraisaki_shain_cd = models.CharField(db_column='TET0602_IRAISAKI_SHAIN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tet0602_iraisaki_shain_nm = models.CharField(db_column='TET0602_IRAISAKI_SHAIN_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tet0602_tenken_kekka = models.CharField(db_column='TET0602_TENKEN_KEKKA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0602_kanryo_date = models.DateTimeField(db_column='TET0602_KANRYO_DATE', blank=True, null=True)  # Field name made lowercase.
    tet0602_del_flg = models.CharField(db_column='TET0602_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tet0602_crt_datetime = models.DateTimeField(db_column='TET0602_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0602_crt_user_id = models.CharField(db_column='TET0602_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0602_crt_prog_nm = models.CharField(db_column='TET0602_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0602_upd_datetime = models.DateTimeField(db_column='TET0602_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tet0602_upd_user_id = models.CharField(db_column='TET0602_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tet0602_upd_prog_nm = models.CharField(db_column='TET0602_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tet0602_upd_cnt = models.DecimalField(db_column='TET0602_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tet0602_kaizen_naiyo = models.TextField(db_column='TET0602_KAIZEN_NAIYO', blank=True, null=True)  # Field name made lowercase.
    tet0602_tanmatu_crt_timestamp = models.CharField(db_column='TET0602_TANMATU_CRT_TIMESTAMP', max_length=17, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TET0602_KAIZEN_DTL'
        unique_together = (('tet0601_kaizen_seq_no', 'tet0602_dtl_no'),)


class Tfm0101Sten(models.Model):
    tmm01_nend = models.SmallIntegerField(db_column='TMM01_NEND', primary_key=True)  # Field name made lowercase.
    tfm0101_sten_cd = models.CharField(db_column='TFM0101_STEN_CD', max_length=2)  # Field name made lowercase.
    tfm0101_sten_nm = models.CharField(db_column='TFM0101_STEN_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tfm0101_sten_hyoj_no = models.SmallIntegerField(db_column='TFM0101_STEN_HYOJ_NO', blank=True, null=True)  # Field name made lowercase.
    tfm0101_del_flg = models.CharField(db_column='TFM0101_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tfm0101_crt_datetime = models.DateTimeField(db_column='TFM0101_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tfm0101_crt_user_id = models.CharField(db_column='TFM0101_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tfm0101_crt_prog_nm = models.CharField(db_column='TFM0101_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tfm0101_upd_datetime = models.DateTimeField(db_column='TFM0101_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tfm0101_upd_user_id = models.CharField(db_column='TFM0101_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tfm0101_upd_prog_nm = models.CharField(db_column='TFM0101_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tfm0101_upd_cnt = models.DecimalField(db_column='TFM0101_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TFM0101_STEN'
        unique_together = (('tmm01_nend', 'tfm0101_sten_cd'),)


class Tfm0102NaniDo(models.Model):
    tfm0102_nani_do = models.CharField(db_column='TFM0102_NANI_DO', primary_key=True, max_length=2)  # Field name made lowercase.
    tfm0102_hyoj_no = models.SmallIntegerField(db_column='TFM0102_HYOJ_NO', blank=True, null=True)  # Field name made lowercase.
    tfm0102_del_flg = models.CharField(db_column='TFM0102_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tfm0102_crt_datetime = models.DateTimeField(db_column='TFM0102_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tfm0102_crt_user_id = models.CharField(db_column='TFM0102_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tfm0102_crt_prog_nm = models.CharField(db_column='TFM0102_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tfm0102_upd_datetime = models.DateTimeField(db_column='TFM0102_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tfm0102_upd_user_id = models.CharField(db_column='TFM0102_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tfm0102_upd_prog_nm = models.CharField(db_column='TFM0102_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tfm0102_upd_cnt = models.DecimalField(db_column='TFM0102_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TFM0102_NANI_DO'


class Tfm0103KanrTkseKb(models.Model):
    tfm0103_kanr_toks_kb = models.CharField(db_column='TFM0103_KANR_TOKS_KB', primary_key=True, max_length=2)  # Field name made lowercase.
    tfm0103_kanr_toks_kb_nm = models.CharField(db_column='TFM0103_KANR_TOKS_KB_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tfm0103_biko = models.CharField(db_column='TFM0103_BIKO', max_length=150, blank=True, null=True)  # Field name made lowercase.
    tfm0103_kanr_toks_kb_hyoj_no = models.SmallIntegerField(db_column='TFM0103_KANR_TOKS_KB_HYOJ_NO', blank=True, null=True)  # Field name made lowercase.
    tfm0103_del_flg = models.CharField(db_column='TFM0103_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tfm0103_crt_datetime = models.DateTimeField(db_column='TFM0103_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tfm0103_crt_user_id = models.CharField(db_column='TFM0103_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tfm0103_crt_prog_nm = models.CharField(db_column='TFM0103_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tfm0103_upd_datetime = models.DateTimeField(db_column='TFM0103_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tfm0103_upd_user_id = models.CharField(db_column='TFM0103_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tfm0103_upd_prog_nm = models.CharField(db_column='TFM0103_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tfm0103_upd_cnt = models.DecimalField(db_column='TFM0103_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TFM0103_KANR_TKSE_KB'


class Tfm0104KanrTkse(models.Model):
    tfm0104_kanr_toks_cd = models.CharField(db_column='TFM0104_KANR_TOKS_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tfm0104_kanr_toks_nm = models.CharField(db_column='TFM0104_KANR_TOKS_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tfm0104_kanr_toks_hyoj_no = models.SmallIntegerField(db_column='TFM0104_KANR_TOKS_HYOJ_NO', blank=True, null=True)  # Field name made lowercase.
    tfm0104_kanr_toks_kb = models.CharField(db_column='TFM0104_KANR_TOKS_KB', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tfm0104_mins_mkhy_flg = models.CharField(db_column='TFM0104_MINS_MKHY_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tfm0104_not_tumi_flg = models.CharField(db_column='TFM0104_NOT_TUMI_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tfm0104_teisei_flg = models.CharField(db_column='TFM0104_TEISEI_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tfm0104_sum_grp_no = models.SmallIntegerField(db_column='TFM0104_SUM_GRP_NO', blank=True, null=True)  # Field name made lowercase.
    tfm0104_tnen_kbn = models.CharField(db_column='TFM0104_TNEN_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tfm0104_jisk_teisei_01 = models.CharField(db_column='TFM0104_JISK_TEISEI_01', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tfm0104_jisk_teisei_02 = models.CharField(db_column='TFM0104_JISK_TEISEI_02', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tfm0104_jisk_teisei_03 = models.CharField(db_column='TFM0104_JISK_TEISEI_03', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tfm0104_jisk_teisei_04 = models.CharField(db_column='TFM0104_JISK_TEISEI_04', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tfm0104_jisk_teisei_05 = models.CharField(db_column='TFM0104_JISK_TEISEI_05', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tfm0104_del_flg = models.CharField(db_column='TFM0104_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tfm0104_crt_datetime = models.DateTimeField(db_column='TFM0104_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tfm0104_crt_user_id = models.CharField(db_column='TFM0104_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tfm0104_crt_prog_nm = models.CharField(db_column='TFM0104_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tfm0104_upd_datetime = models.DateTimeField(db_column='TFM0104_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tfm0104_upd_user_id = models.CharField(db_column='TFM0104_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tfm0104_upd_prog_nm = models.CharField(db_column='TFM0104_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tfm0104_upd_cnt = models.DecimalField(db_column='TFM0104_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tfm0104_point_kbn = models.CharField(db_column='TFM0104_POINT_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TFM0104_KANR_TKSE'


class Tfm0105BmnShain(models.Model):
    tfm0105_shain_seq = models.AutoField(db_column='TFM0105_SHAIN_SEQ', primary_key=True)  # Field name made lowercase.
    tmm01_nend = models.SmallIntegerField(db_column='TMM01_NEND', blank=True, null=True)  # Field name made lowercase.
    tfm0105_bmn_cd = models.CharField(db_column='TFM0105_BMN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tfm0105_shain_cd = models.CharField(db_column='TFM0105_SHAIN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tfm0105_mkhy_shain_kb = models.CharField(db_column='TFM0105_MKHY_SHAIN_KB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tfm0105_hyoji_nm = models.CharField(db_column='TFM0105_HYOJI_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tfm0105_new_plan_kgn = models.CharField(db_column='TFM0105_NEW_PLAN_KGN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tfm0105_chld_bmn_kgn = models.CharField(db_column='TFM0105_CHLD_BMN_KGN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tfm0105_del_flg = models.CharField(db_column='TFM0105_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tfm0105_crt_datetime = models.DateTimeField(db_column='TFM0105_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tfm0105_crt_user_id = models.CharField(db_column='TFM0105_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tfm0105_crt_prog_nm = models.CharField(db_column='TFM0105_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tfm0105_upd_datetime = models.DateTimeField(db_column='TFM0105_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tfm0105_upd_user_id = models.CharField(db_column='TFM0105_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tfm0105_upd_prog_nm = models.CharField(db_column='TFM0105_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tfm0105_upd_cnt = models.DecimalField(db_column='TFM0105_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TFM0105_BMN_SHAIN'


class Tft0101MkhySsak(models.Model):
    tft0101_nend = models.SmallIntegerField(db_column='TFT0101_NEND', primary_key=True)  # Field name made lowercase.
    tft0101_mkhy_ssak_no = models.DecimalField(db_column='TFT0101_MKHY_SSAK_NO', max_digits=18, decimal_places=0)  # Field name made lowercase.
    tft0101_plan_no = models.SmallIntegerField(db_column='TFT0101_PLAN_NO', blank=True, null=True)  # Field name made lowercase.
    tft0101_kais_cd = models.SmallIntegerField(db_column='TFT0101_KAIS_CD', blank=True, null=True)  # Field name made lowercase.
    tft0101_kais_nm = models.CharField(db_column='TFT0101_KAIS_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tft0101_sten_cd = models.CharField(db_column='TFT0101_STEN_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tft0101_kais_kbn = models.CharField(db_column='TFT0101_KAIS_KBN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tft0101_mkhy_ssak_id = models.CharField(db_column='TFT0101_MKHY_SSAK_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tft0101_mkhy_ssak_nm = models.CharField(db_column='TFT0101_MKHY_SSAK_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tft0101_shain_seq = models.DecimalField(db_column='TFT0101_SHAIN_SEQ', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0101_weit = models.DecimalField(db_column='TFT0101_WEIT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0101_kanr_toks_cd = models.CharField(db_column='TFT0101_KANR_TOKS_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tft0101_tnen_mkhy_val = models.DecimalField(db_column='TFT0101_TNEN_MKHY_VAL', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0101_mkhy_ssak_biko = models.CharField(db_column='TFT0101_MKHY_SSAK_BIKO', max_length=150, blank=True, null=True)  # Field name made lowercase.
    tft0101_joi_mkhy_ssak_no = models.DecimalField(db_column='TFT0101_JOI_MKHY_SSAK_NO', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0101_hyoj_no = models.SmallIntegerField(db_column='TFT0101_HYOJ_NO', blank=True, null=True)  # Field name made lowercase.
    tft0101_last_kais_flg = models.CharField(db_column='TFT0101_LAST_KAIS_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tft0101_copy_moto_no = models.DecimalField(db_column='TFT0101_COPY_MOTO_NO', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0101_mkhy_flg = models.CharField(db_column='TFT0101_MKHY_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tft0101_ysn_bumon_cd = models.CharField(db_column='TFT0101_YSN_BUMON_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tft0101_ysn_yosan_utwk_cd = models.CharField(db_column='TFT0101_YSN_YOSAN_UTWK_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tft0101_mkhy_ssak_no_01 = models.DecimalField(db_column='TFT0101_MKHY_SSAK_NO_01', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0101_mkhy_ssak_no_02 = models.DecimalField(db_column='TFT0101_MKHY_SSAK_NO_02', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0101_mkhy_ssak_no_03 = models.DecimalField(db_column='TFT0101_MKHY_SSAK_NO_03', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0101_mkhy_ssak_no_04 = models.DecimalField(db_column='TFT0101_MKHY_SSAK_NO_04', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0101_mkhy_ssak_no_05 = models.DecimalField(db_column='TFT0101_MKHY_SSAK_NO_05', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0101_mkhy_ssak_no_06 = models.DecimalField(db_column='TFT0101_MKHY_SSAK_NO_06', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0101_mkhy_ssak_no_07 = models.DecimalField(db_column='TFT0101_MKHY_SSAK_NO_07', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0101_mkhy_ssak_no_08 = models.DecimalField(db_column='TFT0101_MKHY_SSAK_NO_08', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0101_mkhy_ssak_no_09 = models.DecimalField(db_column='TFT0101_MKHY_SSAK_NO_09', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0101_mkhy_ssak_no_10 = models.DecimalField(db_column='TFT0101_MKHY_SSAK_NO_10', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0101_mkhy_ssak_no_11 = models.DecimalField(db_column='TFT0101_MKHY_SSAK_NO_11', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0101_mkhy_ssak_no_12 = models.DecimalField(db_column='TFT0101_MKHY_SSAK_NO_12', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0101_mkhy_ssak_no_13 = models.DecimalField(db_column='TFT0101_MKHY_SSAK_NO_13', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0101_mkhy_ssak_no_14 = models.DecimalField(db_column='TFT0101_MKHY_SSAK_NO_14', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0101_mkhy_ssak_no_15 = models.DecimalField(db_column='TFT0101_MKHY_SSAK_NO_15', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0101_del_flg = models.CharField(db_column='TFT0101_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tft0101_crt_datetime = models.DateTimeField(db_column='TFT0101_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tft0101_crt_user_id = models.CharField(db_column='TFT0101_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tft0101_crt_prog_nm = models.CharField(db_column='TFT0101_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tft0101_upd_datetime = models.DateTimeField(db_column='TFT0101_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tft0101_upd_user_id = models.CharField(db_column='TFT0101_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tft0101_upd_prog_nm = models.CharField(db_column='TFT0101_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tft0101_upd_cnt = models.DecimalField(db_column='TFT0101_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0101_limit_month = models.SmallIntegerField(db_column='TFT0101_LIMIT_MONTH', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TFT0101_MKHY_SSAK'
        unique_together = (('tft0101_nend', 'tft0101_mkhy_ssak_no'),)


class Tft0102TukiMkhyJisk(models.Model):
    tft0102_nend = models.SmallIntegerField(db_column='TFT0102_NEND', primary_key=True)  # Field name made lowercase.
    tft0102_mkhy_ssak_no = models.DecimalField(db_column='TFT0102_MKHY_SSAK_NO', max_digits=18, decimal_places=0)  # Field name made lowercase.
    tft0102_mkhy_val_01 = models.DecimalField(db_column='TFT0102_MKHY_VAL_01', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_mkhy_val_02 = models.DecimalField(db_column='TFT0102_MKHY_VAL_02', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_mkhy_val_03 = models.DecimalField(db_column='TFT0102_MKHY_VAL_03', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_mkhy_val_04 = models.DecimalField(db_column='TFT0102_MKHY_VAL_04', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_mkhy_val_05 = models.DecimalField(db_column='TFT0102_MKHY_VAL_05', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_mkhy_val_06 = models.DecimalField(db_column='TFT0102_MKHY_VAL_06', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_mkhy_val_07 = models.DecimalField(db_column='TFT0102_MKHY_VAL_07', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_mkhy_val_08 = models.DecimalField(db_column='TFT0102_MKHY_VAL_08', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_mkhy_val_09 = models.DecimalField(db_column='TFT0102_MKHY_VAL_09', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_mkhy_val_10 = models.DecimalField(db_column='TFT0102_MKHY_VAL_10', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_mkhy_val_11 = models.DecimalField(db_column='TFT0102_MKHY_VAL_11', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_mkhy_val_12 = models.DecimalField(db_column='TFT0102_MKHY_VAL_12', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_01 = models.DecimalField(db_column='TFT0102_WEIT_01', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_02 = models.DecimalField(db_column='TFT0102_WEIT_02', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_03 = models.DecimalField(db_column='TFT0102_WEIT_03', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_04 = models.DecimalField(db_column='TFT0102_WEIT_04', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_05 = models.DecimalField(db_column='TFT0102_WEIT_05', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_06 = models.DecimalField(db_column='TFT0102_WEIT_06', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_07 = models.DecimalField(db_column='TFT0102_WEIT_07', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_08 = models.DecimalField(db_column='TFT0102_WEIT_08', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_09 = models.DecimalField(db_column='TFT0102_WEIT_09', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_10 = models.DecimalField(db_column='TFT0102_WEIT_10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_11 = models.DecimalField(db_column='TFT0102_WEIT_11', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_12 = models.DecimalField(db_column='TFT0102_WEIT_12', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_01 = models.DecimalField(db_column='TFT0102_JISK_01', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_02 = models.DecimalField(db_column='TFT0102_JISK_02', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_03 = models.DecimalField(db_column='TFT0102_JISK_03', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_04 = models.DecimalField(db_column='TFT0102_JISK_04', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_05 = models.DecimalField(db_column='TFT0102_JISK_05', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_06 = models.DecimalField(db_column='TFT0102_JISK_06', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_07 = models.DecimalField(db_column='TFT0102_JISK_07', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_08 = models.DecimalField(db_column='TFT0102_JISK_08', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_09 = models.DecimalField(db_column='TFT0102_JISK_09', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_10 = models.DecimalField(db_column='TFT0102_JISK_10', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_11 = models.DecimalField(db_column='TFT0102_JISK_11', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_12 = models.DecimalField(db_column='TFT0102_JISK_12', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_teisei_01 = models.CharField(db_column='TFT0102_JISK_TEISEI_01', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_teisei_02 = models.CharField(db_column='TFT0102_JISK_TEISEI_02', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_teisei_03 = models.CharField(db_column='TFT0102_JISK_TEISEI_03', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_teisei_04 = models.CharField(db_column='TFT0102_JISK_TEISEI_04', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_teisei_05 = models.CharField(db_column='TFT0102_JISK_TEISEI_05', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_teisei_06 = models.CharField(db_column='TFT0102_JISK_TEISEI_06', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_teisei_07 = models.CharField(db_column='TFT0102_JISK_TEISEI_07', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_teisei_08 = models.CharField(db_column='TFT0102_JISK_TEISEI_08', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_teisei_09 = models.CharField(db_column='TFT0102_JISK_TEISEI_09', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_teisei_10 = models.CharField(db_column='TFT0102_JISK_TEISEI_10', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_teisei_11 = models.CharField(db_column='TFT0102_JISK_TEISEI_11', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tft0102_jisk_teisei_12 = models.CharField(db_column='TFT0102_JISK_TEISEI_12', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_jisk_01 = models.DecimalField(db_column='TFT0102_WEIT_JISK_01', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_jisk_02 = models.DecimalField(db_column='TFT0102_WEIT_JISK_02', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_jisk_03 = models.DecimalField(db_column='TFT0102_WEIT_JISK_03', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_jisk_04 = models.DecimalField(db_column='TFT0102_WEIT_JISK_04', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_jisk_05 = models.DecimalField(db_column='TFT0102_WEIT_JISK_05', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_jisk_06 = models.DecimalField(db_column='TFT0102_WEIT_JISK_06', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_jisk_07 = models.DecimalField(db_column='TFT0102_WEIT_JISK_07', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_jisk_08 = models.DecimalField(db_column='TFT0102_WEIT_JISK_08', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_jisk_09 = models.DecimalField(db_column='TFT0102_WEIT_JISK_09', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_jisk_10 = models.DecimalField(db_column='TFT0102_WEIT_JISK_10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_jisk_11 = models.DecimalField(db_column='TFT0102_WEIT_JISK_11', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_weit_jisk_12 = models.DecimalField(db_column='TFT0102_WEIT_JISK_12', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0102_shain_seq_01 = models.DecimalField(db_column='TFT0102_SHAIN_SEQ_01', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0102_shain_seq_02 = models.DecimalField(db_column='TFT0102_SHAIN_SEQ_02', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0102_shain_seq_03 = models.DecimalField(db_column='TFT0102_SHAIN_SEQ_03', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0102_shain_seq_04 = models.DecimalField(db_column='TFT0102_SHAIN_SEQ_04', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0102_shain_seq_05 = models.DecimalField(db_column='TFT0102_SHAIN_SEQ_05', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0102_shain_seq_06 = models.DecimalField(db_column='TFT0102_SHAIN_SEQ_06', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0102_shain_seq_07 = models.DecimalField(db_column='TFT0102_SHAIN_SEQ_07', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0102_shain_seq_08 = models.DecimalField(db_column='TFT0102_SHAIN_SEQ_08', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0102_shain_seq_09 = models.DecimalField(db_column='TFT0102_SHAIN_SEQ_09', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0102_shain_seq_10 = models.DecimalField(db_column='TFT0102_SHAIN_SEQ_10', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0102_shain_seq_11 = models.DecimalField(db_column='TFT0102_SHAIN_SEQ_11', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0102_shain_seq_12 = models.DecimalField(db_column='TFT0102_SHAIN_SEQ_12', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0102_del_flg = models.CharField(db_column='TFT0102_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tft0102_crt_datetime = models.DateTimeField(db_column='TFT0102_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tft0102_crt_user_id = models.CharField(db_column='TFT0102_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tft0102_crt_prog_nm = models.CharField(db_column='TFT0102_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tft0102_upd_datetime = models.DateTimeField(db_column='TFT0102_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tft0102_upd_user_id = models.CharField(db_column='TFT0102_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tft0102_upd_prog_nm = models.CharField(db_column='TFT0102_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tft0102_upd_cnt = models.DecimalField(db_column='TFT0102_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TFT0102_TUKI_MKHY_JISK'
        unique_together = (('tft0102_nend', 'tft0102_mkhy_ssak_no'),)


class Tft0103PlanZens(models.Model):
    tft0103_nend = models.SmallIntegerField(db_column='TFT0103_NEND', primary_key=True)  # Field name made lowercase.
    tft0103_plan_no = models.SmallIntegerField(db_column='TFT0103_PLAN_NO')  # Field name made lowercase.
    tft0103_plan_nm = models.CharField(db_column='TFT0103_PLAN_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tft0103_jisk_inp_sta_tuki = models.CharField(db_column='TFT0103_JISK_INP_STA_TUKI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tft0103_teky_sta_date = models.DateTimeField(db_column='TFT0103_TEKY_STA_DATE', blank=True, null=True)  # Field name made lowercase.
    tft0103_teky_end_date = models.DateTimeField(db_column='TFT0103_TEKY_END_DATE', blank=True, null=True)  # Field name made lowercase.
    tft0103_new_data_flg = models.CharField(db_column='TFT0103_NEW_DATA_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tft0103_copy_moto_plan_no = models.SmallIntegerField(db_column='TFT0103_COPY_MOTO_PLAN_NO', blank=True, null=True)  # Field name made lowercase.
    tft0103_biko = models.CharField(db_column='TFT0103_BIKO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tft0103_del_flg = models.CharField(db_column='TFT0103_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tft0103_crt_datetime = models.DateTimeField(db_column='TFT0103_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tft0103_crt_user_id = models.CharField(db_column='TFT0103_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tft0103_crt_prog_nm = models.CharField(db_column='TFT0103_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tft0103_upd_datetime = models.DateTimeField(db_column='TFT0103_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tft0103_upd_user_id = models.CharField(db_column='TFT0103_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tft0103_upd_prog_nm = models.CharField(db_column='TFT0103_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tft0103_upd_cnt = models.DecimalField(db_column='TFT0103_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TFT0103_PLAN_ZENS'
        unique_together = (('tft0103_nend', 'tft0103_plan_no'),)


class Tft0104PlanLock(models.Model):
    tft0103_nend = models.SmallIntegerField(db_column='TFT0103_NEND', primary_key=True)  # Field name made lowercase.
    tft0103_plan_no = models.SmallIntegerField(db_column='TFT0103_PLAN_NO')  # Field name made lowercase.
    tft0104_bmn_cd = models.CharField(db_column='TFT0104_BMN_CD', max_length=10)  # Field name made lowercase.
    tft0104_shain_seq = models.DecimalField(db_column='TFT0104_SHAIN_SEQ', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tft0104_lock_flg = models.CharField(db_column='TFT0104_LOCK_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tft0104_del_flg = models.CharField(db_column='TFT0104_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tft0104_crt_datetime = models.DateTimeField(db_column='TFT0104_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tft0104_crt_user_id = models.CharField(db_column='TFT0104_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tft0104_crt_prog_nm = models.CharField(db_column='TFT0104_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tft0104_upd_datetime = models.DateTimeField(db_column='TFT0104_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tft0104_upd_user_id = models.CharField(db_column='TFT0104_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tft0104_upd_prog_nm = models.CharField(db_column='TFT0104_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tft0104_upd_cnt = models.DecimalField(db_column='TFT0104_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TFT0104_PLAN_LOCK'
        unique_together = (('tft0103_nend', 'tft0103_plan_no', 'tft0104_bmn_cd', 'tft0104_shain_seq'),)


class Tft0105TantPlan(models.Model):
    tft0103_nend = models.SmallIntegerField(db_column='TFT0103_NEND', primary_key=True)  # Field name made lowercase.
    tft0103_plan_no = models.SmallIntegerField(db_column='TFT0103_PLAN_NO')  # Field name made lowercase.
    tft0105_shain_seq = models.DecimalField(db_column='TFT0105_SHAIN_SEQ', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tft0105_nanido_total = models.CharField(db_column='TFT0105_NANIDO_TOTAL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tft0105_nanido_sten_01 = models.CharField(db_column='TFT0105_NANIDO_STEN_01', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tft0105_nanido_sten_02 = models.CharField(db_column='TFT0105_NANIDO_STEN_02', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tft0105_nanido_sten_03 = models.CharField(db_column='TFT0105_NANIDO_STEN_03', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tft0105_nanido_sten_04 = models.CharField(db_column='TFT0105_NANIDO_STEN_04', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tft0105_nanido_sten_05 = models.CharField(db_column='TFT0105_NANIDO_STEN_05', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tft0105_nen_total_mkhy_weit = models.DecimalField(db_column='TFT0105_NEN_TOTAL_MKHY_WEIT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0105_nen_total_ssak_weit = models.DecimalField(db_column='TFT0105_NEN_TOTAL_SSAK_WEIT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tft0105_evid_path = models.CharField(db_column='TFT0105_EVID_PATH', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tft0105_evid_file_nm_01 = models.CharField(db_column='TFT0105_EVID_FILE_NM_01', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tft0105_evid_file_nm_02 = models.CharField(db_column='TFT0105_EVID_FILE_NM_02', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tft0105_evid_file_nm_03 = models.CharField(db_column='TFT0105_EVID_FILE_NM_03', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tft0105_evid_file_nm_04 = models.CharField(db_column='TFT0105_EVID_FILE_NM_04', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tft0105_evid_file_nm_05 = models.CharField(db_column='TFT0105_EVID_FILE_NM_05', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tft0105_evid_file_nm_06 = models.CharField(db_column='TFT0105_EVID_FILE_NM_06', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tft0105_evid_file_nm_07 = models.CharField(db_column='TFT0105_EVID_FILE_NM_07', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tft0105_evid_file_nm_08 = models.CharField(db_column='TFT0105_EVID_FILE_NM_08', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tft0105_evid_file_nm_09 = models.CharField(db_column='TFT0105_EVID_FILE_NM_09', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tft0105_evid_file_nm_10 = models.CharField(db_column='TFT0105_EVID_FILE_NM_10', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tft0105_evid_file_nm_11 = models.CharField(db_column='TFT0105_EVID_FILE_NM_11', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tft0105_evid_file_nm_12 = models.CharField(db_column='TFT0105_EVID_FILE_NM_12', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tft0105_del_flg = models.CharField(db_column='TFT0105_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tft0105_crt_datetime = models.DateTimeField(db_column='TFT0105_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tft0105_crt_user_id = models.CharField(db_column='TFT0105_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tft0105_crt_prog_nm = models.CharField(db_column='TFT0105_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tft0105_upd_datetime = models.DateTimeField(db_column='TFT0105_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tft0105_upd_user_id = models.CharField(db_column='TFT0105_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tft0105_upd_prog_nm = models.CharField(db_column='TFT0105_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tft0105_upd_cnt = models.DecimalField(db_column='TFT0105_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TFT0105_TANT_PLAN'
        unique_together = (('tft0103_nend', 'tft0103_plan_no', 'tft0105_shain_seq'),)


class Tft0106TantPlanDtl(models.Model):
    tft0103_nend = models.SmallIntegerField(db_column='TFT0103_NEND', primary_key=True)  # Field name made lowercase.
    tft0103_plan_no = models.SmallIntegerField(db_column='TFT0103_PLAN_NO')  # Field name made lowercase.
    tft0105_shain_seq = models.DecimalField(db_column='TFT0105_SHAIN_SEQ', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tft0106_mkhy_ssak_no = models.DecimalField(db_column='TFT0106_MKHY_SSAK_NO', max_digits=18, decimal_places=0)  # Field name made lowercase.
    tft0106_mkhy_ssak_kbn = models.CharField(db_column='TFT0106_MKHY_SSAK_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tft0106_del_flg = models.CharField(db_column='TFT0106_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tft0106_crt_datetime = models.DateTimeField(db_column='TFT0106_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tft0106_crt_user_id = models.CharField(db_column='TFT0106_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tft0106_crt_prog_nm = models.CharField(db_column='TFT0106_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tft0106_upd_datetime = models.DateTimeField(db_column='TFT0106_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tft0106_upd_user_id = models.CharField(db_column='TFT0106_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tft0106_upd_prog_nm = models.CharField(db_column='TFT0106_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tft0106_upd_cnt = models.DecimalField(db_column='TFT0106_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TFT0106_TANT_PLAN_DTL'
        unique_together = (('tft0103_nend', 'tft0103_plan_no', 'tft0105_shain_seq', 'tft0106_mkhy_ssak_no'),)


class Tft0107KaisPlan(models.Model):
    tft0103_nend = models.SmallIntegerField(db_column='TFT0103_NEND', primary_key=True)  # Field name made lowercase.
    tft0103_plan_no = models.SmallIntegerField(db_column='TFT0103_PLAN_NO')  # Field name made lowercase.
    tft0107_kais_cd = models.SmallIntegerField(db_column='TFT0107_KAIS_CD')  # Field name made lowercase.
    tft0107_kais_nm = models.CharField(db_column='TFT0107_KAIS_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tft0107_shain_seq = models.DecimalField(db_column='TFT0107_SHAIN_SEQ', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tft0107_del_flg = models.CharField(db_column='TFT0107_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tft0107_crt_datetime = models.DateTimeField(db_column='TFT0107_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tft0107_crt_user_id = models.CharField(db_column='TFT0107_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tft0107_crt_prog_nm = models.CharField(db_column='TFT0107_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tft0107_upd_datetime = models.DateTimeField(db_column='TFT0107_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tft0107_upd_user_id = models.CharField(db_column='TFT0107_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tft0107_upd_prog_nm = models.CharField(db_column='TFT0107_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tft0107_upd_cnt = models.DecimalField(db_column='TFT0107_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TFT0107_KAIS_PLAN'
        unique_together = (('tft0103_nend', 'tft0103_plan_no', 'tft0107_kais_cd'),)


class Tmm01KeieHosn(models.Model):
    tmm01_nend = models.SmallIntegerField(db_column='TMM01_NEND', primary_key=True)  # Field name made lowercase.
    tmm01_keie_hosn = models.CharField(db_column='TMM01_KEIE_HOSN', max_length=400, blank=True, null=True)  # Field name made lowercase.
    tmm01_visn = models.CharField(db_column='TMM01_VISN', max_length=400, blank=True, null=True)  # Field name made lowercase.
    tmm01_keie_senr = models.CharField(db_column='TMM01_KEIE_SENR', max_length=400, blank=True, null=True)  # Field name made lowercase.
    tmm01_nend_zent_hosn = models.CharField(db_column='TMM01_NEND_ZENT_HOSN', max_length=400, blank=True, null=True)  # Field name made lowercase.
    tmm01_del_flg = models.CharField(db_column='TMM01_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmm01_crt_datetime = models.DateTimeField(db_column='TMM01_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmm01_crt_user_id = models.CharField(db_column='TMM01_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmm01_crt_prog_nm = models.CharField(db_column='TMM01_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmm01_upd_datetime = models.DateTimeField(db_column='TMM01_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmm01_upd_user_id = models.CharField(db_column='TMM01_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmm01_upd_prog_nm = models.CharField(db_column='TMM01_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmm01_upd_cnt = models.DecimalField(db_column='TMM01_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMM01_KEIE_HOSN'


class Tmm02Bmn(models.Model):
    tmm01_nend = models.SmallIntegerField(db_column='TMM01_NEND', primary_key=True)  # Field name made lowercase.
    tmm02_bmn_cd = models.CharField(db_column='TMM02_BMN_CD', max_length=10)  # Field name made lowercase.
    tmm02_bmn_nm = models.CharField(db_column='TMM02_BMN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmm02_bmn_hosn = models.CharField(db_column='TMM02_BMN_HOSN', max_length=400, blank=True, null=True)  # Field name made lowercase.
    tmm02_bmn_top_user_id = models.CharField(db_column='TMM02_BMN_TOP_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmm02_bmn_hyoj_no = models.SmallIntegerField(db_column='TMM02_BMN_HYOJ_NO', blank=True, null=True)  # Field name made lowercase.
    tmm02_top_flg = models.CharField(db_column='TMM02_TOP_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmm02_del_flg = models.CharField(db_column='TMM02_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmm02_crt_datetime = models.DateTimeField(db_column='TMM02_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmm02_crt_user_id = models.CharField(db_column='TMM02_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmm02_crt_prog_nm = models.CharField(db_column='TMM02_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmm02_upd_datetime = models.DateTimeField(db_column='TMM02_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmm02_upd_user_id = models.CharField(db_column='TMM02_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmm02_upd_prog_nm = models.CharField(db_column='TMM02_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmm02_upd_cnt = models.DecimalField(db_column='TMM02_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tmm02_joi_bmn_cd = models.CharField(db_column='TMM02_JOI_BMN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tmm02_kijn_uri_riek_ritu = models.DecimalField(db_column='TMM02_KIJN_URI_RIEK_RITU', max_digits=8, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
    tmm02_hukurihi_rate = models.DecimalField(db_column='TMM02_HUKURIHI_RATE', max_digits=8, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
    tmm02_shokyu_rate = models.DecimalField(db_column='TMM02_SHOKYU_RATE', max_digits=8, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
    tmm02_shokyu_ym = models.CharField(db_column='TMM02_SHOKYU_YM', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tmm02_shoyo_hukurihi_rate = models.DecimalField(db_column='TMM02_SHOYO_HUKURIHI_RATE', max_digits=8, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
    tmm02_shoyo_hikiate_rate = models.DecimalField(db_column='TMM02_SHOYO_HIKIATE_RATE', max_digits=8, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
    tmm02_kenko_rate = models.DecimalField(db_column='TMM02_KENKO_RATE', max_digits=8, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
    tmm02_nenkin_rate = models.DecimalField(db_column='TMM02_NENKIN_RATE', max_digits=8, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
    tmm02_nenkin_kikin_rate = models.DecimalField(db_column='TMM02_NENKIN_KIKIN_RATE', max_digits=8, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
    tmm02_koyo_rate = models.DecimalField(db_column='TMM02_KOYO_RATE', max_digits=8, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
    tmm02_kaigo_rate = models.DecimalField(db_column='TMM02_KAIGO_RATE', max_digits=8, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
    tmm02_bmn_nm_r = models.CharField(db_column='TMM02_BMN_NM_R', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMM02_BMN'
        unique_together = (('tmm01_nend', 'tmm02_bmn_cd'),)


class Tmm03Sten(models.Model):
    tmm01_nend = models.SmallIntegerField(db_column='TMM01_NEND', primary_key=True)  # Field name made lowercase.
    tmm03_sten_cd = models.CharField(db_column='TMM03_STEN_CD', max_length=2)  # Field name made lowercase.
    tmm03_sten_nm = models.CharField(db_column='TMM03_STEN_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tmm03_zens_mkhy_max_rec = models.SmallIntegerField(db_column='TMM03_ZENS_MKHY_MAX_REC', blank=True, null=True)  # Field name made lowercase.
    tmm03_sten_hyoj_no = models.SmallIntegerField(db_column='TMM03_STEN_HYOJ_NO', blank=True, null=True)  # Field name made lowercase.
    tmm03_del_flg = models.CharField(db_column='TMM03_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmm03_crt_datetime = models.DateTimeField(db_column='TMM03_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmm03_crt_user_id = models.CharField(db_column='TMM03_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmm03_crt_prog_nm = models.CharField(db_column='TMM03_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmm03_upd_datetime = models.DateTimeField(db_column='TMM03_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmm03_upd_user_id = models.CharField(db_column='TMM03_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmm03_upd_prog_nm = models.CharField(db_column='TMM03_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmm03_upd_cnt = models.DecimalField(db_column='TMM03_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMM03_STEN'
        unique_together = (('tmm01_nend', 'tmm03_sten_cd'),)


class Tmm04KanrTkse(models.Model):
    tmm04_kanr_toks_cd = models.CharField(db_column='TMM04_KANR_TOKS_CD', primary_key=True, max_length=5)  # Field name made lowercase.
    tmm04_kanr_toks_nm = models.CharField(db_column='TMM04_KANR_TOKS_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tmm04_kanr_toks_hyoj_no = models.SmallIntegerField(db_column='TMM04_KANR_TOKS_HYOJ_NO', blank=True, null=True)  # Field name made lowercase.
    tmm04_del_flg = models.CharField(db_column='TMM04_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmm04_crt_datetime = models.DateTimeField(db_column='TMM04_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmm04_crt_user_id = models.CharField(db_column='TMM04_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmm04_crt_prog_nm = models.CharField(db_column='TMM04_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmm04_upd_datetime = models.DateTimeField(db_column='TMM04_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmm04_upd_user_id = models.CharField(db_column='TMM04_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmm04_upd_prog_nm = models.CharField(db_column='TMM04_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmm04_upd_cnt = models.DecimalField(db_column='TMM04_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tmm04_mins_mkhy_flg = models.CharField(db_column='TMM04_MINS_MKHY_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmm04_not_tumi_flg = models.CharField(db_column='TMM04_NOT_TUMI_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmm04_sum_grp_no = models.SmallIntegerField(db_column='TMM04_SUM_GRP_NO', blank=True, null=True)  # Field name made lowercase.
    tmm04_mins_fugo_flg = models.CharField(db_column='TMM04_MINS_FUGO_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMM04_KANR_TKSE'


class Tmm05NaniDo(models.Model):
    tmm05_nani_do = models.CharField(db_column='TMM05_NANI_DO', primary_key=True, max_length=2)  # Field name made lowercase.
    tmm05_hyoj_no = models.SmallIntegerField(db_column='TMM05_HYOJ_NO', blank=True, null=True)  # Field name made lowercase.
    tmm05_del_flg = models.CharField(db_column='TMM05_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmm05_crt_datetime = models.DateTimeField(db_column='TMM05_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmm05_crt_user_id = models.CharField(db_column='TMM05_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmm05_crt_prog_nm = models.CharField(db_column='TMM05_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmm05_upd_datetime = models.DateTimeField(db_column='TMM05_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmm05_upd_user_id = models.CharField(db_column='TMM05_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmm05_upd_prog_nm = models.CharField(db_column='TMM05_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmm05_upd_cnt = models.DecimalField(db_column='TMM05_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMM05_NANI_DO'


class Tmt01MkhySsak(models.Model):
    tmt01_nend = models.SmallIntegerField(db_column='TMT01_NEND', primary_key=True)  # Field name made lowercase.
    tmt01_mkhy_ssak_no = models.DecimalField(db_column='TMT01_MKHY_SSAK_NO', max_digits=18, decimal_places=0)  # Field name made lowercase.
    tmt01_sten_cd = models.CharField(db_column='TMT01_STEN_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tmt01_kais_kbn = models.CharField(db_column='TMT01_KAIS_KBN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tmt01_bmn_cd = models.CharField(db_column='TMT01_BMN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tmt01_mkhy_ssak_id = models.CharField(db_column='TMT01_MKHY_SSAK_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tmt01_mkhy_ssak_nm = models.CharField(db_column='TMT01_MKHY_SSAK_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tmt01_tant_user_id = models.CharField(db_column='TMT01_TANT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmt01_weit = models.DecimalField(db_column='TMT01_WEIT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tmt01_kanr_toks_cd = models.CharField(db_column='TMT01_KANR_TOKS_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tmt01_tnen_mkhy_val = models.DecimalField(db_column='TMT01_TNEN_MKHY_VAL', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt01_mkhy_ssak_biko = models.CharField(db_column='TMT01_MKHY_SSAK_BIKO', max_length=150, blank=True, null=True)  # Field name made lowercase.
    tmt01_joi_mkhy_ssak_no = models.DecimalField(db_column='TMT01_JOI_MKHY_SSAK_NO', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tmt01_hyoj_no = models.SmallIntegerField(db_column='TMT01_HYOJ_NO', blank=True, null=True)  # Field name made lowercase.
    tmt01_last_kais_flg = models.CharField(db_column='TMT01_LAST_KAIS_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmt01_del_flg = models.CharField(db_column='TMT01_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmt01_crt_datetime = models.DateTimeField(db_column='TMT01_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmt01_crt_user_id = models.CharField(db_column='TMT01_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmt01_crt_prog_nm = models.CharField(db_column='TMT01_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmt01_upd_datetime = models.DateTimeField(db_column='TMT01_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmt01_upd_user_id = models.CharField(db_column='TMT01_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmt01_upd_prog_nm = models.CharField(db_column='TMT01_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmt01_upd_cnt = models.DecimalField(db_column='TMT01_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tmt01_plan_no = models.SmallIntegerField(db_column='TMT01_PLAN_NO', blank=True, null=True)  # Field name made lowercase.
    tmt01_copy_moto_no = models.DecimalField(db_column='TMT01_COPY_MOTO_NO', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tmt01_mkhy_flg = models.CharField(db_column='TMT01_MKHY_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmt01_ysn_bumon_cd = models.CharField(db_column='TMT01_YSN_BUMON_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tmt01_ysn_yosan_utwk_cd = models.CharField(db_column='TMT01_YSN_YOSAN_UTWK_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMT01_MKHY_SSAK'
        unique_together = (('tmt01_nend', 'tmt01_mkhy_ssak_no'),)


class Tmt02TukiMkhyJisk(models.Model):
    tmt02_nend = models.SmallIntegerField(db_column='TMT02_NEND', primary_key=True)  # Field name made lowercase.
    tmt02_mkhy_ssak_no = models.DecimalField(db_column='TMT02_MKHY_SSAK_NO', max_digits=18, decimal_places=0)  # Field name made lowercase.
    tmt02_mkhy_val_01 = models.DecimalField(db_column='TMT02_MKHY_VAL_01', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_mkhy_val_02 = models.DecimalField(db_column='TMT02_MKHY_VAL_02', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_mkhy_val_03 = models.DecimalField(db_column='TMT02_MKHY_VAL_03', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_mkhy_val_04 = models.DecimalField(db_column='TMT02_MKHY_VAL_04', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_mkhy_val_05 = models.DecimalField(db_column='TMT02_MKHY_VAL_05', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_mkhy_val_06 = models.DecimalField(db_column='TMT02_MKHY_VAL_06', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_mkhy_val_07 = models.DecimalField(db_column='TMT02_MKHY_VAL_07', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_mkhy_val_08 = models.DecimalField(db_column='TMT02_MKHY_VAL_08', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_mkhy_val_09 = models.DecimalField(db_column='TMT02_MKHY_VAL_09', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_mkhy_val_10 = models.DecimalField(db_column='TMT02_MKHY_VAL_10', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_mkhy_val_11 = models.DecimalField(db_column='TMT02_MKHY_VAL_11', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_mkhy_val_12 = models.DecimalField(db_column='TMT02_MKHY_VAL_12', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_weit_01 = models.DecimalField(db_column='TMT02_WEIT_01', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tmt02_weit_02 = models.DecimalField(db_column='TMT02_WEIT_02', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tmt02_weit_03 = models.DecimalField(db_column='TMT02_WEIT_03', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tmt02_weit_04 = models.DecimalField(db_column='TMT02_WEIT_04', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tmt02_weit_05 = models.DecimalField(db_column='TMT02_WEIT_05', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tmt02_weit_06 = models.DecimalField(db_column='TMT02_WEIT_06', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tmt02_weit_07 = models.DecimalField(db_column='TMT02_WEIT_07', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tmt02_weit_08 = models.DecimalField(db_column='TMT02_WEIT_08', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tmt02_weit_09 = models.DecimalField(db_column='TMT02_WEIT_09', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tmt02_weit_10 = models.DecimalField(db_column='TMT02_WEIT_10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tmt02_weit_11 = models.DecimalField(db_column='TMT02_WEIT_11', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tmt02_weit_12 = models.DecimalField(db_column='TMT02_WEIT_12', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tmt02_jisk_01 = models.DecimalField(db_column='TMT02_JISK_01', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_jisk_02 = models.DecimalField(db_column='TMT02_JISK_02', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_jisk_03 = models.DecimalField(db_column='TMT02_JISK_03', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_jisk_04 = models.DecimalField(db_column='TMT02_JISK_04', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_jisk_05 = models.DecimalField(db_column='TMT02_JISK_05', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_jisk_06 = models.DecimalField(db_column='TMT02_JISK_06', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_jisk_07 = models.DecimalField(db_column='TMT02_JISK_07', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_jisk_08 = models.DecimalField(db_column='TMT02_JISK_08', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_jisk_09 = models.DecimalField(db_column='TMT02_JISK_09', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_jisk_10 = models.DecimalField(db_column='TMT02_JISK_10', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_jisk_11 = models.DecimalField(db_column='TMT02_JISK_11', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_jisk_12 = models.DecimalField(db_column='TMT02_JISK_12', max_digits=17, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmt02_weit_jisk_01 = models.DecimalField(db_column='TMT02_WEIT_JISK_01', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tmt02_weit_jisk_02 = models.DecimalField(db_column='TMT02_WEIT_JISK_02', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tmt02_weit_jisk_03 = models.DecimalField(db_column='TMT02_WEIT_JISK_03', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tmt02_weit_jisk_04 = models.DecimalField(db_column='TMT02_WEIT_JISK_04', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tmt02_weit_jisk_05 = models.DecimalField(db_column='TMT02_WEIT_JISK_05', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tmt02_weit_jisk_06 = models.DecimalField(db_column='TMT02_WEIT_JISK_06', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tmt02_weit_jisk_07 = models.DecimalField(db_column='TMT02_WEIT_JISK_07', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tmt02_weit_jisk_08 = models.DecimalField(db_column='TMT02_WEIT_JISK_08', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tmt02_weit_jisk_09 = models.DecimalField(db_column='TMT02_WEIT_JISK_09', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tmt02_weit_jisk_10 = models.DecimalField(db_column='TMT02_WEIT_JISK_10', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tmt02_weit_jisk_11 = models.DecimalField(db_column='TMT02_WEIT_JISK_11', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tmt02_weit_jisk_12 = models.DecimalField(db_column='TMT02_WEIT_JISK_12', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tmt02_del_flg = models.CharField(db_column='TMT02_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmt02_crt_datetime = models.DateTimeField(db_column='TMT02_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmt02_crt_user_id = models.CharField(db_column='TMT02_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmt02_crt_prog_nm = models.CharField(db_column='TMT02_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmt02_upd_datetime = models.DateTimeField(db_column='TMT02_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmt02_upd_user_id = models.CharField(db_column='TMT02_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmt02_upd_prog_nm = models.CharField(db_column='TMT02_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmt02_upd_cnt = models.DecimalField(db_column='TMT02_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMT02_TUKI_MKHY_JISK'
        unique_together = (('tmt02_nend', 'tmt02_mkhy_ssak_no'),)


class Tmt03Plan(models.Model):
    tmt03_nend = models.SmallIntegerField(db_column='TMT03_NEND', primary_key=True)  # Field name made lowercase.
    tmt03_plan_no = models.SmallIntegerField(db_column='TMT03_PLAN_NO')  # Field name made lowercase.
    tmt03_plan_nm = models.CharField(db_column='TMT03_PLAN_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tmt03_jisk_inp_sta_tuki = models.CharField(db_column='TMT03_JISK_INP_STA_TUKI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tmt03_teky_sta_date = models.DateTimeField(db_column='TMT03_TEKY_STA_DATE', blank=True, null=True)  # Field name made lowercase.
    tmt03_teky_end_date = models.DateTimeField(db_column='TMT03_TEKY_END_DATE', blank=True, null=True)  # Field name made lowercase.
    tmt03_new_data_flg = models.CharField(db_column='TMT03_NEW_DATA_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmt03_copy_moto_plan_no = models.SmallIntegerField(db_column='TMT03_COPY_MOTO_PLAN_NO', blank=True, null=True)  # Field name made lowercase.
    tmt03_del_flg = models.CharField(db_column='TMT03_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmt03_crt_datetime = models.DateTimeField(db_column='TMT03_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmt03_crt_user_id = models.CharField(db_column='TMT03_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmt03_crt_prog_nm = models.CharField(db_column='TMT03_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmt03_upd_datetime = models.DateTimeField(db_column='TMT03_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmt03_upd_user_id = models.CharField(db_column='TMT03_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmt03_upd_prog_nm = models.CharField(db_column='TMT03_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmt03_upd_cnt = models.DecimalField(db_column='TMT03_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tmt03_biko = models.CharField(db_column='TMT03_BIKO', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMT03_PLAN'
        unique_together = (('tmt03_nend', 'tmt03_plan_no'),)


class Tmt04PlanLock(models.Model):
    tmt03_nend = models.SmallIntegerField(db_column='TMT03_NEND', primary_key=True)  # Field name made lowercase.
    tmt03_plan_no = models.SmallIntegerField(db_column='TMT03_PLAN_NO')  # Field name made lowercase.
    tmt04_bmn_cd = models.CharField(db_column='TMT04_BMN_CD', max_length=10)  # Field name made lowercase.
    tmt04_lock_flg = models.CharField(db_column='TMT04_LOCK_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmt04_del_flg = models.CharField(db_column='TMT04_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmt04_crt_datetime = models.DateTimeField(db_column='TMT04_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmt04_crt_user_id = models.CharField(db_column='TMT04_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmt04_crt_prog_nm = models.CharField(db_column='TMT04_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmt04_upd_datetime = models.DateTimeField(db_column='TMT04_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmt04_upd_user_id = models.CharField(db_column='TMT04_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmt04_upd_prog_nm = models.CharField(db_column='TMT04_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmt04_upd_cnt = models.DecimalField(db_column='TMT04_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMT04_PLAN_LOCK'
        unique_together = (('tmt03_nend', 'tmt03_plan_no', 'tmt04_bmn_cd'),)


class Tmt05TantPlan(models.Model):
    tmt03_nend = models.SmallIntegerField(db_column='TMT03_NEND', primary_key=True)  # Field name made lowercase.
    tmt03_plan_no = models.SmallIntegerField(db_column='TMT03_PLAN_NO')  # Field name made lowercase.
    tmt05_tant_user_id = models.CharField(db_column='TMT05_TANT_USER_ID', max_length=12)  # Field name made lowercase.
    tmt05_nanido_total = models.CharField(db_column='TMT05_NANIDO_TOTAL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmt05_nanido_sten_01 = models.CharField(db_column='TMT05_NANIDO_STEN_01', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmt05_nanido_sten_02 = models.CharField(db_column='TMT05_NANIDO_STEN_02', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmt05_nanido_sten_03 = models.CharField(db_column='TMT05_NANIDO_STEN_03', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmt05_nanido_sten_04 = models.CharField(db_column='TMT05_NANIDO_STEN_04', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmt05_nen_total_mkhy_weit = models.DecimalField(db_column='TMT05_NEN_TOTAL_MKHY_WEIT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tmt05_nen_total_ssak_weit = models.DecimalField(db_column='TMT05_NEN_TOTAL_SSAK_WEIT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tmt05_del_flg = models.CharField(db_column='TMT05_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmt05_crt_datetime = models.DateTimeField(db_column='TMT05_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmt05_crt_user_id = models.CharField(db_column='TMT05_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmt05_crt_prog_nm = models.CharField(db_column='TMT05_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmt05_upd_datetime = models.DateTimeField(db_column='TMT05_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmt05_upd_user_id = models.CharField(db_column='TMT05_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmt05_upd_prog_nm = models.CharField(db_column='TMT05_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmt05_upd_cnt = models.DecimalField(db_column='TMT05_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tmt05_evid_path = models.CharField(db_column='TMT05_EVID_PATH', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tmt05_evid_file_nm_01 = models.CharField(db_column='TMT05_EVID_FILE_NM_01', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tmt05_evid_file_nm_02 = models.CharField(db_column='TMT05_EVID_FILE_NM_02', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tmt05_evid_file_nm_03 = models.CharField(db_column='TMT05_EVID_FILE_NM_03', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tmt05_evid_file_nm_04 = models.CharField(db_column='TMT05_EVID_FILE_NM_04', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tmt05_evid_file_nm_05 = models.CharField(db_column='TMT05_EVID_FILE_NM_05', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tmt05_evid_file_nm_06 = models.CharField(db_column='TMT05_EVID_FILE_NM_06', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tmt05_evid_file_nm_07 = models.CharField(db_column='TMT05_EVID_FILE_NM_07', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tmt05_evid_file_nm_08 = models.CharField(db_column='TMT05_EVID_FILE_NM_08', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tmt05_evid_file_nm_09 = models.CharField(db_column='TMT05_EVID_FILE_NM_09', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tmt05_evid_file_nm_10 = models.CharField(db_column='TMT05_EVID_FILE_NM_10', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tmt05_evid_file_nm_11 = models.CharField(db_column='TMT05_EVID_FILE_NM_11', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tmt05_evid_file_nm_12 = models.CharField(db_column='TMT05_EVID_FILE_NM_12', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tmt05_nanido_sten_05 = models.CharField(db_column='TMT05_NANIDO_STEN_05', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMT05_TANT_PLAN'
        unique_together = (('tmt03_nend', 'tmt03_plan_no', 'tmt05_tant_user_id'),)


class Tmt06TantPlanDtl(models.Model):
    tmt03_nend = models.SmallIntegerField(db_column='TMT03_NEND', primary_key=True)  # Field name made lowercase.
    tmt03_plan_no = models.SmallIntegerField(db_column='TMT03_PLAN_NO')  # Field name made lowercase.
    tmt05_tant_user_id = models.CharField(db_column='TMT05_TANT_USER_ID', max_length=12)  # Field name made lowercase.
    tmt06_mkhy_ssak_no = models.DecimalField(db_column='TMT06_MKHY_SSAK_NO', max_digits=18, decimal_places=0)  # Field name made lowercase.
    tmt06_mkhy_ssak_kbn = models.CharField(db_column='TMT06_MKHY_SSAK_KBN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmt06_del_flg = models.CharField(db_column='TMT06_DEL_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmt06_crt_datetime = models.DateTimeField(db_column='TMT06_CRT_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmt06_crt_user_id = models.CharField(db_column='TMT06_CRT_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmt06_crt_prog_nm = models.CharField(db_column='TMT06_CRT_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmt06_upd_datetime = models.DateTimeField(db_column='TMT06_UPD_DATETIME', blank=True, null=True)  # Field name made lowercase.
    tmt06_upd_user_id = models.CharField(db_column='TMT06_UPD_USER_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tmt06_upd_prog_nm = models.CharField(db_column='TMT06_UPD_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmt06_upd_cnt = models.DecimalField(db_column='TMT06_UPD_CNT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMT06_TANT_PLAN_DTL'
        unique_together = (('tmt03_nend', 'tmt03_plan_no', 'tmt05_tant_user_id', 'tmt06_mkhy_ssak_no'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
