# Ultrasone Signature Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 5.3; 22 4.4; 23 4.0; 25 3.2; 26 2.8; 28 2.2; 30 1.7; 32 1.3; 35 0.8; 37 0.6; 40 0.2; 42 0.1; 45 -0.2; 49 -0.4; 52 -0.5; 56 -0.5; 59 -0.5; 64 -0.5; 68 -0.3; 73 0.4; 78 1.0; 83 0.9; 89 -0.2; 95 -1.1; 102 -1.6; 109 -1.4; 117 -1.1; 125 -1.8; 134 -2.6; 143 -3.1; 153 -3.3; 164 -2.7; 175 -2.7; 188 -3.2; 201 -3.2; 215 -3.1; 230 -2.8; 246 -2.7; 263 -2.3; 282 -1.8; 301 -1.5; 323 -1.2; 345 -1.0; 369 -0.9; 395 -0.9; 423 -0.9; 452 -1.0; 484 -1.3; 518 -1.4; 554 -1.5; 593 -1.4; 635 -1.4; 679 -1.5; 726 -1.3; 777 -1.1; 832 -1.0; 890 -0.9; 952 -0.4; 1019 0.2; 1090 0.8; 1167 1.1; 1248 0.9; 1336 0.5; 1429 0.3; 1529 0.8; 1636 1.9; 1751 2.5; 1873 3.1; 2004 3.8; 2145 5.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.8; 4219 5.6; 4514 5.8; 4830 5.4; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.7; 10167 -2.4; 10879 -3.1; 11640 -2.8; 12455 -1.7; 13327 -0.2; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Signature Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 1.87 | 5.1 dB  |
| Peaking | 180 Hz   | 1.21 | -3.2 dB |
| Peaking | 1104 Hz  | 0.54 | -4.4 dB |
| Peaking | 3698 Hz  | 0.3  | 8.3 dB  |
| Peaking | 10202 Hz | 1.08 | -7.1 dB |
| Peaking | 79 Hz    | 7.86 | 1.6 dB  |
| Peaking | 1492 Hz  | 7.59 | -1.4 dB |
| Peaking | 2338 Hz  | 6.06 | 1.4 dB  |
| Peaking | 6129 Hz  | 3.81 | 4.0 dB  |
| Peaking | 6327 Hz  | 1.89 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20Signature%20Pro/Ultrasone%20Signature%20Pro.png)