# Shure SE215

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 10 -84; 20 -4.1; 22 -4.1; 23 -4.1; 25 -4.2; 26 -4.2; 28 -4.2; 30 -4.3; 32 -4.3; 35 -4.4; 37 -4.4; 40 -4.5; 42 -4.6; 45 -4.7; 49 -4.8; 52 -5.0; 56 -5.1; 59 -5.2; 64 -5.4; 68 -5.6; 73 -5.7; 78 -6.0; 83 -6.1; 89 -6.4; 95 -6.5; 102 -6.7; 109 -6.7; 117 -6.7; 125 -6.8; 134 -6.8; 143 -6.8; 153 -6.8; 164 -6.7; 175 -6.6; 188 -6.5; 201 -6.3; 215 -6.0; 230 -5.7; 246 -5.5; 263 -5.2; 282 -4.8; 301 -4.5; 323 -4.2; 345 -3.7; 369 -3.4; 395 -3.0; 423 -2.5; 452 -2.1; 484 -1.8; 518 -1.5; 554 -1.0; 593 -0.4; 635 -0.1; 679 0.0; 726 0.3; 777 0.6; 832 0.6; 890 0.5; 952 0.3; 1019 -0.0; 1090 -0.2; 1167 -0.3; 1248 -0.7; 1336 -1.5; 1429 -2.3; 1529 -2.9; 1636 -3.6; 1751 -4.1; 1873 -4.4; 2004 -4.7; 2145 -4.9; 2295 -4.6; 2455 -3.5; 2627 -2.0; 2811 -0.2; 3008 2.1; 3219 3.6; 3444 4.4; 3685 3.9; 3943 2.1; 4219 -1.4; 4514 -5.6; 4830 -7.9; 5168 -4.2; 5530 0.6; 5917 3.7; 6331 5.1; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.2636354094547055dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.7dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 48 Hz   | 0.27 | -4.4 dB  |
| Peaking | 178 Hz  | 0.69 | -4.5 dB  |
| Peaking | 2211 Hz | 1.53 | -10.4 dB |
| Peaking | 3538 Hz | 0.78 | 8.8 dB   |
| Peaking | 4701 Hz | 4.9  | -14.4 dB |
| Peaking | 807 Hz  | 2.29 | 1.5 dB   |
| Peaking | 1561 Hz | 5.14 | -1.3 dB  |
| Peaking | 5182 Hz | 9.46 | -3.0 dB  |
| Peaking | 6394 Hz | 3.01 | 5.6 dB   |
| Peaking | 7587 Hz | 1.64 | -3.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE215/Shure%20SE215.png)