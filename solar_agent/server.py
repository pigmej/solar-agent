import click

@click.group()
def cli():
    pass


def validate_class(ctx, param, value):
    supported = ('tcp', )
    if not value in supported:
        raise click.BadParameter("%r is not one of %r" % (value, supported))
    return value


@cli.command()
@click.option('--base', default='tcp', callback=validate_class, type=str)
@click.option('--port', default=5555, type=int)
def run(base, port):
    if base == 'tcp':
        from solar_agent.tcp_server import SolarAgentTCPServer
        runner = SolarAgentTCPServer.run_solar_agent
    runner(port)


if __name__ == '__main__':
    cli()
