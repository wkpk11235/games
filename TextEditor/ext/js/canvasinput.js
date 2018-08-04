canvas=document.getElementById("canvas");
cRect=canvas.getBoundingClientRect();

mouseX=0;
mouseY=0;
mouseV=new vector2(mouseX,mouseY);
isCom=!isMobile();

cl=cRect.left;
ct=cRect.top;

document.addEventListener("mousemove",function(event){
  mouseX=event.clientX-cl;
  mouseY=event.clientY-ct;
  mouseV=new vector2(mouseX,mouseY);
});
function getPos(event){ //for first touch
  if (isCom){
    return new vector2(event.clientX-cl,event.clientY-ct);
  }
  else {
    return new vector2(event.touches[0].clientX-cl,event.touches[0].clientY-ct);
  }
}
