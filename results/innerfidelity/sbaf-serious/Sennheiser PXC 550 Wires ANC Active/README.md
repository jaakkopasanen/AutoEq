# Sennheiser PXC 550 Wires ANC Active

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.7dB
GraphicEQ: 10 -84; 20 6.0; 22 5.9; 23 5.8; 25 5.3; 26 5.0; 28 4.3; 30 3.8; 32 3.4; 35 2.9; 37 2.7; 40 2.6; 42 2.5; 45 2.6; 49 2.8; 52 2.9; 56 3.1; 59 3.2; 64 3.5; 68 3.6; 73 3.7; 78 3.8; 83 3.8; 89 3.6; 95 3.3; 102 2.9; 109 2.6; 117 2.1; 125 1.6; 134 1.1; 143 0.8; 153 0.6; 164 0.6; 175 0.7; 188 0.7; 201 0.7; 215 0.9; 230 1.3; 246 1.5; 263 1.8; 282 2.3; 301 2.6; 323 2.9; 345 3.1; 369 3.2; 395 3.2; 423 3.3; 452 3.2; 484 2.8; 518 2.6; 554 2.6; 593 2.6; 635 2.4; 679 2.1; 726 1.9; 777 1.9; 832 1.4; 890 0.8; 952 0.4; 1019 -0.1; 1090 -0.5; 1167 -0.1; 1248 0.8; 1336 -0.8; 1429 -1.3; 1529 -1.8; 1636 -2.2; 1751 -1.4; 1873 -0.4; 2004 -0.7; 2145 -0.5; 2295 0.1; 2455 1.1; 2627 2.5; 2811 3.1; 3008 3.5; 3219 3.8; 3444 3.6; 3685 1.7; 3943 3.0; 4219 6.1; 4514 3.4; 4830 -3.7; 5168 -3.9; 5530 1.4; 5917 4.2; 6331 4.6; 6775 2.9; 7249 1.0; 7756 -0.9; 8299 -2.8; 8880 -4.3; 9502 -4.1; 10167 -1.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.6; 20000 -3.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.7dB` and instead set Global volume in the UI for both channels to **-67**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 550 Wires ANC Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 13 Hz   |  0.86 | 6.9 dB  |
| Peaking | 69 Hz   |  0.09 | 2.3 dB  |
| Peaking | 3324 Hz |  2.86 | 4.0 dB  |
| Peaking | 6334 Hz |  6.75 | 5.4 dB  |
| Peaking | 9031 Hz |  4.39 | -5.1 dB |
| Peaking | 184 Hz  |  1.94 | -2.1 dB |
| Peaking | 429 Hz  |  1.13 | 1.7 dB  |
| Peaking | 1583 Hz |  2.59 | -2.7 dB |
| Peaking | 4327 Hz |  9.5  | 6.0 dB  |
| Peaking | 4993 Hz | 10.35 | -7.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PXC%20550%20Wires%20ANC%20Active/Sennheiser%20PXC%20550%20Wires%20ANC%20Active.png)