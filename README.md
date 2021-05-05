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
- 测试结果：x（XFAIL），预期失败，实际也失败；X（XPASS），预期失败，实际运行并没有失败
- 对于标记为xfail，但实际结果为XPASS的测试，可以在pytest文件中强制指定结果为FAIL，添加配置参数xfail_strict=true。

## fixture作用范围

- function：函数级别的fixture每个测试函数只需要运行一次
- class：类级别的fixture每个测试类只需要运行一次
- module：模块级别的fixture每个模块只需要运行一次
- session：一次pytest会话只需要运行一次

## 使用usefixtures指定fixture

- 可以在函数的参数列表指定fixture，也可以用@pytest.mark.usefixtures('fixture1', 'fixture2')
  测试函数或测试类，使用此标记需要在参数列表中指定一个或多个fixture，这对测试函数来讲意义不大，但非常适合测试类
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
- pytest-xdist:并行运行测试：通常测试都是依次执行，因为有些资源只能被一个测试用例访问。如果测试用例不需要访问共享资源，可通过并行运行来提速。pytest -n auto可以自动检测cpu数，也可指定cpu数pytest -n
    2.
- 改善输出效果：
    - pytest-instafile:
    - pytest-sugar
    - pytest-emoji

## 常用断言

- assert xx 判断xx为真
- assert not xx 判断xx不为真
- assert a in b 判断b包含a
- assert a == b 判断a等于b
- assert a != b 判断a不等于b

## 使用自定义标记mark

```
@pytest.mark.TestMark1
def test_mark1():
    print("运行mark1")
```

- 需要在pytest.ini文件添加markers配置

```
[pytest]
markers = mark1
          TestMark1
          TestMark2
```

## pytest分布式执行（pytest-xdist）

- 多cpu并行执行用例，直接加个-n参数即可，后面num参数就是并行数量，比如num设置为3

```
pytest -n 3
```

## 重复执行用例（pytest-repeat）

- 重复执行（--count）

```
--count=5
```

- --repeat-scope --repeat-scope类似于pytest fixture的scope参数，--repeat-scope也可以设置参数： session ， module，class或者function（默认值)
  ```
  function（默认）范围针对每个用例重复执行，再执行下一个用例
  class 以class为用例集合单位，重复执行class里面的用例，再执行下一个
  module 以模块为单位，重复执行模块里面的用例，再执行下一个
  session 重复整个测试会话，即所有收集的测试执行一次，然后所有这些测试再次执行等等
  ```
  
- @pytest.mark.repeat(count):如果要在代码中标记要重复多次的测试，可以使用@pytest.mark.repeat(count)装饰器


## 随机执行测试用例(pytest-random-order)
- random-order
- random-order-bucket 随机范围，运行pytest --random-order-bucket=选项，其中可以是global,package,module,class,parent,grandparent
- 模块或类中禁用随机
```
# 写在.py文件最上面即可
pytestmark = pytest.mark.random_order(disabled=True)

def test_number_one():
    assert True

def test_number_two():
    assert True
```
- --random-order-seed 随机种子：如果由于重新排序测试而发现测试失败，则可能希望能够以相同的失败顺序重新运行测试
```
pytest -v --random-order-seed = xxxx
```