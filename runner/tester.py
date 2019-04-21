# encoding = utf8

'''
这个是基本类，目的是将 测试人员口中的测试步骤，与相应的运行命令、及命令结果的判断，作映射关系。
command的子类，应该作的是将 多个测试步骤（字符串名称） 与 一个 运行命令及如何判断运行结果(python函数)， 映射。
如：
“查当前目录”     对应 要下发 “pwd”命令，及 python函数 verify_pwd(pwd_result)
'''
class command:
    result = ""
    parsenameset = set()
    commandname = ""
    def __init__(self, cname):
        self.result = ""
        self.commandname = cname
        print("init class command")

    def addparsename(self, name):
        self.parsenameset.add(name)
        print("add [" + name + "] to (" + self.commandname + ") namelist")

    def parsecommand(self, name):
        func = self.dict_functions[name]
        if name in self.parsenameset:
            print("can't find command [" + name + "]")
            return True
        else:
            print("can't find command [" + name + "]")
            return False

    def do(self, cmdstr):
        print("do [" + cmdstr + "]")
        func = self.parsecommand(cmdstr)
        if self.parsecommand(cmdstr):
            return "execute command string [" + cmdstr + "]"
        return "command not support [" + cmdstr + "]"

    def setresult(self, result):
        self.result = result

    def verify(self, result):
        if result == None:
            print("verify: command not execute, result is [" + str(result) + "]")
            return False
        print("verify [" + result + "]")
        return True


'''
按test steps 一步步运行命令。
是一个测试用例的执行
每一步的执行，通过调用runner实例完成。
'''
class test:
    teststeps = []
    commands = None
    def __init__(self):
        self.commands = runner()
        print("init class test suit")

    def addstep(self, cmdstr):
        self.teststeps.append(cmdstr)

    def getresult(self, cmdstr):
        if cmdstr == None:
            return None
        return "result of " + cmdstr

    def testonestep(self, cmdstr):
        if (self.commands.verify(self.getresult(self.commands.do(cmdstr)))) == True:
            print "test of [" + cmdstr + "] is pass"
        else:
            print "test of [" + cmdstr + "] is fail"

    def runtest(self):
        for s in self.teststeps:
            self.testonestep(s)


'''
这里是 command类多个子类的实例的 集合。
即一个runner可以通过 测试步骤的名称 ，调用相应的 command子类， 得到要下发的命令， 将命令下发后，再调用 command子类的verify来做结果判断。
以此方式，实现每一个测试步骤的执行。
command完成的是得到一个具体测试步骤的 命令，并判断结果。
runner是 command的集合，可执行各种不同的测试步骤。
'''

class runner:
    commandnamelist = []
    dict_name2funcs = {}
    commandset = set()
    def __init__(self):
        print("runner init")

    def addcommand(self, commandinstance):
        if not isinstance(commandinstance, command):
            print(str(commandinstance) + "should be an object of command")
            return
        if commandinstance in self.commandset:
            print(str(commandinstance) + "is in to commandset")
            return
        self.commandset.add(commandinstance)
        print("adding " + str(commandinstance) + "to commandset")


if __name__ == "__main__":
    mytest = test()
    mytest.addstep("first test")
    mytest.addstep("second test")
    mytest.addstep("third test")
    mytest.runtest()