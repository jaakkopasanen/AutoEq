# Creative HN-900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.8; 41 4.9; 45 3.4; 49 1.8; 54 0.1; 60 -0.7; 66 0.1; 72 -1.7; 79 -4.6; 87 -6.7; 96 -7.8; 106 -8.5; 116 -8.9; 128 -9.0; 141 -8.8; 155 -8.7; 170 -8.5; 187 -7.9; 206 -7.4; 227 -6.8; 249 -6.3; 274 -5.8; 302 -5.3; 332 -4.9; 365 -4.5; 402 -4.4; 442 -4.5; 486 -4.9; 535 -5.6; 588 -6.5; 647 -7.3; 712 -7.0; 783 -5.5; 861 -3.0; 947 -0.7; 1042 -0.4; 1146 -1.9; 1261 0.0; 1387 2.0; 1526 2.9; 1678 4.0; 1846 5.9; 2031 5.0; 2234 3.5; 2457 1.8; 2703 4.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.4; 5267 1.6; 5793 2.8; 6373 0.3; 7010 0.7; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.6; 13660 -4.4; 15026 -4.6; 16529 -2.0; 18182 -0.1; 20000 -1.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative HN-900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative HN-900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 38 Hz    |  0.38 | 10.5 dB  |
| Peaking | 113 Hz   |  0.5  | -14.0 dB |
| Peaking | 665 Hz   |  2.3  | -6.2 dB  |
| Peaking | 1813 Hz  |  2.61 | 5.3 dB   |
| Peaking | 3717 Hz  |  1.67 | 6.7 dB   |
| Peaking | 2566 Hz  |  7    | -1.9 dB  |
| Peaking | 2899 Hz  |  8.24 | 2.2 dB   |
| Peaking | 4644 Hz  | 12.94 | 2.1 dB   |
| Peaking | 12169 Hz |  3.43 | 2.5 dB   |
| Peaking | 14226 Hz |  1.89 | -5.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Creative%20HN-900/Creative%20HN-900.png)