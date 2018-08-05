# Torque t103z Deep

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -9.2; 22 -9.3; 23 -9.4; 25 -9.5; 26 -9.5; 28 -9.5; 30 -9.5; 32 -9.6; 35 -9.6; 37 -9.5; 40 -9.5; 42 -9.5; 45 -9.4; 49 -9.3; 52 -9.3; 56 -9.2; 59 -9.1; 64 -9.0; 68 -9.0; 73 -8.9; 78 -9.0; 83 -9.0; 89 -9.2; 95 -9.4; 102 -9.7; 109 -9.9; 117 -10.2; 125 -10.5; 134 -10.7; 143 -10.7; 153 -10.6; 164 -10.4; 175 -10.0; 188 -9.7; 201 -9.4; 215 -8.9; 230 -8.5; 246 -8.1; 263 -7.6; 282 -7.1; 301 -6.6; 323 -6.1; 345 -5.6; 369 -5.1; 395 -4.6; 423 -4.0; 452 -3.4; 484 -3.1; 518 -2.6; 554 -2.0; 593 -1.4; 635 -1.1; 679 -0.4; 726 0.3; 777 0.4; 832 0.5; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.4; 1248 -0.6; 1336 -1.0; 1429 -1.6; 1529 -2.1; 1636 -2.6; 1751 -2.9; 1873 -3.1; 2004 -3.2; 2145 -2.9; 2295 -2.0; 2455 -0.0; 2627 2.0; 2811 3.9; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t103z Deep ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.42 | -8.7 dB |
| Peaking | 164 Hz  | 0.51 | -9.2 dB |
| Peaking | 771 Hz  | 1.9  | 2.1 dB  |
| Peaking | 2008 Hz | 1.77 | -6.5 dB |
| Peaking | 3745 Hz | 0.91 | 7.9 dB  |
| Peaking | 2335 Hz | 8.67 | -0.8 dB |
| Peaking | 2994 Hz | 6.39 | 1.7 dB  |
| Peaking | 3912 Hz | 3.38 | -1.2 dB |
| Peaking | 6297 Hz | 2.42 | 5.4 dB  |
| Peaking | 7339 Hz | 1.53 | -4.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t103z%20Deep/Torque%20t103z%20Deep.png)