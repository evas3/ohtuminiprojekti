from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def list(ctx)
    ctx.run("cat src/data/references.bib", pty=True)
