# Sennheiser PX100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.4; 22 3.7; 23 3.4; 25 2.9; 26 2.6; 28 2.2; 30 1.8; 32 1.5; 35 1.0; 37 0.8; 40 0.4; 42 0.2; 45 0.0; 49 -0.2; 52 -0.4; 56 -0.6; 59 -0.7; 64 -0.9; 68 -1.1; 73 -1.2; 78 -1.3; 83 -1.5; 89 -1.8; 95 -2.2; 102 -2.5; 109 -2.7; 117 -3.0; 125 -3.4; 134 -3.5; 143 -3.6; 153 -3.7; 164 -3.8; 175 -3.6; 188 -3.4; 201 -3.2; 215 -2.8; 230 -2.7; 246 -2.6; 263 -2.4; 282 -2.2; 301 -2.1; 323 -1.8; 345 -1.5; 369 -1.3; 395 -1.2; 423 -0.8; 452 -0.5; 484 -0.4; 518 -0.4; 554 -0.1; 593 0.1; 635 0.3; 679 0.2; 726 0.3; 777 0.4; 832 0.3; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.7; 1336 -1.3; 1429 -2.0; 1529 -2.7; 1636 -3.3; 1751 -3.7; 1873 -3.4; 2004 -2.4; 2145 -1.2; 2295 0.2; 2455 1.8; 2627 4.1; 2811 5.8; 3008 6.0; 3219 6.0; 3444 6.0; 3685 3.5; 3943 -1.8; 4219 -5.7; 4514 -3.5; 4830 1.0; 5168 4.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 1.48 | 4.2 dB   |
| Peaking | 154 Hz   | 0.86 | -3.9 dB  |
| Peaking | 4314 Hz  | 1.22 | -25.1 dB |
| Peaking | 3311 Hz  | 1.98 | 15.6 dB  |
| Peaking | 5369 Hz  | 1.37 | 19.6 dB  |
| Peaking | 895 Hz   | 1.25 | 1.5 dB   |
| Peaking | 1770 Hz  | 2.86 | -3.0 dB  |
| Peaking | 2677 Hz  | 7.21 | 2.7 dB   |
| Peaking | 11666 Hz | 0.44 | 0.3 dB   |
| Peaking | 7978 Hz  | 5.26 | -1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PX100/Sennheiser%20PX100.png)