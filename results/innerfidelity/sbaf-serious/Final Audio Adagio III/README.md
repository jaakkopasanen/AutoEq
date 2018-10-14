# Final Audio Adagio III

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 -10.6; 23 -10.6; 25 -10.6; 28 -10.6; 31 -10.6; 34 -10.6; 37 -10.7; 41 -10.7; 45 -10.8; 49 -10.8; 54 -11.0; 60 -11.1; 66 -11.3; 72 -11.5; 79 -11.7; 87 -11.9; 96 -12.1; 106 -12.1; 116 -12.1; 128 -12.1; 141 -12.0; 155 -11.9; 170 -11.6; 187 -11.3; 206 -10.9; 227 -10.3; 249 -9.8; 274 -9.1; 302 -8.3; 332 -7.5; 365 -6.6; 402 -5.6; 442 -4.4; 486 -3.3; 535 -2.1; 588 -0.5; 647 0.7; 712 1.6; 783 2.5; 861 1.9; 947 0.8; 1042 -0.5; 1146 -1.1; 1261 -0.8; 1387 -0.6; 1526 -0.4; 1678 -0.5; 1846 -0.8; 2031 -1.3; 2234 -2.4; 2457 -3.3; 2703 -2.8; 2973 0.2; 3270 3.4; 3597 5.0; 3957 4.1; 4353 1.0; 4788 -1.6; 5267 -2.1; 5793 2.0; 6373 5.3; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.4dB` and instead set Global volume in the UI for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Adagio III ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.24 | -10.7 dB |
| Peaking | 191 Hz   | 0.79 | -6.9 dB  |
| Peaking | 3642 Hz  | 3.16 | 12.0 dB  |
| Peaking | 3700 Hz  | 1.08 | -6.0 dB  |
| Peaking | 6412 Hz  | 5.45 | 7.2 dB   |
| Peaking | 19 Hz    | 2.24 | -0.9 dB  |
| Peaking | 362 Hz   | 2.24 | -1.8 dB  |
| Peaking | 754 Hz   | 2.43 | 4.1 dB   |
| Peaking | 2523 Hz  | 6.47 | -2.2 dB  |
| Peaking | 10506 Hz | 1.75 | 0.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Final%20Audio%20Adagio%20III/Final%20Audio%20Adagio%20III.png)