# Audio Technica ATH-ANC7B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.8; 26 5.5; 28 4.4; 30 2.8; 32 1.1; 35 -1.1; 37 -2.3; 40 -3.8; 42 -4.6; 45 -5.3; 49 -5.5; 52 -5.2; 56 -4.6; 59 -4.1; 64 -3.6; 68 -3.4; 73 -3.2; 78 -3.1; 83 -3.0; 89 -2.9; 95 -2.9; 102 -2.8; 109 -2.7; 117 -2.6; 125 -2.5; 134 -2.5; 143 -2.5; 153 -2.6; 164 -2.4; 175 -2.3; 188 -2.2; 201 -2.0; 215 -1.9; 230 -1.7; 246 -1.5; 263 -1.3; 282 -1.1; 301 -1.0; 323 -0.7; 345 -0.6; 369 -0.6; 395 -0.6; 423 -0.8; 452 -1.1; 484 -1.5; 518 -2.0; 554 -2.5; 593 -3.2; 635 -3.9; 679 -4.3; 726 -4.1; 777 -3.4; 832 -2.2; 890 -0.8; 952 -0.0; 1019 -0.2; 1090 -1.6; 1167 -2.0; 1248 -1.2; 1336 -1.3; 1429 0.1; 1529 1.0; 1636 2.1; 1751 0.4; 1873 -0.3; 2004 0.5; 2145 0.8; 2295 2.2; 2455 3.1; 2627 4.8; 2811 5.1; 3008 4.8; 3219 4.7; 3444 4.1; 3685 3.4; 3943 4.0; 4219 4.4; 4514 5.2; 4830 3.9; 5168 -0.4; 5530 0.4; 5917 1.9; 6331 4.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.0; 9502 -2.1; 10167 -3.1; 10879 -2.7; 11640 -1.3; 12455 -0.1; 13327 -0.8; 14260 -2.9; 15258 -4.6; 16326 -4.3; 17469 -2.2; 18692 -0.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ANC7B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.67 | 16.6 dB  |
| Peaking | 39 Hz    | 0.63 | -15.4 dB |
| Peaking | 3333 Hz  | 0.72 | 8.4 dB   |
| Peaking | 4016 Hz  | 0.11 | -3.7 dB  |
| Peaking | 6628 Hz  | 6.47 | 5.0 dB   |
| Peaking | 677 Hz   | 2.45 | -5.6 dB  |
| Peaking | 684 Hz   | 1.02 | 3.1 dB   |
| Peaking | 2027 Hz  | 6.2  | -1.7 dB  |
| Peaking | 12756 Hz | 5.2  | 2.9 dB   |
| Peaking | 15598 Hz | 3.67 | -3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-ANC7B/Audio%20Technica%20ATH-ANC7B.png)