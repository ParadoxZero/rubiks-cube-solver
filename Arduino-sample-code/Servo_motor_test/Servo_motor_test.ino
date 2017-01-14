//==========Motor ========

int m1 = 3 ;
int m2 = 5 ;
int m3 = 6 ;
int m4 = 9 ;
int m5 = 10;
int m6 = 11;

void setup(){
  Serial.begin(9600);
}
int sp[2] = {50,245} ;
void loop(){
  if(Serial.available()){
    String data = Serial.readString();
    int a, b = 0 ;
    a = data[0] - '0' ;
    int d = data[1] - '0' ;
    for(int i=2;data[i]!='\0';++i){
      if(data[i] >= '0' && data[i] <= '9')
      b = 10*b + data[i] - '0' ;
    }
    Serial.print(b);
    switch(a){
      case 0 : analogWrite(m1,sp[d]);
               delay(b);
               analogWrite(m1,0); break;
      case 1 : analogWrite(m2,sp[d]);
               delay(b);
               analogWrite(m2,0);break;
      case 2 : analogWrite(m3,sp[d]);
               delay(b);
               analogWrite(m3,0);break;
      case 3 : analogWrite(m4,sp[d]);
               delay(b);
               analogWrite(m4,0);break;
      case 4 : analogWrite(m5,sp[d]);
               delay(b);
               analogWrite(m5,0);break;
      case 5 : analogWrite(m6,sp[d]);
               delay(b);
               analogWrite(m6,0);
    }
  }
}
