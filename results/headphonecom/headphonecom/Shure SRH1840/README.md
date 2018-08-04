# Shure SRH1840

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 5.8; 22 5.1; 23 4.8; 25 4.2; 26 4.0; 28 3.6; 30 3.2; 32 2.9; 35 2.5; 37 2.3; 40 1.9; 42 1.7; 45 1.5; 49 1.3; 52 1.2; 56 1.0; 59 0.9; 64 0.6; 68 0.5; 73 0.7; 78 1.0; 83 1.0; 89 0.5; 95 0.0; 102 -0.3; 109 -0.6; 117 -0.7; 125 -0.9; 134 -1.0; 143 -1.2; 153 -1.3; 164 -1.3; 175 -1.4; 188 -1.5; 201 -1.7; 215 -1.7; 230 -1.7; 246 -1.7; 263 -1.7; 282 -1.7; 301 -1.6; 323 -1.7; 345 -1.5; 369 -1.4; 395 -1.4; 423 -1.2; 452 -0.8; 484 -0.5; 518 -0.2; 554 0.1; 593 0.3; 635 0.4; 679 0.7; 726 0.9; 777 1.3; 832 0.8; 890 0.3; 952 0.2; 1019 0.0; 1090 0.0; 1167 0.1; 1248 0.2; 1336 0.4; 1429 0.7; 1529 0.6; 1636 0.4; 1751 -0.2; 1873 -1.1; 2004 -1.7; 2145 -2.0; 2295 -2.0; 2455 -1.9; 2627 -1.9; 2811 -1.9; 3008 -2.0; 3219 -2.1; 3444 -2.0; 3685 -1.8; 3943 -0.8; 4219 1.2; 4514 2.5; 4830 4.6; 5168 5.9; 5530 5.7; 5917 3.1; 6331 0.8; 6775 1.2; 7249 1.3; 7756 0.2; 8299 -1.5; 8880 -2.8; 9502 -0.9; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1840 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.58 | 7.0 dB  |
| Peaking | 225 Hz  | 1    | -2.0 dB |
| Peaking | 3154 Hz | 1.53 | -3.0 dB |
| Peaking | 5194 Hz | 3.25 | 7.1 dB  |
| Peaking | 8815 Hz | 7.55 | -3.4 dB |
| Peaking | 126 Hz  | 3.96 | -0.5 dB |
| Peaking | 388 Hz  | 3.63 | -0.7 dB |
| Peaking | 740 Hz  | 2.73 | 1.3 dB  |
| Peaking | 1530 Hz | 3.34 | 1.2 dB  |
| Peaking | 2065 Hz | 4.49 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Shure%20SRH1840/Shure%20SRH1840.png)