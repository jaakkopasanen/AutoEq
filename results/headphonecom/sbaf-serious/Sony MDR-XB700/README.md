# Sony MDR-XB700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 -15.6; 22 -15.5; 23 -15.4; 25 -15.1; 26 -14.9; 28 -14.5; 30 -14.1; 32 -14.1; 35 -14.5; 37 -14.9; 40 -15.2; 42 -15.0; 45 -14.2; 49 -12.7; 52 -11.7; 56 -11.4; 59 -12.0; 64 -13.7; 68 -14.8; 73 -15.7; 78 -16.0; 83 -16.0; 89 -15.9; 95 -15.7; 102 -15.1; 109 -14.5; 117 -13.7; 125 -12.9; 134 -11.8; 143 -11.1; 153 -10.6; 164 -9.8; 175 -9.9; 188 -9.2; 201 -8.3; 215 -7.2; 230 -6.3; 246 -5.3; 263 -4.5; 282 -3.8; 301 -3.0; 323 -2.2; 345 -1.7; 369 -1.6; 395 -1.5; 423 -1.0; 452 -0.8; 484 -0.4; 518 0.4; 554 1.1; 593 1.8; 635 3.4; 679 4.6; 726 5.2; 777 5.0; 832 3.8; 890 2.7; 952 1.2; 1019 -0.4; 1090 -1.8; 1167 -2.9; 1248 -4.1; 1336 -5.2; 1429 -6.1; 1529 -6.9; 1636 -7.4; 1751 -7.4; 1873 -7.2; 2004 -6.8; 2145 -5.9; 2295 -4.5; 2455 -2.8; 2627 -1.4; 2811 0.3; 3008 2.7; 3219 4.9; 3444 5.7; 3685 1.0; 3943 -2.9; 4219 -2.8; 4514 -3.0; 4830 -4.3; 5168 -6.1; 5530 -9.5; 5917 -6.7; 6331 0.0; 6775 2.1; 7249 1.3; 7756 0.1; 8299 -2.0; 8880 -4.2; 9502 -5.9; 10167 -5.1; 10879 -0.8; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -3.3; 15258 -5.0; 16326 -2.2; 17469 -0.0; 18692 -0.3; 20000 -5.2
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
| Peaking | 10 Hz    | 1.41 | -15.3 dB |
| Peaking | 23 Hz    | 0.29 | -12.2 dB |
| Peaking | 106 Hz   | 0.85 | -10.4 dB |
| Peaking | 1717 Hz  | 2.79 | -8.4 dB  |
| Peaking | 10491 Hz | 0.43 | -2.5 dB  |
| Peaking | 736 Hz   | 2.58 | 7.1 dB   |
| Peaking | 3347 Hz  | 2.62 | 13.4 dB  |
| Peaking | 5909 Hz  | 0.55 | -11.3 dB |
| Peaking | 7054 Hz  | 2.71 | 14.4 dB  |
| Peaking | 12020 Hz | 2.53 | 7.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-XB700/Sony%20MDR-XB700.png)