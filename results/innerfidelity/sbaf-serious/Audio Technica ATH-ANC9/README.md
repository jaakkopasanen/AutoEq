# Audio Technica ATH-ANC9

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 10 -84; 20 -5.6; 22 -6.1; 23 -6.3; 25 -6.7; 26 -6.8; 28 -7.0; 30 -7.1; 32 -7.1; 35 -6.8; 37 -6.5; 40 -5.8; 42 -5.3; 45 -4.5; 49 -3.6; 52 -3.1; 56 -2.6; 59 -2.3; 64 -2.0; 68 -1.9; 73 -2.0; 78 -2.2; 83 -2.4; 89 -2.8; 95 -3.2; 102 -3.5; 109 -3.6; 117 -3.6; 125 -3.7; 134 -3.6; 143 -3.3; 153 -3.0; 164 -2.6; 175 -2.1; 188 -1.6; 201 -1.1; 215 -0.6; 230 -0.1; 246 0.3; 263 0.5; 282 1.0; 301 1.3; 323 1.7; 345 2.1; 369 2.2; 395 2.0; 423 2.4; 452 2.5; 484 2.5; 518 2.6; 554 3.0; 593 3.6; 635 4.1; 679 4.6; 726 5.0; 777 5.1; 832 4.5; 890 3.4; 952 1.7; 1019 -0.5; 1090 -2.9; 1167 -5.2; 1248 -7.4; 1336 -8.8; 1429 -9.4; 1529 -9.4; 1636 -8.1; 1751 -7.0; 1873 -6.1; 2004 -5.1; 2145 -5.1; 2295 -5.2; 2455 -4.7; 2627 -4.7; 2811 -5.5; 3008 -6.1; 3219 -6.4; 3444 -6.0; 3685 -6.6; 3943 -6.6; 4219 -6.9; 4514 -5.6; 4830 -5.2; 5168 -4.3; 5530 -4.0; 5917 -2.9; 6331 0.1; 6775 0.9; 7249 1.0; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.293491877190763dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ANC9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.0dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 1.01 | -7.4 dB  |
| Peaking | 128 Hz  | 1.4  | -3.7 dB  |
| Peaking | 860 Hz  | 0.85 | 11.6 dB  |
| Peaking | 1351 Hz | 1.15 | -16.0 dB |
| Peaking | 3882 Hz | 1.76 | -6.0 dB  |
| Peaking | 337 Hz  | 3.81 | 0.8 dB   |
| Peaking | 539 Hz  | 4.58 | -0.8 dB  |
| Peaking | 5768 Hz | 3.39 | -3.8 dB  |
| Peaking | 6463 Hz | 2.61 | 4.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-ANC9/Audio%20Technica%20ATH-ANC9.png)