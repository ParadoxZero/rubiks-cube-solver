

//=========================== Motor Specs =============================================
int motor[6] = {3,5,6,9,10,11} ; //FURLBD//urfdlb //635 10 11 
int motor_move[6] = {280,300,300,300,300,300};
int motor_move_2[6] = {600,665,650,650,640,640};
int motor_move_c[6] = {1020,1020,1020,1020,995,995};
int spd[2] = {50,50};
//=====================================================================================

#define p(n) Serial.println(n)
#define buffer_time 10000
String data ;

void delay1(int n){
  int k = millis();
  while(millis()-k < n){ ; }
  
}
void setup(){
  Serial.begin(9600);
  //==== Initialize Motor pin =======================
    for(int i=0; i<6 ; ++i)
      pinMode(motor[i],OUTPUT);
    
}

void move_clk(int m){
  
    analogWrite(motor[m],spd[0]);
    p("d1");
    delay1(motor_move[m]);
    p("d2");
    analogWrite(motor[m],0);
    delay1(buffer_time);
  
}

void move_clk_2(int m){
    analogWrite(motor[m],spd[0]);
    p("d1");
    delay1(motor_move_2[m]);
    p("d2");
    analogWrite(motor[m],0);
    delay1(buffer_time);
    p("d3");
}
void move_anti(int m){
    analogWrite(motor[m],spd[0]);
    p("d1");
    delay1(motor_move_c[m]);
    p("d2");
    analogWrite(motor[m],0);
    delay1(buffer_time);
    p("d3");
}
void loop(){
  for(int i=0;i<6;++i)
    analogWrite(motor[i],0);
  while(!Serial.available());
  int i = 0 ;
  data = Serial.readString();
  char buffer ;
  int motor ;
  for(int i=0;data[i]!='\0';++i){
    buffer = data[i];
    i++;
    switch(buffer){
      case 'U' : motor = 0 ;break ;
      case 'R' : motor = 1 ;break ;
      case 'F' : motor = 2 ;break ;
      case 'D' : motor = 3 ;break ;
      case 'L' : motor = 4 ;break ;
      case 'B' : motor = 5 ;break ;
      default : continue ;
    }
    buffer = data[i];
    if(buffer == ' '){
      move_clk(motor); delay1(buffer_time);
      p(motor);
    } else if (buffer == '\''){
      move_anti(motor); delay1(buffer_time);
      p(motor);
      p("c");
      i++;
      continue;
    } else if( buffer == '2'){
        move_clk_2(motor); delay1(buffer_time);
        p(motor);
        p('t');
        i++;
        continue;      
    }
    
  }
}
