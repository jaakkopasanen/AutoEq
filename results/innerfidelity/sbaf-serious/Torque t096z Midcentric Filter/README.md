# Torque t096z Midcentric Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 10 -84; 20 6.2; 22 5.8; 23 5.6; 25 5.3; 26 5.2; 28 4.9; 30 4.6; 32 4.4; 35 4.1; 37 4.0; 40 3.7; 42 3.6; 45 3.4; 49 3.1; 52 2.9; 56 2.6; 59 2.4; 64 2.1; 68 1.8; 73 1.4; 78 1.1; 83 0.9; 89 0.5; 95 0.1; 102 -0.1; 109 -0.3; 117 -0.5; 125 -0.8; 134 -1.1; 143 -1.3; 153 -1.4; 164 -1.6; 175 -1.7; 188 -1.8; 201 -2.0; 215 -1.9; 230 -1.8; 246 -1.9; 263 -1.9; 282 -1.7; 301 -1.7; 323 -1.6; 345 -1.4; 369 -1.3; 395 -1.1; 423 -0.8; 452 -0.6; 484 -0.5; 518 -0.3; 554 -0.1; 593 0.4; 635 0.5; 679 0.5; 726 0.6; 777 0.8; 832 0.7; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -1.1; 1429 -1.7; 1529 -1.9; 1636 -2.3; 1751 -2.2; 1873 -1.8; 2004 -1.6; 2145 -1.3; 2295 -0.7; 2455 0.4; 2627 0.8; 2811 1.2; 3008 2.0; 3219 2.4; 3444 1.8; 3685 0.2; 3943 -1.7; 4219 -3.9; 4514 -4.2; 4830 -2.7; 5168 0.2; 5530 2.7; 5917 4.5; 6331 5.2; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.6; 10167 -1.8; 10879 -1.9; 11640 -0.8; 12455 -0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.345871656789916dB` and instead set Global volume in the UI for both channels to **-63**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Midcentric Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 1.36 | 5.8 dB   |
| Peaking | 47 Hz    | 1.99 | 2.5 dB   |
| Peaking | 3322 Hz  | 1.78 | 11.1 dB  |
| Peaking | 4354 Hz  | 0.88 | -13.8 dB |
| Peaking | 6015 Hz  | 1.98 | 12.8 dB  |
| Peaking | 233 Hz   | 0.92 | -2.2 dB  |
| Peaking | 775 Hz   | 1.57 | 1.5 dB   |
| Peaking | 1628 Hz  | 4.11 | -1.2 dB  |
| Peaking | 10714 Hz | 5.07 | -2.0 dB  |
| Peaking | 12384 Hz | 1.3  | 1.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Midcentric%20Filter/Torque%20t096z%20Midcentric%20Filter.png)