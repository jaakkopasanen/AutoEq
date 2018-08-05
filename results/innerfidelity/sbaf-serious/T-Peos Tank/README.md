# T-Peos Tank

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 10 -84; 20 -10.0; 22 -9.9; 23 -9.8; 25 -9.7; 26 -9.7; 28 -9.6; 30 -9.5; 32 -9.4; 35 -9.2; 37 -9.1; 40 -8.9; 42 -8.8; 45 -8.6; 49 -8.4; 52 -8.2; 56 -8.0; 59 -7.8; 64 -7.5; 68 -7.4; 73 -7.2; 78 -7.1; 83 -7.0; 89 -7.0; 95 -7.2; 102 -7.3; 109 -7.4; 117 -7.6; 125 -7.8; 134 -7.9; 143 -7.9; 153 -7.7; 164 -7.5; 175 -7.1; 188 -6.7; 201 -6.4; 215 -5.9; 230 -5.4; 246 -5.0; 263 -4.6; 282 -4.1; 301 -3.7; 323 -3.3; 345 -2.8; 369 -2.4; 395 -2.0; 423 -1.5; 452 -1.1; 484 -0.8; 518 -0.5; 554 -0.1; 593 0.4; 635 0.6; 679 0.7; 726 0.8; 777 1.0; 832 0.8; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -0.8; 1248 -1.4; 1336 -2.2; 1429 -3.2; 1529 -4.3; 1636 -5.1; 1751 -5.8; 1873 -6.1; 2004 -6.3; 2145 -6.2; 2295 -5.3; 2455 -3.5; 2627 -1.5; 2811 0.5; 3008 2.7; 3219 4.2; 3444 5.2; 3685 4.9; 3943 3.5; 4219 0.6; 4514 -2.3; 4830 -5.6; 5168 -8.9; 5530 -7.7; 5917 -3.1; 6331 -0.4; 6775 0.7; 7249 0.2; 7756 -1.9; 8299 -4.2; 8880 -5.2; 9502 -4.4; 10167 -2.2; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.8dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Tank ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 9 Hz    | 0.75 | -9.5 dB  |
| Peaking | 34 Hz   | 0.35 | -7.7 dB  |
| Peaking | 164 Hz  | 0.92 | -5.5 dB  |
| Peaking | 1892 Hz | 2.9  | -7.2 dB  |
| Peaking | 8895 Hz | 3.33 | -5.3 dB  |
| Peaking | 730 Hz  | 2.5  | 1.8 dB   |
| Peaking | 2350 Hz | 4.2  | -3.3 dB  |
| Peaking | 3546 Hz | 2.37 | 7.6 dB   |
| Peaking | 5257 Hz | 3.41 | -11.6 dB |
| Peaking | 6563 Hz | 3.19 | 4.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Tank/T-Peos%20Tank.png)