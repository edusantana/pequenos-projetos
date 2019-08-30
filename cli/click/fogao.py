import click

@click.command()
@click.option('--liga/--desliga', help="Liga ou desliga")
@click.option('--boca', 'boca', type=int)
@click.option('-i','--intensidade', 'intensidade', help="Intensidade: baixo|medio|alto")
def hello(liga, boca, intensidade):
    if liga:
        click.secho('Ligando...', fg='green')
        if boca:
            click.echo('boca %s com intensidade %s' % (boca, intensidade))
        else:
            click.secho('Faltou especificar a boca %s' % (boca), fg='red')
    else:
        click.secho('Desligando...', fg='red')
        click.echo('boca %s' % (boca))

if __name__ == '__main__':
    hello()
