Projeto de Casa Inteligente da disciplina de Programação Orientada a Objetos (POO)
Aluna: Clariele Almeida

O objetivo desse projeto é criar um sistema de casa inteligente utilizando conceitos de POO, máquina de estados, padrões de projeto e outras funções vistas em sala. 

# Imports

import argparse

from abc import ABC, abstractmethod

from transitions import Machine

from functools import reduce

# Descrição do projeto;

O projeto permite criar 3 tipos de dispositivos, sendo eles: lâmpadas, termostatos e sistemas de segurança. Para utilizar o programa, o usuário deve utilizar o menu para escolher se deseja criar ou utilizar o dispostivo. Caso queira criar, deve informar o tipo de dispositivo, e configurar um limite para a quantidade disipositivos.

# Descrição dos padrões de design utilizados:

Neste projeto, utilizamos o Singleton, Factory e Observer. O primeiro foi utilizado para garantir que apenas uma casa seja instanciada por vez. O Factory permitiu que criássemos uma família de dispositivos sem especificar suas classes concretas. Por fim, o observer foi utilizado para notificar cada vez que surgisse uma alteração no status de um dispostivo.

# Como os usuários podem utilizá-lo;

O usuário deve rodar o arquivo Main para encontrar o menu de opções e criar ou administrar seus dispositivos. O primeiro menu será:

            "Casa Inteligente\n"
            "[1] Criar Dispositivo\n"
            "[2] Administrar Seus Dispositivos\n"
            "[3] Obter Status de Todos os Dispositivos\n"
            "[4] Desligar Todas as Luzes\n"
            "[5] Listar Dispositivos Ligados\n"
            "[6] Contar Dispositivos Ligados\n"
            "[7] Configurar Limite de Dispositivos\n"
            "[8] Sair"

O usuário deverá criar seus dispostivos digitando o número 1. Ao fazer isto, aparecerá o menu com as opções de dispositivos disponíveis.

                "Qual dispositivo você quer criar?\n"
                "[1] Luz\n"
                "[2] Termostato\n"
                "[3] Sistema de Segurança"

Caso escolha a opção "Administrar Seus Dispostivos", ele poderá escolher o dispositvo que quer modificar e depois terá uma lista de opões do que é possível fazer.

                    "Qual a ação desejada?\n"
                    "[1] Ligar a luz\n"
                    "[2] Desligar a luz\n"
                    "[3] Excluir dispositivo"

Caso escolha administrar o termostato, terá as opções:

                    "Qual a ação desejada?\n"
                    "[1] Aquecer ambiente\n"
                    "[2] Resfriar ambiente\n"
                    "[3] Desligar Termostato\n"
                    "[4] Excluir dispositivo"
