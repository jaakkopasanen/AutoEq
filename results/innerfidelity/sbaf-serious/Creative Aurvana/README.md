# Creative Aurvana
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.7; 25 2.2; 28 1.6; 31 1.2; 34 0.8; 37 0.6; 41 0.3; 45 0.1; 49 -0.2; 54 -0.5; 60 -0.8; 66 -0.8; 72 -1.0; 79 -1.4; 87 -1.9; 96 -2.1; 106 -2.3; 116 -2.3; 128 -2.4; 141 -2.4; 155 -2.2; 170 -2.0; 187 -1.7; 206 -1.5; 227 -1.2; 249 -1.0; 274 -0.7; 302 -0.4; 332 0.0; 365 0.4; 402 0.7; 442 1.1; 486 1.1; 535 1.2; 588 1.4; 647 1.1; 712 0.4; 783 0.0; 861 0.3; 947 0.3; 1042 0.2; 1146 0.5; 1261 0.7; 1387 0.6; 1526 0.5; 1678 0.5; 1846 1.0; 2031 1.6; 2234 2.0; 2457 2.5; 2703 1.4; 2973 0.4; 3270 4.0; 3597 5.2; 3957 2.1; 4353 0.0; 4788 1.2; 5267 4.4; 5793 5.8; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.7; 10263 -0.1; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.1; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 18 Hz   |  1.05 | 4.0 dB  |
| Peaking | 132 Hz  |  0.73 | -3.2 dB |
| Peaking | 581 Hz  |  0.22 | 1.0 dB  |
| Peaking | 3470 Hz |  7.12 | 5.4 dB  |
| Peaking | 5980 Hz |  4.06 | 6.3 dB  |
| Peaking | 557 Hz  |  1.49 | 2.8 dB  |
| Peaking | 641 Hz  |  0.95 | -2.2 dB |
| Peaking | 2339 Hz |  4.91 | 1.8 dB  |
| Peaking | 4437 Hz | 12.58 | -1.7 dB |
| Peaking | 9254 Hz |  4.13 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Creative%20Aurvana/Creative%20Aurvana.png)