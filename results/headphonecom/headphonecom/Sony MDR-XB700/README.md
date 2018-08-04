# Sony MDR-XB700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -16.1; 22 -16.0; 23 -15.9; 25 -15.6; 26 -15.4; 28 -15.0; 30 -14.7; 32 -14.6; 35 -15.0; 37 -15.5; 40 -15.8; 42 -15.6; 45 -14.8; 49 -13.3; 52 -12.3; 56 -11.9; 59 -12.6; 64 -14.3; 68 -15.4; 73 -16.3; 78 -16.7; 83 -16.7; 89 -16.7; 95 -16.5; 102 -16.1; 109 -15.6; 117 -15.0; 125 -14.1; 134 -13.1; 143 -12.4; 153 -11.9; 164 -11.1; 175 -11.3; 188 -10.5; 201 -9.6; 215 -8.5; 230 -7.7; 246 -6.7; 263 -5.8; 282 -5.2; 301 -4.4; 323 -3.6; 345 -3.1; 369 -3.0; 395 -2.8; 423 -2.3; 452 -1.8; 484 -1.1; 518 -0.1; 554 0.6; 593 1.3; 635 3.1; 679 4.6; 726 5.2; 777 4.8; 832 3.8; 890 2.7; 952 1.2; 1019 -0.4; 1090 -1.7; 1167 -2.7; 1248 -3.5; 1336 -3.9; 1429 -4.0; 1529 -4.2; 1636 -4.4; 1751 -4.4; 1873 -4.2; 2004 -3.8; 2145 -2.9; 2295 -1.5; 2455 0.1; 2627 1.6; 2811 3.2; 3008 5.2; 3219 6.0; 3444 6.0; 3685 3.1; 3943 -0.6; 4219 0.8; 4514 1.8; 4830 1.2; 5168 -0.7; 5530 -4.8; 5917 -3.2; 6331 2.3; 6775 3.2; 7249 1.3; 7756 0.3; 8299 -0.6; 8880 -2.3; 9502 -3.3; 10167 -1.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 8 Hz    | 1.43 | -15.7 dB |
| Peaking | 23 Hz   | 0.68 | -11.6 dB |
| Peaking | 99 Hz   | 0.56 | -14.7 dB |
| Peaking | 715 Hz  | 3.54 | 7.2 dB   |
| Peaking | 3251 Hz | 5.72 | 7.2 dB   |
| Peaking | 885 Hz  | 5.65 | 2.4 dB   |
| Peaking | 1597 Hz | 1.03 | -7.4 dB  |
| Peaking | 5622 Hz | 9.46 | -7.8 dB  |
| Peaking | 2554 Hz | 0.25 | 2.8 dB   |
| Peaking | 9402 Hz | 4.41 | -4.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sony%20MDR-XB700/Sony%20MDR-XB700.png)