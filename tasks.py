from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

def list(ctx):
    ctx.run("cat src/data/refrences.bib", pty=True)
