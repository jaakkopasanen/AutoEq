# V-Moda Crossfade Wireless Wired Mode

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 2.9; 22 2.1; 23 1.8; 25 1.1; 26 0.8; 28 0.2; 30 -0.3; 32 -0.7; 35 -1.3; 37 -1.7; 40 -2.1; 42 -2.3; 45 -2.6; 49 -2.9; 52 -3.0; 56 -3.2; 59 -3.2; 64 -3.1; 68 -2.7; 73 -2.5; 78 -3.1; 83 -4.2; 89 -4.7; 95 -4.5; 102 -4.2; 109 -4.9; 117 -5.8; 125 -6.3; 134 -6.6; 143 -6.7; 153 -6.7; 164 -5.9; 175 -5.9; 188 -5.7; 201 -5.2; 215 -4.4; 230 -3.4; 246 -2.3; 263 -1.3; 282 0.2; 301 1.3; 323 2.7; 345 4.0; 369 5.6; 395 6.0; 423 6.0; 452 6.0; 484 6.0; 518 6.0; 554 6.0; 593 5.9; 635 5.4; 679 4.5; 726 3.7; 777 3.0; 832 2.1; 890 1.2; 952 0.4; 1019 -0.2; 1090 -0.8; 1167 -1.1; 1248 -1.5; 1336 -2.0; 1429 -2.4; 1529 -2.7; 1636 -2.9; 1751 -2.9; 1873 -2.4; 2004 -2.0; 2145 -2.0; 2295 -2.4; 2455 -2.1; 2627 -1.0; 2811 -1.5; 3008 -2.1; 3219 -3.0; 3444 -4.2; 3685 -3.7; 3943 -1.3; 4219 0.2; 4514 3.5; 4830 5.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.2; 8880 -3.8; 9502 -4.3; 10167 -3.3; 10879 -1.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade Wireless Wired Mode ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 180 Hz  |  0.59 | -10.4 dB |
| Peaking | 444 Hz  |  0.65 | 12.8 dB  |
| Peaking | 1865 Hz |  0.31 | -4.9 dB  |
| Peaking | 5571 Hz |  1.95 | 9.8 dB   |
| Peaking | 9319 Hz |  4.1  | -5.2 dB  |
| Peaking | 16 Hz   |  1.34 | 4.3 dB   |
| Peaking | 43 Hz   |  2.12 | -1.7 dB  |
| Peaking | 2686 Hz |  3.4  | 2.0 dB   |
| Peaking | 3537 Hz |  4.49 | -3.4 dB  |
| Peaking | 4685 Hz | 10.86 | 2.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20Crossfade%20Wireless%20Wired%20Mode/V-Moda%20Crossfade%20Wireless%20Wired%20Mode.png)