# Audeze LCD-XC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 0.5; 22 0.5; 23 0.6; 25 0.7; 26 0.8; 28 0.9; 30 0.9; 32 0.9; 35 0.8; 37 0.8; 40 0.9; 42 1.0; 45 1.0; 49 1.0; 52 0.7; 56 0.0; 59 -0.4; 64 -0.7; 68 -0.8; 73 -1.0; 78 -1.1; 83 -1.3; 89 -1.4; 95 -1.6; 102 -1.7; 109 -1.8; 117 -1.8; 125 -1.9; 134 -2.1; 143 -2.1; 153 -2.1; 164 -2.1; 175 -2.3; 188 -2.3; 201 -2.1; 215 -2.0; 230 -1.7; 246 -1.4; 263 -0.9; 282 -0.6; 301 -0.8; 323 -0.4; 345 0.8; 369 1.2; 395 1.0; 423 1.1; 452 1.2; 484 1.1; 518 1.5; 554 2.0; 593 2.1; 635 2.4; 679 2.5; 726 2.4; 777 1.9; 832 1.4; 890 1.0; 952 0.4; 1019 -0.1; 1090 -0.6; 1167 -1.0; 1248 -1.7; 1336 -2.5; 1429 -3.2; 1529 -3.8; 1636 -4.3; 1751 -4.1; 1873 -3.8; 2004 -3.0; 2145 -1.6; 2295 -0.3; 2455 0.9; 2627 2.2; 2811 2.4; 3008 2.5; 3219 2.8; 3444 1.0; 3685 -1.0; 3943 -1.8; 4219 0.6; 4514 5.0; 4830 5.6; 5168 4.8; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -0.0; 13327 -3.0; 14260 -5.1; 15258 -5.4; 16326 -6.2; 17469 -7.3; 18692 -5.9; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.072548682101091dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-XC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 683 Hz   |  1.91 | 3.1 dB  |
| Peaking | 1704 Hz  |  1.6  | -4.8 dB |
| Peaking | 2732 Hz  |  3.56 | 3.8 dB  |
| Peaking | 5664 Hz  |  2.44 | 6.9 dB  |
| Peaking | 17137 Hz |  1.23 | -7.7 dB |
| Peaking | 39 Hz    |  1.15 | 1.5 dB  |
| Peaking | 161 Hz   |  0.55 | -2.5 dB |
| Peaking | 389 Hz   |  1.65 | 1.8 dB  |
| Peaking | 3929 Hz  | 11.5  | -3.7 dB |
| Peaking | 11973 Hz |  6.37 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audeze%20LCD-XC/Audeze%20LCD-XC.png)