#!/usr/bin/python
# coding: utf-8

import os
import sys
import glob
import commands
import re
import codecs

wwwpath = sys.argv[1]
pypath = os.path.realpath(sys.path[0]) 

fname2html = {}
fname2title = {}
mdfnames = "%s/md/*.md" % (wwwpath)
for mdfname in glob.glob(mdfnames):
    fname=os.path.split(mdfname)[1]
    m = re.match(r'^(\#{1,6})[ \t]*(.+?)[ \t]*\#*\n+', codecs.open(mdfname,"r","utf-8").read())
    title = fname
    if m:
        gr = m.groups()
        if gr and len(gr)==2:
            title = gr[1]
    print(mdfname)
    fname2title[fname] = title
    htmlfname = "%s/html/%s.html" % (wwwpath,fname)
    cmd = "%s/tools/Markdown.pl %s" % (pypath,mdfname)
    status, output = commands.getstatusoutput(cmd)
    if status==0:
        fname2html[fname] = output.decode('utf-8')

mdhtml = u'''
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>markdown blog</title>
    <meta charset="utf-8">
    <style type="text/css">
    .navbar-fixed-top{position: fixed;top: 0;right: 0;left: 0;z-index: 1030;}
    </style>
</head>

<body>
<div class="navbar navbar-fixed-top">
<a href='/'>index</a>
</div>
%s
</body>
</html>
'''
for fname,mdcontent in fname2html.items():
    htmlfname = "%s/html/%s.html" % (wwwpath,fname)
    html = mdhtml % (mdcontent)
    f = codecs.open(htmlfname, "w", "utf-8")
    f.write(html)
    f.close()
 
#index.html
indexcontent = u"<dl>"
for fname,title in fname2title.items():
    indexcontent += u"<dt><a href='html/%s.html'>%s</a></dt><dd><a href='editor?name=%s'>edit</dd>" % (fname,title,fname)
indexcontent += u"</dl>"

indexhtml = u'''
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>markdown blog</title>
    <meta charset="utf-8">
    <style type="text/css">
    h4{font-size:14px; color:#333;}
    a{color:#069;}
    dl{ border:dashed 1px #666; font-size:14px; padding:4px; background:#FDFBDB;}
    dt{clear:left; float:left; padding:4px 0;}
    dd{ text-align:right;  padding:4px 0;font-size:12px; color:#666;}
    </style>
</head>

<body>
    <h1>Article List</h1>
        <p>
            <input type="button" value="update" onclick="onupdate()">
            <input type="button" value="add" onclick="onadd()">
        </p>
    <content>
    %s
    </content>
<script type="text/javascript">
    function onupdate() {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState==4 && xmlhttp.status==200) {
                location.reload();
                alert(xmlhttp.responseText);
            }
        };
        xmlhttp.open("POST","update",true);
        xmlhttp.send();
    }
    function onadd() {
        window.location.href = '/editor';
    }
    window.onload = function() {
    };
</script>

</body>
</html>
''' % (indexcontent)
indexfname = "%s/html/index.html" % (wwwpath)
f = codecs.open(indexfname, "w", "utf-8")
f.write(indexhtml)
f.close()

