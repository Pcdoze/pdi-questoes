import argparse

class settings:
    def __init__(self):
        self.ALTERNATIVAS = [
            'A',
            'B',
            'C',
            'D',
            'E'
        ]
        self.IMAGEM: str = None
        self.CORRETA: str = None
        
        parser = argparse.ArgumentParser()
    
        parser.add_argument('-i', '--imagem', required=True,
                            help='sum the integers (default: find the max)')
        parser.add_argument('-c', '--correta', required=True,
                            help='sum the integers (default: find the max)')
        
        args = vars(parser.parse_args())
        
        self.IMAGEM = args['imagem']
        self.CORRETA = args['correta']
