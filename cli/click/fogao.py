import click

@click.command()
@click.option('--liga/--desliga', help="Liga ou desliga", default=True, show_default=True)
@click.option('--boca', 'boca', type=int, help="Numero da boca do fogao a ser ligada. Use 0 para o forno.", required=True)
@click.option('-i','--intensidade',  'intensidade', help="Intensidade do fogo.", default="medio", show_default=True, type=click.Choice(['baixo', 'medio', 'alto']))
def hello(liga, boca, intensidade):
    if liga:
        click.secho('Ligando...', fg='green')
        if boca == 0:
            click.echo('o forno %s com intensidade %s' % (boca, intensidade))
        else:
            click.echo('boca %s com intensidade %s' % (boca, intensidade))
    else:
        click.secho('Desligando...', fg='red')
        click.echo('boca %s' % (boca))

if __name__ == '__main__':
    hello()
