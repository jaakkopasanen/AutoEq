# Reid and Heath Acoustics SA-850

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.5; 28 4.4; 31 3.4; 34 2.6; 37 2.0; 41 1.4; 45 1.1; 49 0.9; 54 0.9; 60 0.8; 66 0.8; 72 0.7; 79 0.6; 87 0.5; 96 0.5; 106 0.7; 116 0.5; 128 0.0; 141 -0.4; 155 -0.7; 170 -0.8; 187 -1.1; 206 -1.6; 227 -2.6; 249 -3.0; 274 -3.3; 302 -3.2; 332 -2.8; 365 -3.0; 402 -3.5; 442 -3.8; 486 -4.4; 535 -4.8; 588 -4.5; 647 -4.3; 712 -3.5; 783 -2.0; 861 -0.7; 947 0.3; 1042 -0.4; 1146 -1.9; 1261 -2.6; 1387 -3.5; 1526 -4.6; 1678 -3.7; 1846 -2.1; 2031 -0.2; 2234 1.4; 2457 3.8; 2703 5.6; 2973 6.0; 3270 6.0; 3597 5.8; 3957 6.0; 4353 6.0; 4788 0.6; 5267 -2.8; 5793 -2.0; 6373 -2.0; 7010 -2.7; 7711 -1.1; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Reid and Heath Acoustics SA-850 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.96 | 6.3 dB  |
| Peaking | 274 Hz  | 1.69 | -2.8 dB |
| Peaking | 548 Hz  | 1.82 | -4.7 dB |
| Peaking | 1562 Hz | 2.93 | -5.4 dB |
| Peaking | 3177 Hz | 1.97 | 7.4 dB  |
| Peaking | 866 Hz  | 1.93 | -1.2 dB |
| Peaking | 928 Hz  | 4.44 | 2.9 dB  |
| Peaking | 4384 Hz | 3.6  | 8.9 dB  |
| Peaking | 5069 Hz | 1.93 | -7.3 dB |
| Peaking | 9040 Hz | 4.98 | 0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Reid%20and%20Heath%20Acoustics%20SA-850/Reid%20and%20Heath%20Acoustics%20SA-850.png)