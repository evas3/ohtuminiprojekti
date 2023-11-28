from invoke import tasks

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

