from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

from expiry import deleteDocument

scheduler = BlockingScheduler()
# scheduler.add_job(deleteDocument, "interval", seconds=10, max_instances=2)

scheduler.add_job(
    func=deleteDocument,
    trigger=IntervalTrigger(seconds=2),
    id='deleting my data',
    replace_existing=True
)
scheduler.start()

# atexit.register(lambda: scheduler.shutdown())
