# NuForce Primo 8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 5.8; 22 5.6; 23 5.6; 25 5.5; 26 5.4; 28 5.3; 30 5.2; 32 5.2; 35 5.1; 37 5.0; 40 5.0; 42 4.9; 45 4.9; 49 4.9; 52 4.8; 56 4.7; 59 4.6; 64 4.6; 68 4.5; 73 4.4; 78 4.2; 83 3.9; 89 3.5; 95 3.1; 102 2.5; 109 2.0; 117 1.4; 125 0.8; 134 0.3; 143 -0.1; 153 -0.3; 164 -0.5; 175 -0.6; 188 -0.7; 201 -0.7; 215 -0.6; 230 -0.6; 246 -0.6; 263 -0.5; 282 -0.4; 301 -0.3; 323 -0.3; 345 -0.2; 369 -0.1; 395 -0.0; 423 0.2; 452 0.3; 484 0.4; 518 0.4; 554 0.6; 593 0.9; 635 1.0; 679 0.9; 726 0.9; 777 1.1; 832 0.9; 890 0.6; 952 0.3; 1019 -0.0; 1090 -0.3; 1167 -0.7; 1248 -1.1; 1336 -1.6; 1429 -2.3; 1529 -3.0; 1636 -3.6; 1751 -4.0; 1873 -4.1; 2004 -3.7; 2145 -2.6; 2295 -0.9; 2455 1.5; 2627 3.7; 2811 5.7; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.7; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 3.9; 6775 2.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce Primo 8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.75 | 5.6 dB  |
| Peaking | 71 Hz   | 1.74 | 3.3 dB  |
| Peaking | 749 Hz  | 2.42 | 1.2 dB  |
| Peaking | 1888 Hz | 1.63 | -8.1 dB |
| Peaking | 3444 Hz | 0.87 | 8.3 dB  |
| Peaking | 197 Hz  | 1.85 | -1.2 dB |
| Peaking | 2834 Hz | 5.94 | 2.2 dB  |
| Peaking | 3576 Hz | 1.62 | -1.2 dB |
| Peaking | 5808 Hz | 2.39 | 4.2 dB  |
| Peaking | 7429 Hz | 1.23 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NuForce%20Primo%208/NuForce%20Primo%208.png)