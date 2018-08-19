# Torque t096z Ushaped Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 10 -84; 20 -12.3; 22 -12.3; 23 -12.2; 25 -12.2; 26 -12.2; 28 -12.1; 30 -12.1; 32 -12.0; 35 -11.9; 37 -11.8; 40 -11.7; 42 -11.6; 45 -11.5; 49 -11.3; 52 -11.2; 56 -11.1; 59 -11.1; 64 -10.9; 68 -10.8; 73 -10.8; 78 -10.7; 83 -10.6; 89 -10.5; 95 -10.5; 102 -10.3; 109 -10.0; 117 -9.8; 125 -9.7; 134 -9.4; 143 -9.2; 153 -8.9; 164 -8.6; 175 -8.2; 188 -7.8; 201 -7.5; 215 -7.0; 230 -6.6; 246 -6.3; 263 -5.8; 282 -5.3; 301 -4.9; 323 -4.5; 345 -3.9; 369 -3.5; 395 -3.1; 423 -2.5; 452 -2.1; 484 -1.8; 518 -1.4; 554 -0.9; 593 -0.3; 635 -0.0; 679 0.1; 726 0.4; 777 0.7; 832 0.6; 890 0.4; 952 0.3; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -0.9; 1336 -1.5; 1429 -2.1; 1529 -2.8; 1636 -3.4; 1751 -3.9; 1873 -4.3; 2004 -4.5; 2145 -5.2; 2295 -5.9; 2455 -6.6; 2627 -6.9; 2811 -6.8; 3008 -5.6; 3219 -4.0; 3444 -2.6; 3685 -2.6; 3943 -3.8; 4219 -6.8; 4514 -9.9; 4830 -10.4; 5168 -6.5; 5530 -1.8; 5917 2.1; 6331 3.9; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 -2.1; 10879 -4.3; 11640 -2.7; 12455 -0.1; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.439138965438316dB` and instead set Global volume in the UI for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Ushaped Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.7dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.21 | -12.0 dB |
| Peaking | 164 Hz   | 0.73 | -4.2 dB  |
| Peaking | 2460 Hz  | 1.77 | -6.6 dB  |
| Peaking | 4746 Hz  | 4.45 | -11.1 dB |
| Peaking | 6370 Hz  | 4.47 | 6.3 dB   |
| Peaking | 329 Hz   | 1.74 | -0.9 dB  |
| Peaking | 779 Hz   | 1.4  | 1.7 dB   |
| Peaking | 1622 Hz  | 3.98 | -1.5 dB  |
| Peaking | 10998 Hz | 1.45 | 1.2 dB   |
| Peaking | 11023 Hz | 4.82 | -5.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Ushaped%20Filter/Torque%20t096z%20Ushaped%20Filter.png)