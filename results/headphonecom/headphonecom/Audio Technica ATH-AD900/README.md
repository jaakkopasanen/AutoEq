# Audio Technica ATH-AD900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 5.8; 23 5.7; 25 5.3; 26 5.2; 28 4.8; 30 4.4; 32 4.1; 35 3.7; 37 3.5; 40 3.2; 42 3.0; 45 2.8; 49 2.5; 52 2.3; 56 2.1; 59 2.0; 64 1.8; 68 1.6; 73 1.5; 78 1.8; 83 2.6; 89 2.4; 95 1.1; 102 0.6; 109 0.6; 117 0.5; 125 0.2; 134 -0.1; 143 -0.3; 153 -0.4; 164 -0.4; 175 -0.6; 188 -0.6; 201 -0.6; 215 -0.6; 230 -0.7; 246 -0.8; 263 -0.8; 282 -0.7; 301 -0.6; 323 -0.5; 345 -0.4; 369 -0.4; 395 -0.3; 423 -0.3; 452 -0.1; 484 -0.0; 518 0.2; 554 0.3; 593 0.5; 635 0.6; 679 0.7; 726 0.9; 777 0.7; 832 0.3; 890 0.3; 952 0.3; 1019 0.0; 1090 -0.0; 1167 -0.0; 1248 -0.1; 1336 -0.0; 1429 -0.5; 1529 -1.3; 1636 -1.1; 1751 0.4; 1873 1.2; 2004 2.3; 2145 3.8; 2295 4.0; 2455 5.3; 2627 4.8; 2811 4.0; 3008 3.5; 3219 4.0; 3444 2.2; 3685 -1.2; 3943 -2.2; 4219 -2.1; 4514 -0.8; 4830 2.1; 5168 4.4; 5530 5.9; 5917 5.6; 6331 4.9; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.3; 9502 -0.5; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.75 | 5.7 dB  |
| Peaking | 86 Hz   | 6.7  | 2.0 dB  |
| Peaking | 2640 Hz | 2.35 | 5.3 dB  |
| Peaking | 4118 Hz | 4.29 | -4.8 dB |
| Peaking | 5704 Hz | 3.09 | 6.6 dB  |
| Peaking | 234 Hz  | 1.09 | -0.9 dB |
| Peaking | 688 Hz  | 2.83 | 0.9 dB  |
| Peaking | 1569 Hz | 5    | -2.3 dB |
| Peaking | 2130 Hz | 6.56 | 1.2 dB  |
| Peaking | 8945 Hz | 3.89 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Audio%20Technica%20ATH-AD900/Audio%20Technica%20ATH-AD900.png)