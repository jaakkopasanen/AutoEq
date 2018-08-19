# Sennheiser PXC 550 Wired Power On

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 0.9; 22 0.3; 23 0.1; 25 -0.3; 26 -0.5; 28 -0.8; 30 -1.0; 32 -1.1; 35 -1.3; 37 -1.5; 40 -1.6; 42 -1.7; 45 -1.9; 49 -2.0; 52 -2.1; 56 -2.2; 59 -2.2; 64 -2.2; 68 -2.3; 73 -2.2; 78 -2.0; 83 -2.0; 89 -2.1; 95 -2.1; 102 -2.3; 109 -2.7; 117 -3.0; 125 -3.4; 134 -3.5; 143 -3.7; 153 -4.0; 164 -2.2; 175 -2.1; 188 -2.4; 201 -1.9; 215 -1.1; 230 0.0; 246 0.8; 263 1.4; 282 2.1; 301 2.5; 323 2.7; 345 2.8; 369 2.8; 395 2.8; 423 2.8; 452 2.8; 484 2.6; 518 2.5; 554 2.5; 593 2.6; 635 2.4; 679 2.1; 726 1.8; 777 1.6; 832 1.0; 890 0.6; 952 0.3; 1019 -0.0; 1090 -0.2; 1167 0.4; 1248 0.4; 1336 -0.9; 1429 -1.3; 1529 -2.0; 1636 -2.5; 1751 -2.2; 1873 -1.6; 2004 -1.7; 2145 -1.3; 2295 -0.7; 2455 0.2; 2627 1.2; 2811 1.6; 3008 2.4; 3219 3.1; 3444 3.4; 3685 2.4; 3943 3.3; 4219 6.0; 4514 3.2; 4830 -2.6; 5168 -1.9; 5530 2.4; 5917 5.4; 6331 5.4; 6775 3.6; 7249 1.3; 7756 0.3; 8299 -1.7; 8880 -4.6; 9502 -5.2; 10167 -2.2; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.0; 20000 -1.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099993182728349dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 550 Wired Power On ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 486 Hz  |  0.46 | 10.4 dB |
| Peaking | 502 Hz  |  0.14 | -7.3 dB |
| Peaking | 3452 Hz |  1.59 | 6.4 dB  |
| Peaking | 6288 Hz |  5.31 | 6.7 dB  |
| Peaking | 9250 Hz |  5.72 | -5.8 dB |
| Peaking | 16 Hz   |  1.92 | 2.7 dB  |
| Peaking | 149 Hz  |  4.57 | -1.7 dB |
| Peaking | 292 Hz  |  4.47 | 1.4 dB  |
| Peaking | 4305 Hz | 11.19 | 5.1 dB  |
| Peaking | 4919 Hz |  9.99 | -5.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PXC%20550%20Wired%20Power%20On/Sennheiser%20PXC%20550%20Wired%20Power%20On.png)