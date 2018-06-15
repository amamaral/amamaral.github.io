# FI577 - Instrumentação eletrônica para a física

Bem vindos a página da disciplina de instrumentação eletrônica para a física. Nesta disciplina iremos explorar vários conceitos de eletrônica analógica importantes para a construção e compreensão do funcionamento de instrumentos científicos utilizados em ciências experimentais. Esta disciplina está focada em aspectos de eletrônica analógica, mas utilizaremos também algumas funcionalidades básicas do [arduino](http://www.arduino.cc) para a construção de protótipos de alguns instrumentos. Existe na internet uma grande variedade de informações sobre como utilizar o arduino, inclusive também um breve minicurso ministrado por mim, e que pode ser acessado [clicando aqui](minicurso_arduino.html).

Nesta página serão colocados todos os informativos relativos à disciplina, slides das aulas, roteiros dos experimentos e os materiais suplementares em auxílio a disciplina.

## Materiais suplementares

1. [Informe inicial](https://www.dropbox.com/s/0opfomssomraefd/informe_inicial.pdf?dl=0)
2. [Códigos de resistores](https://www.dropbox.com/s/7tp49dwx68755qn/resistores.pdf?dl=0)
3. [Códigos de capacitores](https://www.dropbox.com/s/484ycuat1s8cm5d/capacitores.pdf?dl=0)
4. [Osciloscópio](https://www.dropbox.com/s/27jkhdf64go2dct/osciloscopio.pdf?dl=0)
5. Softwares gratuitos:
    * [Fritzing](http://www.fritzing.org) (Esquemas de circuitos e projeto de PCB, voltado para a plataforma arduino)
    * [Multisim BLUE](http://br.mouser.com/MultiSimBlue/) (Simulador de circuitos analógicos e digitais)
    * [Circuit Lab](https://www.circuitlab.com/) (Simulador online de circuitos analógicos)
6. Datasheets:
    * [Transistor BC548](https://www.dropbox.com/s/vjcnxffznf18swq/BC548.pdf?dl=0)
    * [Transistor 2N3904](https://www.dropbox.com/s/4tnwkes5p96ynba/2N3904.pdf?dl=0)
    * [Transistor 2N2222A](https://www.dropbox.com/s/vmpjtxr21xmm7u5/2N2222A.pdf?dl=0)
    * [Regulador de tensão positiva LM78XX](https://www.dropbox.com/s/zvql2lrckchqlvy/LM78XX_Positive_Voltage_Regulator.pdf?dl=0)
    * [Regulador de tensão negativa LM79XX](https://www.dropbox.com/s/g34gdrr6cyjczu1/LM79XX_Negative_Voltage_Regulator.pdf?dl=0)
    * [Amplificador Operacional LM741](https://www.dropbox.com/s/5p0oyrvw2b4d112/LM741.pdf?dl=0)
    * [Amplificador Operacional TL071](https://www.dropbox.com/s/yl4hxtseboq2eg6/TL071.pdf?dl=0)
    * [Amplificador Operacional LM324](https://www.dropbox.com/s/374crsunvmv5az1/LM324.pdf?dl=0)


## Slides das aulas

| #  | Tópico                              | slides                          | Roteiros das práticas                        |
|----|-------------------------------------|---------------------------------|----------------------------------------------|
| 01 | Visão geral sobre instrumentação    | [html][s01-html] [pdf][s01-pdf] |                                              |
| 02 | Eletromagnetismo básico             | [html][s02-html] [pdf][s02-pdf] |                                              |
| 03 | Abstração de circuitos eletrônicos  | [html][s03-html] [pdf][s03-pdf] |                                              |
| 04 | Análise de circuitos lineares       | [html][s04-html] [pdf][s04-pdf] | [Prática 01][p01-pdf]                        |
| 05 | Arduino e algumas ferramentas CAD   | [html][s05-html] [pdf][s05-pdf] |                                              |
| 06 | Sinais analógicos                   | [html][s06-html] [pdf][s06-pdf] | [Prática 02][p02-pdf]                        |
| 07 | Filtros passivos                    | [html][s07-html] [pdf][s07-pdf] | [Prática 03][p03-pdf], [Prática 04][p04-pdf] |
| 08 | Diodos e circuitos não lineares     | [html][s08-html] [pdf][s08-pdf] | [Prática 05][p05-pdf]                        |
| 09 | Transistores                        | [html][s09-html] [pdf][s09-pdf] | [Prática 06][p06-pdf]                        |
| 10 | Amplificador diferencial            | [html][s10-html] [pdf][s10-pdf] | [Prática 07][p07-pdf]                        |
| 11 | Amplificador operacional            | [html][s11-html] [pdf][s11-pdf] | [Prática 08][p08-pdf]                        |
| 12 | Filtros ativos                      |                                 | Prática 09                                   |
| 13 | Oscilador e defasador               |                                 | Prática 10                                   |
| 14 | Computador analógico                |                                 | Prática 11                                   |
| 15 | Portas lógicas e eletrônica digital |                                 | Prática 12                                   |

[s01-html]: instrumentacao_fisica/capitulo_1.html
[s01-pdf]: https://www.dropbox.com/s/tumckbsmkx06uwn/capitulo_1.pdf?dl=0
[s02-html]: instrumentacao_fisica/capitulo_2.html
[s02-pdf]: https://www.dropbox.com/s/c8ir438wg78tosy/capitulo_2.pdf?dl=0
[s03-html]: instrumentacao_fisica/capitulo_3.html
[s03-pdf]: https://www.dropbox.com/s/dqiccx40wuluv6k/capitulo_3.pdf?dl=0
[s04-html]: instrumentacao_fisica/capitulo_4.html
[s04-pdf]: https://www.dropbox.com/s/ya5svg2ek802l35/capitulo_4.pdf?dl=0
[s05-html]: instrumentacao_fisica/capitulo_5.html
[s05-pdf]: https://www.dropbox.com/s/aw6rady7hzqwet8/capitulo_5.pdf?dl=0
[s06-html]: instrumentacao_fisica/capitulo_6.html
[s06-pdf]: #
[s07-html]: instrumentacao_fisica/capitulo_7.html
[s07-pdf]: #
[s08-html]: instrumentacao_fisica/capitulo_8.html
[s08-pdf]: #
[s09-html]: instrumentacao_fisica/capitulo_9.html
[s09-pdf]: #
[s10-html]: instrumentacao_fisica/capitulo_10.html
[s10-pdf]: #
[s11-html]: instrumentacao_fisica/capitulo_11.html
[s11-pdf]: #


[p01-pdf]: https://www.dropbox.com/s/3pfmhemipys4nqh/pratica_1.pdf?dl=0
[p02-pdf]: https://www.dropbox.com/s/3gx5mcg7ue63gy4/pratica_2.pdf?dl=0
[p03-pdf]: https://www.dropbox.com/s/37q855js78buat4/pratica_3.pdf?dl=0
[p04-pdf]: https://www.dropbox.com/s/mjqeild4rv878e4/pratica_4.pdf?dl=0
[p05-pdf]: https://www.dropbox.com/s/s6yb17m8byqmz82/pratica_5.pdf?dl=0
[p06-pdf]: https://www.dropbox.com/s/pm5p5ebb0za3a43/pratica_6.pdf?dl=0
[p07-pdf]: https://www.dropbox.com/s/4kiy9holsay9fwu/pratica_7.pdf?dl=0
[p08-pdf]: https://www.dropbox.com/s/ymzvgd0wem9bv3r/pratica_8.pdf?dl=0
