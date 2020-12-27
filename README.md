# Pytest
## 命令行选项
- --collect-only选项：展示在给定的配置下哪些测试用例会被执行
  

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


- -v（--verbose）选项：输出完整信息


- -q（--quite）：简化输出信息

## 跳过测试：添加任意一个装饰器
- @pytest.mark.skip()
- @pytest.mark.skipif()
- 两个装饰器均可添加跳过原因@pytest.mark.skip(reason='xxxxxx')，命令行使用-rs参数可以测试被跳过的原因。

## 标记预期会失败的测试
- @pytest.mark.xfail()
- 测试结果：x（XFAIL），预期失败，世界也失败；X（XPASS），预期失败，实际运行并没有失败
- 对于标记为xfail，但实际结果为XPASS的测试，可以在pytest文件中强制指定结果为FAIL，添加配置参数xfail_strict=true。