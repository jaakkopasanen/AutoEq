# Meelectronics Air-Fi Matrix2 AF62 Wired

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.8dB
GraphicEQ: 10 -84; 20 7.3; 22 6.0; 23 5.4; 25 4.3; 26 3.8; 28 2.9; 30 2.0; 32 1.3; 35 0.3; 37 -0.3; 40 -1.0; 42 -1.4; 45 -1.8; 49 -2.2; 52 -2.4; 56 -2.5; 59 -2.5; 64 -2.5; 68 -2.4; 73 -2.3; 78 -2.2; 83 -2.1; 89 -2.1; 95 -2.1; 102 -2.2; 109 -2.2; 117 -2.3; 125 -2.3; 134 -2.5; 143 -2.6; 153 -2.8; 164 -2.7; 175 -2.4; 188 -2.6; 201 -2.6; 215 -2.5; 230 -2.3; 246 -2.0; 263 -2.4; 282 -2.4; 301 -2.5; 323 -2.5; 345 -2.5; 369 -2.5; 395 -2.6; 423 -2.3; 452 -2.2; 484 -2.4; 518 -2.5; 554 -2.4; 593 -2.2; 635 -2.2; 679 -2.2; 726 -2.1; 777 -1.3; 832 -0.6; 890 -0.5; 952 -0.1; 1019 -0.0; 1090 -0.1; 1167 0.1; 1248 -0.1; 1336 -0.2; 1429 -0.1; 1529 0.2; 1636 0.6; 1751 1.5; 1873 2.4; 2004 2.8; 2145 3.2; 2295 3.4; 2455 3.5; 2627 4.0; 2811 3.6; 3008 3.3; 3219 2.9; 3444 3.1; 3685 4.1; 3943 4.8; 4219 4.9; 4514 6.0; 4830 6.0; 5168 5.2; 5530 3.3; 5917 4.3; 6331 4.8; 6775 3.9; 7249 1.3; 7756 -0.0; 8299 -1.1; 8880 -0.5; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-7.8dB` and instead set Global volume in the UI for both channels to **-78**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meelectronics Air-Fi Matrix2 AF62 Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 1.54 | 9.0 dB  |
| Peaking | 99 Hz    | 0.11 | -2.7 dB |
| Peaking | 2354 Hz  | 1.53 | 3.4 dB  |
| Peaking | 4794 Hz  | 1.73 | 5.6 dB  |
| Peaking | 26635 Hz | 1.46 | -0.5 dB |
| Peaking | 51 Hz    | 3.91 | -0.7 dB |
| Peaking | 840 Hz   | 1.29 | -1.7 dB |
| Peaking | 920 Hz   | 2.29 | 2.5 dB  |
| Peaking | 6517 Hz  | 7.04 | 3.3 dB  |
| Peaking | 8080 Hz  | 2.78 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meelectronics%20Air-Fi%20Matrix2%20AF62%20Wired/Meelectronics%20Air-Fi%20Matrix2%20AF62%20Wired.png)