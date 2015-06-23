# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B("Loudvoicer"),_class="brand",_href="http://www.loudervoicer.com/")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.keywords = '{{=db(db.webadmin).select().first().keyword}}'
response.meta.generator = '{{=db(db.webadmin).select().first().author}}'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('首页'), False, URL('default', 'index'), []),
    (T('后台管理首页'), False, URL('admin', 'index'), [])

]


if "auth" in locals(): auth.wikimenu()
