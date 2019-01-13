# Soul by Ludacris SL300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 4.8; 37 2.0; 41 -2.2; 45 -4.6; 49 -5.2; 54 -4.9; 60 -4.3; 66 -3.4; 72 -2.6; 79 -2.1; 87 -1.8; 96 -1.8; 106 -1.6; 116 -1.5; 128 -1.6; 141 -1.7; 155 -1.7; 170 -1.7; 187 -1.6; 206 -1.5; 227 -1.3; 249 -1.3; 274 -1.0; 302 -0.9; 332 -1.0; 365 -1.2; 402 -1.6; 442 -2.0; 486 -3.1; 535 -3.9; 588 -2.4; 647 0.9; 712 5.8; 783 6.0; 861 5.4; 947 1.2; 1042 -0.2; 1146 -2.2; 1261 -2.6; 1387 -1.9; 1526 -1.7; 1678 -1.0; 1846 -0.4; 2031 -0.3; 2234 -0.4; 2457 1.5; 2703 3.8; 2973 6.0; 3270 6.0; 3597 3.4; 3957 4.0; 4353 -3.2; 4788 -4.5; 5267 -1.6; 5793 1.3; 6373 4.8; 7010 2.5; 7711 0.3; 8482 -1.2; 9330 -2.1; 10263 -0.8; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Soul by Ludacris SL300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soul by Ludacris SL300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 32 Hz   | 0.81 | 15.5 dB  |
| Peaking | 46 Hz   | 0.95 | -15.4 dB |
| Peaking | 769 Hz  | 0.69 | -6.6 dB  |
| Peaking | 782 Hz  | 2.59 | 13.8 dB  |
| Peaking | 3097 Hz | 3.33 | 7.6 dB   |
| Peaking | 548 Hz  | 8.38 | -2.2 dB  |
| Peaking | 3849 Hz | 9.06 | 5.6 dB   |
| Peaking | 4576 Hz | 4.07 | -6.4 dB  |
| Peaking | 6454 Hz | 5.16 | 5.7 dB   |
| Peaking | 9162 Hz | 4.43 | -2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Soul%20by%20Ludacris%20SL300/Soul%20by%20Ludacris%20SL300.png)