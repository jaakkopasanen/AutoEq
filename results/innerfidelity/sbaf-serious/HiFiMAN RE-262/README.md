# HiFiMAN RE-262

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 5.9; 40 5.8; 42 5.8; 45 5.8; 49 5.8; 52 5.8; 56 5.7; 59 5.7; 64 5.5; 68 5.4; 73 5.2; 78 5.0; 83 4.8; 89 4.4; 95 3.9; 102 3.3; 109 2.9; 117 2.2; 125 1.5; 134 1.0; 143 0.6; 153 0.3; 164 0.1; 175 0.1; 188 -0.0; 201 -0.1; 215 -0.2; 230 -0.2; 246 -0.3; 263 -0.3; 282 -0.2; 301 -0.3; 323 -0.4; 345 -0.3; 369 -0.3; 395 -0.3; 423 -0.1; 452 -0.1; 484 -0.1; 518 -0.1; 554 0.2; 593 0.5; 635 0.7; 679 0.7; 726 0.9; 777 1.2; 832 1.0; 890 0.7; 952 0.4; 1019 -0.1; 1090 -0.8; 1167 -1.5; 1248 -2.5; 1336 -3.6; 1429 -4.9; 1529 -6.0; 1636 -6.6; 1751 -6.3; 1873 -4.8; 2004 -2.8; 2145 -0.7; 2295 1.6; 2455 3.9; 2627 5.8; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN RE-262 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 45 Hz   | 0.25 | 6.7 dB   |
| Peaking | 173 Hz  | 0.7  | -3.7 dB  |
| Peaking | 822 Hz  | 2.38 | 1.5 dB   |
| Peaking | 1688 Hz | 1.81 | -11.1 dB |
| Peaking | 3241 Hz | 0.74 | 8.4 dB   |
| Peaking | 10 Hz   | 1.49 | 0.7 dB   |
| Peaking | 2647 Hz | 5.63 | 2.3 dB   |
| Peaking | 3252 Hz | 1.47 | -1.2 dB  |
| Peaking | 6209 Hz | 2.08 | 5.8 dB   |
| Peaking | 7455 Hz | 1.47 | -4.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20RE-262/HiFiMAN%20RE-262.png)