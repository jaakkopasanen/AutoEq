# Torque t103z Deep

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -9.3; 22 -9.4; 23 -9.5; 25 -9.6; 26 -9.6; 28 -9.7; 30 -9.7; 32 -9.8; 35 -9.8; 37 -9.9; 40 -9.9; 42 -9.9; 45 -10.0; 49 -10.1; 52 -10.1; 56 -10.2; 59 -10.2; 64 -10.3; 68 -10.4; 73 -10.5; 78 -10.6; 83 -10.7; 89 -10.8; 95 -10.8; 102 -10.8; 109 -10.7; 117 -10.6; 125 -10.5; 134 -10.4; 143 -10.3; 153 -10.1; 164 -9.8; 175 -9.5; 188 -9.3; 201 -8.9; 215 -8.6; 230 -8.2; 246 -7.8; 263 -7.4; 282 -6.9; 301 -6.5; 323 -6.0; 345 -5.5; 369 -5.0; 395 -4.5; 423 -3.9; 452 -3.4; 484 -3.0; 518 -2.6; 554 -2.0; 593 -1.4; 635 -1.1; 679 -0.4; 726 0.3; 777 0.4; 832 0.5; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.4; 1248 -0.6; 1336 -1.0; 1429 -1.6; 1529 -2.1; 1636 -2.6; 1751 -2.9; 1873 -3.1; 2004 -3.2; 2145 -2.9; 2295 -2.0; 2455 -0.0; 2627 2.0; 2811 3.9; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999998715981dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t103z Deep ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 1.08 | -9.1 dB |
| Peaking | 59 Hz   | 0.33 | -9.2 dB |
| Peaking | 197 Hz  | 0.68 | -4.7 dB |
| Peaking | 2046 Hz | 1.86 | -7.5 dB |
| Peaking | 3579 Hz | 0.82 | 8.0 dB  |
| Peaking | 782 Hz  | 3.26 | 1.6 dB  |
| Peaking | 1496 Hz | 6.09 | -0.9 dB |
| Peaking | 3941 Hz | 5.85 | -1.0 dB |
| Peaking | 6258 Hz | 2.32 | 5.3 dB  |
| Peaking | 7482 Hz | 1.55 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t103z%20Deep/Torque%20t103z%20Deep.png)