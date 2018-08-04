# Shure SRH1840

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.9dB
GraphicEQ: 10 -84; 20 6.3; 22 5.6; 23 5.3; 25 4.8; 26 4.5; 28 4.1; 30 3.8; 32 3.5; 35 3.1; 37 2.9; 40 2.5; 42 2.3; 45 2.1; 49 1.9; 52 1.7; 56 1.6; 59 1.5; 64 1.2; 68 1.1; 73 1.3; 78 1.6; 83 1.7; 89 1.3; 95 0.9; 102 0.7; 109 0.6; 117 0.5; 125 0.3; 134 0.3; 143 0.1; 153 -0.0; 164 -0.0; 175 -0.0; 188 -0.2; 201 -0.3; 215 -0.3; 230 -0.2; 246 -0.3; 263 -0.3; 282 -0.3; 301 -0.3; 323 -0.3; 345 -0.1; 369 -0.0; 395 -0.1; 423 -0.0; 452 0.2; 484 0.3; 518 0.3; 554 0.6; 593 0.8; 635 0.7; 679 0.7; 726 0.8; 777 1.5; 832 0.9; 890 0.4; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.5; 1336 -0.9; 1429 -1.4; 1529 -2.1; 1636 -2.7; 1751 -3.2; 1873 -4.1; 2004 -4.6; 2145 -5.0; 2295 -5.1; 2455 -4.8; 2627 -5.0; 2811 -4.8; 3008 -4.6; 3219 -4.5; 3444 -4.1; 3685 -3.9; 3943 -3.1; 4219 -2.5; 4514 -2.3; 4830 -0.9; 5168 0.7; 5530 1.1; 5917 -0.4; 6331 -1.4; 6775 -0.2; 7249 0.8; 7756 -0.4; 8299 -2.9; 8880 -4.8; 9502 -3.1; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.0; 18692 -0.7; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.9dB` and instead set Global volume in the UI for both channels to **-69**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1840 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.66 | 6.4 dB  |
| Peaking | 81 Hz   | 4.4  | 1.1 dB  |
| Peaking | 800 Hz  | 1.64 | 1.5 dB  |
| Peaking | 2499 Hz | 1.17 | -5.5 dB |
| Peaking | 8944 Hz | 7.84 | -5.1 dB |
| Peaking | 3644 Hz | 3.68 | -0.9 dB |
| Peaking | 4625 Hz | 4.07 | -1.0 dB |
| Peaking | 5290 Hz | 5.23 | 2.8 dB  |
| Peaking | 2586 Hz | 5.98 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH1840/Shure%20SRH1840.png)