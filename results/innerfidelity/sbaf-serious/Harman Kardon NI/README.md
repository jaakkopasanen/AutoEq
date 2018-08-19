# Harman Kardon NI

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 10 -84; 20 -8.2; 22 -8.3; 23 -8.3; 25 -8.3; 26 -8.3; 28 -8.3; 30 -8.2; 32 -8.2; 35 -8.1; 37 -8.0; 40 -7.9; 42 -7.9; 45 -7.8; 49 -7.7; 52 -7.6; 56 -7.5; 59 -7.5; 64 -7.4; 68 -7.4; 73 -7.3; 78 -7.3; 83 -7.3; 89 -7.2; 95 -7.1; 102 -7.0; 109 -6.8; 117 -6.6; 125 -6.5; 134 -6.3; 143 -6.2; 153 -5.9; 164 -5.7; 175 -5.4; 188 -5.0; 201 -4.8; 215 -4.4; 230 -4.1; 246 -3.8; 263 -3.5; 282 -3.1; 301 -2.8; 323 -2.4; 345 -2.0; 369 -1.7; 395 -1.4; 423 -1.0; 452 -0.7; 484 -0.6; 518 -0.4; 554 -0.0; 593 0.4; 635 0.5; 679 0.4; 726 0.4; 777 0.5; 832 0.5; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.2; 1336 -1.9; 1429 -2.6; 1529 -3.3; 1636 -4.0; 1751 -4.7; 1873 -5.3; 2004 -5.9; 2145 -6.8; 2295 -8.0; 2455 -9.1; 2627 -9.5; 2811 -8.4; 3008 -5.5; 3219 -3.0; 3444 -1.1; 3685 -0.6; 3943 -1.3; 4219 -3.6; 4514 -6.3; 4830 -9.5; 5168 -11.7; 5530 -8.1; 5917 -2.2; 6331 1.1; 6775 3.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.6; 17469 -0.1; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.284755229735331dB` and instead set Global volume in the UI for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Harman Kardon NI ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.8dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.1  | -8.1 dB  |
| Peaking | 622 Hz  | 1.1  | 1.9 dB   |
| Peaking | 2386 Hz | 1.96 | -9.1 dB  |
| Peaking | 5159 Hz | 4.99 | -12.7 dB |
| Peaking | 6622 Hz | 3.85 | 4.8 dB   |
| Peaking | 1720 Hz | 2.2  | -3.5 dB  |
| Peaking | 2116 Hz | 1.24 | 3.1 dB   |
| Peaking | 2752 Hz | 4.73 | -4.1 dB  |
| Peaking | 3656 Hz | 3.6  | 2.9 dB   |
| Peaking | 4527 Hz | 4.96 | -2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Harman%20Kardon%20NI/Harman%20Kardon%20NI.png)