# Klipsch Image S2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 10 -84; 20 -6.4; 22 -6.5; 23 -6.5; 25 -6.6; 26 -6.6; 28 -6.7; 30 -6.8; 32 -6.8; 35 -6.7; 37 -6.7; 40 -6.6; 42 -6.5; 45 -6.5; 49 -6.4; 52 -6.3; 56 -6.2; 59 -6.1; 64 -5.9; 68 -5.8; 73 -5.7; 78 -5.6; 83 -5.5; 89 -5.6; 95 -5.7; 102 -5.9; 109 -6.0; 117 -6.2; 125 -6.5; 134 -6.6; 143 -6.6; 153 -6.5; 164 -6.3; 175 -6.0; 188 -5.7; 201 -5.4; 215 -4.9; 230 -4.5; 246 -4.1; 263 -3.8; 282 -3.3; 301 -2.9; 323 -2.4; 345 -1.9; 369 -1.5; 395 -1.1; 423 -0.6; 452 -0.3; 484 -0.1; 518 0.2; 554 0.6; 593 0.9; 635 1.2; 679 1.2; 726 1.3; 777 1.4; 832 1.3; 890 0.8; 952 0.4; 1019 -0.1; 1090 -0.8; 1167 -1.5; 1248 -2.3; 1336 -3.0; 1429 -3.0; 1529 -2.7; 1636 -2.8; 1751 -3.4; 1873 -4.1; 2004 -4.8; 2145 -5.7; 2295 -6.2; 2455 -6.2; 2627 -5.4; 2811 -3.3; 3008 -0.5; 3219 1.8; 3444 3.6; 3685 4.3; 3943 3.8; 4219 1.7; 4514 -0.5; 4830 -2.2; 5168 -4.5; 5530 -7.7; 5917 -5.1; 6331 0.2; 6775 3.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -0.1; 14260 -2.4; 15258 -2.4; 16326 -0.2; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.9dB` and instead set Global volume in the UI for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image S2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.32 | -6.6 dB |
| Peaking | 162 Hz   | 1.08 | -4.9 dB |
| Peaking | 2399 Hz  | 1.68 | -7.9 dB |
| Peaking | 3546 Hz  | 2.47 | 7.3 dB  |
| Peaking | 5500 Hz  | 6.91 | -8.7 dB |
| Peaking | 739 Hz   | 1.74 | 2.2 dB  |
| Peaking | 1337 Hz  | 4.13 | -2.0 dB |
| Peaking | 6101 Hz  | 3.71 | -2.5 dB |
| Peaking | 6649 Hz  | 5.78 | 5.6 dB  |
| Peaking | 14866 Hz | 5.36 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20Image%20S2/Klipsch%20Image%20S2.png)