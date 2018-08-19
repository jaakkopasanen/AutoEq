# Audio Technica ATH-A55

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 6.0; 143 6.0; 153 6.0; 164 6.0; 175 6.0; 188 6.0; 201 6.0; 215 6.0; 230 6.0; 246 5.5; 263 3.5; 282 1.6; 301 0.3; 323 -0.8; 345 -1.2; 369 -1.2; 395 -0.9; 423 -0.5; 452 -0.2; 484 0.1; 518 0.2; 554 0.3; 593 0.4; 635 0.5; 679 0.6; 726 0.4; 777 0.4; 832 0.7; 890 0.7; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.5; 1336 -0.5; 1429 -0.6; 1529 -0.3; 1636 0.9; 1751 1.2; 1873 1.7; 2004 1.6; 2145 0.8; 2295 0.4; 2455 0.4; 2627 1.6; 2811 2.6; 3008 3.1; 3219 4.0; 3444 5.8; 3685 5.9; 3943 1.5; 4219 -3.5; 4514 -2.6; 4830 0.9; 5168 4.4; 5530 6.0; 5917 5.7; 6331 3.2; 6775 2.4; 7249 -0.9; 7756 -2.4; 8299 -2.7; 8880 -2.4; 9502 -0.6; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000003dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A55 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 60 Hz   | 0.27 | 6.8 dB   |
| Peaking | 1223 Hz | 3.96 | -0.8 dB  |
| Peaking | 3685 Hz | 1.62 | 21.1 dB  |
| Peaking | 4232 Hz | 1.39 | -22.1 dB |
| Peaking | 5503 Hz | 2.92 | 11.5 dB  |
| Peaking | 20 Hz   | 2.12 | 1.3 dB   |
| Peaking | 232 Hz  | 1.88 | 4.3 dB   |
| Peaking | 328 Hz  | 1.87 | -4.8 dB  |
| Peaking | 1860 Hz | 6.79 | 1.5 dB   |
| Peaking | 8155 Hz | 7    | -2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-A55/Audio%20Technica%20ATH-A55.png)