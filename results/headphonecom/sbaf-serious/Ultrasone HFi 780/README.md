# Ultrasone HFi 780

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.5; 37 5.2; 40 4.5; 42 4.2; 45 3.7; 49 3.4; 52 3.2; 56 2.7; 59 2.4; 64 2.3; 68 2.4; 73 2.8; 78 3.1; 83 3.3; 89 3.5; 95 3.5; 102 3.8; 109 4.2; 117 4.6; 125 5.1; 134 5.5; 143 5.9; 153 6.0; 164 6.0; 175 6.0; 188 6.0; 201 6.0; 215 6.0; 230 5.9; 246 4.8; 263 4.0; 282 2.6; 301 1.3; 323 0.1; 345 -0.3; 369 -0.5; 395 -1.0; 423 -1.1; 452 -1.1; 484 -1.1; 518 -0.8; 554 -0.2; 593 0.2; 635 0.4; 679 0.5; 726 0.5; 777 0.7; 832 0.5; 890 0.3; 952 0.1; 1019 -0.0; 1090 0.3; 1167 0.6; 1248 -0.3; 1336 -1.1; 1429 -1.6; 1529 -1.8; 1636 -2.0; 1751 -1.8; 1873 -1.5; 2004 -1.3; 2145 2.8; 2295 6.0; 2455 4.7; 2627 3.1; 2811 2.9; 3008 2.9; 3219 2.4; 3444 1.4; 3685 1.2; 3943 2.7; 4219 5.1; 4514 5.4; 4830 3.9; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -1.5; 10167 -2.6; 10879 -1.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFi 780 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 23 Hz   |  0.56 | 6.1 dB  |
| Peaking | 168 Hz  |  1.27 | 6.4 dB  |
| Peaking | 1972 Hz |  2.15 | -6.4 dB |
| Peaking | 2289 Hz |  3.07 | 9.5 dB  |
| Peaking | 5358 Hz |  2.12 | 6.5 dB  |
| Peaking | 239 Hz  |  4.56 | 2.3 dB  |
| Peaking | 392 Hz  |  2.21 | -2.4 dB |
| Peaking | 6347 Hz | 10.82 | 2.0 dB  |
| Peaking | 3016 Hz |  9.7  | 1.1 dB  |
| Peaking | 9898 Hz |  3.89 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20HFi%20780/Ultrasone%20HFi%20780.png)