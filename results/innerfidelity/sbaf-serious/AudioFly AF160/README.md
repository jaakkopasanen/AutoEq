# AudioFly AF160

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.8; 22 4.6; 23 4.6; 25 4.4; 26 4.4; 28 4.3; 30 4.2; 32 4.1; 35 3.9; 37 3.9; 40 3.8; 42 3.7; 45 3.5; 49 3.3; 52 3.1; 56 2.9; 59 2.8; 64 2.5; 68 2.3; 73 2.1; 78 1.8; 83 1.5; 89 1.2; 95 0.9; 102 0.6; 109 0.5; 117 0.3; 125 0.0; 134 -0.2; 143 -0.4; 153 -0.6; 164 -0.7; 175 -0.7; 188 -0.9; 201 -0.9; 215 -0.9; 230 -0.9; 246 -0.9; 263 -1.0; 282 -0.9; 301 -0.8; 323 -0.8; 345 -0.7; 369 -0.6; 395 -0.5; 423 -0.3; 452 -0.2; 484 -0.2; 518 -0.1; 554 0.2; 593 0.5; 635 0.6; 679 0.6; 726 0.7; 777 0.8; 832 0.7; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.6; 1248 -0.8; 1336 -1.1; 1429 -1.5; 1529 -1.8; 1636 -2.0; 1751 -2.0; 1873 -1.7; 2004 -1.3; 2145 -0.9; 2295 -0.3; 2455 0.7; 2627 1.5; 2811 2.2; 3008 3.3; 3219 3.7; 3444 3.6; 3685 3.2; 3943 3.8; 4219 4.9; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099952559277957dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioFly AF160 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.68 | 4.2 dB  |
| Peaking | 52 Hz   | 0.89 | 2.0 dB  |
| Peaking | 204 Hz  | 1.07 | -1.3 dB |
| Peaking | 1724 Hz | 2.54 | -2.8 dB |
| Peaking | 4868 Hz | 1.41 | 6.5 dB  |
| Peaking | 737 Hz  | 1.86 | 1.3 dB  |
| Peaking | 2033 Hz | 0.17 | -0.4 dB |
| Peaking | 3048 Hz | 4.62 | 2.1 dB  |
| Peaking | 6395 Hz | 3.65 | 4.3 dB  |
| Peaking | 7154 Hz | 1.67 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioFly%20AF160/AudioFly%20AF160.png)