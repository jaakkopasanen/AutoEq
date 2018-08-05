# Denon AH-D1100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -3.6; 22 -4.5; 23 -4.9; 25 -5.5; 26 -5.8; 28 -6.2; 30 -6.6; 32 -6.9; 35 -7.5; 37 -7.8; 40 -8.2; 42 -8.4; 45 -8.7; 49 -9.1; 52 -9.3; 56 -9.5; 59 -9.7; 64 -9.9; 68 -10.0; 73 -10.1; 78 -10.3; 83 -10.4; 89 -10.6; 95 -10.7; 102 -10.7; 109 -10.7; 117 -10.6; 125 -11.1; 134 -11.6; 143 -11.7; 153 -12.1; 164 -11.6; 175 -10.3; 188 -11.1; 201 -11.5; 215 -11.6; 230 -11.1; 246 -10.5; 263 -9.8; 282 -8.5; 301 -7.2; 323 -5.5; 345 -3.7; 369 -2.0; 395 -0.0; 423 1.9; 452 2.7; 484 2.8; 518 2.3; 554 1.7; 593 0.9; 635 0.2; 679 -0.5; 726 -0.8; 777 -0.8; 832 -0.9; 890 -0.6; 952 -0.3; 1019 0.1; 1090 0.6; 1167 0.9; 1248 1.2; 1336 1.2; 1429 0.9; 1529 0.4; 1636 0.2; 1751 0.2; 1873 0.2; 2004 0.0; 2145 -2.1; 2295 -2.5; 2455 -2.0; 2627 -0.9; 2811 1.0; 3008 2.9; 3219 2.0; 3444 0.4; 3685 2.9; 3943 5.8; 4219 5.9; 4514 2.2; 4830 1.9; 5168 3.2; 5530 2.5; 5917 2.6; 6331 2.1; 6775 1.8; 7249 1.3; 7756 -0.0; 8299 -1.6; 8880 -2.8; 9502 -3.5; 10167 -3.6; 10879 -2.9; 11640 -1.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D1100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 9 Hz    | 1.74 | -8.9 dB |
| Peaking | 59 Hz   | 0.58 | -9.3 dB |
| Peaking | 146 Hz  | 1.43 | -7.3 dB |
| Peaking | 238 Hz  | 2.68 | -7.7 dB |
| Peaking | 4121 Hz | 3.53 | 5.7 dB  |
| Peaking | 308 Hz  | 4.11 | -2.6 dB |
| Peaking | 460 Hz  | 2.88 | 4.9 dB  |
| Peaking | 2294 Hz | 7.06 | -3.3 dB |
| Peaking | 6349 Hz | 2.59 | 2.5 dB  |
| Peaking | 9675 Hz | 2.73 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D1100/Denon%20AH-D1100.png)