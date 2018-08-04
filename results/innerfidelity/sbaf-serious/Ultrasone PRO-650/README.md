# Ultrasone PRO-650

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.8; 35 5.2; 37 4.8; 40 4.2; 42 4.0; 45 3.8; 49 3.7; 52 3.6; 56 3.7; 59 4.0; 64 3.9; 68 3.2; 73 2.5; 78 2.0; 83 1.7; 89 1.6; 95 1.6; 102 1.3; 109 1.2; 117 0.9; 125 0.8; 134 0.6; 143 0.7; 153 0.9; 164 1.4; 175 1.4; 188 1.6; 201 1.9; 215 2.2; 230 2.5; 246 2.8; 263 3.1; 282 3.1; 301 2.8; 323 2.5; 345 2.0; 369 1.2; 395 0.3; 423 -0.3; 452 -0.3; 484 1.2; 518 2.1; 554 1.4; 593 1.8; 635 2.2; 679 1.4; 726 1.8; 777 1.4; 832 0.7; 890 0.4; 952 0.1; 1019 -0.1; 1090 -0.4; 1167 -0.1; 1248 -0.2; 1336 -0.6; 1429 -1.1; 1529 -1.6; 1636 -1.9; 1751 -1.3; 1873 0.2; 2004 2.5; 2145 2.6; 2295 5.6; 2455 5.0; 2627 0.7; 2811 0.3; 3008 1.2; 3219 0.3; 3444 -0.6; 3685 -0.4; 3943 -0.8; 4219 -0.1; 4514 3.0; 4830 5.6; 5168 3.6; 5530 2.5; 5917 2.4; 6331 1.1; 6775 0.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -2.2; 15258 -5.3; 16326 -4.8; 17469 -2.1; 18692 -0.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO-650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.87 | 4.7 dB  |
| Peaking | 48 Hz    | 0.06 | 1.6 dB  |
| Peaking | 4997 Hz  | 4.75 | 5.2 dB  |
| Peaking | 13576 Hz | 2.15 | 2.0 dB  |
| Peaking | 15614 Hz | 2.4  | -6.7 dB |
| Peaking | 280 Hz   | 3.23 | 1.8 dB  |
| Peaking | 425 Hz   | 7.66 | -2.1 dB |
| Peaking | 1571 Hz  | 3.32 | -2.6 dB |
| Peaking | 2313 Hz  | 5.9  | 6.2 dB  |
| Peaking | 3887 Hz  | 5.53 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20PRO-650/Ultrasone%20PRO-650.png)