# Shure SRH840

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.8; 30 5.3; 32 4.7; 35 3.7; 37 3.0; 40 2.2; 42 1.7; 45 1.1; 49 0.3; 52 -0.2; 56 -0.8; 59 -1.2; 64 -1.6; 68 -1.7; 73 -1.8; 78 -1.8; 83 -1.9; 89 -1.9; 95 -2.3; 102 -2.9; 109 -3.1; 117 -3.4; 125 -3.9; 134 -4.3; 143 -4.4; 153 -4.3; 164 -3.5; 175 -3.4; 188 -3.8; 201 -3.7; 215 -3.5; 230 -3.3; 246 -3.1; 263 -2.8; 282 -3.2; 301 -4.4; 323 -4.4; 345 -3.7; 369 -3.4; 395 -3.1; 423 -2.7; 452 -2.4; 484 -2.3; 518 -2.1; 554 -1.6; 593 -1.1; 635 -0.8; 679 -0.7; 726 -0.5; 777 -0.2; 832 -0.2; 890 -0.1; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.4; 1248 -0.7; 1336 -1.2; 1429 -1.9; 1529 -2.6; 1636 -3.1; 1751 -3.7; 1873 -4.1; 2004 -4.4; 2145 -5.0; 2295 -5.2; 2455 -4.8; 2627 -4.1; 2811 -3.5; 3008 -2.9; 3219 -2.4; 3444 -1.6; 3685 -1.1; 3943 -0.3; 4219 -0.2; 4514 -0.9; 4830 -1.2; 5168 0.8; 5530 3.7; 5917 5.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.1; 8299 -4.1; 8880 -6.9; 9502 -6.5; 10167 -2.9; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH840 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 24 Hz    |  1.17 | 7.0 dB  |
| Peaking | 169 Hz   |  0.44 | -4.1 dB |
| Peaking | 2278 Hz  |  1.66 | -5.3 dB |
| Peaking | 6211 Hz  |  3.9  | 7.2 dB  |
| Peaking | 9060 Hz  |  4.66 | -8.3 dB |
| Peaking | 342 Hz   |  4.24 | -1.4 dB |
| Peaking | 960 Hz   |  1.57 | 1.2 dB  |
| Peaking | 1618 Hz  |  4.05 | -1.0 dB |
| Peaking | 4758 Hz  | 11.65 | -2.0 dB |
| Peaking | 11090 Hz |  7.68 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH840/Shure%20SRH840.png)