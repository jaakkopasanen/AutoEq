# Oppo PM3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.9; 22 0.8; 23 0.8; 25 0.8; 26 0.8; 28 0.8; 30 0.9; 32 0.9; 35 0.9; 37 0.9; 40 0.9; 42 1.0; 45 1.1; 49 1.1; 52 1.2; 56 1.3; 59 1.3; 64 1.4; 68 1.4; 73 1.5; 78 1.5; 83 1.4; 89 1.3; 95 0.9; 102 0.7; 109 0.7; 117 0.6; 125 0.5; 134 0.5; 143 0.2; 153 -0.3; 164 0.4; 175 1.0; 188 0.6; 201 0.4; 215 0.5; 230 0.9; 246 1.3; 263 1.7; 282 2.2; 301 2.4; 323 2.6; 345 2.6; 369 2.4; 395 2.2; 423 2.0; 452 1.7; 484 1.3; 518 1.0; 554 1.0; 593 0.9; 635 0.8; 679 0.6; 726 0.5; 777 0.6; 832 0.6; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.3; 1248 -0.3; 1336 -0.8; 1429 -1.3; 1529 -1.8; 1636 -2.6; 1751 -3.3; 1873 -3.8; 2004 -3.3; 2145 -3.0; 2295 -3.0; 2455 -2.4; 2627 -1.6; 2811 -0.6; 3008 0.5; 3219 0.9; 3444 0.9; 3685 1.4; 3943 1.9; 4219 1.9; 4514 2.4; 4830 4.6; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.74 | 0.9 dB  |
| Peaking | 73 Hz   | 1.89 | 1.3 dB  |
| Peaking | 355 Hz  | 1.33 | 2.6 dB  |
| Peaking | 1962 Hz | 2.14 | -4.1 dB |
| Peaking | 5538 Hz | 2.41 | 6.8 dB  |
| Peaking | 152 Hz  | 9.88 | -0.9 dB |
| Peaking | 2563 Hz | 3.89 | -1.8 dB |
| Peaking | 2910 Hz | 1.76 | 1.4 dB  |
| Peaking | 6558 Hz | 5.6  | 3.1 dB  |
| Peaking | 7133 Hz | 1.78 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM3/Oppo%20PM3.png)