# Westone ADV Alpha

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -7.1; 22 -7.2; 23 -7.2; 25 -7.2; 26 -7.2; 28 -7.2; 30 -7.2; 32 -7.2; 35 -7.2; 37 -7.2; 40 -7.1; 42 -7.1; 45 -7.1; 49 -7.0; 52 -7.0; 56 -7.0; 59 -6.9; 64 -6.9; 68 -6.9; 73 -7.0; 78 -7.0; 83 -7.2; 89 -7.4; 95 -7.7; 102 -8.2; 109 -8.5; 117 -8.8; 125 -9.2; 134 -9.5; 143 -9.6; 153 -9.6; 164 -9.5; 175 -9.3; 188 -9.0; 201 -8.8; 215 -8.4; 230 -8.0; 246 -7.7; 263 -7.3; 282 -6.8; 301 -6.4; 323 -6.0; 345 -5.5; 369 -5.0; 395 -4.6; 423 -4.0; 452 -3.5; 484 -3.1; 518 -2.7; 554 -2.1; 593 -1.5; 635 -1.1; 679 -0.9; 726 -0.5; 777 -0.1; 832 0.1; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.0; 1167 -0.0; 1248 -0.1; 1336 -0.3; 1429 -0.5; 1529 -0.6; 1636 -0.1; 1751 0.3; 1873 0.8; 2004 1.4; 2145 1.9; 2295 2.6; 2455 3.6; 2627 4.5; 2811 5.4; 3008 6.0; 3219 6.0; 3444 6.0; 3685 5.5; 3943 3.4; 4219 -0.0; 4514 -3.0; 4830 -3.8; 5168 -1.5; 5530 1.4; 5917 3.9; 6331 5.3; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone ADV Alpha ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.3  | -6.8 dB |
| Peaking | 176 Hz  | 0.61 | -8.5 dB |
| Peaking | 3320 Hz | 1.68 | 7.4 dB  |
| Peaking | 4700 Hz | 3.88 | -7.6 dB |
| Peaking | 6261 Hz | 4.98 | 5.6 dB  |
| Peaking | 386 Hz  | 2.22 | -0.7 dB |
| Peaking | 798 Hz  | 1.83 | 1.0 dB  |
| Peaking | 1546 Hz | 2.34 | -1.7 dB |
| Peaking | 1638 Hz | 0.93 | 0.6 dB  |
| Peaking | 8291 Hz | 3.95 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20ADV%20Alpha/Westone%20ADV%20Alpha.png)