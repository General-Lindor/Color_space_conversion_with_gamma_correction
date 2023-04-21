# RGB/HSL Color Space Conversion models with/without gamma correction and Visualization #

 Provides four different models for both-directional RGB/HSL conversion.
 Numbers range from 0 to 1, both for R, G, B, H, S and L.
 
## Models: ##
### Wikipedia ###

This model is driven directly from the conversion formulae you can find on the HSL wikipedia page;
https://en.wikipedia.org/wiki/HSL_and_HSV
It is mathematically incorrect for very few colors, but most of the time it works.
 
### Standard: ###

The standard model.
Fast and easy.
 
### Mathematical: ###

My own model. Trades off computational speed for mathematical correctness and beauty.
Serves as a base for applying gamma correction.
 
### Gamma Correction: ###

Based on the Mathematical model.
Convert from RGB to HSL and from HSL to RGB, both with gamma correction, in a mathematically correct way.
 
### Hybrid: ###

Combines the advantages of mathematical and standard.
Like Standard, Hue is a color hexagon instead of a color wheel.
Lightness and Saturation are calculated exactly the same way as in mathematical.
Basically for the human eye it looks the same as mathematical, but it is much faster.
 
### Hybrid with Gamma Correction: ###

Combines the Hybrid model with Gamma Correction.
  
  
## Scripts: ##

### vectors.py: ###

Base script for multidimensional analysis;
could have been done using numpy which would probably have been faster, but i wanted to do it myself and no dependencies.
  
### interpolateWave.py: ###

Used to figure out a smooth graph for the lightness(hue) relation in Visualization.docx
See https://www.desmos.com/calculator/kaf9f5bdub for more.
    
### test.py: ###

Used to test the four models.
    
### ColorSpaceVisualization.py: ###

Used to create the third column Visualization.docx