# Denon AH-D600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -3.8; 22 -3.9; 23 -3.9; 25 -4.0; 26 -4.1; 28 -4.1; 30 -4.1; 32 -4.1; 35 -4.1; 37 -4.0; 40 -3.9; 42 -3.9; 45 -3.7; 49 -3.4; 52 -3.1; 56 -2.8; 59 -2.7; 64 -2.7; 68 -3.0; 73 -3.6; 78 -4.0; 83 -4.1; 89 -4.4; 95 -4.6; 102 -4.9; 109 -5.1; 117 -5.3; 125 -5.5; 134 -5.7; 143 -5.7; 153 -5.5; 164 -4.4; 175 -4.4; 188 -3.8; 201 -2.8; 215 -1.5; 230 0.2; 246 1.6; 263 2.2; 282 2.0; 301 1.2; 323 0.5; 345 0.2; 369 0.3; 395 0.2; 423 0.6; 452 0.9; 484 0.4; 518 -0.0; 554 -0.1; 593 -0.1; 635 0.0; 679 -0.2; 726 -0.1; 777 0.1; 832 0.1; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 -0.6; 1336 -1.2; 1429 -1.9; 1529 -2.5; 1636 -2.9; 1751 -3.2; 1873 -3.1; 2004 -2.5; 2145 -1.6; 2295 -1.6; 2455 -1.7; 2627 -1.3; 2811 -0.9; 3008 0.1; 3219 1.3; 3444 2.7; 3685 4.6; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 5.1; 5917 2.6; 6331 1.1; 6775 3.2; 7249 1.3; 7756 0.3; 8299 -0.2; 8880 -3.7; 9502 -4.8; 10167 -1.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.2; 17469 -2.0; 18692 -3.7; 20000 -3.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.46 | -4.0 dB |
| Peaking | 131 Hz  | 1.76 | -5.4 dB |
| Peaking | 2029 Hz | 1.42 | -3.6 dB |
| Peaking | 4510 Hz | 1.68 | 7.2 dB  |
| Peaking | 9341 Hz | 6.29 | -6.1 dB |
| Peaking | 447 Hz  | 6.21 | 1.0 dB  |
| Peaking | 190 Hz  | 3.56 | -2.1 dB |
| Peaking | 262 Hz  | 3.25 | 3.6 dB  |
| Peaking | 974 Hz  | 3.26 | 0.7 dB  |
| Peaking | 2866 Hz | 7.96 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D600/Denon%20AH-D600.png)