# HiFiMAN HE-500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.5dB
GraphicEQ: 10 -84; 20 4.0; 22 3.5; 23 3.3; 25 2.9; 26 2.8; 28 2.6; 30 2.5; 32 2.4; 35 2.4; 37 2.4; 40 2.4; 42 2.4; 45 2.4; 49 2.5; 52 2.5; 56 2.5; 59 2.5; 64 2.4; 68 2.3; 73 2.3; 78 2.2; 83 2.1; 89 1.9; 95 1.6; 102 1.3; 109 1.1; 117 0.8; 125 0.3; 134 0.1; 143 -0.1; 153 -0.3; 164 -0.3; 175 -0.3; 188 -0.2; 201 -0.4; 215 -0.4; 230 -0.3; 246 -0.3; 263 -0.5; 282 -0.5; 301 -0.4; 323 -0.3; 345 -0.3; 369 -0.5; 395 -0.8; 423 -0.5; 452 -0.2; 484 -0.4; 518 -0.4; 554 -0.1; 593 -0.1; 635 -0.1; 679 -0.0; 726 0.0; 777 0.8; 832 0.7; 890 -0.0; 952 -0.1; 1019 -0.1; 1090 -0.0; 1167 0.1; 1248 0.1; 1336 1.0; 1429 1.0; 1529 1.1; 1636 1.5; 1751 2.0; 1873 2.9; 2004 2.3; 2145 2.2; 2295 2.2; 2455 2.6; 2627 2.3; 2811 2.2; 3008 2.1; 3219 1.4; 3444 1.3; 3685 1.2; 3943 1.4; 4219 -0.1; 4514 -0.5; 4830 0.6; 5168 2.2; 5530 3.2; 5917 2.0; 6331 0.9; 6775 1.0; 7249 1.0; 7756 -0.3; 8299 -3.0; 8880 -5.5; 9502 -5.0; 10167 -1.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.1; 18692 -2.7; 20000 -6.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.5dB` and instead set Global volume in the UI for both channels to **-45**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 19 Hz   |  0.64 | 3.5 dB  |
| Peaking | 67 Hz   |  1.53 | 2.0 dB  |
| Peaking | 2289 Hz |  1.41 | 2.7 dB  |
| Peaking | 5578 Hz |  5.65 | 3.2 dB  |
| Peaking | 9049 Hz |  5.85 | -6.6 dB |
| Peaking | 99 Hz   |  2.26 | 0.9 dB  |
| Peaking | 210 Hz  |  0.76 | -1.5 dB |
| Peaking | 233 Hz  |  1.39 | 1.0 dB  |
| Peaking | 4459 Hz | 11.49 | -1.6 dB |
| Peaking | 7171 Hz |  8.8  | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-500/HiFiMAN%20HE-500.png)