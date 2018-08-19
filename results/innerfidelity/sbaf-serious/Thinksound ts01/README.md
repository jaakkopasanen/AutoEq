# Thinksound ts01

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 10 -84; 20 -6.8; 22 -6.8; 23 -6.8; 25 -6.8; 26 -6.8; 28 -6.9; 30 -6.9; 32 -6.9; 35 -7.0; 37 -7.1; 40 -7.1; 42 -7.2; 45 -7.3; 49 -7.4; 52 -7.5; 56 -7.7; 59 -7.8; 64 -8.0; 68 -8.1; 73 -8.3; 78 -8.5; 83 -8.7; 89 -9.0; 95 -9.2; 102 -9.3; 109 -9.3; 117 -9.4; 125 -9.5; 134 -9.6; 143 -9.6; 153 -9.6; 164 -9.5; 175 -9.3; 188 -9.2; 201 -9.1; 215 -8.8; 230 -8.5; 246 -8.3; 263 -8.0; 282 -7.6; 301 -7.2; 323 -6.8; 345 -6.4; 369 -5.9; 395 -5.5; 423 -4.9; 452 -4.4; 484 -4.0; 518 -3.5; 554 -2.9; 593 -2.2; 635 -1.8; 679 -1.4; 726 -0.9; 777 -0.4; 832 -0.2; 890 -0.0; 952 0.1; 1019 -0.0; 1090 0.1; 1167 0.8; 1248 1.0; 1336 0.7; 1429 0.5; 1529 0.4; 1636 0.3; 1751 0.3; 1873 0.6; 2004 0.8; 2145 0.8; 2295 0.9; 2455 0.9; 2627 0.8; 2811 0.5; 3008 0.7; 3219 1.4; 3444 2.6; 3685 3.2; 3943 3.2; 4219 2.0; 4514 0.8; 4830 -0.0; 5168 -1.1; 5530 -3.9; 5917 -8.1; 6331 -7.0; 6775 -2.3; 7249 0.6; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.553858573878305dB` and instead set Global volume in the UI for both channels to **-35**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thinksound ts01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.2dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 0.19 | -6.5 dB  |
| Peaking | 156 Hz  | 0.67 | -5.6 dB  |
| Peaking | 326 Hz  | 1.21 | -3.1 dB  |
| Peaking | 4309 Hz | 0.77 | 2.8 dB   |
| Peaking | 6017 Hz | 4.84 | -11.0 dB |
| Peaking | 1126 Hz | 1.56 | 1.0 dB   |
| Peaking | 2925 Hz | 5.16 | -1.0 dB  |
| Peaking | 3732 Hz | 5.31 | 2.1 dB   |
| Peaking | 5049 Hz | 0.44 | -0.6 dB  |
| Peaking | 7219 Hz | 7.32 | 2.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Thinksound%20ts01/Thinksound%20ts01.png)