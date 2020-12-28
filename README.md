# Pytest
## 命令行选项
- --collect-only(--co)选项：展示在给定的配置下哪些测试用例会被执行
  

- -k选项：指定需要运行的用例
    - pytest -k “a or b”
    
    
- -m选项：标记（marker）用于标记测试并分组，以便快速选中并执行
    ```
    @pytest.mark.marker_name
    def test_something():
    ```
  - pytest -m marker_name，可以指定多个标记名。使用-m "mark1 and mark2"，-m "mark1 and mark2",-m "mark1 and not mark2"


- -x选项：某个测试用例断言失败或者异常，该测试用例运行就会到此为止，debug时希望遇到失败立即停止整个会话。


- --maxfail=num选项：失败n次后停止


- -s选项：终端输出信息


- --lf（--last-failed）选项：定位到最后一个失败的测试用例重新运行


- --ff（--failed-first）选项：与--lf作用基本相同，不同之处在于--ff会运行完剩余的用例


- -v（--verbose）选项：输出完整信息,显示函数名字


- -q（--quite）：简化输出信息

## 跳过测试：添加任意一个装饰器
- @pytest.mark.skip()
- @pytest.mark.skipif()
- 两个装饰器均可添加跳过原因@pytest.mark.skip(reason='xxxxxx')，命令行使用-rs参数可以测试被跳过的原因。

## 标记预期会失败的测试
- @pytest.mark.xfail()
- 测试结果：x（XFAIL），预期失败，世界也失败；X（XPASS），预期失败，实际运行并没有失败
- 对于标记为xfail，但实际结果为XPASS的测试，可以在pytest文件中强制指定结果为FAIL，添加配置参数xfail_strict=true。

## fixture作用范围
- function：函数级别的fixture每个测试函数只需要运行一次
- class：类级别的fixture每个测试类只需要运行一次
- module：模块级别的fixture每个模块只需要运行一次
- session：一次pytest会话只需要运行一次

## 使用usefixtures指定fixture
- 可以在函数的参数列表指定fixture，也可以用@pytest.mark.usefixtures('fixture1', 'fixture2')测试函数或测试类，使用此标记需要在参数列表中指定一个或多个fixture，这对测试函数来讲意义不大，但非常适合测试类
- 只有直接在测试方法添加测试参数才能够使用fixture返回值

## 为常用fixture添加autouse选项
- 可以通过指定autouse=true选项，使作用域内的测试函数都运行该fixture
```
@pytest.fixture(autouse=True)
```

## 为fixture重名名,测试函数直接使用重命名
```
@pytest.fixture(autouse=True, name='lue')
```

## fixture的参数化：scope='session'时推荐参数化不同类型的登录用户，更改环境变量等
```angular2html
data = ["param1", "param2"]
@pytest.fixture(scope='function', params=data)
def return_params(request):
    return request.param

def test_params(return_params):
    a = return_params
    print(a)
```

## pdb:调试失败的测试用例：--pdb
- p/print expr:输出expr的值
- pp expr：美化输出expr的值
- l/list：列出错误并显示错误之前和之后的5行代码
- a：打印当前函数的参数列表
- q：退出当前调试会话

## 常用插件
- pytest-repeat：重复运行测试，--count=n。（安装库pytest-repeat）
- pytest-xdist:并行运行测试：通常测试都是依次执行，因为有些资源只能被一个测试用例访问。如果测试用例不需要访问共享资源，可通过并行运行来提速。pytest -n auto可以自动检测cpu数，也可指定cpu数pytest -n 2.
- 改善输出效果：
  - pytest-instafile:
  - pytest-sugar
  - pytest-emoji