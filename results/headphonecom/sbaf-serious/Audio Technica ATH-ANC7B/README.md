# Audio Technica ATH-ANC7B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 5.7; 23 5.2; 25 3.6; 26 2.7; 28 0.7; 30 -1.2; 32 -2.8; 35 -5.0; 37 -6.2; 40 -7.7; 42 -8.4; 45 -9.1; 49 -9.2; 52 -8.9; 56 -8.1; 59 -7.6; 64 -7.0; 68 -6.7; 73 -6.3; 78 -5.9; 83 -5.7; 89 -5.3; 95 -5.1; 102 -4.7; 109 -4.3; 117 -4.0; 125 -3.7; 134 -3.5; 143 -3.2; 153 -3.2; 164 -2.9; 175 -2.7; 188 -2.5; 201 -2.3; 215 -2.0; 230 -1.8; 246 -1.6; 263 -1.5; 282 -1.2; 301 -1.1; 323 -0.8; 345 -0.6; 369 -0.7; 395 -0.6; 423 -0.7; 452 -1.0; 484 -1.5; 518 -2.1; 554 -2.6; 593 -3.1; 635 -3.8; 679 -4.4; 726 -4.2; 777 -3.4; 832 -2.2; 890 -0.9; 952 -0.0; 1019 -0.2; 1090 -1.6; 1167 -2.0; 1248 -1.2; 1336 -1.3; 1429 0.1; 1529 1.0; 1636 2.1; 1751 0.4; 1873 -0.3; 2004 0.5; 2145 0.8; 2295 2.2; 2455 3.1; 2627 4.7; 2811 5.0; 3008 4.9; 3219 4.6; 3444 4.0; 3685 3.3; 3943 4.2; 4219 4.4; 4514 5.1; 4830 3.9; 5168 -0.3; 5530 0.5; 5917 1.8; 6331 4.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.1; 9502 -1.9; 10167 -3.0; 10879 -2.9; 11640 -1.5; 12455 -0.0; 13327 -0.5; 14260 -2.9; 15258 -4.8; 16326 -4.4; 17469 -2.1; 18692 -0.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ANC7B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 22 Hz    |  0.59 | 15.6 dB  |
| Peaking | 42 Hz    |  0.62 | -17.7 dB |
| Peaking | 684 Hz   |  2.62 | -4.3 dB  |
| Peaking | 2846 Hz  |  2.74 | 4.9 dB   |
| Peaking | 4366 Hz  |  3.03 | 4.2 dB   |
| Peaking | 1166 Hz  |  8.53 | -1.8 dB  |
| Peaking | 5330 Hz  | 10.97 | -3.0 dB  |
| Peaking | 6565 Hz  |  7.55 | 4.8 dB   |
| Peaking | 15708 Hz |  1.88 | -4.9 dB  |
| Peaking | 24000 Hz |  1.12 | -3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-ANC7B/Audio%20Technica%20ATH-ANC7B.png)