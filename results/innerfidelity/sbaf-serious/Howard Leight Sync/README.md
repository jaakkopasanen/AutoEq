# Howard Leight Sync

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 5.9; 64 4.6; 68 3.3; 73 1.9; 78 0.9; 83 0.3; 89 -1.0; 95 -2.7; 102 -4.6; 109 -6.4; 117 -8.1; 125 -9.7; 134 -10.7; 143 -10.8; 153 -11.6; 164 -11.4; 175 -11.4; 188 -11.7; 201 -11.3; 215 -10.8; 230 -10.4; 246 -10.1; 263 -9.9; 282 -9.3; 301 -8.7; 323 -7.6; 345 -6.6; 369 -6.4; 395 -6.2; 423 -5.6; 452 -4.9; 484 -5.2; 518 -5.1; 554 -4.7; 593 -4.4; 635 -4.2; 679 -4.0; 726 -3.5; 777 -2.9; 832 -2.2; 890 -1.4; 952 -0.4; 1019 -0.0; 1090 -0.0; 1167 0.2; 1248 0.2; 1336 0.1; 1429 -0.5; 1529 -2.0; 1636 -4.2; 1751 -6.7; 1873 -8.9; 2004 -10.8; 2145 -12.8; 2295 -13.5; 2455 -10.7; 2627 -9.1; 2811 -9.6; 3008 -7.7; 3219 -3.2; 3444 1.7; 3685 -1.2; 3943 -2.2; 4219 -2.1; 4514 -2.0; 4830 -3.9; 5168 -6.4; 5530 -10.4; 5917 -15.0; 6331 -15.9; 6775 -14.0; 7249 -12.6; 7756 -12.5; 8299 -14.1; 8880 -16.3; 9502 -17.4; 10167 -16.5; 10879 -14.3; 11640 -12.1; 12455 -11.5; 13327 -12.8; 14260 -14.5; 15258 -14.1; 16326 -11.4; 17469 -8.6; 18692 -7.0; 20000 -6.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Howard Leight Sync ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 208 Hz   | 0.9  | -12.4 dB |
| Peaking | 2222 Hz  | 3.26 | -13.2 dB |
| Peaking | 8108 Hz  | 1.12 | -12.0 dB |
| Peaking | 25961 Hz | 1.9  | -15.5 dB |
| Peaking | 33285 Hz | 0.7  | -11.0 dB |
| Peaking | 26 Hz    | 0.41 | 6.1 dB   |
| Peaking | 57 Hz    | 1.79 | 3.7 dB   |
| Peaking | 128 Hz   | 2.55 | -5.4 dB  |
| Peaking | 4214 Hz  | 2.55 | 4.1 dB   |
| Peaking | 6043 Hz  | 6.98 | -7.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Howard%20Leight%20Sync/Howard%20Leight%20Sync.png)