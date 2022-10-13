# 收件人地址，按位置分组，各组与邮箱均按英文下逗号分隔
receivers={
'城市':'cbh1987@126.com'
# '珠海':'yangh0006@ldygo.com,pengyy0001@ldygo.com,ldy_tanyx001@ldygo.com',
# '重庆':'hujq0001@ldygo.com,yangf0002@ldygo.com,wangjj0002@ldygo.com',
# '中山':'huangjf0001@ldygo.com',
# '郑州':'jinwj0001@ldygo.com,zhangyw0001@ldygo.com,',
# '长沙':'lihx004@ldygo.com,tangz0004@ldygo.com,zhoufl0001@ldygo.com',
# '长春':'lijn003@ldygo.com',
# '西宁':'ldy_lic009@ldygo.com',
# '西安':'liuy0020@ldygo.com,zhangzn0001@ldygo.com,guanbx001@ldygo.com',
# '武汉':'ldy_xingc001@ldygo.com,fengj0001@ldygo.com',
# '太原':'sumf0001@ldygo.com,ldy_yuyf001@ldygo.com',
# '苏州':'liuzy0004@ldygo.com,yehy002@ldygo.com',
# '石家庄':'ldy_peisl001@ldygo.com',
# '沈阳':'shaoab001@ldygo.com,ldy_zuohc001@ldygo.com ,ldy_yuxl001@ldygo.com',
# '深圳':'ldy_jiyf001@ldygo.com,xiongb0001@ldygo.com,wangx0013@ldygo.com',
# '三亚':'ldy_wuxd003@ldygo.com,ldy_lisy003@ldygo.com',
# '青岛':'ldy_liwh002@ldygo.com,ldy_zhumj001@ldygo.com,hezh0002@ldygo.com',
# '宁波':'wangs0006@ldygo.com,ldy_jiangh005@ldygo.com',
# '南宁':'ldy_chensh004@ldygo.com',
# '南京':'yaoyp0002@ldygo.com,ldy_maow001@ldygo.com',
# '南昌':'luyk0001@ldygo.com,liuy0021@ldygo.com,wany002@ldygo.com',
# '绵阳':'ldy_wangj008@ldygo.com,luobx0001@ldygo.com,ldy_liuy007@ldygo.com',
# #'兰州':'zhangy0013@ldygo.com,xieyh0002@ldygo.com',
# '昆明':'sunxm001@ldygo.com,mok0001@ldygo.com,ldy_wangah001@ldygo.com',
# '济南':'gaoyg001@ldygo.com,zhangq003@ldygo.com,songdp0001@ldygo.com',
# '衡阳':'ldy_pengy004@ldygo.com,tanzx0001@ldygo.com,zhangh0008@ldygo.com',
# '合肥':'ldy_chengyx001@ldygo.com,wangw0004@ldygo.com',
# '海口':'fumf001@ldygo.com,xueyb001@ldygo.com',
# '哈尔滨':'ldy_hanxj001@ldygo.com',
# '福州':'zhangc0004@ldygo.com,laily0001@ldygo.com,xuy0003@ldygo.com',
# '东莞':'liangjr0001@ldygo.com,dengb0002@ldygo.com',
# #'大连':'shaoab001@ldygo.com,ldy_yuxl001@ldygo.com,ldy_yufq002@ldygo.com',
# '成都':'ldy_wangj008@ldygo.com,luobx0001@ldygo.com,ldy_liuy007@ldygo.com',
# '厦门':'ldy_daist001@ldygo.com,qiuwc0001@ldygo.com,ldy_liaosw001@ldygo.com,ldy_zhuy001@ldygo.com',
# '银川':'ldy_lvs001@ldygo.com,zhouxy0002@ldygo.com,ldy_zhaojf001@ldygo.com',
# '贵州':'xiangx0001@ldygo.com,lizb0003@ldygo.com,luoy0001@ldygo.com,ldy_lijg003@ldygo.com,zhangx0001@ldygo.com',
# '桂林':'libr0001@ldygo.com,qinhp0001@ldygo.com',
# '佛山':'luzm0001@ldygo.com,ldy_zhangsb001@ldygo.com,qiuzw0001@ldygo.com',
# '广州':'tanhy001@ldygo.com,linmx0001@ldygo.com',






}

# -----------------------------------------------------------------

# 账户信息
account='chenbh002@ldygo.com'
password='caB7HBDPatR6Xi'

# -----------------------------------------------------------------

# 抄送人地址，按英文下逗号分隔
copy_to='chenbh002@ldygo.com'

# -----------------------------------------------------------------

# 邮件主题
subject = 'TEST——9月渠道加油数据'

# -----------------------------------------------------------------

# 邮件正文，换行用\n\，%s代表收件地址中的位置
body='\
%s分公司，\n\
    \n\
    大家好，本次下发数据为9月渠道加油相关数据，如有疑问请联系领动罗楚娜。\
\n\
    以上，请知悉，谢谢！'


# -----------------------------------------------------------------

# 构造附件名，,若无附件则为''，%s代表收件地址中的位置，一定要添加文件类型后缀
enclosures='%s-附件1.xlsx,%s-附件2.xlsx'
# 邮件发送执行

import sendemails
sendemails.sendemails(
            account = account,
            password = password,
            copy_to = copy_to,
            body = body,
            enclosures = enclosures,
            receivers = receivers,
            subject = subject
            )