

class command:
    result = ""
    def __init__(self):
        self.result = ""
        print("init class command")

    def do(self, cmdstr):
        print("do [" + cmdstr + "]")
        return "execute command string [" + cmdstr + "]"

    def setresult(self, result):
        self.result = result

    def verify(self, result):
        print("verify [" + result + "]")
        return True


class testsuit:
    teststeps = []
    commands = None
    def __init__(self):
        self.commands = command()
        print("init class test suit")

    def addstep(self, cmdstr):
        self.teststeps.append(cmdstr)

    def getresult(self, cmdstr):
        return "result of " + cmdstr

    def test(self, cmdstr):
        if (self.commands.verify(self.getresult(self.commands.do(cmdstr)))) == True:
            print "test of [" + cmdstr + "] is pass"
        else:
            print "test of [" + cmdstr + "] is fail"

    def runtestsuit(self):
        for s in self.teststeps:
            self.test(s)


if __name__ == "__main__":
    mytest = testsuit()
    mytest.addstep("first test")
    mytest.addstep("second test")
    mytest.addstep("third test")
    mytest.runtestsuit()