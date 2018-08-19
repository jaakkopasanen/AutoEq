# Audio Technica ATH-W5000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 6.0; 143 6.0; 153 6.0; 164 6.0; 175 6.0; 188 6.0; 201 6.0; 215 6.0; 230 6.0; 246 6.0; 263 5.4; 282 5.6; 301 5.5; 323 5.6; 345 5.6; 369 5.9; 395 6.0; 423 6.0; 452 6.0; 484 6.0; 518 6.0; 554 6.0; 593 5.2; 635 3.6; 679 2.2; 726 1.7; 777 1.4; 832 1.0; 890 0.6; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.4; 1336 -2.0; 1429 -2.6; 1529 -2.8; 1636 -2.5; 1751 -1.8; 1873 -1.9; 2004 -1.9; 2145 -1.1; 2295 0.5; 2455 2.1; 2627 4.2; 2811 5.9; 3008 6.0; 3219 6.0; 3444 6.0; 3685 4.4; 3943 0.7; 4219 1.0; 4514 4.1; 4830 5.8; 5168 6.0; 5530 6.0; 5917 5.9; 6331 3.8; 6775 3.6; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.3; 9502 -3.9; 10167 -1.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.1; 15258 -2.3; 16326 -4.7; 17469 -6.8; 18692 -8.0; 20000 -8.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000003dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-W5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 115 Hz   | 0.07 | 6.3 dB  |
| Peaking | 1523 Hz  | 0.78 | -6.7 dB |
| Peaking | 2985 Hz  | 2.53 | 7.8 dB  |
| Peaking | 5502 Hz  | 2.95 | 6.6 dB  |
| Peaking | 19035 Hz | 1.14 | -8.9 dB |
| Peaking | 566 Hz   | 2.4  | 3.1 dB  |
| Peaking | 689 Hz   | 2.41 | -2.7 dB |
| Peaking | 6718 Hz  | 8.6  | 1.1 dB  |
| Peaking | 9460 Hz  | 7.53 | -4.3 dB |
| Peaking | 13360 Hz | 2.76 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-W5000/Audio%20Technica%20ATH-W5000.png)