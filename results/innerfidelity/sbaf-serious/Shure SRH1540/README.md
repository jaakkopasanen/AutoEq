# Shure SRH1540

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.6dB
GraphicEQ: 10 -84; 20 -3.8; 22 -4.5; 23 -4.8; 25 -5.3; 26 -5.6; 28 -6.0; 30 -6.4; 32 -6.7; 35 -7.1; 37 -7.4; 40 -7.7; 42 -7.8; 45 -8.0; 49 -8.2; 52 -8.3; 56 -8.4; 59 -8.4; 64 -8.4; 68 -8.3; 73 -8.1; 78 -7.8; 83 -7.6; 89 -7.3; 95 -7.2; 102 -7.1; 109 -7.1; 117 -7.1; 125 -7.1; 134 -6.9; 143 -6.4; 153 -5.8; 164 -4.4; 175 -4.5; 188 -4.6; 201 -4.2; 215 -3.9; 230 -3.7; 246 -3.7; 263 -3.6; 282 -3.6; 301 -3.9; 323 -4.1; 345 -4.0; 369 -3.8; 395 -3.5; 423 -3.1; 452 -2.8; 484 -2.5; 518 -2.1; 554 -1.6; 593 -1.1; 635 -0.8; 679 -0.6; 726 -0.2; 777 0.0; 832 0.1; 890 0.2; 952 0.2; 1019 -0.0; 1090 -0.1; 1167 0.1; 1248 0.2; 1336 -0.1; 1429 -0.6; 1529 -1.2; 1636 -1.9; 1751 -2.7; 1873 -3.2; 2004 -3.4; 2145 -3.1; 2295 -3.1; 2455 -2.8; 2627 -2.2; 2811 -1.6; 3008 -1.3; 3219 -1.5; 3444 -1.2; 3685 -1.2; 3943 -1.0; 4219 -0.9; 4514 -0.9; 4830 -0.4; 5168 0.4; 5530 -0.2; 5917 -3.0; 6331 -3.9; 6775 -2.3; 7249 -1.0; 7756 -0.5; 8299 -1.8; 8880 -3.6; 9502 -3.6; 10167 -1.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.642186298493957dB` and instead set Global volume in the UI for both channels to **-6**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1540 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 49 Hz    | 0.52 | -7.8 dB |
| Peaking | 129 Hz   | 1.03 | -3.3 dB |
| Peaking | 352 Hz   | 1.7  | -3.0 dB |
| Peaking | 2232 Hz  | 1.6  | -3.2 dB |
| Peaking | 504 Hz   | 3.41 | -0.9 dB |
| Peaking | 1429 Hz  | 0.64 | 1.2 dB  |
| Peaking | 1815 Hz  | 3.02 | -1.8 dB |
| Peaking | 7813 Hz  | 1.25 | -2.3 dB |
| Peaking | 24000 Hz | 2.3  | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH1540/Shure%20SRH1540.png)