# Meelectronics Air-Fi Matrix2 AF62 Wired

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.3dB
GraphicEQ: 10 -84; 20 7.2; 22 6.0; 23 5.4; 25 4.3; 26 3.8; 28 2.9; 30 2.0; 32 1.2; 35 0.2; 37 -0.4; 40 -1.1; 42 -1.5; 45 -2.0; 49 -2.4; 52 -2.6; 56 -2.8; 59 -2.9; 64 -3.0; 68 -3.0; 73 -3.0; 78 -2.9; 83 -2.9; 89 -2.9; 95 -2.8; 102 -2.8; 109 -2.6; 117 -2.5; 125 -2.4; 134 -2.3; 143 -2.4; 153 -2.5; 164 -2.5; 175 -2.2; 188 -2.4; 201 -2.5; 215 -2.4; 230 -2.1; 246 -1.9; 263 -2.3; 282 -2.3; 301 -2.4; 323 -2.4; 345 -2.4; 369 -2.5; 395 -2.5; 423 -2.3; 452 -2.2; 484 -2.4; 518 -2.5; 554 -2.4; 593 -2.2; 635 -2.2; 679 -2.2; 726 -2.1; 777 -1.3; 832 -0.6; 890 -0.5; 952 -0.1; 1019 -0.0; 1090 -0.1; 1167 0.1; 1248 -0.1; 1336 -0.2; 1429 -0.1; 1529 0.2; 1636 0.6; 1751 1.5; 1873 2.4; 2004 2.8; 2145 3.2; 2295 3.4; 2455 3.5; 2627 4.0; 2811 3.6; 3008 3.3; 3219 2.9; 3444 3.1; 3685 4.1; 3943 4.8; 4219 4.9; 4514 6.0; 4830 6.0; 5168 5.2; 5530 3.3; 5917 4.3; 6331 4.8; 6775 3.9; 7249 1.3; 7756 -0.0; 8299 -1.1; 8880 -0.5; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-7.3458691746956735dB` and instead set Global volume in the UI for both channels to **-73**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meelectronics Air-Fi Matrix2 AF62 Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.03 | 9.3 dB  |
| Peaking | 50 Hz   | 0.39 | -4.0 dB |
| Peaking | 446 Hz  | 0.7  | -2.3 dB |
| Peaking | 2384 Hz | 1.77 | 3.2 dB  |
| Peaking | 4776 Hz | 1.71 | 5.6 dB  |
| Peaking | 721 Hz  | 2.93 | -1.3 dB |
| Peaking | 850 Hz  | 1.49 | 1.1 dB  |
| Peaking | 1390 Hz | 4.32 | -0.8 dB |
| Peaking | 6587 Hz | 6.19 | 3.7 dB  |
| Peaking | 7868 Hz | 2.14 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meelectronics%20Air-Fi%20Matrix2%20AF62%20Wired/Meelectronics%20Air-Fi%20Matrix2%20AF62%20Wired.png)