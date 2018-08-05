# Ultrasone HFi-780

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 6.0; 143 6.0; 153 6.0; 164 6.0; 175 6.0; 188 6.0; 201 6.0; 215 6.0; 230 5.9; 246 4.8; 263 4.0; 282 2.6; 301 1.3; 323 0.1; 345 -0.3; 369 -0.5; 395 -1.0; 423 -1.1; 452 -1.1; 484 -1.1; 518 -0.8; 554 -0.2; 593 0.2; 635 0.4; 679 0.5; 726 0.5; 777 0.7; 832 0.5; 890 0.3; 952 0.1; 1019 -0.0; 1090 0.3; 1167 0.6; 1248 -0.3; 1336 -1.1; 1429 -1.6; 1529 -1.8; 1636 -2.0; 1751 -1.8; 1873 -1.5; 2004 -1.3; 2145 2.8; 2295 6.0; 2455 4.7; 2627 3.1; 2811 2.9; 3008 2.9; 3219 2.4; 3444 1.4; 3685 1.2; 3943 2.7; 4219 5.1; 4514 5.4; 4830 3.9; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -1.5; 10167 -2.6; 10879 -1.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFi-780 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 60 Hz    | 0.27 | 6.8 dB  |
| Peaking | 1948 Hz  | 1.81 | -5.5 dB |
| Peaking | 2328 Hz  | 3.66 | 9.2 dB  |
| Peaking | 5632 Hz  | 1.33 | 7.1 dB  |
| Peaking | 8958 Hz  | 1.45 | -3.4 dB |
| Peaking | 18 Hz    | 1.13 | 1.9 dB  |
| Peaking | 56 Hz    | 0.83 | -1.0 dB |
| Peaking | 223 Hz   | 1.41 | 3.3 dB  |
| Peaking | 369 Hz   | 1.66 | -3.9 dB |
| Peaking | 12202 Hz | 5.58 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20HFi-780/Ultrasone%20HFi-780.png)