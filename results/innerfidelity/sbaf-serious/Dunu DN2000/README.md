# Dunu DN2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.4; 23 -4.3; 25 -4.2; 28 -4.1; 31 -3.9; 34 -3.7; 37 -3.6; 41 -3.4; 45 -3.2; 49 -3.1; 54 -3.0; 60 -2.9; 66 -2.8; 72 -2.8; 79 -2.9; 87 -3.0; 96 -3.2; 106 -3.2; 116 -3.1; 128 -3.2; 141 -3.3; 155 -3.3; 170 -3.3; 187 -3.3; 206 -3.3; 227 -3.1; 249 -3.0; 274 -2.8; 302 -2.7; 332 -2.5; 365 -2.4; 402 -2.2; 442 -1.9; 486 -1.7; 535 -1.4; 588 -0.9; 647 -0.7; 712 -0.6; 783 -0.1; 861 -0.1; 947 -0.1; 1042 0.0; 1146 0.1; 1261 0.2; 1387 0.1; 1526 0.2; 1678 0.4; 1846 1.3; 2031 2.3; 2234 3.1; 2457 3.9; 2703 4.0; 2973 5.3; 3270 6.0; 3597 6.0; 3957 4.3; 4353 -0.1; 4788 -2.5; 5267 0.5; 5793 3.6; 6373 4.1; 7010 2.5; 7711 -1.1; 8482 -5.4; 9330 -6.2; 10263 -2.6; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DN2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.31 | -4.4 dB |
| Peaking | 191 Hz  | 0.49 | -3.1 dB |
| Peaking | 3090 Hz | 2.02 | 6.3 dB  |
| Peaking | 6473 Hz | 5.09 | 5.1 dB  |
| Peaking | 8963 Hz | 3.83 | -7.5 dB |
| Peaking | 1617 Hz | 4.72 | -0.3 dB |
| Peaking | 2141 Hz | 5.09 | 1.3 dB  |
| Peaking | 3794 Hz | 6.59 | 3.3 dB  |
| Peaking | 4726 Hz | 3.78 | -4.9 dB |
| Peaking | 5625 Hz | 5.65 | 2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20DN2000/Dunu%20DN2000.png)