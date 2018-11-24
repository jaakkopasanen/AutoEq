# B&O PLAY H6

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.1; 23 -2.3; 25 -2.4; 28 -2.6; 31 -2.7; 34 -2.8; 37 -2.7; 41 -2.6; 45 -2.3; 49 -2.0; 54 -1.6; 60 -1.3; 66 -1.3; 72 -1.3; 79 -1.4; 87 -1.6; 96 -1.6; 106 -1.6; 116 -1.5; 128 -1.2; 141 -0.6; 155 0.3; 170 1.6; 187 3.1; 206 4.6; 227 5.5; 249 5.9; 274 5.4; 302 4.3; 332 3.2; 365 2.1; 402 1.4; 442 1.0; 486 0.6; 535 0.4; 588 0.3; 647 0.1; 712 -0.0; 783 -0.0; 861 0.0; 947 0.0; 1042 0.0; 1146 0.1; 1261 0.2; 1387 0.1; 1526 -0.1; 1678 -0.7; 1846 -1.5; 2031 -2.0; 2234 -1.5; 2457 -0.1; 2703 1.5; 2973 3.3; 3270 4.3; 3597 4.6; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.4; 7010 2.0; 7711 -1.1; 8482 -4.1; 9330 -4.7; 10263 -0.7; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`B&O PLAY H6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `B&O PLAY H6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 39 Hz    |  0.09 | -2.4 dB |
| Peaking | 247 Hz   |  1.47 | 8.0 dB  |
| Peaking | 2105 Hz  |  2.27 | -4.3 dB |
| Peaking | 5089 Hz  |  0.72 | 7.5 dB  |
| Peaking | 8699 Hz  |  2.47 | -9.0 dB |
| Peaking | 37 Hz    |  1.81 | -0.7 dB |
| Peaking | 63 Hz    |  1.8  | 1.0 dB  |
| Peaking | 121 Hz   |  3.13 | -0.7 dB |
| Peaking | 6282 Hz  | 12.29 | 1.2 dB  |
| Peaking | 14931 Hz |  1.79 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/B&O%20PLAY%20H6/B&O%20PLAY%20H6.png)