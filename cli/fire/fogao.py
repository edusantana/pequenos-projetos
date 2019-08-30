import fire

def liga(boca="1", intensidade="baixa"):
  """A canvas with which to make binary art, one bit at a time."""
  return "Ligando boca %s %s!" % (boca, intensidade)

def desliga(boca="1", intensidade="baixa"):
  return "Ligando boca %s %s!" % (boca, intensidade)


if __name__ == '__main__':
  fire.Fire({
      'liga': liga,
      'desliga': desliga,
  })
