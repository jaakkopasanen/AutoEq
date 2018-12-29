# VSonic VS05
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.5dB
GraphicEQ: 21 0.0; 23 2.5; 25 2.1; 28 1.6; 31 1.2; 34 0.9; 37 0.5; 41 0.2; 45 -0.2; 49 -0.5; 54 -0.8; 60 -1.2; 66 -1.7; 72 -2.0; 79 -2.4; 87 -2.8; 96 -3.4; 106 -3.6; 116 -3.8; 128 -4.2; 141 -4.4; 155 -4.5; 170 -4.6; 187 -4.6; 206 -4.7; 227 -4.5; 249 -4.4; 274 -4.2; 302 -4.0; 332 -3.7; 365 -3.4; 402 -3.0; 442 -2.6; 486 -2.3; 535 -1.9; 588 -1.2; 647 -0.8; 712 -0.5; 783 -0.0; 861 0.1; 947 0.1; 1042 0.1; 1146 0.1; 1261 0.1; 1387 -0.1; 1526 0.1; 1678 0.4; 1846 0.9; 2031 1.3; 2234 1.8; 2457 2.5; 2703 2.9; 2973 3.6; 3270 4.2; 3597 4.2; 3957 3.2; 4353 0.9; 4788 -0.6; 5267 -1.6; 5793 -3.5; 6373 -4.2; 7010 -3.0; 7711 -3.3; 8482 -5.1; 9330 -5.0; 10263 -1.4; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic VS05 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VS05 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.82 | 3.7 dB  |
| Peaking | 179 Hz   | 0.5  | -4.9 dB |
| Peaking | 3395 Hz  | 1.35 | 5.0 dB  |
| Peaking | 6010 Hz  | 1.95 | -4.9 dB |
| Peaking | 8836 Hz  | 4.4  | -5.3 dB |
| Peaking | 408 Hz   | 1.96 | -0.5 dB |
| Peaking | 810 Hz   | 1.84 | 0.8 dB  |
| Peaking | 1476 Hz  | 3.71 | -0.4 dB |
| Peaking | 11152 Hz | 6.65 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VS05/VSonic%20VS05.png)