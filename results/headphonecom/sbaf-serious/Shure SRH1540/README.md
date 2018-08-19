# Shure SRH1540

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.9dB
GraphicEQ: 10 -84; 20 -3.4; 22 -4.1; 23 -4.4; 25 -4.9; 26 -5.2; 28 -5.6; 30 -5.9; 32 -6.2; 35 -6.6; 37 -6.8; 40 -7.1; 42 -7.3; 45 -7.5; 49 -7.6; 52 -7.7; 56 -7.8; 59 -7.8; 64 -7.7; 68 -7.6; 73 -7.3; 78 -7.0; 83 -6.6; 89 -6.2; 95 -6.0; 102 -5.9; 109 -5.9; 117 -5.9; 125 -5.8; 134 -5.5; 143 -5.1; 153 -4.4; 164 -3.1; 175 -3.3; 188 -3.7; 201 -3.5; 215 -3.7; 230 -3.9; 246 -4.1; 263 -4.1; 282 -4.2; 301 -4.4; 323 -4.5; 345 -4.4; 369 -4.1; 395 -3.8; 423 -3.3; 452 -2.9; 484 -2.5; 518 -2.2; 554 -1.9; 593 -1.5; 635 -1.0; 679 -0.6; 726 -0.4; 777 -0.0; 832 0.1; 890 0.1; 952 0.2; 1019 -0.0; 1090 -0.1; 1167 0.3; 1248 0.3; 1336 -0.1; 1429 -0.8; 1529 -1.5; 1636 -2.3; 1751 -2.8; 1873 -3.3; 2004 -3.3; 2145 -2.7; 2295 -2.3; 2455 -1.8; 2627 -0.9; 2811 -0.3; 3008 0.2; 3219 -0.2; 3444 0.1; 3685 0.2; 3943 -0.6; 4219 -1.0; 4514 -1.0; 4830 -0.5; 5168 0.6; 5530 0.3; 5917 -2.5; 6331 -2.8; 6775 -1.3; 7249 -0.7; 7756 -0.6; 8299 -1.8; 8880 -3.7; 9502 -4.7; 10167 -2.8; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.0; 18692 -1.6; 20000 -4.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.9420331875402671dB` and instead set Global volume in the UI for both channels to **-9**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1540 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.59 | -5.3 dB |
| Peaking | 90 Hz   | 0.58 | -3.9 dB |
| Peaking | 339 Hz  | 1.28 | -3.5 dB |
| Peaking | 9305 Hz | 4.04 | -4.8 dB |
| Peaking | 1284 Hz | 1.17 | 1.8 dB  |
| Peaking | 1894 Hz | 1.64 | -4.2 dB |
| Peaking | 2992 Hz | 3.27 | 1.1 dB  |
| Peaking | 6216 Hz | 9.92 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH1540/Shure%20SRH1540.png)