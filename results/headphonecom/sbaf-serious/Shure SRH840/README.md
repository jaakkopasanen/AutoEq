# Shure SRH840

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 10 -84; 20 3.6; 22 2.2; 23 1.6; 25 0.4; 26 -0.1; 28 -1.1; 30 -1.8; 32 -2.5; 35 -3.3; 37 -3.8; 40 -4.8; 42 -5.4; 45 -6.3; 49 -7.0; 52 -7.1; 56 -6.9; 59 -6.6; 64 -6.6; 68 -7.0; 73 -7.8; 78 -8.6; 83 -9.1; 89 -9.5; 95 -9.7; 102 -9.8; 109 -9.5; 117 -9.2; 125 -8.7; 134 -8.4; 143 -8.0; 153 -7.2; 164 -6.1; 175 -5.8; 188 -5.1; 201 -4.1; 215 -3.4; 230 -2.9; 246 -2.7; 263 -2.3; 282 -2.3; 301 -4.3; 323 -4.5; 345 -3.6; 369 -3.2; 395 -2.8; 423 -2.5; 452 -2.3; 484 -2.2; 518 -1.9; 554 -1.6; 593 -1.2; 635 -0.9; 679 -0.7; 726 -0.5; 777 0.0; 832 0.1; 890 0.3; 952 0.2; 1019 0.0; 1090 0.1; 1167 0.3; 1248 0.3; 1336 0.0; 1429 -0.8; 1529 -1.5; 1636 -2.6; 1751 -3.4; 1873 -3.8; 2004 -4.1; 2145 -4.5; 2295 -4.4; 2455 -4.1; 2627 -3.3; 2811 -3.0; 3008 -2.4; 3219 -1.9; 3444 -1.5; 3685 -1.1; 3943 -0.7; 4219 -1.5; 4514 -3.2; 4830 -2.8; 5168 -0.6; 5530 2.2; 5917 3.6; 6331 3.5; 6775 3.4; 7249 1.3; 7756 -1.7; 8299 -7.0; 8880 -11.1; 9502 -10.2; 10167 -3.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.2dB` and instead set Global volume in the UI for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH840 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 48 Hz    | 2.33 | -3.9 dB  |
| Peaking | 105 Hz   | 0.89 | -9.7 dB  |
| Peaking | 356 Hz   | 2.4  | -2.5 dB  |
| Peaking | 2231 Hz  | 2.01 | -4.8 dB  |
| Peaking | 9087 Hz  | 6.47 | -13.0 dB |
| Peaking | 1133 Hz  | 3.09 | 1.1 dB   |
| Peaking | 4695 Hz  | 4.87 | -4.5 dB  |
| Peaking | 6308 Hz  | 2.42 | 5.4 dB   |
| Peaking | 8331 Hz  | 6.12 | -4.0 dB  |
| Peaking | 10932 Hz | 8.39 | 1.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH840/Shure%20SRH840.png)