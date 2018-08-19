# Shure SE530

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.9; 22 2.8; 23 2.8; 25 2.7; 26 2.7; 28 2.6; 30 2.5; 32 2.4; 35 2.3; 37 2.2; 40 2.1; 42 2.0; 45 1.8; 49 1.7; 52 1.5; 56 1.2; 59 1.0; 64 0.7; 68 0.5; 73 0.3; 78 -0.0; 83 -0.4; 89 -0.6; 95 -0.8; 102 -1.0; 109 -1.2; 117 -1.3; 125 -1.6; 134 -1.8; 143 -2.0; 153 -2.1; 164 -2.3; 175 -2.4; 188 -2.5; 201 -2.5; 215 -2.6; 230 -2.6; 246 -2.6; 263 -2.6; 282 -2.6; 301 -2.3; 323 -2.2; 345 -2.1; 369 -1.8; 395 -1.6; 423 -1.6; 452 -1.5; 484 -1.5; 518 -1.2; 554 -1.0; 593 -0.7; 635 -0.4; 679 -0.2; 726 0.1; 777 0.2; 832 0.3; 890 0.3; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.4; 1248 -0.6; 1336 -0.9; 1429 -1.4; 1529 -1.9; 1636 -2.3; 1751 -2.7; 1873 -2.9; 2004 -3.1; 2145 -2.9; 2295 -2.1; 2455 -0.9; 2627 0.3; 2811 1.5; 3008 2.6; 3219 3.8; 3444 4.9; 3685 5.6; 3943 5.4; 4219 4.6; 4514 4.0; 4830 4.4; 5168 5.5; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.088006189830304dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE530 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.56 | 2.9 dB  |
| Peaking | 206 Hz  | 0.67 | -2.8 dB |
| Peaking | 2012 Hz | 2.11 | -4.1 dB |
| Peaking | 3657 Hz | 2.03 | 5.6 dB  |
| Peaking | 5814 Hz | 3.26 | 5.7 dB  |
| Peaking | 495 Hz  | 1.73 | -0.6 dB |
| Peaking | 798 Hz  | 1.52 | 0.9 dB  |
| Peaking | 1508 Hz | 5.1  | -0.6 dB |
| Peaking | 6587 Hz | 8.48 | 1.9 dB  |
| Peaking | 7789 Hz | 2.42 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE530/Shure%20SE530.png)