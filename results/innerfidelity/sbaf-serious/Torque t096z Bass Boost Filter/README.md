# Torque t096z Bass Boost Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -11.5; 22 -11.5; 23 -11.5; 25 -11.4; 26 -11.4; 28 -11.3; 30 -11.3; 32 -11.2; 35 -11.1; 37 -11.0; 40 -10.9; 42 -10.8; 45 -10.7; 49 -10.5; 52 -10.4; 56 -10.3; 59 -10.3; 64 -10.2; 68 -10.0; 73 -10.0; 78 -9.9; 83 -9.8; 89 -9.7; 95 -9.7; 102 -9.5; 109 -9.2; 117 -9.0; 125 -8.7; 134 -8.5; 143 -8.3; 153 -8.1; 164 -7.8; 175 -7.4; 188 -7.0; 201 -6.7; 215 -6.3; 230 -5.8; 246 -5.4; 263 -5.1; 282 -4.5; 301 -4.1; 323 -3.7; 345 -3.2; 369 -2.7; 395 -2.4; 423 -1.8; 452 -1.4; 484 -1.1; 518 -0.7; 554 -0.2; 593 0.3; 635 0.5; 679 0.6; 726 0.7; 777 1.0; 832 0.9; 890 0.7; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.5; 1336 -2.3; 1429 -3.2; 1529 -4.2; 1636 -5.3; 1751 -6.3; 1873 -7.2; 2004 -7.5; 2145 -7.2; 2295 -5.7; 2455 -3.1; 2627 -0.8; 2811 1.2; 3008 3.5; 3219 4.5; 3444 5.1; 3685 3.8; 3943 1.6; 4219 -1.4; 4514 -1.2; 4830 2.1; 5168 5.7; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.096025095977879dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Bass Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.23 | -11.2 dB |
| Peaking | 157 Hz   | 0.8  | -4.0 dB  |
| Peaking | 1986 Hz  | 2.34 | -8.5 dB  |
| Peaking | 3234 Hz  | 3.97 | 6.5 dB   |
| Peaking | 5846 Hz  | 3.73 | 7.0 dB   |
| Peaking | 769 Hz   | 1.88 | 2.0 dB   |
| Peaking | 1513 Hz  | 4.57 | -1.2 dB  |
| Peaking | 4397 Hz  | 6.43 | -6.9 dB  |
| Peaking | 4495 Hz  | 2.71 | 3.2 dB   |
| Peaking | 24000 Hz | 1.72 | 0.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Bass%20Boost%20Filter/Torque%20t096z%20Bass%20Boost%20Filter.png)