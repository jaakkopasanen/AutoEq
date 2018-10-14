# Klipsch XR8i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -7.2; 23 -7.3; 25 -7.3; 28 -7.4; 31 -7.3; 34 -7.3; 37 -7.3; 41 -7.2; 45 -7.2; 49 -7.1; 54 -7.1; 60 -7.0; 66 -7.0; 72 -6.9; 79 -6.9; 87 -6.9; 96 -6.9; 106 -6.7; 116 -6.4; 128 -6.3; 141 -6.0; 155 -5.8; 170 -5.5; 187 -5.1; 206 -4.7; 227 -4.2; 249 -4.0; 274 -3.6; 302 -3.2; 332 -2.7; 365 -2.3; 402 -1.9; 442 -1.4; 486 -1.2; 535 -0.8; 588 -0.2; 647 0.1; 712 0.2; 783 0.5; 861 0.4; 947 0.2; 1042 -0.0; 1146 -0.2; 1261 -0.5; 1387 -1.0; 1526 -1.4; 1678 -1.5; 1846 -1.4; 2031 -1.2; 2234 -1.1; 2457 -0.6; 2703 -0.0; 2973 1.7; 3270 4.1; 3597 5.4; 3957 5.1; 4353 3.5; 4788 4.2; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch XR8i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.13 | -7.3 dB |
| Peaking | 802 Hz  | 0.77 | 2.6 dB  |
| Peaking | 2777 Hz | 0.35 | -3.1 dB |
| Peaking | 3579 Hz | 2.39 | 7.2 dB  |
| Peaking | 5730 Hz | 2.23 | 7.8 dB  |
| Peaking | 6621 Hz | 7.58 | 2.1 dB  |
| Peaking | 7260 Hz | 2.11 | -1.7 dB |
| Peaking | 8985 Hz | 0.7  | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20XR8i/Klipsch%20XR8i.png)