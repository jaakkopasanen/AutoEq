# Thinksound ts01

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 10 -84; 20 -6.7; 22 -6.7; 23 -6.7; 25 -6.7; 26 -6.7; 28 -6.7; 30 -6.7; 32 -6.7; 35 -6.7; 37 -6.7; 40 -6.7; 42 -6.7; 45 -6.7; 49 -6.7; 52 -6.7; 56 -6.7; 59 -6.7; 64 -6.7; 68 -6.7; 73 -6.8; 78 -6.9; 83 -7.1; 89 -7.4; 95 -7.8; 102 -8.2; 109 -8.6; 117 -9.0; 125 -9.5; 134 -9.8; 143 -10.0; 153 -10.1; 164 -10.0; 175 -9.9; 188 -9.7; 201 -9.5; 215 -9.2; 230 -8.8; 246 -8.6; 263 -8.2; 282 -7.8; 301 -7.4; 323 -6.9; 345 -6.5; 369 -6.0; 395 -5.6; 423 -5.0; 452 -4.4; 484 -4.1; 518 -3.6; 554 -2.9; 593 -2.2; 635 -1.8; 679 -1.4; 726 -1.0; 777 -0.4; 832 -0.2; 890 -0.0; 952 0.1; 1019 -0.0; 1090 0.1; 1167 0.8; 1248 1.0; 1336 0.7; 1429 0.5; 1529 0.4; 1636 0.3; 1751 0.3; 1873 0.6; 2004 0.8; 2145 0.8; 2295 0.9; 2455 0.9; 2627 0.8; 2811 0.5; 3008 0.7; 3219 1.4; 3444 2.6; 3685 3.2; 3943 3.2; 4219 2.0; 4514 0.8; 4830 -0.0; 5168 -1.1; 5530 -3.9; 5917 -8.1; 6331 -7.0; 6775 -2.3; 7249 0.6; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.0dB` and instead set Global volume in the UI for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thinksound ts01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 16 Hz   | 0.2  | -6.4 dB  |
| Peaking | 188 Hz  | 0.6  | -9.1 dB  |
| Peaking | 7166 Hz | 5.68 | 2.9 dB   |
| Peaking | 4291 Hz | 0.86 | 3.3 dB   |
| Peaking | 6098 Hz | 3.65 | -11.4 dB |
| Peaking | 131 Hz  | 2.33 | -1.1 dB  |
| Peaking | 408 Hz  | 0.88 | -3.6 dB  |
| Peaking | 456 Hz  | 0.41 | 2.9 dB   |
| Peaking | 3273 Hz | 1.66 | -2.1 dB  |
| Peaking | 3677 Hz | 4.32 | 2.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Thinksound%20ts01/Thinksound%20ts01.png)