# Philips Fidelio S2 Early 2013

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 21 -0.3; 23 -0.4; 25 -0.4; 28 -0.6; 31 -0.7; 34 -0.7; 37 -0.8; 41 -0.9; 45 -1.0; 49 -1.1; 54 -1.2; 60 -1.4; 66 -1.6; 72 -1.8; 79 -2.0; 87 -2.2; 96 -2.5; 106 -2.5; 116 -2.5; 128 -2.6; 141 -2.6; 155 -2.5; 170 -2.4; 187 -2.2; 206 -2.0; 227 -1.7; 249 -1.5; 274 -1.2; 302 -0.9; 332 -0.7; 365 -0.3; 402 -0.1; 442 0.3; 486 0.4; 535 0.6; 588 1.1; 647 1.1; 712 1.1; 783 1.2; 861 0.8; 947 0.4; 1042 -0.2; 1146 -0.7; 1261 -1.2; 1387 -2.1; 1526 -2.8; 1678 -3.4; 1846 -3.5; 2031 -3.3; 2234 -2.9; 2457 -1.9; 2703 -0.6; 2973 0.9; 3270 2.3; 3597 2.4; 3957 0.9; 4353 -2.2; 4788 -3.9; 5267 -2.2; 5793 0.8; 6373 3.3; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.0dB` and instead set Global volume in the UI for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio S2 Early 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 119 Hz  | 0.75 | -2.8 dB |
| Peaking | 1908 Hz | 1.99 | -4.1 dB |
| Peaking | 3528 Hz | 2.93 | 4.1 dB  |
| Peaking | 4753 Hz | 3.5  | -5.1 dB |
| Peaking | 6492 Hz | 4.93 | 4.6 dB  |
| Peaking | 34 Hz   | 1.46 | -0.4 dB |
| Peaking | 240 Hz  | 1.94 | -0.6 dB |
| Peaking | 715 Hz  | 1.17 | 1.7 dB  |
| Peaking | 1142 Hz | 2.69 | -0.5 dB |
| Peaking | 1464 Hz | 4.52 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20S2%20Early%202013/Philips%20Fidelio%20S2%20Early%202013.png)