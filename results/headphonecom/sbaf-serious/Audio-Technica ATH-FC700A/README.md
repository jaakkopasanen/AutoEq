# Audio-Technica ATH-FC700A

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.9; 49 5.3; 52 4.6; 56 4.3; 59 4.5; 64 4.2; 68 3.3; 73 2.5; 78 1.9; 83 1.5; 89 0.9; 95 0.5; 102 0.1; 109 -0.2; 117 -0.4; 125 -0.4; 134 0.5; 143 0.7; 153 0.2; 164 0.0; 175 -0.3; 188 -0.2; 201 -0.1; 215 -0.1; 230 -0.1; 246 -0.0; 263 -0.5; 282 -1.1; 301 -1.0; 323 -0.6; 345 -0.3; 369 -0.3; 395 -0.3; 423 -0.0; 452 0.0; 484 0.1; 518 0.2; 554 0.4; 593 0.6; 635 0.6; 679 0.7; 726 0.8; 777 0.7; 832 0.5; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.3; 1248 -0.6; 1336 -0.7; 1429 -1.0; 1529 -1.7; 1636 -2.1; 1751 -2.5; 1873 -2.9; 2004 -3.1; 2145 -3.1; 2295 -2.7; 2455 -1.9; 2627 -0.8; 2811 -0.3; 3008 0.7; 3219 1.5; 3444 1.9; 3685 2.6; 3943 2.9; 4219 2.9; 4514 3.6; 4830 3.8; 5168 6.0; 5530 -0.3; 5917 -5.0; 6331 -4.9; 6775 -8.4; 7249 -8.9; 7756 -7.3; 8299 -5.5; 8880 -3.6; 9502 -1.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -0.0; 14260 -2.4; 15258 -4.0; 16326 -3.9; 17469 -2.8; 18692 -0.5; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-FC700A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.81 | 6.9 dB   |
| Peaking | 2035 Hz  | 2.2  | -3.8 dB  |
| Peaking | 4831 Hz  | 1.67 | 7.1 dB   |
| Peaking | 6931 Hz  | 2.42 | -11.7 dB |
| Peaking | 16073 Hz | 2.71 | -4.5 dB  |
| Peaking | 62 Hz    | 3.98 | 1.5 dB   |
| Peaking | 108 Hz   | 2.51 | -1.4 dB  |
| Peaking | 291 Hz   | 3.53 | -1.2 dB  |
| Peaking | 711 Hz   | 2.61 | 1.0 dB   |
| Peaking | 10829 Hz | 3.69 | 1.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio-Technica%20ATH-FC700A/Audio-Technica%20ATH-FC700A.png)