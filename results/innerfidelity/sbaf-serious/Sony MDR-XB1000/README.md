# Sony MDR-XB1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 -0.7; 22 -1.5; 23 -1.9; 25 -2.6; 26 -3.0; 28 -3.8; 30 -4.6; 32 -5.2; 35 -5.7; 37 -5.9; 40 -6.2; 42 -6.3; 45 -6.5; 49 -6.7; 52 -7.0; 56 -7.5; 59 -7.7; 64 -8.0; 68 -8.1; 73 -8.2; 78 -8.3; 83 -8.6; 89 -8.8; 95 -9.2; 102 -9.6; 109 -9.9; 117 -10.3; 125 -10.7; 134 -11.0; 143 -11.2; 153 -11.4; 164 -11.4; 175 -11.6; 188 -11.6; 201 -11.5; 215 -11.3; 230 -11.2; 246 -11.0; 263 -10.5; 282 -10.0; 301 -9.4; 323 -8.8; 345 -8.2; 369 -7.7; 395 -7.2; 423 -6.4; 452 -5.7; 484 -4.8; 518 -4.0; 554 -3.4; 593 -1.4; 635 0.3; 679 1.7; 726 2.5; 777 4.0; 832 4.3; 890 3.4; 952 1.7; 1019 -0.5; 1090 -2.9; 1167 -4.6; 1248 -4.4; 1336 -3.1; 1429 -1.0; 1529 0.9; 1636 3.0; 1751 5.5; 1873 6.0; 2004 6.0; 2145 3.8; 2295 -3.3; 2455 -8.3; 2627 -7.9; 2811 -5.8; 3008 -4.3; 3219 -3.6; 3444 -2.7; 3685 -2.7; 3943 -2.9; 4219 -2.7; 4514 -2.2; 4830 2.1; 5168 6.0; 5530 4.1; 5917 -0.2; 6331 -3.4; 6775 -2.0; 7249 0.6; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.7; 10167 -1.6; 10879 -1.3; 11640 -0.6; 12455 -0.0; 13327 0.0; 14260 -0.3; 15258 -1.7; 16326 -2.5; 17469 -2.0; 18692 -1.3; 20000 -0.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 101 Hz   | 0.35 | -8.3 dB  |
| Peaking | 272 Hz   | 0.77 | -7.3 dB  |
| Peaking | 1277 Hz  | 3.07 | -10.6 dB |
| Peaking | 1977 Hz  | 0.73 | 26.0 dB  |
| Peaking | 2524 Hz  | 1.18 | -28.2 dB |
| Peaking | 792 Hz   | 4.66 | 4.0 dB   |
| Peaking | 488 Hz   | 3.1  | -1.8 dB  |
| Peaking | 5247 Hz  | 5.69 | 12.2 dB  |
| Peaking | 5409 Hz  | 1.78 | -5.2 dB  |
| Peaking | 16885 Hz | 1.56 | -2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-XB1000/Sony%20MDR-XB1000.png)