# Ultrasone Edition 8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.7; 49 5.3; 52 5.0; 56 4.9; 59 4.8; 64 4.7; 68 4.5; 73 4.2; 78 4.0; 83 3.9; 89 4.1; 95 3.9; 102 3.4; 109 2.8; 117 2.3; 125 1.8; 134 1.4; 143 1.1; 153 1.0; 164 1.4; 175 0.5; 188 -0.2; 201 -0.6; 215 -0.6; 230 -0.4; 246 -0.3; 263 0.2; 282 0.1; 301 -0.2; 323 -0.1; 345 0.1; 369 0.2; 395 0.2; 423 0.4; 452 0.5; 484 0.4; 518 0.5; 554 0.8; 593 1.2; 635 1.3; 679 1.2; 726 1.3; 777 1.3; 832 1.0; 890 0.6; 952 0.2; 1019 0.2; 1090 0.6; 1167 1.1; 1248 1.5; 1336 1.9; 1429 2.3; 1529 2.5; 1636 2.8; 1751 3.6; 1873 5.2; 2004 6.0; 2145 6.0; 2295 6.0; 2455 3.0; 2627 1.1; 2811 2.0; 3008 3.4; 3219 4.6; 3444 4.3; 3685 2.0; 3943 2.4; 4219 5.2; 4514 6.0; 4830 6.0; 5168 6.0; 5530 4.9; 5917 -1.7; 6331 -4.3; 6775 -3.1; 7249 -0.2; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -1.4; 14260 -4.8; 15258 -3.6; 16326 -0.3; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Edition 8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.44 | 6.3 dB   |
| Peaking | 2011 Hz  | 2.09 | 5.8 dB   |
| Peaking | 5332 Hz  | 1.06 | 20.0 dB  |
| Peaking | 7134 Hz  | 1.07 | 8.2 dB   |
| Peaking | 6299 Hz  | 1.25 | -28.1 dB |
| Peaking | 212 Hz   | 3.1  | -1.6 dB  |
| Peaking | 721 Hz   | 1.91 | 1.2 dB   |
| Peaking | 970 Hz   | 5.85 | -0.9 dB  |
| Peaking | 12666 Hz | 2.58 | 2.0 dB   |
| Peaking | 14420 Hz | 4.94 | -4.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20Edition%208/Ultrasone%20Edition%208.png)