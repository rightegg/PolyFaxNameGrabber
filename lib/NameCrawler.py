
import os
from lib.Crawler import Crawler
from lib.Repository import Repository


class NameCrawler(Crawler):
    def __init__(self, FileName="RepositoryList.csv"):
        super(NameCrawler, self).__init__(FileName)

        if os.path.exists(self.FileName):
            os.rename(self.FileName, self.FileName+"-back.csv")

    def GrabProject(self):
        RepoList = []
        print(self.Names)
        for Name in self.Names:
            print("===>[Name]: ", Name, end=", ")
            Result = self.GetRepoByName(Name)

            RepoList.append(Result)
        RepoNum = len(RepoList)
        if RepoNum == 0:
            print("")
            return

        print("RepoNum: %u" % RepoNum)
        for Repo in RepoList:
            LangsDict = self.GetRepoLangs(Repo['languages_url'])
            MainLang = self.GetMainLang(LangsDict)

            LangsDict = self.LangValidate(LangsDict)
            if LangsDict == None:
                continue

            Langs = list(LangsDict.keys())
            if len(Langs) == 0:
                continue

            print("\t[%u][%u] --> %s" %
                  (len(self.RepoList), Repo['id'], Repo['clone_url']))
            RepoData = Repository(Repo['id'], Repo['stargazers_count'], Langs, Repo['url'], Repo['clone_url'], Repo['topics'],
                                  Repo['description'], Repo['created_at'], Repo['pushed_at'])
            RepoData.SetMainLang(MainLang)
            RepoData.SetName(Repo['name'])

            Exist = self.RepoList.get(Repo['id'])
            if Exist != None:
                continue

            self.RepoList[Repo['id']] = RepoData
            self.AppendSave(RepoData)
            print("saved-----------------------------------\n")

        # self.Save()
