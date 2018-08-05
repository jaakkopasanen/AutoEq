# Oppo PM3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.8; 22 1.7; 23 1.7; 25 1.6; 26 1.6; 28 1.6; 30 1.5; 32 1.5; 35 1.5; 37 1.5; 40 1.6; 42 1.6; 45 1.6; 49 1.7; 52 1.8; 56 1.8; 59 1.8; 64 1.8; 68 1.9; 73 1.9; 78 1.9; 83 1.9; 89 1.8; 95 1.4; 102 0.9; 109 0.5; 117 0.2; 125 -0.2; 134 -0.4; 143 -0.7; 153 -0.8; 164 -0.1; 175 0.1; 188 -0.3; 201 -0.2; 215 0.1; 230 0.6; 246 1.0; 263 1.5; 282 2.1; 301 2.5; 323 2.8; 345 3.0; 369 3.0; 395 2.8; 423 2.6; 452 2.2; 484 1.7; 518 1.2; 554 1.0; 593 0.9; 635 0.7; 679 0.4; 726 0.3; 777 0.3; 832 0.3; 890 0.2; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.4; 1248 -0.4; 1336 -0.8; 1429 -1.3; 1529 -1.7; 1636 -2.1; 1751 -2.7; 1873 -3.2; 2004 -2.9; 2145 -2.9; 2295 -3.0; 2455 -2.1; 2627 -1.4; 2811 -0.9; 3008 -0.1; 3219 0.4; 3444 0.6; 3685 0.5; 3943 0.7; 4219 0.7; 4514 1.7; 4830 3.8; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 78 Hz    | 0.32 | 2.4 dB  |
| Peaking | 157 Hz   | 1.07 | -2.9 dB |
| Peaking | 359 Hz   | 1.55 | 2.9 dB  |
| Peaking | 1998 Hz  | 1.87 | -3.5 dB |
| Peaking | 5659 Hz  | 2.81 | 6.9 dB  |
| Peaking | 10272 Hz | 1.8  | -0.2 dB |
| Peaking | 6580 Hz  | 7.97 | 2.1 dB  |
| Peaking | 7612 Hz  | 2.8  | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM3/Oppo%20PM3.png)