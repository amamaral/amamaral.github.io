/* Variáveis globais */
int VoutPin = 9;  // Pino usado como saída analógica
int VoutValue = 0;// Valor (bits) enviado à esta saída
int VoutStep = 5; // Variação (em bits) da tensão aplicada em cada passo da medida
int T = XXX;      // Substituir o valor de T em ms
float Rs = 1000.0;// Resistência (em Ohms) do resistor sensor de corrente
int medida_atual = 1;

/* Configurações iniciais */
void setup(){
  pinMode(VoutPin, OUTPUT); // Configura o pino VoutPin como saída
  pinMode(2, INPUT);        // Configura D2 como entrada (botão)
  Serial.begin(9600);       // Configura comunicação serial a 9600 bits/s
}

/* Configurações iniciais */
void loop(){
  int i, v0, v1;
  float ddp, current;
  // Aguarda até que a tensão no pino D2 seja +5V para iniciar a medida
  if(digitalRead(2)==1){
    Serial.print("--- Início da medida ");
    Serial.println(medida_atual);

    // Cabeçalho do conjunto de dados
    Serial.println("V\tI");

    for(i=0; i<=255; i=i+VoutStep){
      // Ajusta o novo valor da tensão de saída Vout
      analogWrite(VoutPin, i);
      // Aguarda 6*T para que a tensão aplicada se estabilize
      delay(6*T);
      // Mede as tensões em A0 e A1 (valores em bits)
      v0 = analogRead(A0);
      v1 = analogRead(A1);

      // Obtém ddp e corrente sob o DUT
      ddp = (v0-v1)* 5.0 / 1023.0;                  // ddp em Volts
      current = v1 * 5.0 / 1023.0 * (1000.0 / Rs);  // Corrente expressa em mA

      // Envia os dados para o computador: formato V + Tab + I.
      // Valores informados com 3 algarismos após o decimal
      Serial.print(ddp, 3);        // Manda DDP sobre o DUT para o monitor serial
      Serial.print('\t');          // Separa V de I por uma tabulação
      Serial.println(current, 3);  // Corrente em mA
    }
    analogWrite(VoutPin, 0); // Reduz a tensão aplicada a zero
    delay(6*T);

    Serial.print("--- Fim da medida ");
    Serial.println(medida_atual);
    medida_atual++;
  }
}
