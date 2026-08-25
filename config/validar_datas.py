
def validar_datas(data_inicial: str, data_final: str):
    data_comp_inicial = data_inicial.split("-")
    data_comp_final = data_final.split("-")

    if data_comp_inicial[0] > data_comp_final[0]:
        print('data incial incorreta\nErro: Data inicial maior que data final')
    elif data_comp_inicial[0] == data_comp_final[0]:
        if data_comp_inicial[1] > data_comp_final[1]:
            print("Mês da data inicial maior que mês final de comparação")
        elif data_comp_inicial[1] == data_comp_final[1]:
            if data_comp_inicial[2] >= data_comp_final[2]:
                print("Dia da data inicial maior que dia final de comparação")
            else:
                print("Datas válidas")
        else: 
            print("Datas válidas")
    else:
        print("Datas válidas")







