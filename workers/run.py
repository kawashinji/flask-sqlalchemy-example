import workers.tasks

print('========== Start Task ==========')
worker = workers.tasks.run.delay()
while not worker.ready():
    pass
print(worker.result)
print('========== End Task ==========')
