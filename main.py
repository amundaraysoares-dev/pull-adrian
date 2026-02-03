class conta_bancaria:
    def __init__(self, N_cliente,Nu_conta,T_interese,saldo):
        self.__N_cliente = N_cliente
        self.__Nu_conta  = Nu_conta
        self.__T_interese = T_interese
        self.__saldo = saldo

    def get_Ncliente(self):
        return self.__N_cliente
    def get_Nuconta(self):
        return self.__Nu_conta
    def get_Tinterese(self):
        return self.__T_interese
    def get_saldo(self):
        return self.__saldo

    def set_Ncliente(self, nombre):
        self.__N_cliente = nombre

    N_cliente = property(get_Ncliente,set_Ncliente)

    def set_Nuconta(self, numero):
        self.__Nu_conta = numero

    Nu_conta = property(get_Nuconta, set_Nuconta)

    def set_Tinterese(self, interes):
        self.__T_interese = interes

    T_interese = property(get_Tinterese, set_Tinterese)

    def set_saldo(self, dinero):
        self.__saldo = dinero

    saldo = property(get_saldo, set_saldo)

    def SUM_ingreso(self,ingreso):
        self.__saldo += ingreso
        print(f"se ingrso el siguiente saldo {ingreso}")
        print(self.__saldo)
    def Reintegro(self,sacar):
        if sacar >= 0:
            self.__saldo -= sacar
        else:
            print("error valor no valido")

    def transferencia(self, conta_destino, importe):
        self.__saldo -= importe
        conta_destino.SUM_ingreso(importe)
        print(f"Transferencia de {importe} realizada de {self.__N_cliente} a {conta_destino.__N_cliente}.")
        print(f"Novo saldo orixe: {self.__saldo}")
        print(f"Novo saldo destino: {conta_destino.saldo}")
    def cuenta(self):
        print(f"nombre de la cuenta: {self.__N_cliente}")
        print(f"numero de cuenta: {self.__Nu_conta}")
        print(f"intereses: {self.__T_interese}")
        print(f"saldo: {self.__saldo}")
        print("")

conta = conta_bancaria("alan",45,3,5890)
contaDestino = conta_bancaria("aitor",45,6,100)
conta.cuenta()
contaDestino.cuenta()
conta.SUM_ingreso(10)
conta.Reintegro(1)

conta.transferencia(contaDestino, 50)

