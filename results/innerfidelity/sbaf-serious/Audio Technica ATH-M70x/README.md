# Audio Technica ATH-M70x

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 10 -84; 20 -0.5; 22 -1.0; 23 -1.2; 25 -1.6; 26 -1.7; 28 -2.0; 30 -2.3; 32 -2.4; 35 -2.6; 37 -2.7; 40 -2.8; 42 -2.7; 45 -2.7; 49 -2.3; 52 -1.9; 56 -1.3; 59 -0.9; 64 -0.5; 68 0.0; 73 1.2; 78 2.3; 83 3.2; 89 3.7; 95 3.0; 102 1.0; 109 -0.8; 117 -2.0; 125 -1.9; 134 -0.7; 143 0.2; 153 1.0; 164 2.7; 175 -0.1; 188 -0.7; 201 -0.1; 215 0.2; 230 0.2; 246 0.2; 263 0.2; 282 0.5; 301 0.7; 323 0.9; 345 1.1; 369 1.2; 395 1.3; 423 1.6; 452 1.8; 484 1.8; 518 1.9; 554 2.3; 593 2.9; 635 3.7; 679 2.9; 726 2.3; 777 1.7; 832 0.9; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.4; 1248 -0.7; 1336 -1.1; 1429 -1.6; 1529 -2.3; 1636 -3.0; 1751 -3.4; 1873 -3.6; 2004 -3.5; 2145 -3.1; 2295 -2.5; 2455 -1.3; 2627 0.3; 2811 1.0; 3008 1.3; 3219 0.5; 3444 -0.1; 3685 -0.6; 3943 -1.0; 4219 -3.2; 4514 -4.7; 4830 -3.6; 5168 -1.9; 5530 1.5; 5917 3.4; 6331 4.0; 6775 3.3; 7249 1.3; 7756 -0.9; 8299 -3.4; 8880 -5.1; 9502 -5.5; 10167 -4.1; 10879 -0.7; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.122550884546181dB` and instead set Global volume in the UI for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M70x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.4dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 87 Hz    | 6.97 | 4.3 dB   |
| Peaking | 1819 Hz  | 0.99 | -9.4 dB  |
| Peaking | 4665 Hz  | 2.33 | -11.6 dB |
| Peaking | 6571 Hz  | 0.36 | 30.1 dB  |
| Peaking | 8579 Hz  | 0.54 | -28.8 dB |
| Peaking | 38 Hz    | 1.49 | -3.1 dB  |
| Peaking | 233 Hz   | 2.23 | -0.5 dB  |
| Peaking | 640 Hz   | 4.48 | 1.9 dB   |
| Peaking | 930 Hz   | 3.71 | -1.2 dB  |
| Peaking | 11472 Hz | 7.59 | 2.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-M70x/Audio%20Technica%20ATH-M70x.png)