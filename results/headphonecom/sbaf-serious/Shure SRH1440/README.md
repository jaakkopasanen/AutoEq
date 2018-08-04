# Shure SRH1440

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 5.9; 83 5.5; 89 5.1; 95 4.6; 102 4.1; 109 3.6; 117 3.1; 125 2.5; 134 2.0; 143 1.6; 153 1.2; 164 1.1; 175 0.9; 188 0.7; 201 0.6; 215 0.4; 230 0.5; 246 0.3; 263 0.3; 282 0.3; 301 0.1; 323 0.2; 345 0.4; 369 0.5; 395 0.5; 423 0.7; 452 0.6; 484 0.7; 518 0.5; 554 0.7; 593 0.9; 635 1.2; 679 1.5; 726 1.1; 777 1.1; 832 0.8; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.6; 1248 -1.0; 1336 -1.4; 1429 -2.2; 1529 -3.1; 1636 -4.1; 1751 -5.0; 1873 -5.4; 2004 -5.7; 2145 -6.1; 2295 -6.4; 2455 -6.2; 2627 -6.1; 2811 -6.7; 3008 -6.6; 3219 -6.6; 3444 -6.7; 3685 -6.5; 3943 -6.1; 4219 -6.0; 4514 -5.4; 4830 -3.8; 5168 -2.8; 5530 -1.3; 5917 -1.2; 6331 -2.0; 6775 -0.4; 7249 -0.3; 7756 -1.0; 8299 -3.0; 8880 -5.7; 9502 -7.4; 10167 -6.5; 10879 -2.7; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 50 Hz    | 0.25 | 6.8 dB  |
| Peaking | 178 Hz   | 0.79 | -3.3 dB |
| Peaking | 805 Hz   | 1.18 | 1.9 dB  |
| Peaking | 2742 Hz  | 0.83 | -7.3 dB |
| Peaking | 9627 Hz  | 5.2  | -7.7 dB |
| Peaking | 3 Hz     | 1.47 | 0.5 dB  |
| Peaking | 2666 Hz  | 5.82 | 1.1 dB  |
| Peaking | 4382 Hz  | 2.51 | -2.3 dB |
| Peaking | 5671 Hz  | 2.01 | 2.1 dB  |
| Peaking | 12006 Hz | 6.88 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH1440/Shure%20SRH1440.png)