# Tekfusion Twinwoofers

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -10.1; 22 -10.2; 23 -10.2; 25 -10.2; 26 -10.3; 28 -10.3; 30 -10.4; 32 -10.4; 35 -10.3; 37 -10.2; 40 -10.2; 42 -10.2; 45 -10.1; 49 -10.0; 52 -10.0; 56 -9.9; 59 -9.8; 64 -9.8; 68 -9.7; 73 -9.7; 78 -9.7; 83 -9.8; 89 -10.0; 95 -10.2; 102 -10.5; 109 -10.7; 117 -11.0; 125 -11.3; 134 -11.5; 143 -11.5; 153 -11.4; 164 -11.1; 175 -10.8; 188 -10.4; 201 -10.0; 215 -9.5; 230 -9.0; 246 -8.5; 263 -8.0; 282 -7.3; 301 -6.8; 323 -6.1; 345 -5.4; 369 -4.8; 395 -4.1; 423 -3.3; 452 -2.6; 484 -2.0; 518 -1.4; 554 -0.8; 593 -0.2; 635 -0.0; 679 -0.1; 726 -0.4; 777 -0.4; 832 0.6; 890 0.9; 952 0.3; 1019 -0.0; 1090 -0.2; 1167 -0.2; 1248 -0.1; 1336 -0.1; 1429 -0.0; 1529 0.1; 1636 0.4; 1751 1.0; 1873 1.6; 2004 2.4; 2145 3.2; 2295 4.0; 2455 5.0; 2627 5.8; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 5.5; 3943 3.7; 4219 1.3; 4514 -1.0; 4830 -2.7; 5168 -4.2; 5530 -3.5; 5917 -1.9; 6331 1.2; 6775 2.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tekfusion Twinwoofers ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.17 | -9.9 dB |
| Peaking | 178 Hz  | 0.78 | -7.5 dB |
| Peaking | 3268 Hz | 1.3  | 8.1 dB  |
| Peaking | 5181 Hz | 2.1  | -7.6 dB |
| Peaking | 6643 Hz | 4.91 | 4.5 dB  |
| Peaking | 327 Hz  | 2.92 | -0.9 dB |
| Peaking | 874 Hz  | 5.88 | 1.5 dB  |
| Peaking | 598 Hz  | 3.12 | 1.5 dB  |
| Peaking | 1506 Hz | 1.36 | -0.9 dB |
| Peaking | 2418 Hz | 4.39 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Tekfusion%20Twinwoofers/Tekfusion%20Twinwoofers.png)