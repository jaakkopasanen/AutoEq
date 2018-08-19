# Beyerdynamic DJX-1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.7; 32 5.4; 35 4.9; 37 4.7; 40 4.3; 42 4.1; 45 3.8; 49 3.4; 52 3.2; 56 2.9; 59 2.7; 64 2.5; 68 2.5; 73 2.3; 78 2.0; 83 1.9; 89 2.0; 95 1.7; 102 1.4; 109 1.2; 117 0.9; 125 0.5; 134 0.2; 143 -0.2; 153 -0.4; 164 -0.2; 175 -0.4; 188 -0.8; 201 -1.0; 215 -1.2; 230 -1.2; 246 -1.3; 263 -1.4; 282 -1.2; 301 -1.0; 323 -0.7; 345 -0.4; 369 -0.1; 395 0.1; 423 0.2; 452 0.0; 484 -0.3; 518 -0.8; 554 -1.1; 593 -1.2; 635 -1.4; 679 -1.5; 726 -1.5; 777 -1.3; 832 -1.2; 890 -0.9; 952 -0.3; 1019 -0.2; 1090 -0.8; 1167 -0.6; 1248 -0.4; 1336 -0.4; 1429 -0.3; 1529 -0.2; 1636 -0.4; 1751 -0.1; 1873 0.2; 2004 0.6; 2145 0.9; 2295 1.0; 2455 1.3; 2627 1.9; 2811 2.2; 3008 2.6; 3219 2.7; 3444 2.9; 3685 4.1; 3943 5.7; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.0; 8299 -2.7; 8880 -3.7; 9502 -2.7; 10167 -1.0; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DJX-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 24 Hz   |  0.53 | 6.4 dB  |
| Peaking | 91 Hz   |  1.76 | 1.4 dB  |
| Peaking | 537 Hz  |  0.07 | -1.1 dB |
| Peaking | 5252 Hz |  0.89 | 7.8 dB  |
| Peaking | 8714 Hz |  2.64 | -6.9 dB |
| Peaking | 247 Hz  |  2.32 | -0.7 dB |
| Peaking | 411 Hz  |  2.7  | 1.3 dB  |
| Peaking | 681 Hz  |  3.42 | -0.8 dB |
| Peaking | 6369 Hz | 11.31 | 0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DJX-1/Beyerdynamic%20DJX-1.png)