import logging

log = logging.getLogger(__name__)

class PluginBase:
    # private
    name = ""
    number = 0
    # public
    label = ""
    #openFrom = ["DISKMENU", "PLUGINSMENU", "FINDLIST", "SHORTCUT", "COMMANDLINE", "EDITOR", "VIEWER", "FILEPANEL"]
    openFrom = []
    Configure = None # override with method when configuration dialog is needed

    def __init__(self, parent, info, ffi, ffic):
        self.parent = parent
        self.info = info
        self.ffi = ffi
        self.ffic = ffic
        self.hplugin = self.ffi.cast('void *', id(self))

    def s2f(self, s):
        return self.ffi.new("wchar_t []", s)

    def f2s(self, s):
        return self.ffi.string(self.ffi.cast("wchar_t *", s))

    @staticmethod
    def HandleCommandLine(line):
        log.debug("Plugin.HandleCommandLine({0})".format(line))
        return False

    def OpenPlugin(self, OpenFrom):
        log.debug("Plugin.OpenPlugin({0})".format(OpenFrom))

    def Close(self):
        log.debug("Plugin.Close()")


class PluginVFS(PluginBase):

    def GetOpenPluginInfo(self, OpenInfo):
        log.debug("VFS.GetOpenPluginInfo({0})".format(OpenInfo))

    def FreeFindData(self, PanelItem, ItemsNumber):
        log.debug("VFS.FreeFindData({0}, {1})".format(PanelItem, ItemsNumber))

    def FreeVirtualFindData(self, PanelItem, ItemsNumber):
        log.debug("VFS.FreeVirtualFindData({0}, {1})".format(PanelItem, ItemsNumber))

    def Compare(self, PanelItem1, PanelItem2, Mode):
        log.debug("VFS.Compare({0}, {1}, {2})".format(PanelItem1, PanelItem2, Mode))
        return -2

    def DeleteFiles(self, PanelItem, ItemsNumber, OpMode):
        log.debug("VFS.DeleteFiles({0}, {1}, {2})".format(PanelItem, ItemsNumber, OpMode))
        return 0

    def GetFiles(self, PanelItem, ItemsNumber, Move, DestPath, OpMode):
        log.debug("VFS.GetFiles({0}, {1}, {2}, {3}, {4}".format(
            PanelItem,
            ItemsNumber,
            Move,
            DestPath,
            OpMode,
            )
        )
        return 0

    def GetFindData(self, PanelItem, ItemsNumber, OpMode):
        log.debug("VFS.GetFindData({0}, {1}, {2})".format(PanelItem, ItemsNumber, OpMode))
        return 0

    def GetVirtualFindData(self, PanelItem, ItemsNumber, Path):
        log.debug("VFS.GetVirtualFindData({0}, {1}, {2})".format(PanelItem, ItemsNumber, Path))
        return 0

    def MakeDirectory(self, Name, OpMode):
        log.debug("VFS.GetMakeDirectoryFindData({0}, {1})".format(Name, OpMode))
        return 0

    def ProcessEvent(self, Event, Param):
        log.debug("VFS.ProcessEvent({0}, {1})".format(Event, Param))
        return 0

    def ProcessHostFile(self, PanelItem, ItemsNumber, OpMode):
        log.debug("VFS.ProcessHostFile({0}, {1}, {2})".format(PanelItem, ItemsNumber, OpMode))
        return 0

    def ProcessKey(self, Key, ControlState):
        log.debug("VFS.ProcessKey({0}, {1})".format(Key, ControlState))
        return 0

    def PutFiles(self, PanelItem, ItemsNumber, Move, SrcPath, OpMode):
        log.debug("VFS.PutFiles({0}, {1}, {2}, {3}, {4}".format(
            PanelItem,
            ItemsNumber,
            Move,
            SrcPath,
            OpMode,
            )
        )
        return 0

    def SetDirectory(self, Dir, OpMode):
        log.debug("VFS.SetDirectory({0}, {1})".format(Dir, OpMode))
        return 0

    def SetFindList(self, PanelItem, ItemsNumber):
        log.debug("VFS.SetFindList({0}, {1})".format(PanelItem, ItemsNumber))
        return 0
