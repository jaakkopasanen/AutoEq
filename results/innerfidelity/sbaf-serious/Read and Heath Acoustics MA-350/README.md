# Read and Heath Acoustics MA-350

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 10 -84; 20 -10.2; 22 -10.2; 23 -10.1; 25 -10.1; 26 -10.0; 28 -9.9; 30 -9.8; 32 -9.7; 35 -9.5; 37 -9.4; 40 -9.2; 42 -9.1; 45 -8.9; 49 -8.6; 52 -8.4; 56 -8.2; 59 -8.0; 64 -7.8; 68 -7.6; 73 -7.4; 78 -7.3; 83 -7.3; 89 -7.3; 95 -7.4; 102 -7.6; 109 -7.7; 117 -7.9; 125 -8.0; 134 -8.1; 143 -8.1; 153 -8.0; 164 -7.8; 175 -7.4; 188 -7.0; 201 -6.7; 215 -6.2; 230 -5.7; 246 -5.3; 263 -4.9; 282 -4.4; 301 -3.9; 323 -3.5; 345 -3.0; 369 -2.5; 395 -2.1; 423 -1.6; 452 -1.3; 484 -1.1; 518 -0.9; 554 -0.6; 593 -0.2; 635 -0.2; 679 -0.1; 726 0.1; 777 0.2; 832 0.1; 890 -0.0; 952 -0.0; 1019 -0.0; 1090 -0.0; 1167 -0.1; 1248 -0.0; 1336 -0.1; 1429 -0.3; 1529 -0.4; 1636 -0.3; 1751 -0.1; 1873 0.4; 2004 0.9; 2145 1.4; 2295 1.7; 2455 2.1; 2627 2.4; 2811 2.5; 3008 2.4; 3219 2.0; 3444 1.4; 3685 0.4; 3943 -0.9; 4219 -3.2; 4514 -5.6; 4830 -7.8; 5168 -8.9; 5530 -7.0; 5917 -2.2; 6331 1.2; 6775 3.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.0dB` and instead set Global volume in the UI for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Read and Heath Acoustics MA-350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 9 Hz    | 0.84 | -9.8 dB  |
| Peaking | 32 Hz   | 0.38 | -8.0 dB  |
| Peaking | 164 Hz  | 0.81 | -6.0 dB  |
| Peaking | 2846 Hz | 1.92 | 3.1 dB   |
| Peaking | 4999 Hz | 4.58 | -10.2 dB |
| Peaking | 302 Hz  | 2.85 | -0.5 dB  |
| Peaking | 668 Hz  | 1.46 | 0.7 dB   |
| Peaking | 1582 Hz | 4.4  | -0.8 dB  |
| Peaking | 5548 Hz | 8.5  | -2.8 dB  |
| Peaking | 6684 Hz | 5.75 | 4.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Read%20and%20Heath%20Acoustics%20MA-350/Read%20and%20Heath%20Acoustics%20MA-350.png)