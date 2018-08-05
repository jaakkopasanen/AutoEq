# Audeze LCD-2 sample 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.0dB
GraphicEQ: 10 -84; 20 6.4; 22 6.0; 23 5.8; 25 5.5; 26 5.4; 28 5.3; 30 5.2; 32 5.1; 35 5.1; 37 5.2; 40 5.1; 42 5.1; 45 5.1; 49 5.1; 52 5.0; 56 4.8; 59 4.6; 64 4.1; 68 3.8; 73 3.7; 78 3.6; 83 3.6; 89 3.4; 95 3.2; 102 2.8; 109 2.6; 117 2.2; 125 1.8; 134 1.6; 143 1.3; 153 1.2; 164 1.1; 175 1.0; 188 0.9; 201 0.8; 215 0.8; 230 0.8; 246 0.7; 263 0.6; 282 0.7; 301 0.6; 323 0.5; 345 0.5; 369 0.4; 395 0.3; 423 0.4; 452 0.3; 484 0.3; 518 0.6; 554 0.7; 593 0.6; 635 0.2; 679 -0.1; 726 -0.2; 777 -0.3; 832 -0.6; 890 -0.7; 952 -0.5; 1019 0.2; 1090 1.9; 1167 3.2; 1248 3.6; 1336 3.9; 1429 3.5; 1529 3.3; 1636 4.2; 1751 5.3; 1873 6.0; 2004 6.0; 2145 5.6; 2295 4.5; 2455 4.6; 2627 4.6; 2811 4.6; 3008 5.8; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-7.0dB` and instead set Global volume in the UI for both channels to **-70**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.82 | 6.0 dB  |
| Peaking | 50 Hz   | 0.57 | 4.1 dB  |
| Peaking | 1864 Hz | 1.58 | 4.9 dB  |
| Peaking | 3734 Hz | 1.56 | 5.2 dB  |
| Peaking | 5740 Hz | 3.07 | 4.6 dB  |
| Peaking | 956 Hz  | 2.4  | -3.6 dB |
| Peaking | 1190 Hz | 1.77 | 3.5 dB  |
| Peaking | 1543 Hz | 4.17 | -2.0 dB |
| Peaking | 6572 Hz | 7.6  | 2.1 dB  |
| Peaking | 7845 Hz | 2.18 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20sample%201/Audeze%20LCD-2%20sample%201.png)