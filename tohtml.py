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
</head>

<body>
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
indexcontent = ""
for fname,title in fname2title.items():
    indexcontent += "<li><a href='html/%s.html'>%s</a></li>" % (fname,title)

indexhtml = u'''
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>markdown blog</title>
    <meta charset="utf-8">
</head>

<body>
    <h1>首页</h1>
        <p>
            <input type="button" value="更新" onclick="onupdate()">
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

