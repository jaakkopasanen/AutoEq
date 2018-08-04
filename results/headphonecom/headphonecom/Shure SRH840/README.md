# Shure SRH840

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.1; 22 1.7; 23 1.1; 25 -0.1; 26 -0.6; 28 -1.6; 30 -2.4; 32 -3.0; 35 -3.8; 37 -4.4; 40 -5.4; 42 -6.0; 45 -6.9; 49 -7.6; 52 -7.7; 56 -7.4; 59 -7.2; 64 -7.1; 68 -7.5; 73 -8.4; 78 -9.2; 83 -9.8; 89 -10.3; 95 -10.6; 102 -10.8; 109 -10.7; 117 -10.5; 125 -10.0; 134 -9.6; 143 -9.3; 153 -8.5; 164 -7.4; 175 -7.2; 188 -6.5; 201 -5.5; 215 -4.8; 230 -4.3; 246 -4.0; 263 -3.7; 282 -3.7; 301 -5.7; 323 -5.8; 345 -5.0; 369 -4.6; 395 -4.1; 423 -3.7; 452 -3.3; 484 -2.9; 518 -2.5; 554 -2.1; 593 -1.6; 635 -1.2; 679 -0.8; 726 -0.4; 777 -0.1; 832 -0.0; 890 0.3; 952 0.2; 1019 0.0; 1090 0.2; 1167 0.6; 1248 0.9; 1336 1.4; 1429 1.3; 1529 1.1; 1636 0.5; 1751 -0.4; 1873 -0.9; 2004 -1.2; 2145 -1.5; 2295 -1.4; 2455 -1.2; 2627 -0.3; 2811 -0.1; 3008 0.2; 3219 0.4; 3444 0.5; 3685 1.0; 3943 1.6; 4219 2.1; 4514 1.6; 4830 2.6; 5168 4.8; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.8; 8299 -5.6; 8880 -9.1; 9502 -7.6; 10167 -1.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH840 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 47 Hz    | 2.22 | -4.0 dB  |
| Peaking | 107 Hz   | 0.81 | -10.7 dB |
| Peaking | 358 Hz   | 2    | -3.4 dB  |
| Peaking | 5937 Hz  | 2.36 | 7.0 dB   |
| Peaking | 8922 Hz  | 4.96 | -11.4 dB |
| Peaking | 537 Hz   | 3.69 | -0.7 dB  |
| Peaking | 831 Hz   | 2.48 | 0.6 dB   |
| Peaking | 1406 Hz  | 3.18 | 1.8 dB   |
| Peaking | 2144 Hz  | 2.86 | -1.9 dB  |
| Peaking | 10549 Hz | 9.51 | 1.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Shure%20SRH840/Shure%20SRH840.png)