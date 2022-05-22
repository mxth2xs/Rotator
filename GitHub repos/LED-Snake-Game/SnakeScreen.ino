
#include <avr/pgmspace.h>
#include <Adafruit_GFX.h>   // Core graphics library
#include <RGBmatrixPanel.h> // Hardware-specific library

#define CLK 8  // MUST be on PORTB!
#define LAT A3
#define OE  9
#define A   A0
#define B   A1
#define C   A2
// Last parameter = 'true' enables double-buffering, for flicker-free,
// buttery smooth animation.  Note that NOTHING WILL SHOW ON THE DISPLAY
// until the first call to swapBuffers().  This is normal.
RGBmatrixPanel matrix(A, B, C, CLK, LAT, OE, false);



// <-O-> the values after "matrix.Color333" represent the RGB values with 7 being the brightest value for that particular colour

char serialData;


void setup() 
{ 
  matrix.begin();
  matrix.drawPixel(0, 0, matrix.Color333(7, 7, 7));  
  Serial.begin(115200);
  delay(1000);
}





void loop() {
  /*
  if(Serial.available() > 0) {
    serialData = Serial.read();
    if (serialData == ('1')){
      matrix.fillScreen(matrix.Color333(7,7,7));
    }
    else if (serialData == ('2')) {
      matrix.fillScreen(matrix.Color333(7,0,0));
    }
    
    
  }
  */
  if(Serial.read() == ('M')){
    matrix.fillScreen(matrix.Color333(0,0,0));

    int xfood = Serial.parseInt();
    int yfood = Serial.parseInt();

    matrix.drawPixel(xfood, yfood, matrix.Color333(7,7,0));
    
    int nextVal = Serial.parseInt();
    int xval;
    int yval;
    while (nextVal != -99) {
      xval = nextVal;
      yval = Serial.parseInt();
      matrix.drawPixel(xval,yval, matrix.Color333(0,7,0));
      nextVal = Serial.parseInt();
    }
    
  }
}
