# Shure SRH750DJ

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 10 -84; 20 -3.3; 22 -3.8; 23 -4.1; 25 -4.5; 26 -4.7; 28 -5.0; 30 -5.3; 32 -5.6; 35 -5.9; 37 -6.0; 40 -6.2; 42 -6.3; 45 -6.4; 49 -6.5; 52 -6.4; 56 -6.2; 59 -6.2; 64 -6.4; 68 -6.5; 73 -6.8; 78 -6.7; 83 -6.4; 89 -5.7; 95 -4.8; 102 -4.0; 109 -3.6; 117 -4.5; 125 -6.1; 134 -6.8; 143 -7.4; 153 -7.5; 164 -6.2; 175 -6.2; 188 -6.6; 201 -6.0; 215 -5.2; 230 -4.9; 246 -5.1; 263 -4.3; 282 -3.4; 301 -2.5; 323 -1.6; 345 -1.0; 369 -0.6; 395 -0.4; 423 -0.3; 452 -0.4; 484 -0.6; 518 -0.8; 554 -0.7; 593 -0.6; 635 -0.6; 679 -0.6; 726 -0.5; 777 -0.1; 832 0.3; 890 0.6; 952 0.6; 1019 -0.2; 1090 -0.6; 1167 -0.4; 1248 -0.3; 1336 -0.8; 1429 -1.8; 1529 -2.6; 1636 -3.7; 1751 -5.3; 1873 -6.5; 2004 -7.6; 2145 -8.2; 2295 -7.6; 2455 -5.9; 2627 -4.1; 2811 -2.2; 3008 -0.6; 3219 0.5; 3444 0.9; 3685 0.8; 3943 0.0; 4219 -3.0; 4514 -3.6; 4830 -0.8; 5168 0.7; 5530 1.4; 5917 5.3; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -1.0; 8299 -4.8; 8880 -6.9; 9502 -6.5; 10167 -4.3; 10879 -1.3; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.4dB` and instead set Global volume in the UI for both channels to **-64**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH750DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 0.54 | -6.5 dB |
| Peaking | 177 Hz  | 1.32 | -5.5 dB |
| Peaking | 2105 Hz | 2.73 | -8.8 dB |
| Peaking | 6354 Hz | 4.58 | 7.2 dB  |
| Peaking | 9081 Hz | 3.71 | -8.1 dB |
| Peaking | 12 Hz   | 1.71 | -0.6 dB |
| Peaking | 393 Hz  | 5.15 | 1.0 dB  |
| Peaking | 914 Hz  | 5.11 | 1.3 dB  |
| Peaking | 3502 Hz | 4.22 | 2.4 dB  |
| Peaking | 4419 Hz | 8.43 | -4.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH750DJ/Shure%20SRH750DJ.png)