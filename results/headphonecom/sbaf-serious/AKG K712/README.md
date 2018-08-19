# AKG K712

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 10 -84; 20 0.5; 22 0.1; 23 -0.1; 25 -0.5; 26 -0.7; 28 -1.0; 30 -1.2; 32 -1.5; 35 -1.8; 37 -2.0; 40 -2.2; 42 -2.4; 45 -2.6; 49 -2.8; 52 -3.0; 56 -3.2; 59 -3.3; 64 -3.4; 68 -3.6; 73 -3.7; 78 -3.8; 83 -4.0; 89 -4.2; 95 -4.6; 102 -4.9; 109 -5.0; 117 -5.0; 125 -5.2; 134 -5.5; 143 -5.6; 153 -5.8; 164 -5.8; 175 -5.5; 188 -5.9; 201 -6.0; 215 -6.1; 230 -6.2; 246 -6.2; 263 -6.2; 282 -6.1; 301 -6.0; 323 -5.9; 345 -5.5; 369 -5.4; 395 -5.3; 423 -5.2; 452 -5.0; 484 -4.8; 518 -4.5; 554 -3.6; 593 -3.6; 635 -3.7; 679 -3.3; 726 -2.7; 777 -2.2; 832 -1.7; 890 -1.1; 952 -0.5; 1019 0.2; 1090 1.2; 1167 1.7; 1248 1.6; 1336 1.4; 1429 0.5; 1529 -0.3; 1636 -1.4; 1751 -2.2; 1873 -3.8; 2004 -5.5; 2145 -5.8; 2295 -4.0; 2455 -1.8; 2627 1.0; 2811 4.1; 3008 4.7; 3219 3.0; 3444 1.7; 3685 0.9; 3943 -0.4; 4219 -2.3; 4514 -3.1; 4830 -2.0; 5168 -2.5; 5530 -2.8; 5917 -3.4; 6331 -4.1; 6775 -6.6; 7249 -7.3; 7756 -6.4; 8299 -5.0; 8880 -3.9; 9502 -3.4; 10167 -3.5; 10879 -3.0; 11640 -0.7; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.4; 17469 -1.9; 18692 -2.8; 20000 -3.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.027100013778978dB` and instead set Global volume in the UI for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.7dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 158 Hz   | 0.36 | -5.1 dB  |
| Peaking | 448 Hz   | 0.7  | -2.8 dB  |
| Peaking | 2103 Hz  | 2.32 | -15.3 dB |
| Peaking | 2402 Hz  | 0.78 | 10.8 dB  |
| Peaking | 6595 Hz  | 0.91 | -7.6 dB  |
| Peaking | 1182 Hz  | 5.01 | 1.7 dB   |
| Peaking | 2976 Hz  | 5.34 | 3.8 dB   |
| Peaking | 4854 Hz  | 0.69 | -2.5 dB  |
| Peaking | 5711 Hz  | 3.19 | 4.1 dB   |
| Peaking | 12650 Hz | 2.71 | 2.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K712/AKG%20K712.png)