from BGLogger.BGLogger import *

log = Log(process_name='TESTING LOG SYSTEM', record=True, return_every_log=False, output_style=OutputStyle.UNDERLINE, color=True)

log.d(tag='TEST', message='DEBUG LOG IS COOL')
log.i(tag='TEST', message='INFO LOG IS COOL')
log.e(tag='TEST', message='ERROR LOG IS COOL')
log.s(tag='TEST', message='SUCCESS LOG IS COOL')
log.w(tag='TEST', message='WARNING LOG IS COOL')
log.save_logs_to_file('logging result.py')
log.f(tag='TEST', message='FATAL LOG WILL BE THE LAST IN YOUR ALIVE PROGRAM. That\'s why you should save your logs to a file first',
      exit_type=ExitType.RAISE_EXCEPTION)