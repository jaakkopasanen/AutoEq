# Shure SRH240

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.8; 68 5.4; 73 4.9; 78 4.6; 83 4.5; 89 4.4; 95 4.3; 102 4.3; 109 4.3; 117 4.5; 125 4.5; 134 4.6; 143 4.9; 153 5.3; 164 5.7; 175 5.9; 188 6.0; 201 5.8; 215 5.6; 230 5.2; 246 4.8; 263 4.3; 282 2.9; 301 1.4; 323 0.3; 345 -0.6; 369 -1.1; 395 -1.6; 423 -2.1; 452 -2.6; 484 -2.9; 518 -3.0; 554 -2.9; 593 -2.5; 635 -2.1; 679 -1.7; 726 -1.3; 777 -1.0; 832 -0.7; 890 -0.6; 952 -0.3; 1019 0.0; 1090 0.2; 1167 0.2; 1248 0.2; 1336 0.4; 1429 0.8; 1529 1.1; 1636 1.3; 1751 1.5; 1873 1.6; 2004 1.8; 2145 2.0; 2295 2.0; 2455 1.8; 2627 1.6; 2811 1.7; 3008 1.9; 3219 1.9; 3444 1.6; 3685 1.8; 3943 2.3; 4219 3.5; 4514 4.9; 4830 5.8; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.6; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH240 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.35 | 6.2 dB  |
| Peaking | 213 Hz  | 1.09 | 6.0 dB  |
| Peaking | 451 Hz  | 1.04 | -4.6 dB |
| Peaking | 2063 Hz | 1.08 | 1.8 dB  |
| Peaking | 5382 Hz | 2.27 | 6.6 dB  |
| Peaking | 6518 Hz | 6.95 | 2.5 dB  |
| Peaking | 8039 Hz | 2.05 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Shure%20SRH240/Shure%20SRH240.png)