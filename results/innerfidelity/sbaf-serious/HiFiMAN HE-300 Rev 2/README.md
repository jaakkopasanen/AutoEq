# HiFiMAN HE-300 Rev 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 5.9; 25 5.4; 26 5.1; 28 4.3; 30 3.5; 32 2.7; 35 1.7; 37 1.1; 40 0.3; 42 -0.2; 45 -0.8; 49 -1.4; 52 -1.6; 56 -1.9; 59 -2.1; 64 -2.3; 68 -2.6; 73 -3.2; 78 -3.5; 83 -3.7; 89 -3.9; 95 -4.4; 102 -4.7; 109 -4.9; 117 -5.0; 125 -5.1; 134 -5.0; 143 -4.9; 153 -4.6; 164 -4.1; 175 -3.8; 188 -3.6; 201 -3.3; 215 -2.9; 230 -2.9; 246 -3.5; 263 -3.2; 282 -2.5; 301 -2.0; 323 -1.6; 345 -1.2; 369 -0.9; 395 -0.6; 423 -0.2; 452 0.0; 484 0.3; 518 0.7; 554 1.2; 593 1.6; 635 1.7; 679 1.9; 726 2.1; 777 1.6; 832 0.9; 890 0.5; 952 0.1; 1019 -0.1; 1090 -0.6; 1167 -1.1; 1248 -1.6; 1336 -2.2; 1429 -3.0; 1529 -3.5; 1636 -4.0; 1751 -3.3; 1873 -4.4; 2004 -4.9; 2145 -4.4; 2295 -4.2; 2455 -3.7; 2627 -3.8; 2811 -4.0; 3008 -5.4; 3219 -6.0; 3444 -5.2; 3685 -4.2; 3943 -3.9; 4219 -4.6; 4514 -5.7; 4830 -6.1; 5168 -5.3; 5530 -3.3; 5917 -0.1; 6331 1.6; 6775 1.1; 7249 0.9; 7756 0.3; 8299 0.0; 8880 -1.9; 9502 -3.5; 10167 -2.3; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-300 Rev 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.63 | 6.6 dB  |
| Peaking | 118 Hz   | 0.76 | -5.3 dB |
| Peaking | 1913 Hz  | 2.08 | -3.8 dB |
| Peaking | 3809 Hz  | 1.36 | -5.2 dB |
| Peaking | 23493 Hz | 2.42 | -3.8 dB |
| Peaking | 262 Hz   | 4.54 | -1.5 dB |
| Peaking | 668 Hz   | 2.22 | 2.7 dB  |
| Peaking | 5148 Hz  | 4.17 | -5.4 dB |
| Peaking | 6171 Hz  | 1.98 | 4.2 dB  |
| Peaking | 9541 Hz  | 6    | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-300%20Rev%202/HiFiMAN%20HE-300%20Rev%202.png)