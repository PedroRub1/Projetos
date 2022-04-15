from models.cliente import Cliente
from models.conta import Conta


Roberto: Cliente = Cliente('Roberto', 'Robertp@gmail.com', '123.456.789-01', '02/09/1987')


contaR: Conta = Conta(Roberto)

