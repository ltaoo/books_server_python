
`books`项目的后端部分，`Python`版，使用`docker`运行`php`容器和`mysql`容器提供接口。

## 使用

首先是构建镜像：
```bash
docker build -t bookshop .
```

运行数据库容器与 php 容器：
```bash
./start.sh
```

开启名为`books`的`php`容器和名为`books_db`的`mysql`容器，再初始化数据表
```bash
docker exec -i books_db mysql -uroot -p123 bookshop < setup.sql
```

## Api

### 用户相关

#### 用户登录

<table>
    <tr>
        <td>POST</td>
        <td>/api/user/login</td>
    </tr>
    <tr>
        <td>Body Parameter</td>
        <td>
            <table>
                <tr>
                    <td>Content-Type</td>
                    <td>application/json</td>
                </tr>
                <tr>
                    <td>Body</body>
                    <td><pre><code>
{
    "username": "ltaoo",
    "password": "hello520"
}
                    </code></pre></td>
                </tr>
            </table>
        </td>
    </tr>
    <tr>
        <td>Response Body</td>
        <td><pre><code>
{
    "c" : 0,
    "m" : "",
    "d" : null
}
        </code></pre></td>
    </tr>
</table>

#### 用户注册

```javascript
{
    POST: '/api/user/create',
    'Body Parameter': {
        'Content-Type': 'application/json',
        Body: `{
            "username": "ltaoo",
            "password": "hello520"
        }`,
    },
    'Response Body': `{
        "c" : 0,
        "m" : "",
        "d" : null
    }`
}
```

#### 搜索用户

#### 删除用户

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #e0f0ff">DELETE</td><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #ffd">/api/user/:id</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Body Parameter</td><td style="padding: 10px 10px;border: 1px solid #ddd"><table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #e0f0ff">Content-Type</td><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #ffd">application/json</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Body</td><td style="padding: 10px 10px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>{
"username": "ltaoo",
"password": "hello520"
}</code></pre></td></tr></table></td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>{
"c" : 0,
"m" : "",
"d" : null
}</code></pre></td></tr></table>
```javascript
{
    DELETE: '/api/user/:id',
    'Body Parameter': {
        'Content-Type': 'application/json',
        Body: `{
            "username": "ltaoo",
            "password": "hello520"
        }`,
    },
    'Response Body': `{
        "c" : 0,
        "m" : "",
        "d" : null
    }`
}
```

#### 编辑用户

#### 管理员登录

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #e0f0ff">POST</td><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #ffd">/api/login.php</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">API Description</td><td style="padding: 10px 10px;border: 1px solid #ddd">管理员登录接口</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Body Parameter</td><td style="padding: 10px 10px;border: 1px solid #ddd"><table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #e0f0ff">Content-Type</td><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #ffd">form-data</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Body</td><td style="padding: 10px 10px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>------WebKitFormBoundaryNn4581wdKEoIBHqJ
        Content-Disposition: form-data; name="username"

        admin
        ------WebKitFormBoundaryNn4581wdKEoIBHqJ
        Content-Disposition: form-data; name="password"

        123456
        ------WebKitFormBoundaryNn4581wdKEoIBHqJ--</code></pre></td></tr></table></td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
        {
            data: ["1", "admin", "123456", "0"],
            state: "success"
        }
    </code></pre></td></tr></table>

```javascript
{
    POST: '/api/login.php',
    'API Description': '管理员登录接口',
    'Body Parameter': {
        'Content-Type': 'form-data',
        'Body': `------WebKitFormBoundaryNn4581wdKEoIBHqJ
        Content-Disposition: form-data; name="username"

        admin
        ------WebKitFormBoundaryNn4581wdKEoIBHqJ
        Content-Disposition: form-data; name="password"

        123456
        ------WebKitFormBoundaryNn4581wdKEoIBHqJ--`,
    },
    'Response Body': `
        {
            data: ["1", "admin", "123456", "0"],
            state: "success"
        }
    `,
}
```

#### 添加管理员

#### 编辑管理员

#### 删除管理员

#### 搜索管理员

### 图书相关

#### 获取图书列表

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #e0f0ff">GET</td><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #ffd">/api/getBooks.service.php?action=getBookList</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">API Description</td><td style="padding: 10px 10px;border: 1px solid #ddd">获取图书列表</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Request URL</td><td style="padding: 10px 10px;border: 1px solid #ddd">http://localhost:8080/api/getBooks.service.php?action=getBookList</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
        [
            {
                bookId: "1",
                bookImg: "https://img1.doubanio.com/mpic/s29105337.jpg",
                bookTitle: "React Native 入门实践",
                bookIsbn: "9787115411914",
                bookPrice: "79",
                // 借阅状态
                bookState: "0",
                bookSummary: "本书共4部分，首先简要介绍了React Native的开发基础知识..",
                borrowTimes: "0",
                createTime: "2017-03-08",
                // 归还时间
                returnTime: null,
            }
        ]
    </code></pre></td></tr></table>

```javascript
{
    GET: '/api/getBooks.service.php?action=getBookList',
    'API Description': '获取图书列表',
    'Request Parameter': [
    ],
    'Request URL': 'http://localhost:8080/api/getBooks.service.php?action=getBookList',
    'Response Body': `
        [
            {
                bookId: "1",
                bookImg: "https://img1.doubanio.com/mpic/s29105337.jpg",
                bookTitle: "React Native 入门实践",
                bookIsbn: "9787115411914",
                bookPrice: "79",
                // 借阅状态
                bookState: "0",
                bookSummary: "本书共4部分，首先简要介绍了React Native的开发基础知识..",
                borrowTimes: "0",
                createTime: "2017-03-08",
                // 归还时间
                returnTime: null,
            }
        ]
    `
}
```

#### 搜索图书

```javascript
{
    GET: '/api/getBooks.service.php',
    'API Description': '搜索读者',
    'Path Parameter': [
        ['searchByIsbn', 'long', true, '按学号搜索，&bookIsbn=1218040201'],
        ['searchByName', 'long', true, '按书名搜索，&bookName=ltaoo']
    ],
    'Request URL': 'http://localhost:8080/api/getBooks.service.php?action=searchByIsbn&bookIsbn=react',
    'Response Body': `
        {
            data: [{
                // 同图书详情
            }],
            // ???
            state: 200
        }
    `,
}
```

#### 增加图书

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #e0f0ff">POST</td><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #ffd">/api/addBook.service.php</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">API Description</td><td style="padding: 10px 10px;border: 1px solid #ddd">增加图书</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Request URL</td><td style="padding: 10px 10px;border: 1px solid #ddd">http://localhost:8080/api/addBook.service.php</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Body Parameter</td><td style="padding: 10px 10px;border: 1px solid #ddd"><table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #e0f0ff">Content-Type</td><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #ffd">multipart/form-data</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Body</td><td style="padding: 10px 10px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
            ------WebKitFormBoundaryNkhY9LevoTlBsDsD
Content-Disposition: form-data; name="title"

React
------WebKitFormBoundaryNkhY9LevoTlBsDsD
Content-Disposition: form-data; name="price"

65
------WebKitFormBoundaryNkhY9LevoTlBsDsD
Content-Disposition: form-data; name="isbn13"

9787121259364
------WebKitFormBoundaryNkhY9LevoTlBsDsD
Content-Disposition: form-data; name="summary"

2014 年横空出世的由Facebook 推出的开源框架React.js，基于Virtual DOM 重新定义了用户界面的开发方式，彻底革新了大家对前端框架的认识，将PHP 风格的开发方式迁移到客户端应用开发。其优势在于可以与各种类库、框架搭配使用。《React：引领未来的用户界面开发框架》是这一领域的首作，由多位一线专家精心撰写，采用一个全程实例全面介绍和剖析了ReactReact.js 的方方面面，适合广大前端开发者、设计人员，及所有对未来技术趋势感兴趣者阅读。
------WebKitFormBoundaryNkhY9LevoTlBsDsD
Content-Disposition: form-data; name="image"

https://img1.doubanio.com/mpic/s28061237.jpg
------WebKitFormBoundaryNkhY9LevoTlBsDsD--
        </code></pre></td></tr></table></td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
        {
            bookId: 2,
        }
    </code></pre></td></tr></table>

```javascript
{
    POST: '/api/addBook.service.php',
    'API Description': '增加图书',
    'Request URL': 'http://localhost:8080/api/addBook.service.php',
    'Body Parameter': {
        'Content-Type': 'multipart/form-data',
        Body: `
            ------WebKitFormBoundaryNkhY9LevoTlBsDsD
Content-Disposition: form-data; name="title"

React
------WebKitFormBoundaryNkhY9LevoTlBsDsD
Content-Disposition: form-data; name="price"

65
------WebKitFormBoundaryNkhY9LevoTlBsDsD
Content-Disposition: form-data; name="isbn13"

9787121259364
------WebKitFormBoundaryNkhY9LevoTlBsDsD
Content-Disposition: form-data; name="summary"

2014 年横空出世的由Facebook 推出的开源框架React.js，基于Virtual DOM 重新定义了用户界面的开发方式，彻底革新了大家对前端框架的认识，将PHP 风格的开发方式迁移到客户端应用开发。其优势在于可以与各种类库、框架搭配使用。《React：引领未来的用户界面开发框架》是这一领域的首作，由多位一线专家精心撰写，采用一个全程实例全面介绍和剖析了ReactReact.js 的方方面面，适合广大前端开发者、设计人员，及所有对未来技术趋势感兴趣者阅读。
------WebKitFormBoundaryNkhY9LevoTlBsDsD
Content-Disposition: form-data; name="image"

https://img1.doubanio.com/mpic/s28061237.jpg
------WebKitFormBoundaryNkhY9LevoTlBsDsD--
        `
    },
    'Response Body': `
        {
            bookId: 2,
        }
    `
}
```

#### 删除图书

未完成。

### 读者相关

#### 获取读者列表

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #e0f0ff">GET</td><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #ffd">/api/getMembers.service.php?action=getMemberList</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">API Description</td><td style="padding: 10px 10px;border: 1px solid #ddd">获取全部的读者列表</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Request URL</td><td style="padding: 10px 10px;border: 1px solid #ddd">http://localhost:8080/api/getMembers.service.php?action=getMemberList</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
        [
            {
                memberId: "1",
                memberName: "ltaoo",
                // 学号
                memberNum: "123456",
                // 电话
                memberTel: "123456",
                // 等级
                memberRank: "1",
                // 地址
                memberAddress: "8-8-218",
                // 创建时间
                memberCreateTime: "2015-10-20",
                // 当前借书数
                borrowNum: "0",
                // 总借阅次数
                borrowTimes: "0"
            },
            // ...
        ]
    </code></pre></td></tr></table>

```javascript
{
    GET: '/api/getMembers.service.php?action=getMemberList',
    'API Description': '获取全部的读者列表',
    'Request URL': 'http://localhost:8080/api/getMembers.service.php?action=getMemberList',
    'Response Body': `
        [
            {
                memberId: "1",
                memberName: "ltaoo",
                // 学号
                memberNum: "123456",
                // 电话
                memberTel: "123456",
                // 等级
                memberRank: "1",
                // 地址
                memberAddress: "8-8-218",
                // 创建时间
                memberCreateTime: "2015-10-20",
                // 当前借书数
                borrowNum: "0",
                // 总借阅次数
                borrowTimes: "0"
            },
            // ...
        ]
    `
}
```

#### 根据 id 获取详情

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #e0f0ff">GET</td><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #ffd">/api/getMembers.service.php?action=searchById</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">API Description</td><td style="padding: 10px 10px;border: 1px solid #ddd">根据 id 搜索读者</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Path Parameter</td><td  style="padding: 10px 10px;border: 1px solid #ddd"><table style="border-collapse: collapse;">
                <tr>
                    <th style="padding: 10px 10px;border: 1px solid #ddd;background-color: #f0f0f0">Parameter</th>
                    <th style="padding: 10px 10px;border: 1px solid #ddd;background-color: #f0f0f0">Data Type</th>
                    <th style="padding: 10px 10px;border: 1px solid #ddd;background-color: #f0f0f0">Required</th>
                    <th style="padding: 10px 10px;border: 1px solid #ddd;background-color: #f0f0f0">Description</th>
                </tr>
                <tr><td style="padding: 10px 10px;border: 1px solid #ddd">memberId</td><td style="padding: 10px 10px;border: 1px solid #ddd">int</td><td style="padding: 10px 10px;border: 1px solid #ddd">true</td><td style="padding: 10px 10px;border: 1px solid #ddd"></td></tr>
            </table></td><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Request URL</td><td style="padding: 10px 10px;border: 1px solid #ddd">http://localhost:8080/api/getMembers.service.php?action=searchByNum&memberId=2</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
        {
            data: {
                memberId: "1",
                memberName: "ltaoo",
                // 学号
                memberNum: "123456",
                // 电话
                memberTel: "123456",
                // 等级
                memberRank: "1",
                // 地址
                memberAddress: "8-8-218",
                // 创建时间
                memberCreateTime: "2015-10-20",
                // 当前借书数
                borrowNum: "0",
                // 总借阅次数
                borrowTimes: "0"
            },
        }
    </code></pre></td></tr></table>

````javascript
{
    GET: '/api/getMembers.service.php?action=searchById',
    'API Description': '根据 id 搜索读者',
    'Path Parameter': [
        ['memberId', 'int', true, '']
    ],
    'Request URL': 'http://localhost:8080/api/getMembers.service.php?action=searchById&memberId=2',
    'Response Body': `
        {
            data: {
                memberId: "1",
                memberName: "ltaoo",
                // 学号
                memberNum: "123456",
                // 电话
                memberTel: "123456",
                // 等级
                memberRank: "1",
                // 地址
                memberAddress: "8-8-218",
                // 创建时间
                memberCreateTime: "2015-10-20",
                // 当前借书数
                borrowNum: "0",
                // 总借阅次数
                borrowTimes: "0"
            },
        }
    `,
}
```

#### 搜索

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #e0f0ff">GET</td><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #ffd">/api/getMembers.service.php</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">API Description</td><td style="padding: 10px 10px;border: 1px solid #ddd">搜索读者</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Path Parameter</td><td  style="padding: 10px 10px;border: 1px solid #ddd"><table style="border-collapse: collapse;">
                <tr>
                    <th style="padding: 10px 10px;border: 1px solid #ddd;background-color: #f0f0f0">Parameter</th>
                    <th style="padding: 10px 10px;border: 1px solid #ddd;background-color: #f0f0f0">Data Type</th>
                    <th style="padding: 10px 10px;border: 1px solid #ddd;background-color: #f0f0f0">Required</th>
                    <th style="padding: 10px 10px;border: 1px solid #ddd;background-color: #f0f0f0">Description</th>
                </tr>
                <tr><td style="padding: 10px 10px;border: 1px solid #ddd">searchByNum</td><td style="padding: 10px 10px;border: 1px solid #ddd">long</td><td style="padding: 10px 10px;border: 1px solid #ddd">true</td><td style="padding: 10px 10px;border: 1px solid #ddd">按学号搜索，&memberNum=1218040201</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">searchByName</td><td style="padding: 10px 10px;border: 1px solid #ddd">long</td><td style="padding: 10px 10px;border: 1px solid #ddd">true</td><td style="padding: 10px 10px;border: 1px solid #ddd">按姓名搜索，&memberName=ltaoo</td></tr>
            </table></td><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Request URL</td><td style="padding: 10px 10px;border: 1px solid #ddd">http://localhost:8080/api/getMembers.service.php?action=searchByNum&memberNum=1218040201</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
        {
            data: [{
                // 同读者详情
            }],
        }
    </code></pre></td></tr></table>

```javascript
{
    GET: '/api/getMembers.service.php',
    'API Description': '搜索读者',
    'Path Parameter': [
        ['searchByNum', 'long', true, '按学号搜索，&memberNum=1218040201'],
        ['searchByName', 'long', true, '按姓名搜索，&memberName=ltaoo']
    ],
    'Request URL': 'http://localhost:8080/api/getMembers.service.php?action=searchByNum&memberNum=1218040201',
    'Response Body': `
        {
            data: [{
                // 同读者详情
            }],
        }
    `,
}
```

#### 新增读者

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #e0f0ff">POST</td><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #ffd">/api/addMember.service.php</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">API Description</td><td style="padding: 10px 10px;border: 1px solid #ddd">新增读者</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Request URL</td><td style="padding: 10px 10px;border: 1px solid #ddd">http://localhost:8080/api/addMember.service.php</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Body Parameter</td><td style="padding: 10px 10px;border: 1px solid #ddd"><table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #e0f0ff">Content-Type</td><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #ffd">multipart/form-data</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Body</td><td style="padding: 10px 10px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
        ------WebKitFormBoundary3w9mXc15I0ROC52A
Content-Disposition: form-data; name="memberName"

无涯
------WebKitFormBoundary3w9mXc15I0ROC52A
Content-Disposition: form-data; name="memberNum"

1218040201
------WebKitFormBoundary3w9mXc15I0ROC52A
Content-Disposition: form-data; name="memberTel"

13822136046
------WebKitFormBoundary3w9mXc15I0ROC52A
Content-Disposition: form-data; name="memberAddress"

8
------WebKitFormBoundary3w9mXc15I0ROC52A
Content-Disposition: form-data; name="memberRank"

1
------WebKitFormBoundary3w9mXc15I0ROC52A--
        </code></pre></td></tr></table></td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
        {
            memberId: 2,
        }
    </code></pre></td></tr></table>

```javascript
{
    POST: '/api/addMember.service.php',
    'API Description': '新增读者',
    'Request URL': 'http://localhost:8080/api/addMember.service.php',
    'Body Parameter': {
        'Content-Type': 'multipart/form-data',
        Body: `
        ------WebKitFormBoundary3w9mXc15I0ROC52A
Content-Disposition: form-data; name="memberName"

无涯
------WebKitFormBoundary3w9mXc15I0ROC52A
Content-Disposition: form-data; name="memberNum"

1218040201
------WebKitFormBoundary3w9mXc15I0ROC52A
Content-Disposition: form-data; name="memberTel"

13822136046
------WebKitFormBoundary3w9mXc15I0ROC52A
Content-Disposition: form-data; name="memberAddress"

8
------WebKitFormBoundary3w9mXc15I0ROC52A
Content-Disposition: form-data; name="memberRank"

1
------WebKitFormBoundary3w9mXc15I0ROC52A--
        `,
    },
    'Response Body': `
        {
            memberId: 2,
        }
    `,
}
```

#### 更新读者信息

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #e0f0ff">POST</td><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #ffd">/api/getMembers.service.php?action=update</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Request URL</td><td style="padding: 10px 10px;border: 1px solid #ddd">http://localhost:8080/api/getMembers.service.php?action=update</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Body Parameter</td><td style="padding: 10px 10px;border: 1px solid #ddd"><table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #e0f0ff">Content-Type</td><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #ffd">multipart/form-data</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Body</td><td style="padding: 10px 10px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
            ------WebKitFormBoundaryOsMk99NnUBtK76I6
Content-Disposition: form-data; name="memberId"

2
------WebKitFormBoundaryOsMk99NnUBtK76I6
Content-Disposition: form-data; name="memberName"

无涯
------WebKitFormBoundaryOsMk99NnUBtK76I6
Content-Disposition: form-data; name="memberNum"

1218040201
------WebKitFormBoundaryOsMk99NnUBtK76I6
Content-Disposition: form-data; name="memberTel"

13822136046
------WebKitFormBoundaryOsMk99NnUBtK76I6
Content-Disposition: form-data; name="memberAddress"

87234
------WebKitFormBoundaryOsMk99NnUBtK76I6
Content-Disposition: form-data; name="memberRank"

0
------WebKitFormBoundaryOsMk99NnUBtK76I6
Content-Disposition: form-data; name="memberCreateTime"

2018-02-13
------WebKitFormBoundaryOsMk99NnUBtK76I6
Content-Disposition: form-data; name="borrowNum"

0
------WebKitFormBoundaryOsMk99NnUBtK76I6
Content-Disposition: form-data; name="borrowTimes"

0
------WebKitFormBoundaryOsMk99NnUBtK76I6--
        </code></pre></td></tr></table></td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
        {
            state: 'success'
        }
    </code></pre></td></tr></table>

```javascript
{
    POST: '/api/getMembers.service.php?action=update',
    'API Description': '更新指定读者信息',
    'Request URL': 'http://localhost:8080/api/getMembers.service.php?action=update',
    'Body Parameter': {
        'Content-Type': 'multipart/form-data',
        Body: `
            ------WebKitFormBoundaryOsMk99NnUBtK76I6
Content-Disposition: form-data; name="memberId"

2
------WebKitFormBoundaryOsMk99NnUBtK76I6
Content-Disposition: form-data; name="memberName"

无涯
------WebKitFormBoundaryOsMk99NnUBtK76I6
Content-Disposition: form-data; name="memberNum"

1218040201
------WebKitFormBoundaryOsMk99NnUBtK76I6
Content-Disposition: form-data; name="memberTel"

13822136046
------WebKitFormBoundaryOsMk99NnUBtK76I6
Content-Disposition: form-data; name="memberAddress"

87234
------WebKitFormBoundaryOsMk99NnUBtK76I6
Content-Disposition: form-data; name="memberRank"

0
------WebKitFormBoundaryOsMk99NnUBtK76I6
Content-Disposition: form-data; name="memberCreateTime"

2018-02-13
------WebKitFormBoundaryOsMk99NnUBtK76I6
Content-Disposition: form-data; name="borrowNum"

0
------WebKitFormBoundaryOsMk99NnUBtK76I6
Content-Disposition: form-data; name="borrowTimes"

0
------WebKitFormBoundaryOsMk99NnUBtK76I6--
        `
    },
    'Response Body': `
        {
            state: 'success'
        }
    `
}
```

#### 删除读者

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #e0f0ff">GET</td><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #ffd">/api/getMembers.service.php?action=delete</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">API Description</td><td style="padding: 10px 10px;border: 1px solid #ddd">根据 id 从数据库物理删除读者</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Request URL</td><td style="padding: 10px 10px;border: 1px solid #ddd">http://localhost:8080/api/getMembers.service.php?action=delete&memberId=2</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Path Parameter</td><td  style="padding: 10px 10px;border: 1px solid #ddd"><table style="border-collapse: collapse;">
                <tr>
                    <th style="padding: 10px 10px;border: 1px solid #ddd;background-color: #f0f0f0">Parameter</th>
                    <th style="padding: 10px 10px;border: 1px solid #ddd;background-color: #f0f0f0">Data Type</th>
                    <th style="padding: 10px 10px;border: 1px solid #ddd;background-color: #f0f0f0">Required</th>
                    <th style="padding: 10px 10px;border: 1px solid #ddd;background-color: #f0f0f0">Description</th>
                </tr>
                <tr><td style="padding: 10px 10px;border: 1px solid #ddd">memberId</td><td style="padding: 10px 10px;border: 1px solid #ddd">int</td><td style="padding: 10px 10px;border: 1px solid #ddd">true</td><td style="padding: 10px 10px;border: 1px solid #ddd"></td></tr>
            </table></td><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
        {
            state: 'success',
        }
    </code></pre></td></tr></table>

```javascript
{
    GET: '/api/getMembers.service.php?action=delete',
    'API Description': '根据 id 从数据库物理删除读者',
    'Request URL': 'http://localhost:8080/api/getMembers.service.php?action=delete&memberId=2',
    'Path Parameter': [
        ['memberId', 'int', true, '']
    ],
    'Response Body': `
        {
            state: 'success',
        }
    `
}
```

### 借阅记录

#### 借阅记录列表

```javascript
{
    GET: 
}
```

### 借阅相关

#### 获取借阅记录列表

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #e0f0ff">GET</td><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #ffd">/api/getRecords.service.php?action=recordsList</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">API Description</td><td style="padding: 10px 10px;border: 1px solid #ddd">获取借阅记录列表</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Request URL</td><td style="padding: 10px 10px;border: 1px solid #ddd">http://localhost:8080/api/getRecords.service.php?action=recordsList</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
       {
            "state": 200, 
            "data": [
                {
                    "recordId": "1", 
                    "memberId": "3", 
                    "memberNum": "1218040201", 
                    "memberName": "wuya", 
                    "memberTel": "13822136046", 
                    "memberAddress": "8", 
                    "memberRank": "2", 
                    "memberCreateTime": "2018-02-13", 
                    "bookId": "2", 
                    "bookIsbn": "9787121259364", 
                    "bookTitle": "React", 
                    "bookImg": "https://img1.doubanio.com/mpic/s28061237.jpg", 
                    "borrowTime": "2018-02-13", 
                    "returnTime": null
                }
            ]
        }
    </code></pre></td></tr></table>

```javascript
{
    GET: '/api/getRecords.service.php?action=recordsList',
    'API Description': '获取借阅记录列表',
    'Request URL': 'http://localhost:8080/api/getRecords.service.php?action=recordsList',
    'Response Body': `
       {
            "state": 200, 
            "data": [
                {
                    "recordId": "1", 
                    "memberId": "3", 
                    "memberNum": "1218040201", 
                    "memberName": "wuya", 
                    "memberTel": "13822136046", 
                    "memberAddress": "8", 
                    "memberRank": "2", 
                    "memberCreateTime": "2018-02-13", 
                    "bookId": "2", 
                    "bookIsbn": "9787121259364", 
                    "bookTitle": "React", 
                    "bookImg": "https://img1.doubanio.com/mpic/s28061237.jpg", 
                    "borrowTime": "2018-02-13", 
                    "returnTime": null
                }
            ]
        }
    `
}
```

#### 提交借阅记录

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #e0f0ff">POST</td><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #ffd">/api/addRecords.service.php</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">API Description</td><td style="padding: 10px 10px;border: 1px solid #ddd">增加借阅记录</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Request URL</td><td style="padding: 10px 10px;border: 1px solid #ddd">http://localhost:8080/api/addRecords.service.php</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Body Parameter</td><td style="padding: 10px 10px;border: 1px solid #ddd"><table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #e0f0ff">Content-Type</td><td style="padding: 10px 10px;border: 1px solid #ddd;background-color: #ffd">multipart/form-data</td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Body</td><td style="padding: 10px 10px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
            ------WebKitFormBoundaryWBUe8snfejNj5gbu
Content-Disposition: form-data; name="memberId"

3
------WebKitFormBoundaryWBUe8snfejNj5gbu
Content-Disposition: form-data; name="bookId"

2
------WebKitFormBoundaryWBUe8snfejNj5gbu--
        </code></pre></td></tr></table></td></tr><tr><td style="padding: 10px 10px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
        {
            recordId: 1
        }
    </code></pre></td></tr></table>

```javascript
{
    POST: '/api/addRecords.service.php',
    'API Description': '增加借阅记录',
    'Request URL': 'http://localhost:8080/api/addRecords.service.php',
    'Body Parameter': {
        'Content-Type': 'multipart/form-data',
        Body: `
            ------WebKitFormBoundaryWBUe8snfejNj5gbu
Content-Disposition: form-data; name="memberId"

3
------WebKitFormBoundaryWBUe8snfejNj5gbu
Content-Disposition: form-data; name="bookId"

2
------WebKitFormBoundaryWBUe8snfejNj5gbu--
        `
    },
    'Response Body': `
        {
            recordId: 1
        }
    `
}
```

## 数据库表

### 读者信息表

该表字段包含读者编号、读者姓名、读者身份证号、读者联系方式、读者地址、读者等级、读者添加时间，如图3.1所示。

![表3.1 读者信息表](http://oyy3cbpm3.bkt.clouddn.com/15184452355824.jpg)

### 图书信息表

该表字段包含图书编号、图书名称、图书ISBN码、图书价格、图书简介、图书封面地址、图书状态、添加时间，如表3.2所示。

![表3.2图书信息表](http://oyy3cbpm3.bkt.clouddn.com/15184452968281.jpg)

### 借阅记录表

该表在进行图书借阅时将生成记录，记录中写入借阅读者编号、所借图书编号、借阅时间，并自动生成借阅编号。在还书时，对该表的还书时间字段进行更新，写入当前时间，如图3.3所示。

![3.3借阅记录表](http://oyy3cbpm3.bkt.clouddn.com/15184453438344.jpg)

### 订单记录表

用户提交订单后将生成记录，写入购书读者编号、购买图书编号列表、留言、下单时间，并自动生成编号。管理员在后台对该订单进行确认或取消操作时，对订单状态字段进行更新，如表3.4所示。

![3.4订单记录表](http://oyy3cbpm3.bkt.clouddn.com/15184465946142.jpg)

### 购物车记录表

用户将图书加入到购物车时，首先根据用户编号结合当前时间生成唯一记录码，用以识别不同用户的购物车记录，同时将图书编号、图书折后价格写入。如表3.5所示。

![3.5购物车记录表](http://oyy3cbpm3.bkt.clouddn.com/15184466472209.jpg)

### 图书评论表

读者登录后在图书详情页进行评论时将生成记录，将图书ISBN码、留言内容，读者编号，留言时间写入，同时生成评论编号，如表3.6所示。

![3.6图书评论表](http://oyy3cbpm3.bkt.clouddn.com/15184468987893.jpg)

### 管理员信息表

记录可登录后台管理员账户密码、权限。

![3.7管理员信息表](http://oyy3cbpm3.bkt.clouddn.com/15184469499412.jpg)
