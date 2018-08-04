# AKG K712

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 10 -84; 20 -3.5; 22 -3.9; 23 -4.1; 25 -4.5; 26 -4.7; 28 -5.0; 30 -5.2; 32 -5.4; 35 -5.7; 37 -5.9; 40 -6.1; 42 -6.2; 45 -6.4; 49 -6.6; 52 -6.7; 56 -6.8; 59 -6.8; 64 -6.8; 68 -6.8; 73 -6.8; 78 -6.7; 83 -6.6; 89 -6.6; 95 -6.8; 102 -6.8; 109 -6.6; 117 -6.3; 125 -6.4; 134 -6.5; 143 -6.4; 153 -6.4; 164 -6.3; 175 -5.9; 188 -6.2; 201 -6.3; 215 -6.3; 230 -6.3; 246 -6.3; 263 -6.3; 282 -6.2; 301 -6.1; 323 -5.9; 345 -5.6; 369 -5.5; 395 -5.4; 423 -5.2; 452 -4.9; 484 -4.8; 518 -4.6; 554 -3.7; 593 -3.5; 635 -3.6; 679 -3.4; 726 -2.8; 777 -2.2; 832 -1.7; 890 -1.1; 952 -0.5; 1019 0.2; 1090 1.2; 1167 1.7; 1248 1.6; 1336 1.4; 1429 0.4; 1529 -0.2; 1636 -1.4; 1751 -2.3; 1873 -3.7; 2004 -5.5; 2145 -5.8; 2295 -4.0; 2455 -1.7; 2627 1.0; 2811 4.0; 3008 4.9; 3219 3.0; 3444 1.6; 3685 0.8; 3943 -0.2; 4219 -2.3; 4514 -3.2; 4830 -2.1; 5168 -2.5; 5530 -2.8; 5917 -3.5; 6331 -4.2; 6775 -6.5; 7249 -7.2; 7756 -6.4; 8299 -5.3; 8880 -4.0; 9502 -3.2; 10167 -3.3; 10879 -3.2; 11640 -0.9; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.4; 17469 -1.8; 18692 -2.7; 20000 -3.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.6dB` and instead set Global volume in the UI for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 70 Hz    | 0.26 | -6.5 dB  |
| Peaking | 425 Hz   | 0.66 | -3.8 dB  |
| Peaking | 2105 Hz  | 2.34 | -15.2 dB |
| Peaking | 2413 Hz  | 0.79 | 10.7 dB  |
| Peaking | 6601 Hz  | 0.9  | -7.6 dB  |
| Peaking | 1182 Hz  | 5.07 | 1.7 dB   |
| Peaking | 2986 Hz  | 5.72 | 3.9 dB   |
| Peaking | 4862 Hz  | 0.7  | -2.5 dB  |
| Peaking | 5715 Hz  | 3.18 | 4.0 dB   |
| Peaking | 12710 Hz | 2.76 | 2.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K712/AKG%20K712.png)