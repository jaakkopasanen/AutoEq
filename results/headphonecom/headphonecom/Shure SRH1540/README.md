# Shure SRH1540

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 -7.9; 22 -8.6; 23 -8.9; 25 -9.4; 26 -9.7; 28 -10.1; 30 -10.4; 32 -10.7; 35 -11.1; 37 -11.3; 40 -11.6; 42 -11.7; 45 -11.9; 49 -12.0; 52 -12.0; 56 -12.0; 59 -11.9; 64 -11.7; 68 -11.4; 73 -11.0; 78 -10.5; 83 -10.0; 89 -9.4; 95 -9.0; 102 -8.8; 109 -8.7; 117 -8.5; 125 -8.2; 134 -7.8; 143 -7.1; 153 -6.3; 164 -4.9; 175 -5.1; 188 -5.3; 201 -5.1; 215 -5.3; 230 -5.5; 246 -5.6; 263 -5.6; 282 -5.6; 301 -5.9; 323 -5.9; 345 -5.9; 369 -5.5; 395 -5.1; 423 -4.4; 452 -3.9; 484 -3.3; 518 -2.9; 554 -2.4; 593 -1.9; 635 -1.3; 679 -0.8; 726 -0.4; 777 -0.1; 832 -0.0; 890 0.1; 952 0.1; 1019 -0.0; 1090 -0.0; 1167 0.5; 1248 0.9; 1336 1.3; 1429 1.3; 1529 1.2; 1636 0.7; 1751 0.2; 1873 -0.4; 2004 -0.4; 2145 0.4; 2295 0.7; 2455 1.2; 2627 2.0; 2811 2.6; 3008 2.9; 3219 2.2; 3444 2.1; 3685 2.2; 3943 2.0; 4219 2.6; 4514 3.7; 4830 4.9; 5168 6.0; 5530 5.0; 5917 1.0; 6331 -0.6; 6775 0.2; 7249 0.5; 7756 0.3; 8299 -0.6; 8880 -1.9; 9502 -1.9; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1540 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.22 | -2.8 dB |
| Peaking | 52 Hz    | 0.39 | -9.3 dB |
| Peaking | 343 Hz   | 1.53 | -4.3 dB |
| Peaking | 3079 Hz  | 1.85 | 2.5 dB  |
| Peaking | 5097 Hz  | 5.08 | 6.0 dB  |
| Peaking | 89 Hz    | 4.8  | 0.4 dB  |
| Peaking | 1531 Hz  | 1.56 | 1.8 dB  |
| Peaking | 1904 Hz  | 3.12 | -2.2 dB |
| Peaking | 9151 Hz  | 5.46 | -2.6 dB |
| Peaking | 37549 Hz | 2.35 | 0.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Shure%20SRH1540/Shure%20SRH1540.png)