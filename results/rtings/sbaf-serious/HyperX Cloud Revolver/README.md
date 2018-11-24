# HyperX Cloud Revolver

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.6; 23 -0.9; 25 -1.2; 28 -1.4; 31 -1.6; 34 -1.8; 37 -1.9; 41 -2.1; 45 -2.4; 49 -2.7; 54 -3.0; 60 -3.3; 66 -3.6; 72 -3.6; 79 -3.6; 87 -3.6; 96 -3.6; 106 -3.6; 116 -3.6; 128 -3.6; 141 -3.3; 155 -3.1; 170 -2.8; 187 -2.4; 206 -2.0; 227 -1.5; 249 -0.9; 274 -0.5; 302 -0.1; 332 0.7; 365 1.2; 402 1.2; 442 1.1; 486 1.5; 535 1.9; 588 2.0; 647 2.0; 712 1.8; 783 1.8; 861 1.1; 947 0.4; 1042 -0.2; 1146 -0.5; 1261 -0.9; 1387 -1.9; 1526 -3.3; 1678 -5.1; 1846 -5.3; 2031 -4.7; 2234 -3.2; 2457 -1.7; 2703 -0.7; 2973 0.5; 3270 3.3; 3597 6.0; 3957 6.0; 4353 4.7; 4788 4.2; 5267 5.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.2; 9330 -2.6; 10263 -0.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Revolver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Revolver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 111 Hz  |  0.38 | -4.2 dB |
| Peaking | 507 Hz  |  0.53 | 3.2 dB  |
| Peaking | 1848 Hz |  1.57 | -6.4 dB |
| Peaking | 3788 Hz |  2.66 | 6.8 dB  |
| Peaking | 5876 Hz |  3.68 | 5.9 dB  |
| Peaking | 452 Hz  |  9.33 | -0.5 dB |
| Peaking | 3018 Hz | 11.76 | -0.6 dB |
| Peaking | 6578 Hz |  9.68 | 1.3 dB  |
| Peaking | 9244 Hz |  5.58 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/HyperX%20Cloud%20Revolver/HyperX%20Cloud%20Revolver.png)