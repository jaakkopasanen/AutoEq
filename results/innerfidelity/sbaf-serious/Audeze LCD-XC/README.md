# Audeze LCD-XC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.5; 22 4.5; 23 4.6; 25 4.6; 26 4.7; 28 4.8; 30 4.9; 32 4.9; 35 4.6; 37 4.4; 40 4.3; 42 4.3; 45 4.3; 49 4.2; 52 4.1; 56 3.7; 59 3.1; 64 2.4; 68 2.2; 73 2.1; 78 2.0; 83 1.8; 89 1.6; 95 1.4; 102 1.2; 109 1.0; 117 0.6; 125 0.3; 134 0.1; 143 0.0; 153 0.1; 164 0.1; 175 -0.2; 188 -0.1; 201 0.1; 215 0.3; 230 0.6; 246 0.8; 263 1.1; 282 1.4; 301 1.5; 323 1.7; 345 1.9; 369 2.1; 395 2.1; 423 2.2; 452 2.1; 484 1.9; 518 1.8; 554 2.1; 593 2.2; 635 2.3; 679 2.0; 726 1.7; 777 1.4; 832 1.0; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.7; 1167 -1.1; 1248 -1.7; 1336 -2.3; 1429 -3.1; 1529 -3.7; 1636 -4.2; 1751 -4.2; 1873 -3.9; 2004 -3.1; 2145 -1.8; 2295 -0.8; 2455 0.5; 2627 1.7; 2811 2.0; 3008 2.8; 3219 3.1; 3444 2.9; 3685 2.2; 3943 0.9; 4219 -0.2; 4514 0.4; 4830 0.6; 5168 3.0; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -0.3; 14260 -1.6; 15258 -1.4; 16326 -1.4; 17469 -2.7; 18692 -4.0; 20000 -4.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-XC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.69 | 5.2 dB  |
| Peaking | 546 Hz   | 0.93 | 2.5 dB  |
| Peaking | 1695 Hz  | 1.65 | -5.0 dB |
| Peaking | 3004 Hz  | 2.65 | 3.9 dB  |
| Peaking | 5965 Hz  | 4.2  | 6.8 dB  |
| Peaking | 175 Hz   | 2.03 | -0.9 dB |
| Peaking | 312 Hz   | 2.68 | 0.6 dB  |
| Peaking | 4442 Hz  | 3.88 | -3.3 dB |
| Peaking | 4453 Hz  | 1.91 | 1.9 dB  |
| Peaking | 19423 Hz | 0.98 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-XC/Audeze%20LCD-XC.png)