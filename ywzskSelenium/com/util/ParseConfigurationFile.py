from ConfigParser import ConfigParser
from com.config.VarConfig import pageElementLocatorPath

class ParseCofigFile(object):
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(pageElementLocatorPath)

    def getItemSection(self,sectionName):
        optionsDict = dict(self.cf.items(sectionName))
        return optionsDict
    def getOptionValue(self,sectionName,optionName):
        value = self.cf.get(sectionName,optionName)
        return value

if __name__ == "__main__":
    pc = ParseCofigFile()
    #print pc.getItemSection("yizsk_login")
   # print pc.getOptionValue("yizsk_login","loginPage.username")
