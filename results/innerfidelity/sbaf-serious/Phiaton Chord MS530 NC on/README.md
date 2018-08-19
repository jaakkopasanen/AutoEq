# Phiaton Chord MS530 NC on

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 6.0; 143 6.0; 153 6.0; 164 6.0; 175 6.0; 188 6.0; 201 6.0; 215 6.0; 230 6.0; 246 5.8; 263 5.6; 282 5.5; 301 5.3; 323 4.9; 345 4.7; 369 4.5; 395 4.2; 423 4.0; 452 3.6; 484 3.2; 518 3.7; 554 3.1; 593 2.4; 635 1.6; 679 0.7; 726 0.9; 777 1.6; 832 1.6; 890 0.6; 952 -0.1; 1019 -0.1; 1090 -0.5; 1167 -0.2; 1248 0.6; 1336 0.4; 1429 0.4; 1529 3.0; 1636 3.8; 1751 1.6; 1873 2.2; 2004 3.8; 2145 5.1; 2295 5.9; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000003dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton Chord MS530 NC on ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 37 Hz   |  0.16 | 6.0 dB  |
| Peaking | 277 Hz  |  0.78 | 3.1 dB  |
| Peaking | 2473 Hz |  2.1  | 5.0 dB  |
| Peaking | 3945 Hz |  1.79 | 4.8 dB  |
| Peaking | 5784 Hz |  3.12 | 4.7 dB  |
| Peaking | 528 Hz  |  6.74 | 1.3 dB  |
| Peaking | 1234 Hz |  1.21 | -1.6 dB |
| Peaking | 1590 Hz | 13.38 | 4.0 dB  |
| Peaking | 2382 Hz |  0.33 | 0.4 dB  |
| Peaking | 8379 Hz |  3.14 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20Chord%20MS530%20NC%20on/Phiaton%20Chord%20MS530%20NC%20on.png)