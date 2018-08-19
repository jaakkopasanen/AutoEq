# Torque t402v OnEar Red

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -1.4; 22 -2.1; 23 -2.5; 25 -3.1; 26 -3.4; 28 -3.9; 30 -4.4; 32 -4.8; 35 -5.3; 37 -5.6; 40 -6.1; 42 -6.3; 45 -6.6; 49 -7.0; 52 -7.2; 56 -7.6; 59 -7.8; 64 -8.1; 68 -8.4; 73 -8.6; 78 -8.8; 83 -8.9; 89 -9.2; 95 -9.5; 102 -9.9; 109 -10.2; 117 -10.5; 125 -10.7; 134 -10.8; 143 -10.9; 153 -11.0; 164 -10.8; 175 -10.7; 188 -10.7; 201 -10.6; 215 -10.4; 230 -10.0; 246 -9.8; 263 -9.4; 282 -8.9; 301 -8.5; 323 -8.2; 345 -7.9; 369 -7.5; 395 -6.9; 423 -6.2; 452 -5.7; 484 -5.3; 518 -4.5; 554 -3.4; 593 -2.0; 635 -0.6; 679 0.6; 726 1.9; 777 2.9; 832 3.1; 890 2.4; 952 1.1; 1019 -0.4; 1090 -2.0; 1167 -3.2; 1248 -4.2; 1336 -4.4; 1429 -3.9; 1529 -4.9; 1636 -4.0; 1751 -2.8; 1873 -2.2; 2004 -2.3; 2145 -2.9; 2295 -3.4; 2455 -3.5; 2627 -3.4; 2811 -3.2; 3008 -2.6; 3219 -1.8; 3444 -1.1; 3685 -1.0; 3943 -1.0; 4219 -1.9; 4514 -2.1; 4830 -0.7; 5168 2.4; 5530 5.5; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0638661943366365dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OnEar Red ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 91 Hz   | 0.43 | -8.7 dB |
| Peaking | 244 Hz  | 0.94 | -6.0 dB |
| Peaking | 2285 Hz | 0.98 | -3.5 dB |
| Peaking | 5999 Hz | 3.88 | 7.4 dB  |
| Peaking | 8186 Hz | 2.89 | -0.6 dB |
| Peaking | 473 Hz  | 1.65 | -3.3 dB |
| Peaking | 811 Hz  | 2.12 | 5.3 dB  |
| Peaking | 1002 Hz | 0.4  | 1.6 dB  |
| Peaking | 1285 Hz | 2    | -4.9 dB |
| Peaking | 4516 Hz | 7.33 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OnEar%20Red/Torque%20t402v%20OnEar%20Red.png)