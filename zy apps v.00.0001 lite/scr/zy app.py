from UI import mainUI
from scr import dacon
import config

def check_init():
    onReady = dacon.OnReady()
    has_configure = onReady.check_init()
    if has_configure == True:
        run()
    else:
        onReady.initialize()
        rerun()
        
def rerun():
    check_init()

def run():
    app_name = config.cfgInfo.APP_NAME
    app_version = config.cfgInfo.APP_VERSION
    app_status = config.cfgInfo.APP_STATUS

    mainUI.run_app(app_name, app_version, app_status)

if __name__ == '__main__':
    check_init()
    
