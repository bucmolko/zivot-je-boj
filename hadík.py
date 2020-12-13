  # -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 11:15:09 2020

@author: elekk
"""
 <title> hadíček <title>
 
 <canvas width= "600" height="600"></canvas>
 
 <style>
 body 
    background:#eecdcf;
    text - allign: center;
    
canvas{
  border : 10px solid #1bf8b0;
  <script>
// listeners 
document.addEventListener
  
// canvas 

  const canvas = document.querySelector('canvas')
  
  const ctx= canvas .getContext ('2d') 
  
  
// player 

  const snakeSize=50;
  
  let snakeSpeed= 5;
  let snake PosX=0
  let snake PosY=canvas.height/2-snakeSize/2
  
  snakePosX= snakePosX + 4;
  
  // loop 
  function gameloop ( ) { 
  drawStuff() ;
  moveStuff() ;
  requestAnimationFrame (gameloop);
  gameLoop () ;
  
   /**
  *  MOVE EVERYTHING 
  */
  function moveStuff() { 
  snakePosX+= snakeSpeed
   
   if ( snakePosX>canvas.width) }
   snakePosX=0;
  /**
  * DRAW EVERYTHING 
  */
  function drawStuff
  rectangle ("white",0,0,,canvas.width canvas.height) 
  
  rectangle ("black",snake PosX,snake PosY ,snakeSize,snakeSize) 
  
  
  
  // draw rectangle 
  
  
  /**
  * KEYBOARD 
  */
   function keyPush(event) { 
    switch (event.key) ;
    case "ArrowLeft " :
    snakePosX-= snakeSpeed ;
     case "ArrowUp " 
    snakePosY-= snakeSpeed ;
    case "ArrowRight " 
    snakePosX+= snakeSpeed ;
  case "ArrowDown " 
    snakePosY+= snakeSpeed ;
      
 

 

