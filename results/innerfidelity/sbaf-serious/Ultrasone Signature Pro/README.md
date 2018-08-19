# Ultrasone Signature Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.3; 22 4.4; 23 3.9; 25 3.2; 26 2.8; 28 2.2; 30 1.7; 32 1.3; 35 0.7; 37 0.5; 40 0.1; 42 -0.1; 45 -0.3; 49 -0.6; 52 -0.8; 56 -0.9; 59 -0.9; 64 -1.0; 68 -0.9; 73 -0.3; 78 0.3; 83 0.1; 89 -1.0; 95 -1.8; 102 -2.2; 109 -1.8; 117 -1.3; 125 -1.8; 134 -2.5; 143 -2.9; 153 -3.1; 164 -2.4; 175 -2.4; 188 -3.0; 201 -3.0; 215 -2.9; 230 -2.7; 246 -2.6; 263 -2.2; 282 -1.8; 301 -1.4; 323 -1.2; 345 -1.0; 369 -0.9; 395 -0.9; 423 -0.9; 452 -1.0; 484 -1.3; 518 -1.4; 554 -1.5; 593 -1.4; 635 -1.4; 679 -1.5; 726 -1.3; 777 -1.1; 832 -1.0; 890 -0.9; 952 -0.4; 1019 0.2; 1090 0.8; 1167 1.1; 1248 0.9; 1336 0.5; 1429 0.3; 1529 0.8; 1636 1.9; 1751 2.5; 1873 3.1; 2004 3.8; 2145 5.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.8; 4219 5.6; 4514 5.8; 4830 5.4; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.7; 10167 -2.4; 10879 -3.1; 11640 -2.8; 12455 -1.7; 13327 -0.2; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999999759dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Signature Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 1.84 | 5.1 dB  |
| Peaking | 164 Hz   | 1.6  | -1.6 dB |
| Peaking | 494 Hz   | 0.19 | -1.8 dB |
| Peaking | 3725 Hz  | 0.54 | 7.4 dB  |
| Peaking | 10446 Hz | 1.56 | -4.9 dB |
| Peaking | 1473 Hz  | 6.46 | -1.4 dB |
| Peaking | 2340 Hz  | 4.65 | 1.7 dB  |
| Peaking | 4468 Hz  | 1.56 | -1.8 dB |
| Peaking | 6466 Hz  | 1.54 | 3.4 dB  |
| Peaking | 7494 Hz  | 4.15 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20Signature%20Pro/Ultrasone%20Signature%20Pro.png)