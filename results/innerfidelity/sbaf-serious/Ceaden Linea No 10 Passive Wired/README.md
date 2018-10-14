# Ceaden Linea No 10 Passive Wired

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.3; 23 -1.8; 25 -2.1; 28 -2.5; 31 -2.8; 34 -3.0; 37 -3.2; 41 -3.3; 45 -3.4; 49 -3.5; 54 -3.8; 60 -4.1; 66 -4.3; 72 -4.4; 79 -4.5; 87 -4.7; 96 -4.8; 106 -4.8; 116 -4.7; 128 -4.7; 141 -4.7; 155 -4.4; 170 -3.8; 187 -3.4; 206 -2.7; 227 -1.7; 249 -1.4; 274 -1.4; 302 -1.1; 332 -0.7; 365 -0.2; 402 0.1; 442 0.6; 486 0.8; 535 1.1; 588 1.4; 647 1.2; 712 0.9; 783 0.8; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.4; 1387 -0.7; 1526 -0.9; 1678 -0.7; 1846 0.2; 2031 1.4; 2234 2.9; 2457 4.7; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 4.5; 4788 3.0; 5267 5.2; 5793 6.0; 6373 4.7; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ceaden Linea No 10 Passive Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 66 Hz   | 0.46 | -3.9 dB |
| Peaking | 141 Hz  | 1.24 | -2.3 dB |
| Peaking | 557 Hz  | 2.24 | 1.7 dB  |
| Peaking | 3249 Hz | 1.73 | 6.7 dB  |
| Peaking | 5836 Hz | 3.81 | 5.3 dB  |
| Peaking | 1714 Hz | 1.19 | -5.2 dB |
| Peaking | 2657 Hz | 0.63 | 5.2 dB  |
| Peaking | 3229 Hz | 3.77 | -3.7 dB |
| Peaking | 6157 Hz | 0.96 | -2.8 dB |
| Peaking | 6590 Hz | 5.07 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ceaden%20Linea%20No%2010%20Passive%20Wired/Ceaden%20Linea%20No%2010%20Passive%20Wired.png)