# Creative Aurvana Gold
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.5; 23 -6.3; 25 -6.8; 28 -7.1; 31 -6.9; 34 -6.7; 37 -6.5; 41 -6.2; 45 -5.9; 49 -5.7; 54 -5.5; 60 -5.4; 66 -5.4; 72 -5.4; 79 -5.5; 87 -5.6; 96 -5.7; 106 -5.9; 116 -6.1; 128 -6.2; 141 -6.3; 155 -6.3; 170 -6.3; 187 -6.2; 206 -6.0; 227 -5.9; 249 -5.9; 274 -5.9; 302 -6.0; 332 -6.1; 365 -6.3; 402 -6.4; 442 -6.6; 486 -6.4; 535 -4.9; 588 -2.7; 647 -0.5; 712 0.7; 783 0.7; 861 0.5; 947 0.7; 1042 -0.5; 1146 -0.6; 1261 0.2; 1387 0.8; 1526 1.8; 1678 2.6; 1846 3.3; 2031 4.0; 2234 5.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 3.6; 5267 -0.2; 5793 -1.4; 6373 1.2; 7010 2.3; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana Gold GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 0.13 | -6.3 dB |
| Peaking | 405 Hz  | 1.77 | -4.2 dB |
| Peaking | 2829 Hz | 0.93 | 6.1 dB  |
| Peaking | 4394 Hz | 3.36 | 3.1 dB  |
| Peaking | 5580 Hz | 5.82 | -4.7 dB |
| Peaking | 68 Hz   | 0.82 | 3.1 dB  |
| Peaking | 72 Hz   | 0.38 | -2.1 dB |
| Peaking | 705 Hz  | 5.25 | 2.7 dB  |
| Peaking | 926 Hz  | 3.89 | 2.0 dB  |
| Peaking | 1093 Hz | 2.79 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Creative%20Aurvana%20Gold/Creative%20Aurvana%20Gold.png)