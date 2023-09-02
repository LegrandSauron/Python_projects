"""Exemplo 4.5"""

"""Momento de inercia da seção"""

"""mm"""
class flexao():
	def __init__(self,forca:float, dimensoes:list, ponto_atuacao:float):
		self.forca =forca
		self.dimensoes= dimensoes
		self.ponto_atuacao=ponto_atuacao
		
	def momento_de_inercia_I(self):
		i=(1/12)*(self.dimensoes[1]*self.dimensoes[0]**3)- (1/12)*((self.dimensoes[1]-self.dimensoes[3])*(self.dimensoes[0]-2*self.dimensoes[2])**3)
		return i
	

	def momento(self):
		m=self.forca*self.momento_de_inercia_I()/self.ponto_atuacao
		return m
	
		
	
	def tensao(self):
		pass
	






if __name__== "__main__":
	a=flexao(forca=345000000,dimensoes=[0.4,0.3,0.025,0.02],ponto_atuacao=0.2)      
        
	

