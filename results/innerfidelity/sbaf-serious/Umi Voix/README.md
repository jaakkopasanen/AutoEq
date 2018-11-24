# Umi Voix

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.6; 23 -3.7; 25 -3.7; 28 -3.8; 31 -3.9; 34 -3.9; 37 -4.0; 41 -4.0; 45 -4.1; 49 -4.2; 54 -4.3; 60 -4.3; 66 -4.5; 72 -4.7; 79 -4.9; 87 -5.1; 96 -5.2; 106 -5.3; 116 -5.2; 128 -5.2; 141 -5.1; 155 -5.0; 170 -4.8; 187 -4.4; 206 -4.1; 227 -3.5; 249 -3.0; 274 -2.3; 302 -1.5; 332 -0.8; 365 0.1; 402 0.9; 442 2.0; 486 2.5; 535 2.7; 588 3.3; 647 3.1; 712 2.7; 783 2.3; 861 1.5; 947 0.6; 1042 -0.4; 1146 -1.1; 1261 -1.8; 1387 -2.5; 1526 -2.7; 1678 -2.2; 1846 -0.7; 2031 1.3; 2234 3.5; 2457 5.8; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.3; 4353 2.7; 4788 5.5; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Umi Voix GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Umi Voix ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.51 | -3.9 dB |
| Peaking | 108 Hz  | 1.26 | -3.8 dB |
| Peaking | 189 Hz  | 2.15 | -3.1 dB |
| Peaking | 3044 Hz | 2.14 | 6.6 dB  |
| Peaking | 5598 Hz | 2.66 | 6.0 dB  |
| Peaking | 280 Hz  | 2.07 | -1.6 dB |
| Peaking | 603 Hz  | 1.09 | 3.9 dB  |
| Peaking | 1481 Hz | 1.57 | -4.2 dB |
| Peaking | 2380 Hz | 4.48 | 3.1 dB  |
| Peaking | 8333 Hz | 4.74 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Umi%20Voix/Umi%20Voix.png)