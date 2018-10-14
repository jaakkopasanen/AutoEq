# Beats Mixr 2014

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.9; 23 -1.4; 25 -1.8; 28 -2.2; 31 -2.5; 34 -2.7; 37 -2.9; 41 -3.1; 45 -3.2; 49 -3.3; 54 -3.6; 60 -3.7; 66 -3.9; 72 -4.1; 79 -4.2; 87 -4.5; 96 -4.9; 106 -5.2; 116 -4.9; 128 -4.8; 141 -5.3; 155 -5.7; 170 -5.2; 187 -5.6; 206 -5.6; 227 -5.3; 249 -4.4; 274 -2.8; 302 -1.3; 332 -0.4; 365 2.0; 402 3.3; 442 4.4; 486 3.4; 535 2.8; 588 2.2; 647 1.5; 712 0.9; 783 0.6; 861 0.2; 947 0.1; 1042 0.1; 1146 0.3; 1261 0.6; 1387 0.5; 1526 0.2; 1678 -0.1; 1846 -0.2; 2031 -0.5; 2234 -1.0; 2457 -1.1; 2703 -1.7; 2973 -1.1; 3270 -0.2; 3597 1.7; 3957 3.1; 4353 4.0; 4788 0.4; 5267 4.9; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Mixr 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.91 | -1.7 dB |
| Peaking | 103 Hz  | 0.62 | -3.9 dB |
| Peaking | 219 Hz  | 1.18 | -4.2 dB |
| Peaking | 434 Hz  | 1.7  | 5.8 dB  |
| Peaking | 5830 Hz | 3.05 | 6.5 dB  |
| Peaking | 1311 Hz | 5.79 | 0.6 dB  |
| Peaking | 2782 Hz | 2.55 | -2.0 dB |
| Peaking | 4216 Hz | 4.9  | 4.0 dB  |
| Peaking | 4331 Hz | 4.01 | -1.4 dB |
| Peaking | 8200 Hz | 5.48 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Mixr%202014/Beats%20Mixr%202014.png)