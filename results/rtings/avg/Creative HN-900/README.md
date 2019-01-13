# Creative HN-900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.8; 41 4.9; 45 3.4; 49 1.8; 54 0.1; 60 -0.7; 66 0.1; 72 -1.7; 79 -4.6; 87 -6.7; 96 -7.8; 106 -8.5; 116 -8.9; 128 -9.0; 141 -8.8; 155 -8.7; 170 -8.5; 187 -7.9; 206 -7.4; 227 -6.8; 249 -6.3; 274 -5.8; 302 -5.3; 332 -4.9; 365 -4.5; 402 -4.4; 442 -4.5; 486 -4.9; 535 -5.6; 588 -6.5; 647 -7.3; 712 -7.0; 783 -5.5; 861 -3.0; 947 -0.7; 1042 -0.4; 1146 -1.9; 1261 0.0; 1387 2.0; 1526 2.9; 1678 4.0; 1846 5.9; 2031 5.0; 2234 3.6; 2457 1.8; 2703 3.8; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 4.2; 5267 -1.0; 5793 0.3; 6373 -0.9; 7010 -0.0; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -3.4; 13660 -7.7; 15026 -7.3; 16529 -5.0; 18182 -4.4; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative HN-900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative HN-900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 38 Hz    | 0.38 | 10.3 dB  |
| Peaking | 113 Hz   | 0.51 | -13.7 dB |
| Peaking | 674 Hz   | 1.99 | -6.7 dB  |
| Peaking | 2836 Hz  | 0.66 | 5.7 dB   |
| Peaking | 15953 Hz | 0.82 | -6.9 dB  |
| Peaking | 1845 Hz  | 6.33 | 2.6 dB   |
| Peaking | 2486 Hz  | 6.6  | -4.0 dB  |
| Peaking | 4643 Hz  | 2.51 | 6.8 dB   |
| Peaking | 5173 Hz  | 2.82 | -7.7 dB  |
| Peaking | 10967 Hz | 4.83 | 2.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Creative%20HN-900/Creative%20HN-900.png)