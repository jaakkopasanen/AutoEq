# Sony MDRV-SA5000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.9; 68 5.4; 73 4.8; 78 4.2; 83 3.6; 89 3.0; 95 2.4; 102 2.0; 109 1.8; 117 1.6; 125 1.4; 134 1.3; 143 1.1; 153 1.0; 164 1.3; 175 1.8; 188 1.9; 201 2.0; 215 2.2; 230 2.4; 246 2.6; 263 2.9; 282 3.2; 301 3.4; 323 3.7; 345 3.4; 369 2.5; 395 1.4; 423 2.4; 452 2.7; 484 2.5; 518 2.2; 554 2.0; 593 1.9; 635 1.8; 679 1.2; 726 0.8; 777 0.4; 832 -0.2; 890 -0.7; 952 -0.5; 1019 0.2; 1090 1.3; 1167 2.2; 1248 3.0; 1336 3.2; 1429 2.9; 1529 2.3; 1636 1.6; 1751 1.1; 1873 0.1; 2004 -0.7; 2145 -1.9; 2295 -3.3; 2455 -3.8; 2627 -3.3; 2811 -2.2; 3008 -0.2; 3219 1.7; 3444 4.6; 3685 6.0; 3943 5.9; 4219 3.5; 4514 2.1; 4830 4.4; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.2; 8299 -2.0; 8880 -4.2; 9502 -3.7; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDRV-SA5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.57 | 6.8 dB  |
| Peaking | 352 Hz  | 0.96 | 2.9 dB  |
| Peaking | 8970 Hz | 4.84 | -5.5 dB |
| Peaking | 3748 Hz | 6.83 | 5.9 dB  |
| Peaking | 5770 Hz | 2.64 | 6.8 dB  |
| Peaking | 66 Hz   | 3.74 | 1.4 dB  |
| Peaking | 123 Hz  | 1.99 | -0.9 dB |
| Peaking | 954 Hz  | 2.62 | -3.7 dB |
| Peaking | 1235 Hz | 1.3  | 3.9 dB  |
| Peaking | 2417 Hz | 3.42 | -5.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDRV-SA5000/Sony%20MDRV-SA5000.png)