from bot import CMD_SUFFIX

class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = [f'mirror2{CMD_SUFFIX}', f'm2{CMD_SUFFIX}']
        self.YtdlCommand = [f'ytdl2{CMD_SUFFIX}', f'y2{CMD_SUFFIX}']
        self.LeechCommand = [f'leech2{CMD_SUFFIX}', f'l2{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'ytdlleech2{CMD_SUFFIX}', f'yl2{CMD_SUFFIX}']
        self.CloneCommand = [f'clone2{CMD_SUFFIX}', f'c2{CMD_SUFFIX}']
        self.CountCommand = f'count{CMD_SUFFIX}'
        self.DeleteCommand = f'del2{CMD_SUFFIX}'
        self.StopAllCommand = [f'stopall{CMD_SUFFIX}', 'stopallbot']
        self.ListCommand = f'list{CMD_SUFFIX}'
        self.SearchCommand = f'search2{CMD_SUFFIX}'
        self.StatusCommand = [f'status2{CMD_SUFFIX}', 'statusall']
        self.UsersCommand = f'users2{CMD_SUFFIX}'
        self.AuthorizeCommand = f'authorize{CMD_SUFFIX}'
        self.UnAuthorizeCommand = f'unauthorize{CMD_SUFFIX}'
        self.AddSudoCommand = f'addsudo{CMD_SUFFIX}'
        self.RmSudoCommand = f'rmsudo{CMD_SUFFIX}'
        self.PingCommand = [f'ping{CMD_SUFFIX}', 'pingall']
        self.RestartCommand = [f'restart{CMD_SUFFIX}', 'restartall']
        self.StatsCommand = [f'stats2{CMD_SUFFIX}', 'statsall']
        self.HelpCommand = f'help2{CMD_SUFFIX}'
        self.LogCommand = f'log{CMD_SUFFIX}'
        self.ShellCommand = f'shell{CMD_SUFFIX}'
        self.EvalCommand = f'eval{CMD_SUFFIX}'
        self.ExecCommand = f'exec{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_SUFFIX}'
        self.BotSetCommand = f'bsetting{CMD_SUFFIX}'
        self.UserSetCommand = [f'usetting{CMD_SUFFIX}', f'us{CMD_SUFFIX}']
        self.BtSelectCommand = f'btsel{CMD_SUFFIX}'
        self.SpeedCommand = f'speedtest{CMD_SUFFIX}'
        self.RssCommand = f'rss{CMD_SUFFIX}'
        self.AddImageCommand = f'addimg{CMD_SUFFIX}'
        self.ImagesCommand = f'images{CMD_SUFFIX}'
        self.MediaInfoCommand = f'mediainfo{CMD_SUFFIX}'
        self.BroadcastCommand = [f'broadcast{CMD_SUFFIX}', 'broadcastall']

BotCommands = _BotCommands()
