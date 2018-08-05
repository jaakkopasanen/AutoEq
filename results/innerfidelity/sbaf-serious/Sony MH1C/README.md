# Sony MH1C

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -10.9; 22 -10.7; 23 -10.6; 25 -10.5; 26 -10.4; 28 -10.2; 30 -10.1; 32 -9.9; 35 -9.6; 37 -9.4; 40 -9.1; 42 -8.9; 45 -8.7; 49 -8.3; 52 -8.0; 56 -7.7; 59 -7.5; 64 -7.1; 68 -6.9; 73 -6.6; 78 -6.4; 83 -6.3; 89 -6.2; 95 -6.3; 102 -6.5; 109 -6.6; 117 -6.7; 125 -6.9; 134 -7.0; 143 -6.9; 153 -6.7; 164 -6.5; 175 -6.1; 188 -5.8; 201 -5.5; 215 -5.1; 230 -4.7; 246 -4.3; 263 -3.9; 282 -3.5; 301 -3.1; 323 -2.8; 345 -2.4; 369 -2.1; 395 -1.7; 423 -1.3; 452 -1.0; 484 -0.8; 518 -0.6; 554 -0.2; 593 0.2; 635 0.4; 679 0.3; 726 0.5; 777 0.6; 832 0.5; 890 0.2; 952 -0.0; 1019 0.0; 1090 -0.5; 1167 -1.3; 1248 -1.2; 1336 -1.3; 1429 -1.6; 1529 -2.1; 1636 -2.6; 1751 -2.8; 1873 -2.9; 2004 -2.8; 2145 -2.8; 2295 -2.6; 2455 -2.1; 2627 -1.8; 2811 -1.2; 3008 -0.2; 3219 1.1; 3444 2.4; 3685 3.0; 3943 3.2; 4219 2.5; 4514 2.4; 4830 3.4; 5168 4.9; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.4; 15258 -1.5; 16326 -0.2; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MH1C ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 10 Hz    | 0.67 | -10.4 dB |
| Peaking | 34 Hz    | 0.45 | -7.2 dB  |
| Peaking | 161 Hz   | 0.88 | -5.1 dB  |
| Peaking | 1966 Hz  | 1.98 | -3.5 dB  |
| Peaking | 5542 Hz  | 2.06 | 6.2 dB   |
| Peaking | 727 Hz   | 2.42 | 1.3 dB   |
| Peaking | 3376 Hz  | 1.59 | -1.9 dB  |
| Peaking | 3579 Hz  | 3.57 | 4.2 dB   |
| Peaking | 12193 Hz | 0.59 | -0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MH1C/Sony%20MH1C.png)