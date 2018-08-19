# Denon AH-NC732K

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.7dB
GraphicEQ: 10 -84; 20 6.6; 22 5.6; 23 5.3; 25 4.7; 26 4.5; 28 4.2; 30 3.9; 32 3.7; 35 3.3; 37 3.1; 40 3.2; 42 3.4; 45 3.6; 49 3.7; 52 3.9; 56 4.2; 59 4.3; 64 4.6; 68 4.7; 73 4.7; 78 4.6; 83 4.5; 89 4.6; 95 4.6; 102 4.8; 109 4.8; 117 4.9; 125 5.0; 134 5.1; 143 5.2; 153 5.5; 164 5.5; 175 5.3; 188 5.4; 201 5.4; 215 5.4; 230 5.4; 246 5.4; 263 5.6; 282 5.6; 301 5.6; 323 5.5; 345 5.5; 369 5.4; 395 5.3; 423 5.2; 452 5.1; 484 4.8; 518 4.5; 554 4.3; 593 4.0; 635 3.7; 679 3.6; 726 3.6; 777 3.4; 832 2.7; 890 1.6; 952 0.5; 1019 -0.1; 1090 -0.5; 1167 -1.1; 1248 -2.3; 1336 -3.4; 1429 -3.8; 1529 -0.7; 1636 0.3; 1751 -0.6; 1873 2.0; 2004 4.7; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.1; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.699489629957844dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-NC732K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.49 | 5.5 dB  |
| Peaking | 90 Hz   | 0.37 | 3.9 dB  |
| Peaking | 394 Hz  | 0.5  | 4.0 dB  |
| Peaking | 1376 Hz | 1.95 | -7.7 dB |
| Peaking | 3123 Hz | 0.64 | 7.1 dB  |
| Peaking | 19 Hz   | 0.97 | -0.5 dB |
| Peaking | 2155 Hz | 5.86 | 2.4 dB  |
| Peaking | 3266 Hz | 0.85 | -1.0 dB |
| Peaking | 6225 Hz | 1.81 | 5.7 dB  |
| Peaking | 7426 Hz | 1.4  | -4.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-NC732K/Denon%20AH-NC732K.png)