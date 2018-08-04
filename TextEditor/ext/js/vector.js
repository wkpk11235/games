class vector2 {
  constructor(x,y) {
    this.x=x;
    this.y=y;
    //for readability
  }
  multiply_num(toX){return new vector2(this.x*toX,this.y*toX);}
  multiply_vect(toX){return this.x*toX.y-this.y*toX.x;}
  add_num(toP){return new vector2(this.x+toP,this.y+toP);}
  add_vect(toP){return new vector2(this.x+toP.x,this.y+toP.y);}
  subtract_num(toM){return new vector2(this.m-toM,this.y-toM);}
  subtract_vect(toM){return new vector2(this.x-toM.x,this.y-toM.y);}
  divide(toD){return new vector2(this.x/toD,this.y/toD);}
  self_multiply_num(toX){this.x*=toX;this.y*=toX;}
  self_multiply_vect(toX){this.x=this.x*toX.y-this.y*toX.x;this.y=0;}
  self_add_num(toP){this.x+=toP;this.y+=toP;}
  self_add_vect(toP){this.x+=toP.x;this.y+=toP.y;}
  self_subtract_num(toM){this.x-=toM;this.y-=toM;}
  self_subtract_num(toM){this.x-=toM.x;this.y-=toM.y;}
  self_divide(toD){this.x/=toD;this.y/=toD;}
  equals(vect){return this.x==vect.x&&this.y==vect.y;}
  copy(){return new vector2(this.x,this.y);}
  len(){return Math.sqrt(Math.pow(this.x,2)+Math.pow(this.y,2));}
  normalized(n=1,pivot=nullVect){
    var tempv=new vector2(this.x-pivot.x,this.y-pivot.y);
    tempv.self_multiply_num(n/tempv.len());
    tempv.x+=pivot.x;
    tempv.y+=pivot.y;
    return tempv;
  }
  self_normalized(n=1,pivot=nullVect){
    this.x-=pivot.x;
    this.y-=pivot.y;
    var len=n/this.len();
    this.x*=len;
    this.y*=len;
    this.x+=pivot.x;
    this.y+=pivot.y;
  }
}
nullVect=new vector2(0,0);

function distance(v1,v2){return Math.sqrt(Math.pow(v1.x-v2.x,2)+Math.pow(v1.y-v2.y,2))}
function rad2deg(r){return r*180/Math.PI;}
function deg2rad(d){return r*Math.PI/180;}


function line2circle(v1,v2,r,pivot=nullVect){
  //maps the line v1->v2 to a circle with radius r
  var theta=Math.atan2(v1.y-startPoint.y,v1.x-startPoint.x);
  return new vector2(Math.cos(theta),Math.sin(theta)).multiply_num(r).add_vect(pivot);
}
