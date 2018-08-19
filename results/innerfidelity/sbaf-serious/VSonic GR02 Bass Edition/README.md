# VSonic GR02 Bass Edition

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -5.4; 22 -5.4; 23 -5.4; 25 -5.4; 26 -5.4; 28 -5.3; 30 -5.3; 32 -5.3; 35 -5.2; 37 -5.2; 40 -5.2; 42 -5.2; 45 -5.1; 49 -5.1; 52 -5.1; 56 -5.1; 59 -5.1; 64 -5.2; 68 -5.2; 73 -5.2; 78 -5.3; 83 -5.3; 89 -5.4; 95 -5.4; 102 -5.4; 109 -5.2; 117 -5.1; 125 -5.0; 134 -5.0; 143 -4.9; 153 -4.7; 164 -4.5; 175 -4.2; 188 -4.1; 201 -3.8; 215 -3.5; 230 -3.3; 246 -3.0; 263 -2.7; 282 -2.4; 301 -2.1; 323 -1.8; 345 -1.6; 369 -1.3; 395 -1.0; 423 -0.7; 452 -0.5; 484 -0.4; 518 -0.1; 554 0.2; 593 0.5; 635 0.6; 679 0.6; 726 0.6; 777 0.7; 832 0.6; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -0.8; 1429 -1.0; 1529 -1.2; 1636 -1.2; 1751 -1.0; 1873 -0.3; 2004 0.6; 2145 1.6; 2295 2.8; 2455 4.4; 2627 5.8; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.9; 4514 3.5; 4830 3.2; 5168 3.6; 5530 3.6; 5917 2.5; 6331 0.8; 6775 0.4; 7249 1.0; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.09999999995353dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic GR02 Bass Edition ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.38 | -4.9 dB |
| Peaking | 122 Hz  | 0.47 | -4.5 dB |
| Peaking | 655 Hz  | 1.18 | 1.4 dB  |
| Peaking | 1701 Hz | 1.46 | -3.7 dB |
| Peaking | 3116 Hz | 1.09 | 7.4 dB  |
| Peaking | 3291 Hz | 4.41 | -2.1 dB |
| Peaking | 3576 Hz | 1.51 | 2.9 dB  |
| Peaking | 4950 Hz | 0.84 | -2.1 dB |
| Peaking | 5547 Hz | 5.5  | 2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20GR02%20Bass%20Edition/VSonic%20GR02%20Bass%20Edition.png)