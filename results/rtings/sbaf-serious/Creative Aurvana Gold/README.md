# Creative Aurvana Gold

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.1; 23 -6.0; 25 -6.5; 28 -6.9; 31 -6.9; 34 -6.7; 37 -6.6; 41 -6.4; 45 -6.2; 49 -6.1; 54 -5.9; 60 -5.7; 66 -5.6; 72 -5.4; 79 -5.3; 87 -5.2; 96 -5.3; 106 -5.4; 116 -5.6; 128 -5.7; 141 -5.7; 155 -5.7; 170 -5.7; 187 -5.6; 206 -5.5; 227 -5.4; 249 -5.3; 274 -5.2; 302 -5.2; 332 -5.2; 365 -5.2; 402 -5.4; 442 -5.5; 486 -5.2; 535 -3.7; 588 -1.6; 647 0.6; 712 1.6; 783 1.2; 861 0.7; 947 0.8; 1042 -0.5; 1146 -0.4; 1261 0.4; 1387 0.7; 1526 1.4; 1678 2.2; 1846 3.3; 2031 4.4; 2234 5.5; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.2; 5267 2.8; 5793 2.5; 6373 4.8; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana Gold GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.25 | -6.2 dB |
| Peaking | 216 Hz  | 0.89 | -4.0 dB |
| Peaking | 432 Hz  | 2.84 | -4.2 dB |
| Peaking | 2431 Hz | 1.54 | 4.5 dB  |
| Peaking | 4122 Hz | 1.28 | 5.0 dB  |
| Peaking | 535 Hz  | 4.48 | -2.0 dB |
| Peaking | 702 Hz  | 2.44 | 2.8 dB  |
| Peaking | 1126 Hz | 4.17 | -1.4 dB |
| Peaking | 6546 Hz | 6.17 | 5.0 dB  |
| Peaking | 6976 Hz | 1.7  | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Creative%20Aurvana%20Gold/Creative%20Aurvana%20Gold.png)