# Zoukbox ZLX30

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 10 -84; 20 -9.8; 22 -9.8; 23 -9.8; 25 -9.7; 26 -9.7; 28 -9.7; 30 -9.7; 32 -9.7; 35 -9.6; 37 -9.5; 40 -9.5; 42 -9.4; 45 -9.3; 49 -9.2; 52 -9.1; 56 -9.1; 59 -9.0; 64 -8.9; 68 -8.9; 73 -8.8; 78 -8.8; 83 -8.7; 89 -8.7; 95 -8.6; 102 -8.5; 109 -8.2; 117 -8.0; 125 -7.9; 134 -7.7; 143 -7.4; 153 -7.2; 164 -6.9; 175 -6.6; 188 -6.2; 201 -5.9; 215 -5.5; 230 -5.1; 246 -4.7; 263 -4.4; 282 -3.9; 301 -3.5; 323 -3.1; 345 -2.7; 369 -2.2; 395 -1.9; 423 -1.4; 452 -1.1; 484 -0.8; 518 -0.6; 554 -0.1; 593 0.3; 635 0.6; 679 0.6; 726 0.8; 777 1.1; 832 0.9; 890 0.7; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -0.8; 1248 -1.2; 1336 -2.0; 1429 -2.7; 1529 -3.5; 1636 -4.3; 1751 -5.0; 1873 -5.8; 2004 -6.4; 2145 -7.1; 2295 -7.6; 2455 -7.2; 2627 -6.0; 2811 -3.9; 3008 -1.6; 3219 -1.0; 3444 -1.9; 3685 -4.2; 3943 -7.2; 4219 -10.0; 4514 -9.3; 4830 -4.8; 5168 1.6; 5530 4.7; 5917 5.5; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.1; 10167 -2.4; 10879 -2.2; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -1.5; 16326 -2.6; 17469 -0.4; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.678136579966278dB` and instead set Global volume in the UI for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Zoukbox ZLX30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.25 | -9.6 dB  |
| Peaking | 153 Hz   | 0.8  | -3.8 dB  |
| Peaking | 2163 Hz  | 2.18 | -7.7 dB  |
| Peaking | 4372 Hz  | 4.51 | -12.0 dB |
| Peaking | 5839 Hz  | 3.28 | 8.2 dB   |
| Peaking | 762 Hz   | 1.95 | 1.9 dB   |
| Peaking | 1558 Hz  | 4.01 | -1.5 dB  |
| Peaking | 10449 Hz | 6.46 | -3.3 dB  |
| Peaking | 12753 Hz | 0.09 | 0.2 dB   |
| Peaking | 16270 Hz | 4.38 | -3.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Zoukbox%20ZLX30/Zoukbox%20ZLX30.png)