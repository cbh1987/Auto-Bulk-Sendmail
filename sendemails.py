import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def sendemails(account,password,copy_to,body,enclosures,receivers,subject):
    '''
    发送邮件  
    '''
    smt_set = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
    try:
        smt_set.login(account, password)
    except:
        print('***********ERR:账号密码不正确,邮件未发送！**********')
        return
    is_ok = 0
    i = 1
    for city,addr in receivers.items():
        print ('***********正在撰写第%s封邮件！**********'%i)
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = account
        msg['Cc'] = copy_to
        msg['To'] = addr
        msg.attach(MIMEText(body%city,'plain','utf-8'))
        i += 1
        if enclosures == '':
            pass
        else:
            try:
                for enclo in enclosures.split(','):
                    enclosure_name = enclo%city  
                    enclosure = MIMEApplication(open(enclosure_name,'rb').read())
                    enclosure.add_header('content-disposition','attachment',filename=('gbk','',enclosure_name))
                    msg.attach(enclosure)
            except:
                is_ok = 1        
        if is_ok == 0:
            print('sending....发至%s，收件人%s,抄送%s'%(city,addr,copy_to))
            smt_set.sendmail(account, addr.split(',')+copy_to.split(','), msg.as_string()) 
            print('***********成功！**********\n\n')
        else:
            print('***********ERR:附件设置不正确,邮件未发送！**********')
            return
    smt_set.quit()