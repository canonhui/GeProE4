First day: 2017/6/21
- 对于像我一样的菜鸟的忠告：在项目一开始的时候就建立一个空白文档来保留自己在开发过程中的总结。很多时候，我们没有这么做不是因为懒，而是缺少这种习惯。建立一个空白文档这样的小小的举动会给我们这方面很强的暗示。

- 将一个未登录的访问需要登录权限的内容的用户重定向到登录页面，登录之后再转到之前请求页面，需要将 login_manager.login_view 设置为登录视图函数，并在登录函数中将 request.args.get('next') 的值传递给 url_for

- Python 编程一定要养成按空格缩进而不是 tab 的习惯。到时候如果因为这一行缩进为空格下一行为 tab 而焦头烂额了几个小时时别怪我没提醒你。。。相关错误提示：
	IndentationError: unindent does not match any outer indentation level

- Flask 不同 APP 之间不能相互 redirect

- 使用多个 APP 的原因：

- SQLAlchemy and SQLite: database is locked:
	https://stackoverflow.com/questions/13895176/sqlalchemy-and-sqlite-database-is-locked

- 当出现 redirect 不能重定向到某一个函数时，检查你的函数名是否和 redirect 的参数相匹配！！看起来问题很脑残对不对？我ＴＭ找了两个小时！

- jinja 模板中很多时候会在 JS 中出现 python 变量。机智的做法是将这些变量传递给 html 页面中某个元素的 class 或其他属性，然后再用 JS(jQuery) 获取属性内容 (stack overflow) 上看到的，不知道是不是真机智

- 从 $(document).ready(function() {
	$('th').on('click', function() {
到 $(document).on('click', 'th', function() {
需要多长时间？整整一个下午加半个晚上！！！
第一种方法中使用 ajax 点击表头给表格排序时，点一下之后接下来的动作就没反应了。当时我心情之酸爽简直秒老坛。
这件事给我的另一个教训是什么呢？一定要学会如何使用英文搜素你遇到的问题，编程真的是一个细节活，几个字母的差距就是几个小时甚至上天的代价。像再遇到这种一时找不到逻辑的问题时，首先要做的是麒麟手离开鼠标，面壁沉思，好好组织语言描述所遇到的问题。当然这是对孤军奋战而言，如果你有大腿指点迷津当我没说
	https://stackoverflow.com/questions/23123086/jquery-functionality-not-working-after-ajax-call

- 不得不说 stack overflow 真的是猿的天堂，基本上只有你想不到，没有你查不到的问题。当你觉得你遇到的问题很小众，甚至还为此有点洋洋得意的时候，绝大多数时候只是你没找对这个问题的问法而已。



############################# jQuery #########################
2017/07/03
- jQuery get position relative to document:
	.offset(), which returns an object with the attributes top, bottom, left, right etc


############################# sqlalchemy #########################
2017/06/28
- 传说中的 ORM 技术：Object-Relational Mapping: 把关系数据库的表结构映射到对象上。表的各字段组成一个 tuple, 并用一个 class 实例来表示。各行记录用组成一个 list.

- Sqlite databases are the most convenient choice for small applications, as each database is stored in a single file and there is no need to start a database server!


2017/07/01
- Delete records from many-to-many table:
	https://stackoverflow.com/questions/26948397/flask-and-sqlalchemy-how-to-delete-records-from-manytomany-table

- An InstrumentedList object is used to implement a list-like object which is aware of insertions and deletions of related objects to an object


2017/07/02
- sqlalchemy query notin_ clause in <filter>


2017/07/03
- Dependency rule tried to blank-out primary key column in many-to-many model relationship when trying to delete record, solution:
	Add cascade='all, delete-orphan' in the relationship of the "one endpoint".
	https://stackoverflow.com/questions/23699651/dependency-rule-tried-to-blank-out-primary-key-in-sqlalchemy-when-foreign-key-c

- 


































