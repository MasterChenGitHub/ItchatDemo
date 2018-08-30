#coding=utf8
import itchat
# tuling plugin can be get here:
# https://github.com/littlecodersh/EasierLife/tree/master/Plugins/Tuling
from tuling import get_response
import itchat

@itchat.msg_register('Text')
def text_reply(msg):

    if u'获取图片' in msg['Text']:
        itchat.send('@img@applaud.gif', msg['FromUserName']) # there should be a picture
    else:
        return get_response(msg['Text']) or u'收到：' + msg['Text']

@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def atta_reply(msg):
    return ({ 'Picture': u'图片', 'Recording': u'录音',
        'Attachment': u'附件', 'Video': u'视频', }.get(msg['Type']) +
        u'已下载到本地') # download function is: msg['Text'](msg['FileName'])

@itchat.msg_register(['Map', 'Card', 'Note', 'Sharing'])
def mm_reply(msg):
    if msg['Type'] == 'Map':
        return u'收到位置分享'
    elif msg['Type'] == 'Sharing':
        return u'收到分享' + msg['Text']
    elif msg['Type'] == 'Note':
        return u'收到：' + msg['Text']
    elif msg['Type'] == 'Card':
        return u'收到好友信息：' + msg['Text']['Alias']

@itchat.msg_register('Text', isGroupChat = True)
def group_reply(msg):
    print msg['Text']
    if msg['isAt']:
        return u'@%s\u2005%s' % (msg['ActualNickName'],
            get_response(msg['Text']) or u'收到：' + msg['Text'])

@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg(u'项目主页：github.com/littlecodersh/ItChat\n'
        + u'源代码  ：回复源代码\n' + u'图片获取：回复获取图片\n'
        + u'欢迎Star我的项目关注更新！', msg['RecommendInfo']['UserName'])

@itchat.msg_register( 'Note', isGroupChat=True)
def group_join_note(msg):
   if u'邀请' in msg['Content'] or u'invited' in msg['Content']:
       str = msg['Content'];
       pos_start = str.find('"')
       pos_end = str.find('"',pos_start+1)
       inviter = str[pos_start+1:pos_end]
       rpos_start = str.rfind('"')
       rpos_end = str.rfind('"',0, rpos_start)
       invitee = str[(rpos_end+1) : rpos_start]
       itchat.send_msg(u"@%s 欢迎来到本群[微笑]，感谢%s邀请。" % (invitee,inviter), msg['FromUserName'])
itchat.auto_login()
itchat.run()