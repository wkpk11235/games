//region initialization
canvas=document.getElementById("canvas");
screen=canvas.getContext("2d");
cRect = canvas.getBoundingClientRect();

if (isCom){canvas.addEventListener("mousedown",function(event){rawInput(getPos(event));});}
else {canvas.addEventListener("touchstart",function(event){rawInput(getPos(event));});}

//Date.now() //miliseconds since epoch

cw=canvas.width;
ch=canvas.height;

screen.lineWidth=3;
screen.strokeStyle="black";

function drawCircle(x,y,r){
  screen.beginPath();
  screen.arc(x,y,r,0,2*Math.PI,false);
  screen.stroke();
}

function drawLine(v1,v2){
  screen.beginPath();
  screen.moveTo(v1.x,v1.y);
  screen.lineTo(v2.x,v2.y);
  screen.stroke();
}

function drawLines(linez){
  screen.beginPath();
  var l=linez.length;
  var t;
  for (i=0;i<l;++i){
    t=linez[i];
    screen.moveTo(t[0].x,t[0].y);
    screen.lineTo(t[1].x,t[1].y);
  }
  screen.stroke();
}
//endregion

radius=300;

pivotV=new vector2(400,400);

start=true;
startPoint=null;
lines=[];

function rawInput(vect2){
  if (start){
    startPoint=vect2.normalized(radius,pivotV);
  }
  else {
    var end=line2circle(mouseV,startPoint,radius,pivotV);
    lines.push([startPoint,end]);
  }
  start=!start;
}

function drawPrototype(){
  if (!start&&isCom){
    var end=line2circle(mouseV,startPoint,radius,pivotV);
    drawLine(startPoint,end);
  }
}

function str(s){return String(s);}

function main(){
  screen.clearRect(0,0,cw,ch);
  drawCircle(400,400,radius);
  drawLines(lines);
  drawPrototype()
  //handlePlayer();
}

setInterval(main,1);
