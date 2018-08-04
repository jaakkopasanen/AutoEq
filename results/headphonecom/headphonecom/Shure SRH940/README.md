# Shure SRH940

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.2; 22 3.4; 23 3.0; 25 2.3; 26 2.0; 28 1.3; 30 0.7; 32 0.2; 35 -0.5; 37 -0.9; 40 -1.5; 42 -1.8; 45 -2.2; 49 -2.6; 52 -2.8; 56 -3.0; 59 -3.1; 64 -3.2; 68 -2.8; 73 -2.0; 78 -1.0; 83 -0.3; 89 -0.7; 95 -1.7; 102 -2.4; 109 -2.5; 117 -2.1; 125 -1.5; 134 -2.0; 143 -2.2; 153 -2.3; 164 -1.7; 175 -2.5; 188 -3.3; 201 -3.7; 215 -4.0; 230 -4.2; 246 -4.4; 263 -4.5; 282 -4.2; 301 -4.1; 323 -5.1; 345 -5.0; 369 -4.1; 395 -3.6; 423 -3.2; 452 -2.8; 484 -2.4; 518 -2.0; 554 -1.7; 593 -1.2; 635 -0.9; 679 -0.7; 726 -0.5; 777 -0.1; 832 0.4; 890 -0.0; 952 -0.1; 1019 0.0; 1090 0.1; 1167 0.2; 1248 0.4; 1336 0.6; 1429 1.0; 1529 1.1; 1636 1.0; 1751 0.9; 1873 0.9; 2004 1.0; 2145 1.2; 2295 1.5; 2455 2.8; 2627 2.8; 2811 2.5; 3008 2.2; 3219 1.5; 3444 0.7; 3685 0.3; 3943 0.1; 4219 0.9; 4514 1.9; 4830 3.4; 5168 5.4; 5530 6.0; 5917 5.9; 6331 5.6; 6775 3.9; 7249 1.3; 7756 -0.3; 8299 -4.6; 8880 -7.8; 9502 -6.2; 10167 -0.6; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH940 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 19 Hz   | 1.13 | 4.8 dB   |
| Peaking | 53 Hz   | 1.14 | -3.3 dB  |
| Peaking | 285 Hz  | 1    | -4.8 dB  |
| Peaking | 5949 Hz | 1.74 | 6.6 dB   |
| Peaking | 8884 Hz | 4.51 | -10.3 dB |
| Peaking | 84 Hz   | 6.63 | 1.7 dB   |
| Peaking | 103 Hz  | 4.62 | -1.3 dB  |
| Peaking | 1441 Hz | 1.09 | 0.8 dB   |
| Peaking | 2654 Hz | 3.3  | 2.4 dB   |
| Peaking | 3950 Hz | 4.34 | -2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Shure%20SRH940/Shure%20SRH940.png)