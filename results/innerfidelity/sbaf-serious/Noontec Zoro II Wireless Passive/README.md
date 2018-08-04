# Noontec Zoro II Wireless Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 10 -84; 20 -2.0; 22 -2.1; 23 -2.2; 25 -2.3; 26 -2.4; 28 -2.5; 30 -2.5; 32 -2.6; 35 -2.6; 37 -2.6; 40 -2.6; 42 -2.6; 45 -2.6; 49 -2.6; 52 -2.6; 56 -2.5; 59 -2.6; 64 -2.6; 68 -2.5; 73 -2.5; 78 -2.7; 83 -2.9; 89 -3.3; 95 -3.8; 102 -4.3; 109 -4.7; 117 -5.1; 125 -5.5; 134 -5.8; 143 -6.1; 153 -6.2; 164 -6.0; 175 -6.2; 188 -6.2; 201 -6.1; 215 -5.9; 230 -5.6; 246 -5.5; 263 -5.2; 282 -4.8; 301 -4.6; 323 -4.2; 345 -3.8; 369 -3.6; 395 -3.6; 423 -3.3; 452 -3.1; 484 -2.9; 518 -2.7; 554 -2.2; 593 -1.6; 635 -1.2; 679 -0.9; 726 -0.6; 777 -0.1; 832 -0.2; 890 -0.0; 952 0.0; 1019 0.1; 1090 0.0; 1167 -0.1; 1248 -0.5; 1336 -0.9; 1429 -1.4; 1529 -1.7; 1636 -1.9; 1751 -1.8; 1873 -1.5; 2004 -0.9; 2145 -0.2; 2295 0.3; 2455 0.8; 2627 1.3; 2811 1.7; 3008 2.0; 3219 1.7; 3444 2.1; 3685 3.5; 3943 5.5; 4219 4.8; 4514 3.1; 4830 1.7; 5168 1.2; 5530 2.4; 5917 5.2; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.3dB` and instead set Global volume in the UI for both channels to **-63**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro II Wireless Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.25 | -1.9 dB |
| Peaking | 40 Hz   | 1.87 | -1.1 dB |
| Peaking | 182 Hz  | 0.58 | -6.2 dB |
| Peaking | 3982 Hz | 3.84 | 5.3 dB  |
| Peaking | 6247 Hz | 5.45 | 5.9 dB  |
| Peaking | 495 Hz  | 2.01 | -1.2 dB |
| Peaking | 927 Hz  | 0.76 | 1.4 dB  |
| Peaking | 1647 Hz | 2.08 | -2.4 dB |
| Peaking | 2729 Hz | 3.28 | 1.6 dB  |
| Peaking | 3551 Hz | 0.24 | -0.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro%20II%20Wireless%20Passive/Noontec%20Zoro%20II%20Wireless%20Passive.png)