# Sony MDR-ZX700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 5.8; 40 5.0; 42 4.4; 45 3.6; 49 2.6; 52 1.9; 56 0.9; 59 0.2; 64 -0.6; 68 -1.0; 73 -1.1; 78 -0.7; 83 -0.5; 89 -0.5; 95 -1.5; 102 -2.9; 109 -3.4; 117 -3.8; 125 -4.0; 134 -4.1; 143 -4.1; 153 -4.0; 164 -2.9; 175 -3.2; 188 -3.7; 201 -3.8; 215 -4.0; 230 -4.1; 246 -4.1; 263 -4.0; 282 -4.0; 301 -4.4; 323 -4.8; 345 -5.9; 369 -5.3; 395 -4.8; 423 -4.6; 452 -4.4; 484 -3.8; 518 -3.3; 554 -2.6; 593 -1.8; 635 -1.0; 679 -0.3; 726 -0.1; 777 -0.3; 832 -0.0; 890 0.1; 952 0.1; 1019 0.0; 1090 0.0; 1167 0.2; 1248 0.4; 1336 0.6; 1429 0.6; 1529 0.2; 1636 -0.5; 1751 -2.0; 1873 -3.1; 2004 -4.2; 2145 -4.5; 2295 -3.9; 2455 -3.1; 2627 -2.3; 2811 -1.6; 3008 -0.8; 3219 0.5; 3444 1.9; 3685 4.4; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.2; 7756 -3.7; 8299 -8.6; 8880 -9.4; 9502 -5.6; 10167 -0.6; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.92 | 7.2 dB   |
| Peaking | 244 Hz   | 0.4  | -5.0 dB  |
| Peaking | 2420 Hz  | 1.22 | -13.5 dB |
| Peaking | 3710 Hz  | 0.42 | 11.2 dB  |
| Peaking | 8666 Hz  | 3.32 | -15.9 dB |
| Peaking | 10 Hz    | 2.32 | 1.4 dB   |
| Peaking | 380 Hz   | 4.46 | -1.6 dB  |
| Peaking | 3268 Hz  | 8.47 | -1.8 dB  |
| Peaking | 6397 Hz  | 5.14 | 1.8 dB   |
| Peaking | 14490 Hz | 1.39 | -1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sony%20MDR-ZX700/Sony%20MDR-ZX700.png)