# T-Peos Altone 200 2014

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.2dB
GraphicEQ: 10 -84; 20 -2.2; 22 -2.8; 23 -3.0; 25 -3.4; 26 -3.7; 28 -4.0; 30 -4.3; 32 -4.5; 35 -4.8; 37 -5.0; 40 -5.2; 42 -5.3; 45 -5.5; 49 -5.6; 52 -5.7; 56 -5.8; 59 -5.8; 64 -5.9; 68 -5.9; 73 -6.0; 78 -6.2; 83 -6.3; 89 -6.6; 95 -6.9; 102 -7.3; 109 -7.6; 117 -7.9; 125 -8.3; 134 -8.5; 143 -8.6; 153 -8.6; 164 -8.5; 175 -8.2; 188 -7.9; 201 -7.6; 215 -7.2; 230 -6.7; 246 -6.4; 263 -6.0; 282 -5.5; 301 -5.1; 323 -4.6; 345 -4.1; 369 -3.7; 395 -3.2; 423 -2.7; 452 -2.2; 484 -1.9; 518 -1.5; 554 -1.0; 593 -0.4; 635 -0.0; 679 0.1; 726 0.3; 777 0.6; 832 0.6; 890 0.5; 952 0.3; 1019 -0.0; 1090 -0.4; 1167 -0.6; 1248 -1.0; 1336 -1.7; 1429 -2.5; 1529 -3.2; 1636 -4.1; 1751 -4.8; 1873 -5.4; 2004 -5.8; 2145 -6.3; 2295 -6.1; 2455 -5.1; 2627 -4.3; 2811 -3.5; 3008 -2.8; 3219 -2.7; 3444 -2.5; 3685 -2.5; 3943 -2.4; 4219 -2.1; 4514 -1.0; 4830 0.0; 5168 0.4; 5530 0.3; 5917 -0.4; 6331 -1.7; 6775 -3.7; 7249 -4.3; 7756 -4.3; 8299 -5.2; 8880 -7.0; 9502 -8.8; 10167 -8.7; 10879 -6.4; 11640 -3.0; 12455 -0.4; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.2dB` and instead set Global volume in the UI for both channels to **-12**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Altone 200 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 2 Hz     | 1.86 | -1.2 dB |
| Peaking | 56 Hz    | 0.38 | -4.7 dB |
| Peaking | 176 Hz   | 0.83 | -6.4 dB |
| Peaking | 2160 Hz  | 1.8  | -6.3 dB |
| Peaking | 9588 Hz  | 2.48 | -9.3 dB |
| Peaking | 808 Hz   | 2.42 | 1.8 dB  |
| Peaking | 4020 Hz  | 2.84 | -1.9 dB |
| Peaking | 5275 Hz  | 2.48 | 2.4 dB  |
| Peaking | 7001 Hz  | 5.35 | -2.6 dB |
| Peaking | 13007 Hz | 4.29 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Altone%20200%202014/T-Peos%20Altone%20200%202014.png)