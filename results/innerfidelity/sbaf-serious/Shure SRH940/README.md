# Shure SRH940

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.5; 37 5.1; 40 4.5; 42 4.1; 45 3.5; 49 3.0; 52 2.6; 56 2.3; 59 2.1; 64 1.9; 68 1.8; 73 2.0; 78 2.7; 83 3.2; 89 4.0; 95 4.2; 102 3.2; 109 2.2; 117 1.4; 125 1.0; 134 0.5; 143 0.0; 153 -0.5; 164 -0.7; 175 -1.6; 188 -2.7; 201 -3.3; 215 -3.7; 230 -3.8; 246 -3.9; 263 -3.8; 282 -3.6; 301 -3.4; 323 -4.2; 345 -4.4; 369 -3.7; 395 -3.2; 423 -2.7; 452 -2.5; 484 -2.2; 518 -1.9; 554 -1.4; 593 -0.8; 635 -0.5; 679 -0.4; 726 -0.0; 777 0.3; 832 0.3; 890 0.2; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.1; 1248 -0.2; 1336 -0.6; 1429 -1.3; 1529 -1.8; 1636 -2.4; 1751 -2.9; 1873 -3.1; 2004 -3.1; 2145 -3.0; 2295 -2.9; 2455 -2.0; 2627 -2.1; 2811 -2.1; 3008 -1.8; 3219 -1.7; 3444 -2.0; 3685 -2.0; 3943 -2.0; 4219 -2.6; 4514 -2.3; 4830 -1.8; 5168 -0.6; 5530 1.1; 5917 1.3; 6331 1.1; 6775 0.8; 7249 -1.0; 7756 -3.6; 8299 -6.8; 8880 -9.2; 9502 -9.2; 10167 -5.9; 10879 -0.9; 11640 0.0; 12455 0.0; 13327 -0.8; 14260 -3.4; 15258 -2.3; 16326 -0.1; 17469 0.0; 18692 -1.5; 20000 -5.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH940 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.87 | 6.5 dB   |
| Peaking | 96 Hz    | 2.58 | 3.8 dB   |
| Peaking | 276 Hz   | 1.08 | -4.5 dB  |
| Peaking | 2243 Hz  | 1.36 | -3.0 dB  |
| Peaking | 9167 Hz  | 4.21 | -10.6 dB |
| Peaking | 890 Hz   | 2.28 | 1.2 dB   |
| Peaking | 4454 Hz  | 3.77 | -2.0 dB  |
| Peaking | 6104 Hz  | 2.86 | 3.7 dB   |
| Peaking | 11577 Hz | 3.92 | 3.3 dB   |
| Peaking | 19256 Hz | 0.14 | -1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH940/Shure%20SRH940.png)