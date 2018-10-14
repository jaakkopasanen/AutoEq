# Philips Fidelio L1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 21 -5.9; 23 -6.3; 25 -6.6; 28 -6.9; 31 -7.2; 34 -7.4; 37 -7.6; 41 -7.8; 45 -7.9; 49 -7.9; 54 -8.0; 60 -8.1; 66 -8.1; 72 -8.1; 79 -8.1; 87 -8.1; 96 -8.0; 106 -7.9; 116 -7.7; 128 -8.0; 141 -8.0; 155 -7.9; 170 -7.1; 187 -6.6; 206 -6.6; 227 -6.5; 249 -6.5; 274 -6.2; 302 -5.7; 332 -5.2; 365 -4.6; 402 -3.9; 442 -3.3; 486 -2.9; 535 -2.1; 588 -1.3; 647 -0.6; 712 -0.2; 783 0.3; 861 0.2; 947 0.1; 1042 0.0; 1146 -0.3; 1261 -1.0; 1387 -3.1; 1526 -5.2; 1678 -6.9; 1846 -7.6; 2031 -7.4; 2234 -8.1; 2457 -8.1; 2703 -7.3; 2973 -5.7; 3270 -3.1; 3597 -1.5; 3957 -0.3; 4353 1.1; 4788 3.0; 5267 5.0; 5793 5.0; 6373 3.3; 7010 -2.3; 7711 -4.0; 8482 -3.9; 9330 -0.5; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.6; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.2dB` and instead set Global volume in the UI for both channels to **-51**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio L1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 44 Hz   | 0.36 | -7.6 dB |
| Peaking | 147 Hz  | 0.94 | -3.8 dB |
| Peaking | 298 Hz  | 1.56 | -3.6 dB |
| Peaking | 2237 Hz | 1.53 | -9.0 dB |
| Peaking | 5318 Hz | 3.8  | 6.8 dB  |
| Peaking | 1023 Hz | 1.62 | 2.0 dB  |
| Peaking | 1628 Hz | 4.88 | -2.8 dB |
| Peaking | 6285 Hz | 7.21 | 3.3 dB  |
| Peaking | 7815 Hz | 2.53 | -7.1 dB |
| Peaking | 8081 Hz | 1.03 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20L1/Philips%20Fidelio%20L1.png)