代码结构
-- business    主要存放工具代码
-- testcases   主要存放测试用例
-- data        存放参数化测试数据 
-- conftest    存放前置fixture函数
-- pytest.ini  配置文件
-- confglobal  存放接口配置

-- 使用的库：requests、pytest、openpyxl、allure-pytest
-- 集成工具（git + jenkins），jenkins安装插件allure，需要下载allure，并配置环境变量