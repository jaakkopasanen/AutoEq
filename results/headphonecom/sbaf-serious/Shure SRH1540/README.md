# Shure SRH1540

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.4dB
GraphicEQ: 10 -84; 20 -7.4; 22 -8.1; 23 -8.4; 25 -8.9; 26 -9.1; 28 -9.5; 30 -9.9; 32 -10.2; 35 -10.5; 37 -10.7; 40 -11.0; 42 -11.1; 45 -11.3; 49 -11.4; 52 -11.4; 56 -11.4; 59 -11.3; 64 -11.1; 68 -10.9; 73 -10.4; 78 -9.8; 83 -9.3; 89 -8.6; 95 -8.2; 102 -7.8; 109 -7.6; 117 -7.3; 125 -6.9; 134 -6.5; 143 -5.8; 153 -5.0; 164 -3.6; 175 -3.7; 188 -4.0; 201 -3.8; 215 -3.9; 230 -4.1; 246 -4.2; 263 -4.2; 282 -4.3; 301 -4.5; 323 -4.5; 345 -4.4; 369 -4.2; 395 -3.8; 423 -3.2; 452 -2.9; 484 -2.6; 518 -2.4; 554 -1.9; 593 -1.4; 635 -1.0; 679 -0.7; 726 -0.5; 777 0.0; 832 0.1; 890 0.1; 952 0.2; 1019 -0.0; 1090 -0.1; 1167 0.2; 1248 0.3; 1336 -0.1; 1429 -0.8; 1529 -1.5; 1636 -2.3; 1751 -2.8; 1873 -3.3; 2004 -3.3; 2145 -2.7; 2295 -2.3; 2455 -1.7; 2627 -1.0; 2811 -0.4; 3008 0.3; 3219 -0.2; 3444 0.1; 3685 0.2; 3943 -0.3; 4219 -1.0; 4514 -1.1; 4830 -0.5; 5168 0.6; 5530 0.3; 5917 -2.5; 6331 -2.8; 6775 -1.2; 7249 -0.5; 7756 -0.6; 8299 -2.0; 8880 -3.8; 9502 -4.5; 10167 -2.7; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.0; 18692 -1.5; 20000 -4.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.4dB` and instead set Global volume in the UI for both channels to **-14**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1540 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 25 Hz   |  0.66 | -4.0 dB |
| Peaking | 60 Hz   |  0.51 | -9.7 dB |
| Peaking | 342 Hz  |  1.58 | -3.3 dB |
| Peaking | 1955 Hz |  3.07 | -3.5 dB |
| Peaking | 9264 Hz |  4.12 | -4.7 dB |
| Peaking | 455 Hz  |  0.2  | -0.2 dB |
| Peaking | 168 Hz  |  9.57 | 1.4 dB  |
| Peaking | 964 Hz  |  1.61 | 1.0 dB  |
| Peaking | 6121 Hz |  8.01 | -3.3 dB |
| Peaking | 5360 Hz | 11.17 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH1540/Shure%20SRH1540.png)