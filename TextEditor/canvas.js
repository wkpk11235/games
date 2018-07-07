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

function drawLine(x1,y1,x2,y2){
  screen.beginPath();
  screen.moveTo(x1,y1);
  screen.lineTo(x2,y2);
  screen.stroke();
}

function drawLines(linez){
  screen.beginPath();
  var l=linez.length;
  var t;
  for (i=0;i<l;++i){
    t=linez[i];
    screen.moveTo(t[0],t[1]);
    screen.lineTo(t[2],t[3]);
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
    //vect2.self_normalized(radius,pivotV);
    vect2.self_normalized(radius,startPoint);

    lines.push([startPoint.x,startPoint.y,vect2.x,vect2.y]);
  }
  start=!start;
}

function drawPrototype(){
  if (!start&&isCom){drawLine(startPoint.x,startPoint.y,mouseX,mouseY);}
}


function main(){
  screen.clearRect(0,0,cw,ch);
  drawCircle(400,400,radius);
  drawLines(lines);
  drawPrototype()
  //handlePlayer();
}

setInterval(main,1);
