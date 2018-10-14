# Logitech UE 6000 passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.0; 23 -2.1; 25 -2.2; 28 -2.3; 31 -2.3; 34 -2.3; 37 -2.2; 41 -2.2; 45 -2.1; 49 -2.0; 54 -1.9; 60 -1.7; 66 -1.6; 72 -1.6; 79 -1.5; 87 -1.4; 96 -1.5; 106 -1.3; 116 -1.6; 128 -1.5; 141 -1.6; 155 -1.5; 170 -0.2; 187 -0.7; 206 -0.8; 227 -0.3; 249 0.4; 274 1.2; 302 1.8; 332 2.1; 365 2.5; 402 2.6; 442 2.5; 486 2.1; 535 1.7; 588 1.5; 647 0.9; 712 0.3; 783 0.3; 861 0.1; 947 0.1; 1042 0.0; 1146 0.0; 1261 0.5; 1387 0.6; 1526 0.9; 1678 1.6; 1846 2.5; 2031 4.3; 2234 5.7; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 4.2; 4788 5.7; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech UE 6000 passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.66 | -2.2 dB |
| Peaking | 406 Hz  | 0.77 | 5.9 dB  |
| Peaking | 1017 Hz | 0.1  | -3.8 dB |
| Peaking | 2839 Hz | 0.83 | 9.5 dB  |
| Peaking | 5714 Hz | 2.3  | 5.7 dB  |
| Peaking | 1785 Hz | 2.3  | -1.1 dB |
| Peaking | 2176 Hz | 3.41 | 1.3 dB  |
| Peaking | 2838 Hz | 4.28 | -1.0 dB |
| Peaking | 5951 Hz | 0.18 | 0.3 dB  |
| Peaking | 7886 Hz | 5.14 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Logitech%20UE%206000%20passive/Logitech%20UE%206000%20passive.png)