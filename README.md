markdown
========

simple markdown editor

### build
```
  $ cd markdown
  $ ./httpd.py `pwd`/app
```
  
### use

* 浏览器进入主页 <http://localhost:8080>
* 主页有更新按钮，可以更新`index.html`和转换所有已经编辑完且已经保存的m文件为html文件
* 浏览器进入编辑 <http://localhost:8080/editor>
* 需要修改某个已经编辑的文件 <http://localhost:8080/editor?name=xxy>

### todo

* 美化界面：包括主页，文章以及编辑器
* 优化编辑器体验：编辑框和预览框滚动条同步
* 添加实时保存
* 添加发布按钮（更新单个文件），最后去掉主页那个按钮


### other copyright

[Markdown](http://daringfireball.net/projects/markdown/) 是由 John Gruber 和 Aaron Swartz 共同创建的一种轻量级标记语言

[showdown.js](http://yanghao.org/tools/markdown.html) 是一个 javascript 写的 markdown 渲染库

[codemirror](http://codemirror.net)  是一款“Online Source Editor”，基于Javascript，短小精悍，实时在线代码高亮显示，他不是某个富文本编辑器的附属产品，他是许多大名鼎鼎的在线代码编辑器的基础库。

