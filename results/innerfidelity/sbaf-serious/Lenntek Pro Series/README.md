# Lenntek Pro Series

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 5.8; 83 5.5; 89 5.0; 95 4.6; 102 4.0; 109 3.5; 117 2.9; 125 2.3; 134 1.8; 143 1.4; 153 1.2; 164 1.0; 175 1.0; 188 0.9; 201 0.8; 215 0.9; 230 0.9; 246 0.9; 263 0.9; 282 1.0; 301 1.0; 323 1.1; 345 1.1; 369 1.2; 395 1.2; 423 1.4; 452 1.4; 484 1.3; 518 1.3; 554 1.5; 593 1.8; 635 1.8; 679 1.6; 726 1.5; 777 1.5; 832 1.2; 890 0.8; 952 0.4; 1019 -0.2; 1090 -0.7; 1167 -1.2; 1248 -1.8; 1336 -2.6; 1429 -3.6; 1529 -4.5; 1636 -5.3; 1751 -6.2; 1873 -6.7; 2004 -6.8; 2145 -6.2; 2295 -4.6; 2455 -2.0; 2627 0.5; 2811 2.5; 3008 4.3; 3219 4.8; 3444 4.7; 3685 3.7; 3943 1.3; 4219 -2.7; 4514 -3.3; 4830 0.6; 5168 5.2; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lenntek Pro Series ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 41 Hz   | 0.46 | 6.7 dB   |
| Peaking | 999 Hz  | 0.64 | 7.0 dB   |
| Peaking | 2019 Hz | 0.57 | -12.9 dB |
| Peaking | 3078 Hz | 2.25 | 13.2 dB  |
| Peaking | 5920 Hz | 2.98 | 9.2 dB   |
| Peaking | 4 Hz    | 2.42 | 0.9 dB   |
| Peaking | 85 Hz   | 2.79 | 1.3 dB   |
| Peaking | 155 Hz  | 1.95 | -1.0 dB  |
| Peaking | 4347 Hz | 2.46 | 3.7 dB   |
| Peaking | 4415 Hz | 6.82 | -8.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Lenntek%20Pro%20Series/Lenntek%20Pro%20Series.png)