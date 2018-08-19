# T-Peos Altone 200 2014

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.8dB
GraphicEQ: 10 -84; 20 -2.3; 22 -2.8; 23 -3.1; 25 -3.6; 26 -3.8; 28 -4.2; 30 -4.5; 32 -4.7; 35 -5.1; 37 -5.3; 40 -5.6; 42 -5.8; 45 -6.1; 49 -6.3; 52 -6.5; 56 -6.7; 59 -6.9; 64 -7.2; 68 -7.3; 73 -7.5; 78 -7.8; 83 -8.0; 89 -8.1; 95 -8.3; 102 -8.4; 109 -8.3; 117 -8.3; 125 -8.3; 134 -8.3; 143 -8.2; 153 -8.1; 164 -7.9; 175 -7.7; 188 -7.4; 201 -7.2; 215 -6.8; 230 -6.4; 246 -6.1; 263 -5.8; 282 -5.3; 301 -4.9; 323 -4.5; 345 -4.0; 369 -3.6; 395 -3.2; 423 -2.6; 452 -2.1; 484 -1.8; 518 -1.4; 554 -0.9; 593 -0.4; 635 -0.0; 679 0.1; 726 0.3; 777 0.6; 832 0.6; 890 0.5; 952 0.3; 1019 -0.0; 1090 -0.4; 1167 -0.6; 1248 -1.0; 1336 -1.7; 1429 -2.5; 1529 -3.2; 1636 -4.1; 1751 -4.8; 1873 -5.4; 2004 -5.8; 2145 -6.3; 2295 -6.1; 2455 -5.1; 2627 -4.3; 2811 -3.5; 3008 -2.8; 3219 -2.7; 3444 -2.5; 3685 -2.5; 3943 -2.4; 4219 -2.1; 4514 -1.0; 4830 0.0; 5168 0.4; 5530 0.3; 5917 -0.4; 6331 -1.7; 6775 -3.7; 7249 -4.3; 7756 -4.3; 8299 -5.2; 8880 -7.0; 9502 -8.8; 10167 -8.7; 10879 -6.4; 11640 -3.0; 12455 -0.4; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.7794372241984426dB` and instead set Global volume in the UI for both channels to **-7**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Altone 200 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 60 Hz    | 0.47 | -6.0 dB |
| Peaking | 144 Hz   | 0.93 | -4.7 dB |
| Peaking | 270 Hz   | 1.58 | -2.8 dB |
| Peaking | 2156 Hz  | 1.77 | -6.3 dB |
| Peaking | 9589 Hz  | 2.48 | -9.3 dB |
| Peaking | 820 Hz   | 2.52 | 1.7 dB  |
| Peaking | 4049 Hz  | 2.93 | -1.8 dB |
| Peaking | 5275 Hz  | 2.46 | 2.4 dB  |
| Peaking | 6955 Hz  | 5.32 | -2.6 dB |
| Peaking | 13189 Hz | 4.31 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Altone%20200%202014/T-Peos%20Altone%20200%202014.png)