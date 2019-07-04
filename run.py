
import unittest
import time
#8.3执行测试用例方案三如下：
#8.3.1构造测试集（简化了方案二中先要创建测试套件然后再依次加载测试用例）
#执行顺序同方案一：执行顺序是命名顺序：先执行test_case1，再执行test_case2
from HTMLTestRunner import HTMLTestRunner

test_dir = './mallApiTest'
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
discover = unittest.TestLoader().discover(test_dir)
#8.3.2执行测试用例
#8.3.2.1实例化TextTestRunner类

#8.3.2.2使用run()方法运行测试套件（即运行测试套件中的所有用例）

current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
baseDir = "./mallResult"
report_path = baseDir + current_time + '.html'  # 生成测试报告的路径
fp = open(report_path, "wb")

# #在if __name__ == '__main__'代码块中，用下面代码块替换runner = unittest.TextTestRunner()
if __name__ == "__main__":
    # runner=unittest.TextTestRunner()
    runner = HTMLTestRunner(stream=fp,
                                title=u'自动化测试报告',
                                description=u'用例执行情况',
                                verbosity=2
                                )
    runner.run(discover)
    fp.close()