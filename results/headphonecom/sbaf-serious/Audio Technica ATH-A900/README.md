# Audio Technica ATH-A900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.9; 32 5.4; 35 4.4; 37 3.6; 40 2.6; 42 2.0; 45 1.3; 49 0.6; 52 0.1; 56 -0.2; 59 -0.2; 64 0.3; 68 1.0; 73 1.5; 78 0.7; 83 0.1; 89 0.0; 95 0.4; 102 1.3; 109 1.6; 117 1.7; 125 1.9; 134 2.1; 143 2.4; 153 2.7; 164 3.5; 175 3.8; 188 4.0; 201 4.3; 215 4.6; 230 4.8; 246 4.6; 263 3.9; 282 2.7; 301 1.4; 323 0.2; 345 -1.2; 369 -2.1; 395 -2.4; 423 -2.2; 452 -2.0; 484 -1.8; 518 -1.5; 554 -1.1; 593 -0.6; 635 -0.4; 679 -0.5; 726 -0.5; 777 0.1; 832 0.9; 890 0.3; 952 -0.0; 1019 -0.1; 1090 -0.4; 1167 -0.6; 1248 -0.9; 1336 -1.8; 1429 -1.7; 1529 -1.0; 1636 -0.8; 1751 -0.9; 1873 -0.8; 2004 -0.6; 2145 -0.2; 2295 0.8; 2455 1.9; 2627 2.3; 2811 2.5; 3008 2.8; 3219 3.3; 3444 4.1; 3685 4.3; 3943 4.4; 4219 4.5; 4514 2.8; 4830 5.4; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -1.4; 17469 -1.1; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.53 | 6.7 dB  |
| Peaking | 237 Hz   | 1.18 | 6.6 dB  |
| Peaking | 379 Hz   | 1.39 | -5.0 dB |
| Peaking | 3595 Hz  | 2.37 | 3.8 dB  |
| Peaking | 5655 Hz  | 2.82 | 6.2 dB  |
| Peaking | 13 Hz    | 2.43 | 1.0 dB  |
| Peaking | 1527 Hz  | 2.24 | -1.6 dB |
| Peaking | 2598 Hz  | 6.39 | 1.4 dB  |
| Peaking | 8233 Hz  | 5    | -1.2 dB |
| Peaking | 31170 Hz | 4.73 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-A900/Audio%20Technica%20ATH-A900.png)