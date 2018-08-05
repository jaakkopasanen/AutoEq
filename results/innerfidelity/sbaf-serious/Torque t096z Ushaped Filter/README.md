# Torque t096z Ushaped Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 10 -84; 20 -12.2; 22 -12.2; 23 -12.2; 25 -12.1; 26 -12.1; 28 -12.0; 30 -11.9; 32 -11.8; 35 -11.6; 37 -11.5; 40 -11.3; 42 -11.1; 45 -10.9; 49 -10.6; 52 -10.4; 56 -10.1; 59 -10.0; 64 -9.7; 68 -9.4; 73 -9.2; 78 -9.1; 83 -9.0; 89 -9.0; 95 -9.1; 102 -9.2; 109 -9.3; 117 -9.4; 125 -9.7; 134 -9.6; 143 -9.6; 153 -9.4; 164 -9.1; 175 -8.7; 188 -8.3; 201 -7.9; 215 -7.4; 230 -6.9; 246 -6.5; 263 -6.1; 282 -5.5; 301 -5.1; 323 -4.6; 345 -4.0; 369 -3.6; 395 -3.1; 423 -2.5; 452 -2.2; 484 -1.8; 518 -1.4; 554 -0.9; 593 -0.4; 635 -0.0; 679 0.1; 726 0.4; 777 0.6; 832 0.6; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -0.9; 1336 -1.5; 1429 -2.1; 1529 -2.8; 1636 -3.4; 1751 -3.9; 1873 -4.3; 2004 -4.5; 2145 -5.2; 2295 -5.9; 2455 -6.6; 2627 -6.9; 2811 -6.8; 3008 -5.6; 3219 -4.0; 3444 -2.6; 3685 -2.6; 3943 -3.8; 4219 -6.8; 4514 -9.9; 4830 -10.4; 5168 -6.5; 5530 -1.8; 5917 2.1; 6331 3.9; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 -2.1; 10879 -4.3; 11640 -2.7; 12455 -0.1; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.9dB` and instead set Global volume in the UI for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Ushaped Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 8 Hz     | 0.84 | -11.9 dB |
| Peaking | 31 Hz    | 0.31 | -10.2 dB |
| Peaking | 171 Hz   | 0.81 | -6.3 dB  |
| Peaking | 2475 Hz  | 1.83 | -6.9 dB  |
| Peaking | 4669 Hz  | 6.34 | -10.8 dB |
| Peaking | 800 Hz   | 2.13 | 1.7 dB   |
| Peaking | 1627 Hz  | 4.27 | -1.5 dB  |
| Peaking | 5131 Hz  | 7.78 | -3.2 dB  |
| Peaking | 6398 Hz  | 4.15 | 5.7 dB   |
| Peaking | 10985 Hz | 6.33 | -4.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Ushaped%20Filter/Torque%20t096z%20Ushaped%20Filter.png)