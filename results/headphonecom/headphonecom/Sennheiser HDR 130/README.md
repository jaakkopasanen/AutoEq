# Sennheiser HDR 130

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.9; 52 5.2; 56 3.7; 59 2.7; 64 1.6; 68 0.7; 73 -0.5; 78 -1.5; 83 -2.3; 89 -3.2; 95 -3.7; 102 -4.7; 109 -5.2; 117 -5.5; 125 -5.7; 134 -6.2; 143 -6.5; 153 -6.7; 164 -6.7; 175 -6.9; 188 -7.0; 201 -6.6; 215 -6.9; 230 -7.5; 246 -7.1; 263 -7.1; 282 -7.1; 301 -7.0; 323 -6.6; 345 -6.4; 369 -6.4; 395 -5.8; 423 -5.8; 452 -5.6; 484 -5.2; 518 -5.0; 554 -4.2; 593 -2.9; 635 -2.3; 679 -1.6; 726 -1.1; 777 -1.5; 832 -1.7; 890 -1.2; 952 -0.6; 1019 0.1; 1090 0.4; 1167 -0.4; 1248 -1.6; 1336 -2.0; 1429 -2.4; 1529 -2.8; 1636 -2.5; 1751 -2.6; 1873 -2.8; 2004 -1.6; 2145 -0.3; 2295 1.7; 2455 2.6; 2627 -0.3; 2811 -2.7; 3008 -4.6; 3219 -4.1; 3444 -4.6; 3685 -5.1; 3943 -1.6; 4219 -5.8; 4514 -6.0; 4830 -2.5; 5168 -0.3; 5530 -1.3; 5917 -2.8; 6331 -3.4; 6775 2.2; 7249 1.3; 7756 0.3; 8299 -2.2; 8880 -6.4; 9502 -6.7; 10167 -3.1; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HDR 130 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 44 Hz    | 0.48 | 11.4 dB  |
| Peaking | 109 Hz   | 0.46 | -10.5 dB |
| Peaking | 344 Hz   | 0.96 | -3.8 dB  |
| Peaking | 3959 Hz  | 1.49 | -4.6 dB  |
| Peaking | 22161 Hz | 2.09 | -3.6 dB  |
| Peaking | 1728 Hz  | 3.08 | -2.4 dB  |
| Peaking | 2409 Hz  | 5.41 | 5.0 dB   |
| Peaking | 2966 Hz  | 6.31 | -2.5 dB  |
| Peaking | 7155 Hz  | 7    | 3.8 dB   |
| Peaking | 9254 Hz  | 5.84 | -7.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HDR%20130/Sennheiser%20HDR%20130.png)