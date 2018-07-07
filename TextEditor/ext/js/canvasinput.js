canvas=document.getElementById("canvas");
cRect=canvas.getBoundingClientRect();

mouseX=0;
mouseY=0;

isCom=!isMobile();

document.addEventListener("mousemove",function(event){
  mouseX=event.clientX-cRect.left;
  mouseY=event.clientY-cRect.top;
});
function getPos(event){ //for first touch
  if (isCom){
    return new vector2(event.clientX-cRect.left,event.clientY-cRect.top);
  }
  else {
    return new vector2(event.touches[0].clientX-cRect.left,event.touches[0].clientY-cRect.top);
  }
}
