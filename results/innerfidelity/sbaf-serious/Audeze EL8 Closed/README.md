# Audeze EL8 Closed

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.3; 22 2.2; 23 2.2; 25 2.1; 26 2.1; 28 2.1; 30 2.1; 32 2.1; 35 2.3; 37 2.4; 40 2.4; 42 2.4; 45 2.5; 49 3.0; 52 3.4; 56 3.1; 59 2.5; 64 1.5; 68 1.2; 73 1.1; 78 0.9; 83 0.7; 89 0.4; 95 0.0; 102 -0.4; 109 -0.5; 117 -0.6; 125 -0.6; 134 -0.3; 143 0.1; 153 0.6; 164 1.4; 175 1.2; 188 1.8; 201 2.3; 215 2.7; 230 3.1; 246 3.2; 263 3.4; 282 3.5; 301 3.4; 323 3.3; 345 3.2; 369 3.2; 395 2.9; 423 2.8; 452 2.6; 484 2.4; 518 2.2; 554 2.2; 593 2.2; 635 1.9; 679 1.5; 726 1.1; 777 1.0; 832 0.6; 890 0.4; 952 0.2; 1019 -0.0; 1090 0.1; 1167 -0.1; 1248 -0.5; 1336 -0.9; 1429 -1.3; 1529 -1.9; 1636 -2.4; 1751 -2.5; 1873 -2.5; 2004 -2.0; 2145 -1.5; 2295 -0.9; 2455 -0.2; 2627 0.2; 2811 -0.3; 3008 -0.7; 3219 -1.1; 3444 -1.5; 3685 -1.5; 3943 -1.4; 4219 -2.0; 4514 -3.7; 4830 -4.4; 5168 0.2; 5530 5.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.5; 9502 -0.8; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -1.2; 15258 -2.9; 16326 -1.8; 17469 -0.2; 18692 -0.4; 20000 -3.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze EL8 Closed ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 43 Hz    | 1.19 | 3.0 dB  |
| Peaking | 347 Hz   | 0.7  | 4.4 dB  |
| Peaking | 6502 Hz  | 0.03 | -1.2 dB |
| Peaking | 4756 Hz  | 4.31 | -6.0 dB |
| Peaking | 5916 Hz  | 2.93 | 9.1 dB  |
| Peaking | 118 Hz   | 2.71 | -1.8 dB |
| Peaking | 1257 Hz  | 0.92 | 1.6 dB  |
| Peaking | 1797 Hz  | 1.13 | -3.1 dB |
| Peaking | 2524 Hz  | 3.14 | 2.4 dB  |
| Peaking | 11986 Hz | 3.53 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20EL8%20Closed/Audeze%20EL8%20Closed.png)