# Read and Heath Acoustics MA-350

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.5dB
GraphicEQ: 10 -84; 20 -10.3; 22 -10.2; 23 -10.2; 25 -10.2; 26 -10.1; 28 -10.1; 30 -10.0; 32 -9.9; 35 -9.8; 37 -9.7; 40 -9.6; 42 -9.6; 45 -9.5; 49 -9.4; 52 -9.3; 56 -9.2; 59 -9.1; 64 -9.1; 68 -9.0; 73 -8.9; 78 -8.9; 83 -8.9; 89 -8.8; 95 -8.8; 102 -8.7; 109 -8.5; 117 -8.2; 125 -8.0; 134 -7.9; 143 -7.7; 153 -7.5; 164 -7.2; 175 -6.9; 188 -6.5; 201 -6.2; 215 -5.8; 230 -5.4; 246 -5.1; 263 -4.7; 282 -4.2; 301 -3.8; 323 -3.3; 345 -2.9; 369 -2.5; 395 -2.1; 423 -1.6; 452 -1.2; 484 -1.1; 518 -0.8; 554 -0.6; 593 -0.2; 635 -0.1; 679 -0.1; 726 0.1; 777 0.2; 832 0.1; 890 -0.0; 952 -0.0; 1019 -0.0; 1090 -0.0; 1167 -0.1; 1248 -0.0; 1336 -0.1; 1429 -0.3; 1529 -0.4; 1636 -0.3; 1751 -0.1; 1873 0.4; 2004 0.9; 2145 1.4; 2295 1.7; 2455 2.1; 2627 2.4; 2811 2.5; 3008 2.4; 3219 2.0; 3444 1.4; 3685 0.4; 3943 -0.9; 4219 -3.2; 4514 -5.6; 4830 -7.8; 5168 -8.9; 5530 -7.0; 5917 -2.2; 6331 1.2; 6775 3.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.5323503451546414dB` and instead set Global volume in the UI for both channels to **-35**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Read and Heath Acoustics MA-350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.3dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 0.2  | -9.9 dB  |
| Peaking | 157 Hz  | 0.71 | -4.0 dB  |
| Peaking | 3050 Hz | 1.58 | 3.8 dB   |
| Peaking | 5144 Hz | 2.58 | -11.2 dB |
| Peaking | 6596 Hz | 3.86 | 6.5 dB   |
| Peaking | 142 Hz  | 4.31 | 0.3 dB   |
| Peaking | 678 Hz  | 1.9  | 0.8 dB   |
| Peaking | 1592 Hz | 4.86 | -0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Read%20and%20Heath%20Acoustics%20MA-350/Read%20and%20Heath%20Acoustics%20MA-350.png)