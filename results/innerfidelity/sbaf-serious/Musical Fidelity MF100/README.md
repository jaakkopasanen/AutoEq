# Musical Fidelity MF100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 10 -84; 20 2.4; 22 1.7; 23 1.3; 25 0.8; 26 0.5; 28 0.0; 30 -0.3; 32 -0.6; 35 -1.0; 37 -1.2; 40 -1.4; 42 -1.4; 45 -1.4; 49 -1.4; 52 -1.2; 56 -1.1; 59 -1.1; 64 -0.9; 68 -0.7; 73 -0.4; 78 -0.1; 83 0.5; 89 0.9; 95 0.6; 102 0.2; 109 0.2; 117 0.1; 125 0.0; 134 0.3; 143 0.4; 153 0.3; 164 0.5; 175 0.8; 188 0.9; 201 1.0; 215 1.3; 230 1.6; 246 2.0; 263 2.5; 282 2.7; 301 2.7; 323 2.9; 345 3.0; 369 2.8; 395 2.6; 423 2.5; 452 2.4; 484 2.3; 518 2.4; 554 2.6; 593 2.8; 635 2.9; 679 3.1; 726 3.2; 777 2.9; 832 1.9; 890 0.9; 952 0.3; 1019 0.0; 1090 0.4; 1167 0.1; 1248 -0.2; 1336 -0.3; 1429 0.1; 1529 0.1; 1636 -0.2; 1751 -0.5; 1873 -0.8; 2004 -1.1; 2145 -1.3; 2295 -1.5; 2455 -1.2; 2627 -1.1; 2811 -1.1; 3008 -1.1; 3219 -1.1; 3444 -1.0; 3685 -0.6; 3943 0.2; 4219 -0.5; 4514 -2.2; 4830 -2.2; 5168 -0.6; 5530 -0.4; 5917 0.0; 6331 0.2; 6775 -2.0; 7249 -2.6; 7756 -2.4; 8299 -3.4; 8880 -4.6; 9502 -3.3; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.7dB` and instead set Global volume in the UI for both channels to **-37**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Musical Fidelity MF100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 3 Hz     |  1.89 | 1.5 dB  |
| Peaking | 331 Hz   |  1.28 | 2.9 dB  |
| Peaking | 684 Hz   |  2.3  | 2.9 dB  |
| Peaking | 2671 Hz  |  0.72 | -1.2 dB |
| Peaking | 8677 Hz  |  3.9  | -4.5 dB |
| Peaking | 16 Hz    |  1.5  | 3.3 dB  |
| Peaking | 43 Hz    |  1.52 | -2.0 dB |
| Peaking | 7060 Hz  | 14.53 | -1.8 dB |
| Peaking | 10401 Hz |  9.73 | 1.1 dB  |
| Peaking | 11870 Hz |  3.36 | 0.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Musical%20Fidelity%20MF100/Musical%20Fidelity%20MF100.png)