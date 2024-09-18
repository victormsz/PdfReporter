import threading as thr
import random as rnd
import time
# uma corrida entre alguns participantes de thread, onde cada um tem 50% de chance de ganhar cada iteracao

class corredor(thr.Thread):
    def __init__(self, nome,velocidade,poder,competidores):
        thr.Thread.__init__(self)
        self.nome = nome
        self.velocidade = velocidade
        self.poder = poder
        self.vitorias = 0
        self.trajeto = 0
        self.competidores = competidores
        self.acelerando = 5


    def azar(self):
        if(rnd.randrange(0,100)>=90): # pega um n aleatorio
                perdeu = rnd.randrange(8,12) - self.poder
                self.trajeto -= perdeu # perde 50 se tiver o azar
                print(f'{self.nome} perdeu {perdeu}m')
    def jogar_bomba(self):
        if rnd.randrange(0, 100) < 10:  # 5% de chance de jogar bomba
            alvo = rnd.choice([c for c in self.competidores if c != self])
            ataque = self.poder + rnd.randrange(1,5)
            alvo.trajeto -= ataque
            alvo.acelerando = 0
            if alvo.trajeto < 0:
                alvo.trajeto = 0
            print(f'{self.nome} jogou uma bomba em {alvo.nome} (ele perdeu {ataque}m)!')
    def boost(self):
        if rnd.randrange(0, 100) < 10:
            turbo = 5 + self.velocidade
            self.trajeto += turbo
            self.acelerando = 5
            print(f'{self.nome} usou um boost e ganhou {turbo}m!')




    def run(self):
        global vencedor
        self.trajeto = 0
        while vencedor == None:
            self.azar()
            self.jogar_bomba()
            self.boost()
            if self.acelerando <5:
                self.acelerando += 1
            else:   
                self.trajeto += self.velocidade + rnd.randrange(-2, 2)
                time.sleep(0.5)
                print(f'{self.trajeto} {self.nome}')
                if self.trajeto >= fim:
                    vencedor = self.nome
                    time.sleep(0.1)
                    print(f'Vencedor: {vencedor}')
                    break
vencedor = None

fim = 500
c1 = corredor('Mario',5,7,[])
c2 = corredor('Luigi',6,6,[])
c3 = corredor('Toad',7,5,[])
c1.competidores = [c2,c3]
c2.competidores = [c1,c3]
c3.competidores = [c1,c2]
c1.start()
c2.start()
c3.start()