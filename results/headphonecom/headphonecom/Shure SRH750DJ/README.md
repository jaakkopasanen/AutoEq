# Shure SRH750DJ

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -7.9; 22 -8.4; 23 -8.6; 25 -9.0; 26 -9.2; 28 -9.6; 30 -9.9; 32 -10.1; 35 -10.4; 37 -10.6; 40 -10.8; 42 -10.9; 45 -11.0; 49 -11.1; 52 -10.9; 56 -10.8; 59 -10.8; 64 -10.8; 68 -11.0; 73 -11.2; 78 -11.0; 83 -10.6; 89 -9.7; 95 -8.6; 102 -7.4; 109 -6.8; 117 -7.4; 125 -8.5; 134 -8.9; 143 -9.3; 153 -9.2; 164 -7.8; 175 -7.8; 188 -8.0; 201 -7.4; 215 -6.6; 230 -6.3; 246 -6.6; 263 -5.7; 282 -4.7; 301 -3.8; 323 -3.0; 345 -2.4; 369 -2.0; 395 -1.6; 423 -1.5; 452 -1.4; 484 -1.4; 518 -1.3; 554 -1.2; 593 -1.0; 635 -0.9; 679 -0.7; 726 -0.5; 777 -0.2; 832 0.2; 890 0.6; 952 0.5; 1019 -0.2; 1090 -0.5; 1167 -0.1; 1248 0.3; 1336 0.6; 1429 0.3; 1529 0.1; 1636 -0.7; 1751 -2.3; 1873 -3.6; 2004 -4.6; 2145 -5.2; 2295 -4.6; 2455 -3.0; 2627 -1.1; 2811 0.7; 3008 2.0; 3219 2.8; 3444 3.0; 3685 2.9; 3943 2.4; 4219 0.6; 4514 1.2; 4830 4.6; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.3; 8299 -3.4; 8880 -5.0; 9502 -3.9; 10167 -0.9; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH750DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 36 Hz   | 0.51 | -10.2 dB |
| Peaking | 74 Hz   | 2.09 | -3.7 dB  |
| Peaking | 178 Hz  | 1    | -6.5 dB  |
| Peaking | 2116 Hz | 4.65 | -6.0 dB  |
| Peaking | 5511 Hz | 2.9  | 6.9 dB   |
| Peaking | 139 Hz  | 8.42 | -1.2 dB  |
| Peaking | 902 Hz  | 5.04 | 1.0 dB   |
| Peaking | 6554 Hz | 6.99 | 2.5 dB   |
| Peaking | 3312 Hz | 5.27 | 3.1 dB   |
| Peaking | 8836 Hz | 4.42 | -6.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Shure%20SRH750DJ/Shure%20SRH750DJ.png)