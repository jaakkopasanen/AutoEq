# NuForce HEM8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.0; 22 0.9; 23 0.9; 25 0.7; 26 0.7; 28 0.6; 30 0.5; 32 0.5; 35 0.4; 37 0.4; 40 0.3; 42 0.3; 45 0.2; 49 0.1; 52 0.1; 56 0.1; 59 0.0; 64 -0.1; 68 -0.2; 73 -0.3; 78 -0.5; 83 -0.8; 89 -1.1; 95 -1.6; 102 -2.2; 109 -2.7; 117 -3.2; 125 -3.9; 134 -4.3; 143 -4.5; 153 -4.8; 164 -5.0; 175 -4.9; 188 -5.0; 201 -5.0; 215 -4.9; 230 -4.7; 246 -4.7; 263 -4.6; 282 -4.3; 301 -4.2; 323 -4.0; 345 -3.7; 369 -3.6; 395 -3.3; 423 -3.0; 452 -2.7; 484 -2.5; 518 -2.2; 554 -1.7; 593 -1.1; 635 -0.7; 679 -0.4; 726 0.0; 777 0.4; 832 0.6; 890 0.5; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.6; 1248 -0.7; 1336 -0.5; 1429 0.3; 1529 1.4; 1636 3.0; 1751 4.6; 1873 5.9; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 5.7; 5917 4.8; 6331 3.9; 6775 3.8; 7249 1.3; 7756 0.3; 8299 -0.2; 8880 -2.7; 9502 -3.3; 10167 -1.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce HEM8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 83 Hz   | 0.57 | 3.6 dB  |
| Peaking | 173 Hz  | 0.49 | -7.6 dB |
| Peaking | 226 Hz  | 1.55 | 0.9 dB  |
| Peaking | 3594 Hz | 0.59 | 6.9 dB  |
| Peaking | 9163 Hz | 3.08 | -5.5 dB |
| Peaking | 19 Hz   | 1.53 | 0.9 dB  |
| Peaking | 804 Hz  | 2.37 | 1.4 dB  |
| Peaking | 1355 Hz | 1.83 | -3.5 dB |
| Peaking | 1873 Hz | 2.46 | 3.4 dB  |
| Peaking | 3427 Hz | 3.73 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NuForce%20HEM8/NuForce%20HEM8.png)