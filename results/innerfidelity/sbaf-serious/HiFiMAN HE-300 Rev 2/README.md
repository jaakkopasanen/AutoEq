# HiFiMAN HE-300 Rev 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 5.9; 25 5.4; 26 5.0; 28 4.3; 30 3.4; 32 2.7; 35 1.6; 37 1.0; 40 0.2; 42 -0.3; 45 -1.0; 49 -1.6; 52 -1.9; 56 -2.3; 59 -2.5; 64 -2.8; 68 -3.2; 73 -3.9; 78 -4.3; 83 -4.5; 89 -4.7; 95 -5.1; 102 -5.3; 109 -5.3; 117 -5.2; 125 -5.1; 134 -4.9; 143 -4.7; 153 -4.4; 164 -3.8; 175 -3.6; 188 -3.4; 201 -3.1; 215 -2.7; 230 -2.7; 246 -3.4; 263 -3.2; 282 -2.4; 301 -2.0; 323 -1.6; 345 -1.2; 369 -0.9; 395 -0.6; 423 -0.2; 452 0.1; 484 0.3; 518 0.7; 554 1.3; 593 1.6; 635 1.7; 679 1.9; 726 2.1; 777 1.6; 832 0.9; 890 0.5; 952 0.1; 1019 -0.1; 1090 -0.6; 1167 -1.1; 1248 -1.6; 1336 -2.2; 1429 -3.0; 1529 -3.5; 1636 -4.0; 1751 -3.3; 1873 -4.4; 2004 -4.9; 2145 -4.4; 2295 -4.2; 2455 -3.7; 2627 -3.8; 2811 -4.0; 3008 -5.4; 3219 -6.0; 3444 -5.2; 3685 -4.2; 3943 -3.9; 4219 -4.6; 4514 -5.7; 4830 -6.1; 5168 -5.3; 5530 -3.3; 5917 -0.1; 6331 1.6; 6775 1.1; 7249 0.9; 7756 0.3; 8299 0.0; 8880 -1.9; 9502 -3.5; 10167 -2.3; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-300 Rev 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.43 | 6.6 dB  |
| Peaking | 109 Hz   | 0.72 | -5.6 dB |
| Peaking | 1910 Hz  | 2.08 | -3.8 dB |
| Peaking | 3809 Hz  | 1.36 | -5.2 dB |
| Peaking | 23479 Hz | 2.42 | -3.8 dB |
| Peaking | 258 Hz   | 4.89 | -1.5 dB |
| Peaking | 668 Hz   | 2.22 | 2.7 dB  |
| Peaking | 5152 Hz  | 4.14 | -5.4 dB |
| Peaking | 6153 Hz  | 1.97 | 4.3 dB  |
| Peaking | 9525 Hz  | 6.01 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-300%20Rev%202/HiFiMAN%20HE-300%20Rev%202.png)