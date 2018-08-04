# Sony MDR-V6

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 5.9; 40 5.4; 42 5.0; 45 4.5; 49 4.1; 52 3.8; 56 3.4; 59 3.1; 64 3.0; 68 3.2; 73 3.6; 78 3.4; 83 3.0; 89 2.7; 95 2.4; 102 2.0; 109 1.8; 117 1.5; 125 1.3; 134 1.2; 143 1.1; 153 1.1; 164 1.3; 175 1.5; 188 1.7; 201 1.8; 215 1.8; 230 1.1; 246 0.2; 263 0.3; 282 0.5; 301 0.9; 323 0.8; 345 0.5; 369 0.0; 395 -0.6; 423 -0.8; 452 -0.9; 484 -1.0; 518 -1.2; 554 -1.1; 593 -0.9; 635 -0.8; 679 -0.7; 726 -0.5; 777 -0.4; 832 -0.4; 890 -0.2; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 -0.8; 1336 -0.9; 1429 -1.2; 1529 -2.0; 1636 -2.4; 1751 -2.6; 1873 -2.7; 2004 -2.7; 2145 -3.0; 2295 -3.2; 2455 -3.2; 2627 -3.9; 2811 -4.8; 3008 -5.1; 3219 -5.0; 3444 -4.7; 3685 -3.8; 3943 -3.1; 4219 -4.6; 4514 -5.9; 4830 -4.7; 5168 -1.3; 5530 2.2; 5917 4.5; 6331 4.1; 6775 1.8; 7249 -0.1; 7756 -1.3; 8299 -3.0; 8880 -5.5; 9502 -7.5; 10167 -6.8; 10879 -2.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.19 | 6.4 dB  |
| Peaking | 2965 Hz  | 0.98 | -4.6 dB |
| Peaking | 4666 Hz  | 4.81 | -4.9 dB |
| Peaking | 5963 Hz  | 3.46 | 7.2 dB  |
| Peaking | 9528 Hz  | 4.02 | -8.2 dB |
| Peaking | 127 Hz   | 2.16 | -0.5 dB |
| Peaking | 200 Hz   | 3.73 | 1.2 dB  |
| Peaking | 517 Hz   | 2.4  | -1.3 dB |
| Peaking | 1026 Hz  | 4.13 | 0.8 dB  |
| Peaking | 11644 Hz | 6.94 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-V6/Sony%20MDR-V6.png)