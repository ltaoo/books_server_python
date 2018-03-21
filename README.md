
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

## 运行 python 代码

```bash
docker run --name ${NAME} -v $PWD:${DIR} -p ${PORT}:80 -it python /bin/bash
```

上述命令，表示运行一个名字为`${name}`的，将当前目录映射到`${DIR}`文件夹的，端口为`${PORT}`的`python`项目。

```bash
docker run --name books-server -v $PWD:/var/www/books-server -p 8888:80 -it python /bin/bash
```

运行成功后，进入容器的`/var/www/books-server`文件夹，在里面安装`Flask`。

```bash
cd /var/www/books-server
pip install flask
```

### 初始化数据

```bash
from index import db, Role, User
admin_role = Role(name='Admin')
admin = User(username='ltaoo', email='184009428@qq.com', tel='13822136046', role=admin_role, address='218', rank=1)
db.session.add_all([admin_role, admin])
db.session.commit()
```
AttributeError: 'Role' object has no attribute 'translate'
这里有一个一定要注意的点是，虽然在表中定义的是`role_id`字段，但是这里实际要传入的是`role`！！

admin = User(username='litao', email='litaowork@aliyun.com', password='helloworld', tel='13822136046', role_id=1, address='218', rank=1)

### 运行项目

```bash
python manage.py runserver --host 0.0.0.0
```

### 依赖管理

生成依赖列表

```bash
pip freeze >requirements.txt
```

安装依赖

```bash
pip install -r requirements.txt
```

## Api

### 用户相关

本系统中「用户」、「会员」、「读者」是同一个意思。

#### 用户登录

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #e0f0ff">POST</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #ffd">/api/memberLogin.php</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">API Description</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">用户登录</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Request URL</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">http://localhost:8080/api/memberLogin.php</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Body Parameter</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #e0f0ff">Content-Type</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #ffd">multipart/form-data</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Body</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
        ------WebKitFormBoundary9ihVrBVB9FYor0tT
Content-Disposition: form-data; name="username"

123456
------WebKitFormBoundary9ihVrBVB9FYor0tT
Content-Disposition: form-data; name="password"

123456
------WebKitFormBoundary9ihVrBVB9FYor0tT--
        </code></pre></td></tr></table></td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
        {
            "state":"success",
            "data":["1","ltaoo","123456","123456","8-8-218","1","2015-10-20"]
        }
    </code></pre></td></tr></table>


```javascript
{
    POST: '/api/memberLogin.php',
    'API Description': '用户登录',
    'Request URL': 'http://localhost:8080/api/memberLogin.php',
    'Body Parameter': {
        'Content-Type': 'multipart/form-data',
        Body: `
        ------WebKitFormBoundary9ihVrBVB9FYor0tT
Content-Disposition: form-data; name="username"

123456
------WebKitFormBoundary9ihVrBVB9FYor0tT
Content-Disposition: form-data; name="password"

123456
------WebKitFormBoundary9ihVrBVB9FYor0tT--
        `
    },
    'Response Body': `
        {
            "state":"success",
            "data":["1","ltaoo","123456","123456","8-8-218","1","2015-10-20"]
        }
    `
}
```

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

<div style="display: none;">
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
</div>

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

<div style="display: none;">
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
</div>

#### 搜索

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #e0f0ff">GET</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #ffd">/api/getMembers.service.php</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">API Description</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">搜索读者</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Path Parameter</td><td  style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><table style="border-collapse: collapse;">
                <tr>
                    <th style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #f0f0f0">Parameter</th>
                    <th style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #f0f0f0">Data Type</th>
                    <th style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #f0f0f0">Required</th>
                    <th style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #f0f0f0">Description</th>
                </tr>
                <tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">searchByNum</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">long</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">true</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">按学号搜索，&memberNum=1218040201</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">searchByName</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">long</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">true</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">按姓名搜索，&memberName=ltaoo</td></tr>
            </table></td><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Request URL</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">http://localhost:8080/api/getMembers.service.php?action=searchByNum&memberNum=1218040201</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
        {
            data: [{
                // 同读者详情
            }],
        }
    </code></pre></td></tr></table>

<div style="display: none;">
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
</div>

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


<div style="display: none;">
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
</div>

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


<div style="display: none;">
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
</div>

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


<div style="display: none;">
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
</div>

#### 管理员登录

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #e0f0ff">POST</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #ffd">/api/login.php</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">API Description</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">管理员登录</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Request URL</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">http://localhost:8080/api/login.php</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Body Parameter</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #e0f0ff">Content-Type</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #ffd">multipart/form-data</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Body</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
        ------WebKitFormBoundaryagwWet4VwQUMUI9k
Content-Disposition: form-data; name="username"

admin
------WebKitFormBoundaryagwWet4VwQUMUI9k
Content-Disposition: form-data; name="password"

123456
------WebKitFormBoundaryagwWet4VwQUMUI9k--
        </code></pre></td></tr></table></td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
        {
            "state":"success",
            "data":["1","admin","123456","0"]
        }
    </code></pre></td></tr></table>

```javascript
{
    POST: '/api/login.php',
    'API Description': '管理员登录',
    'Request URL': 'http://localhost:8080/api/login.php',
    'Body Parameter': {
        'Content-Type': 'multipart/form-data',
        Body: `
        ------WebKitFormBoundaryagwWet4VwQUMUI9k
Content-Disposition: form-data; name="username"

admin
------WebKitFormBoundaryagwWet4VwQUMUI9k
Content-Disposition: form-data; name="password"

123456
------WebKitFormBoundaryagwWet4VwQUMUI9k--
        `,
    },
    'Response Body': `
        {
            "state":"success",
            "data":["1","admin","123456","0"]
        }
    `
}
```

### 图书相关

#### 获取图书列表

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #e0f0ff">GET</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #ffd">/api/getBooks.service.php?action=getBookList</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">API Description</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">获取图书列表</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Request URL</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">http://localhost:8080/api/getBooks.service.php?action=getBookList</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
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

<div style="display: none;">
{
    GET: '/api/getBooks.service.php?action=getBookList',
    'API Description': '获取图书列表',
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
</div>

#### 搜索图书

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #e0f0ff">GET</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #ffd">/api/getBooks.service.php</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">API Description</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">搜索图书</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Path Parameter</td><td  style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><table style="border-collapse: collapse;">
                <tr>
                    <th style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #f0f0f0">Parameter</th>
                    <th style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #f0f0f0">Data Type</th>
                    <th style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #f0f0f0">Required</th>
                    <th style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #f0f0f0">Description</th>
                </tr>
                <tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">searchByIsbn</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">long</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">true</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">按ISBN搜索，&bookIsbn=1218040201</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">searchByName</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">long</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">true</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">按书名搜索，&bookName=ltaoo</td></tr>
            </table></td><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Request URL</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">http://localhost:8080/api/getBooks.service.php?action=searchByIsbn&bookIsbn=react</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
        {
            data: [{
                // 同图书详情
            }],
            // ???
            state: 200
        }
    </code></pre></td></tr></table>

<div style="display: none;">
```javascript
{
    GET: '/api/getBooks.service.php',
    'API Description': '搜索图书',
    'Path Parameter': [
        ['searchByIsbn', 'long', true, '按ISBN搜索，&bookIsbn=1218040201'],
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
</div>

#### 增加图书

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #e0f0ff">POST</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #ffd">/api/addBook.service.php</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">API Description</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">增加图书</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Request URL</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">http://localhost:8080/api/addBook.service.php</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Body Parameter</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #e0f0ff">Content-Type</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #ffd">multipart/form-data</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Body</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
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

2014 年横空出世的由Facebook 推出的开源框架....
------WebKitFormBoundaryNkhY9LevoTlBsDsD
Content-Disposition: form-data; name="image"

https://img1.doubanio.com/mpic/s28061237.jpg
------WebKitFormBoundaryNkhY9LevoTlBsDsD--
        </code></pre></td></tr></table></td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
        {
            bookId: 2,
        }
    </code></pre></td></tr></table>


<div style="display: none;">
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

2014 年横空出世的由Facebook 推出的开源框架...
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
</div>

#### 删除图书

未完成。

### 读者相关



### 借阅记录

#### 借阅记录列表

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


<div style="display: none;">
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
</div>

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


<div style="display: none;">
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
</div>

#### 查询借阅记录

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #e0f0ff">GET</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #ffd">/api/getRecords.service.php?action=searchByNumber&memberNum=1218040201</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">API Description</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">根据不同条件查询借阅记录</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Path Parameter</td><td  style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><table style="border-collapse: collapse;">
                <tr>
                    <th style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #f0f0f0">Parameter</th>
                    <th style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #f0f0f0">Data Type</th>
                    <th style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #f0f0f0">Required</th>
                    <th style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #f0f0f0">Description</th>
                </tr>
                <tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">action</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">string</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">false</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">searchByNumber | searchByName | searchByIsbn | searchByTitle</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">memberNum</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">string</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">false</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">与 searchByNumber 一起使用</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">memberName</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">string</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">false</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">与 searchByName 一起使用</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">bookIsbn</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">string</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">false</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">与 searchByIsbn 一起使用</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">bookTitle</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">string</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">false</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">与 searchByTitle 一起使用</td></tr>
            </table></td><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Request URL</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">http://localhost:8080/api/getRecords.service.php?action=searchByNumber&memberNum=1218040201</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
        {
            "data": [
                {
                    "recordId":"1",
                    "memberId":"3",
                    "memberNum":"1218040201",
                    "memberName":"wuya",
                    "memberRank":"2",
                    "memberCreateTime":"2018-02-13",
                    "bookId":"2",
                    "bookIsbn":"9787121259364",
                    "bookTitle":"React",
                    "bookImg":"https://img1.doubanio.com/mpic/s28061237.jpg","borrowTime":"2018-02-13"
                },
                // ...
            ]
        }
    </code></pre></td></tr></table>

```javascript
{
    GET: '/api/getRecords.service.php?action=searchByNumber&memberNum=1218040201',
    'API Description': '根据不同条件查询借阅记录',
    'Path Parameter': [
        ['action', 'string', false, 'searchByNumber | searchByName | searchByIsbn | searchByTitle'],
        ['memberNum', 'string', false, '与 searchByNumber 一起使用'],
        ['memberName', 'string', false, '与 searchByName 一起使用'],
        ['bookIsbn', 'string', false, '与 searchByIsbn 一起使用'],
        ['bookTitle', 'string', false, '与 searchByTitle 一起使用'],
    ],
    'Request URL': 'http://localhost:8080/api/getRecords.service.php?action=searchByNumber&memberNum=1218040201',
    'Response Body': `
        {
            "data": [
                {
                    "recordId":"1",
                    "memberId":"3",
                    "memberNum":"1218040201",
                    "memberName":"wuya",
                    "memberRank":"2",
                    "memberCreateTime":"2018-02-13",
                    "bookId":"2",
                    "bookIsbn":"9787121259364",
                    "bookTitle":"React",
                    "bookImg":"https:\/\/img1.doubanio.com\/mpic\/s28061237.jpg","borrowTime":"2018-02-13"
                },
                // ...
            ]
        }
    `
}
```

#### 归还图书

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #e0f0ff">GET</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #ffd">/api/getRecords.service.php?action=update&recordId=1</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">API Description</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">归还图书，其实就是更新借阅记录</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Path Parameter</td><td  style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><table style="border-collapse: collapse;">
                <tr>
                    <th style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #f0f0f0">Parameter</th>
                    <th style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #f0f0f0">Data Type</th>
                    <th style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #f0f0f0">Required</th>
                    <th style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #f0f0f0">Description</th>
                </tr>
                <tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">recordId</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">int</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">true</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">记录 id</td></tr>
            </table></td><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Request URL</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">http://localhost:8080/api/getRecords.service.php?action=update&recordId=1</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>null</code></pre></td></tr></table>

```javascript
{
    GET: '/api/getRecords.service.php?action=update&recordId=1',
    'API Description': '归还图书，其实就是更新借阅记录',
    'Path Parameter': [
        ['recordId', 'int', true, '记录 id']
    ],
    'Request URL': 'http://localhost:8080/api/getRecords.service.php?action=update&recordId=1',
    'Response Body': `null`
}
```

### 订单

#### 订单列表

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #e0f0ff">GET</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #ffd">/api/order.php?action=fetchList</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">API Description</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">获取所有订单</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Request URL</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">http://localhost:8080/api/order.php?action=fetchList</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
        {
            "state":200,
            "data":[],
            "msg":"empty"
        }
    </code></pre></td></tr></table>

```javascript
{
    GET: '/api/order.php?action=fetchList',
    'API Description': '获取所有订单',
    'Request URL': 'http://localhost:8080/api/order.php?action=fetchList',
    'Response Body': `
        {
            "state":200,
            "data":[],
            "msg":"empty"
        }
    `
}
```

#### 搜索订单

#### 加入购物车

<table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #e0f0ff">POST</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #ffd">http://localhost:8080/api/cart.php?action=addCart</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">API Description</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">将指定商品添加至购物车</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Request URL</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">http://localhost:8080/api/cart.php?action=addCart</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Body Parameter</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><table style="border-collapse: collapse;"><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #e0f0ff">Content-Type</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd;background-color: #ffd">multipart/form-data</td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Body</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
            ------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="bookId"

1
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="bookTitle"

React Native入门与实战
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="bookIsbn"

9787115411914
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="bookPrice"

79
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="borrowTimes"

0
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="returnTime"

null
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="bookSummary"

本书共4部分，首先简要介绍了React Native的开发基础知识，然后介绍了React Native的API、组件以及Native扩展和组件的封装，接着介绍了App的动态更新和上架过程，最后通过3个案例介绍了如何使用React Native开发原生App。
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="bookState"

0
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="bookImg"

https://img1.doubanio.com/mpic/s29105337.jpg
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="createTime"

2017-03-08
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="newPrice"

59.25
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="cartsession"

123
------WebKitFormBoundaryL2hq1BTbAPeMPrul--
        </code></pre></td></tr></table></td></tr><tr><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd">Response Body</td><td style="padding: 10px 10px; min-width: 150px;border: 1px solid #ddd"><pre style="border: 1px solid #b7b7b7; border-radius: 5px; padding: 10px 20px;"><code>
        {
            "state":"success",
            "cartId":1
        }
    </code></pre></td></tr></table>

```javascript
{
    POST: 'http://localhost:8080/api/cart.php?action=addCart',
    'API Description': '将指定商品添加至购物车',
    'Request URL': 'http://localhost:8080/api/cart.php?action=addCart',
    'Body Parameter': {
        'Content-Type': 'multipart/form-data',
        Body: `
            ------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="bookId"

1
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="bookTitle"

React Native入门与实战
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="bookIsbn"

9787115411914
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="bookPrice"

79
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="borrowTimes"

0
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="returnTime"

null
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="bookSummary"

本书共4部分，首先简要介绍了React Native的开发基础知识，然后介绍了React Native的API、组件以及Native扩展和组件的封装，接着介绍了App的动态更新和上架过程，最后通过3个案例介绍了如何使用React Native开发原生App。
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="bookState"

0
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="bookImg"

https://img1.doubanio.com/mpic/s29105337.jpg
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="createTime"

2017-03-08
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="newPrice"

59.25
------WebKitFormBoundaryL2hq1BTbAPeMPrul
Content-Disposition: form-data; name="cartsession"

123
------WebKitFormBoundaryL2hq1BTbAPeMPrul--
        `
    },
    'Response Body': `
        {
            "state":"success",
            "cartId":1
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
