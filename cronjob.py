from apscheduler.schedulers.blocking import BlockingScheduler

from expiry import deleteDocument

scheduler = BlockingScheduler()
scheduler.add_job(deleteDocument, "interval", seconds=10, max_instances=2)

scheduler.start()