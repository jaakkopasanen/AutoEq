# Nuforce NE 600X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 10 -84; 20 -13.2; 22 -13.1; 23 -13.0; 25 -12.9; 26 -12.8; 28 -12.6; 30 -12.4; 32 -12.3; 35 -12.0; 37 -11.8; 40 -11.6; 42 -11.4; 45 -11.1; 49 -10.8; 52 -10.5; 56 -10.2; 59 -10.0; 64 -9.6; 68 -9.4; 73 -9.1; 78 -8.9; 83 -8.8; 89 -8.7; 95 -8.8; 102 -8.9; 109 -9.0; 117 -9.1; 125 -9.3; 134 -9.3; 143 -9.2; 153 -9.0; 164 -8.7; 175 -8.3; 188 -7.9; 201 -7.5; 215 -7.0; 230 -6.5; 246 -6.1; 263 -5.6; 282 -5.1; 301 -4.6; 323 -4.1; 345 -3.7; 369 -3.2; 395 -2.8; 423 -2.3; 452 -1.9; 484 -1.6; 518 -1.2; 554 -0.8; 593 -0.2; 635 -0.0; 679 0.2; 726 0.3; 777 0.6; 832 0.6; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.3; 1429 -1.9; 1529 -2.4; 1636 -3.0; 1751 -3.4; 1873 -3.6; 2004 -3.8; 2145 -4.3; 2295 -4.7; 2455 -4.9; 2627 -5.1; 2811 -5.1; 3008 -4.4; 3219 -3.4; 3444 -1.8; 3685 -1.5; 3943 -2.5; 4219 -5.0; 4514 -6.7; 4830 -6.1; 5168 -4.0; 5530 -0.6; 5917 2.3; 6331 4.0; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -1.1; 10167 -2.1; 10879 -0.5; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.8; 15258 -1.4; 16326 -1.0; 17469 -0.4; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.9dB` and instead set Global volume in the UI for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nuforce NE 600X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 8 Hz     | 0.75 | -13.0 dB |
| Peaking | 32 Hz    | 0.33 | -10.0 dB |
| Peaking | 168 Hz   | 0.82 | -6.0 dB  |
| Peaking | 2418 Hz  | 1.75 | -5.3 dB  |
| Peaking | 4597 Hz  | 6.49 | -6.8 dB  |
| Peaking | 792 Hz   | 2.07 | 1.6 dB   |
| Peaking | 1615 Hz  | 4.6  | -1.2 dB  |
| Peaking | 6430 Hz  | 3.84 | 5.7 dB   |
| Peaking | 5149 Hz  | 8.17 | -2.5 dB  |
| Peaking | 10873 Hz | 0.47 | -0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nuforce%20NE%20600X/Nuforce%20NE%20600X.png)