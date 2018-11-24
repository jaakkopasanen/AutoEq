# Dunu Titan 3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 21 -1.4; 23 -1.4; 25 -1.4; 28 -1.5; 31 -1.6; 34 -1.6; 37 -1.7; 41 -1.8; 45 -2.0; 49 -2.1; 54 -2.1; 60 -2.3; 66 -2.6; 72 -2.9; 79 -3.1; 87 -3.3; 96 -3.7; 106 -3.6; 116 -3.7; 128 -3.9; 141 -3.8; 155 -3.7; 170 -3.6; 187 -3.4; 206 -3.2; 227 -2.8; 249 -2.6; 274 -2.1; 302 -1.9; 332 -1.5; 365 -1.2; 402 -0.7; 442 0.3; 486 0.1; 535 0.3; 588 0.8; 647 1.0; 712 1.0; 783 1.0; 861 0.7; 947 0.3; 1042 -0.2; 1146 -0.6; 1261 -1.2; 1387 -2.0; 1526 -2.9; 1678 -3.7; 1846 -4.2; 2031 -4.6; 2234 -5.1; 2457 -4.7; 2703 -3.7; 2973 -1.3; 3270 1.2; 3597 2.3; 3957 1.1; 4353 -2.6; 4788 -7.0; 5267 -8.3; 5793 -1.5; 6373 3.1; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu Titan 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu Titan 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 70 Hz   | 0.52 | -2.3 dB  |
| Peaking | 163 Hz  | 1.04 | -2.8 dB  |
| Peaking | 2075 Hz | 2.27 | -5.4 dB  |
| Peaking | 5121 Hz | 6.07 | -10.4 dB |
| Peaking | 6539 Hz | 4.7  | 4.9 dB   |
| Peaking | 19 Hz   | 1.46 | -0.7 dB  |
| Peaking | 716 Hz  | 1.72 | 1.6 dB   |
| Peaking | 1478 Hz | 4.97 | -1.1 dB  |
| Peaking | 3457 Hz | 1.44 | -3.1 dB  |
| Peaking | 3575 Hz | 3.48 | 7.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20Titan%203/Dunu%20Titan%203.png)