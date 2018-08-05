# Sony MDR-EX600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.9; 26 5.9; 28 5.7; 30 5.5; 32 5.4; 35 5.1; 37 5.0; 40 4.9; 42 4.8; 45 4.7; 49 4.6; 52 4.5; 56 4.4; 59 4.3; 64 4.2; 68 4.0; 73 3.9; 78 3.7; 83 3.4; 89 2.9; 95 2.4; 102 1.8; 109 1.3; 117 0.7; 125 0.1; 134 -0.4; 143 -0.7; 153 -1.0; 164 -1.2; 175 -1.3; 188 -1.4; 201 -1.4; 215 -1.4; 230 -1.4; 246 -1.4; 263 -1.3; 282 -1.1; 301 -1.1; 323 -1.0; 345 -0.8; 369 -0.7; 395 -0.7; 423 -0.5; 452 -0.3; 484 -0.2; 518 -0.1; 554 0.2; 593 0.6; 635 0.7; 679 0.7; 726 0.9; 777 1.0; 832 0.8; 890 0.6; 952 0.3; 1019 -0.0; 1090 -0.4; 1167 -0.8; 1248 -1.1; 1336 -1.6; 1429 -2.2; 1529 -2.7; 1636 -3.1; 1751 -3.1; 1873 -2.7; 2004 -2.0; 2145 -1.0; 2295 0.3; 2455 2.1; 2627 3.8; 2811 5.3; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.3; 4514 2.8; 4830 -0.2; 5168 -3.5; 5530 -3.4; 5917 0.8; 6331 3.8; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.5; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.91 | 6.1 dB  |
| Peaking | 66 Hz    | 1.94 | 3.2 dB  |
| Peaking | 1760 Hz  | 2.22 | -4.4 dB |
| Peaking | 3256 Hz  | 1.99 | 7.4 dB  |
| Peaking | 24000 Hz | 2.34 | 1.1 dB  |
| Peaking | 219 Hz   | 1.23 | -1.8 dB |
| Peaking | 754 Hz   | 2.62 | 1.3 dB  |
| Peaking | 4190 Hz  | 5.99 | 3.3 dB  |
| Peaking | 5319 Hz  | 4.43 | -6.5 dB |
| Peaking | 6424 Hz  | 5.71 | 5.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-EX600/Sony%20MDR-EX600.png)