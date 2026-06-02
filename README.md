# GlobalS_Python

--> Integrantes do Grupo 

    João Victor Pereira Gimenes - 571662
    Juan Duarte - 570331
    Julio Cesar da Silva Cocco - 569463
    Rafael Boletini de Oliveira - 570219
    Victor Rossi Sales Zanandre - 573844

Hoje existem mais de 30 mil pedaços de lixo orbital catalogados girando ao redor da Terra a 28 mil km/h. Parafusos, restos de foguete, satélites mortos, fragmentos de colisões antigas. Cada nova colisão gera milhares de fragmentos novos — é o efeito Kessler, conceito real e citável: se a órbita baixa entrar em cascata, a humanidade perde GPS, internet por satélite, comunicação e previsão do tempo.
O OrbitWatch é uma plataforma de monitoramento que rastreia esses detritos, cruza com a órbita de satélites ativos (Starlink, ISS, satélites brasileiros como o Amazônia-1) e alerta operadoras quando o risco de colisão passa de um limite. O operador recebe a alerta antes do impacto e pode comandar manobra evasiva.
Como funciona (fluxo geral)

Sistema recebe dados de detritos (catálogo da NASA/Space-Track — mockados pra simulação)
Calcula posição orbital de cada objeto usando trigonometria
Compara distância entre detritos e satélites ativos
Quando distância < limite seguro → dispara alerta com nível de risco
Operador vê no dashboard, decide ação

Público-alvo
Operadoras de satélite, agências espaciais (NASA, ESA, AEB brasileira), e indiretamente toda infraestrutura global que depende de órbita baixa.
ODS - 9 (infraestrutura e inovação) como principal, 13 (sustentabilidade orbital) como complemento.