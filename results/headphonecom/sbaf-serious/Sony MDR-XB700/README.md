# Sony MDR-XB700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 -11.6; 22 -11.5; 23 -11.4; 25 -11.1; 26 -10.9; 28 -10.5; 30 -10.1; 32 -10.1; 35 -10.5; 37 -10.9; 40 -11.2; 42 -11.0; 45 -10.2; 49 -8.8; 52 -7.7; 56 -7.4; 59 -8.1; 64 -9.8; 68 -11.0; 73 -11.9; 78 -12.4; 83 -12.6; 89 -12.7; 95 -12.8; 102 -12.7; 109 -12.4; 117 -12.1; 125 -11.7; 134 -10.9; 143 -10.5; 153 -10.2; 164 -9.5; 175 -9.8; 188 -9.1; 201 -8.2; 215 -7.1; 230 -6.3; 246 -5.3; 263 -4.5; 282 -3.8; 301 -3.0; 323 -2.2; 345 -1.7; 369 -1.6; 395 -1.5; 423 -1.0; 452 -0.8; 484 -0.4; 518 0.4; 554 1.1; 593 1.8; 635 3.4; 679 4.6; 726 5.2; 777 5.0; 832 3.8; 890 2.7; 952 1.2; 1019 -0.4; 1090 -1.8; 1167 -2.9; 1248 -4.1; 1336 -5.2; 1429 -6.1; 1529 -6.9; 1636 -7.4; 1751 -7.4; 1873 -7.2; 2004 -6.8; 2145 -5.9; 2295 -4.5; 2455 -2.8; 2627 -1.4; 2811 0.3; 3008 2.7; 3219 4.9; 3444 5.7; 3685 1.0; 3943 -2.9; 4219 -2.8; 4514 -3.0; 4830 -4.3; 5168 -6.1; 5530 -9.5; 5917 -6.7; 6331 0.0; 6775 2.1; 7249 1.3; 7756 0.1; 8299 -2.0; 8880 -4.2; 9502 -5.9; 10167 -5.1; 10879 -0.8; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -3.3; 15258 -5.0; 16326 -2.2; 17469 -0.0; 18692 -0.3; 20000 -5.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 10 Hz    | 1.12 | -11.5 dB |
| Peaking | 21 Hz    | 0.22 | -8.2 dB  |
| Peaking | 120 Hz   | 0.88 | -9.2 dB  |
| Peaking | 1717 Hz  | 2.79 | -8.4 dB  |
| Peaking | 10492 Hz | 0.43 | -2.5 dB  |
| Peaking | 737 Hz   | 2.63 | 7.1 dB   |
| Peaking | 3347 Hz  | 2.62 | 13.4 dB  |
| Peaking | 5932 Hz  | 0.56 | -11.4 dB |
| Peaking | 7054 Hz  | 2.67 | 14.6 dB  |
| Peaking | 12021 Hz | 2.52 | 7.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-XB700/Sony%20MDR-XB700.png)