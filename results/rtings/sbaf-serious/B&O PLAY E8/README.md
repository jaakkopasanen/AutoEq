# B&O PLAY E8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 0.0; 23 2.8; 25 2.5; 28 2.0; 31 1.6; 34 1.2; 37 1.1; 41 1.0; 45 1.1; 49 1.3; 54 1.5; 60 1.7; 66 1.9; 72 2.3; 79 2.6; 87 2.8; 96 2.8; 106 2.4; 116 2.0; 128 1.4; 141 0.7; 155 0.1; 170 -0.7; 187 -1.5; 206 -2.3; 227 -2.9; 249 -3.2; 274 -3.3; 302 -3.2; 332 -3.0; 365 -2.7; 402 -2.3; 442 -1.8; 486 -1.2; 535 -0.6; 588 0.0; 647 0.8; 712 1.5; 783 1.7; 861 1.4; 947 0.5; 1042 -0.4; 1146 -1.1; 1261 -1.5; 1387 -1.9; 1526 -2.3; 1678 -2.2; 1846 -1.1; 2031 1.3; 2234 3.8; 2457 4.5; 2703 4.5; 2973 4.4; 3270 4.9; 3597 5.7; 3957 5.2; 4353 3.4; 4788 3.0; 5267 3.1; 5793 1.8; 6373 -3.1; 7010 -7.0; 7711 -5.4; 8482 -4.0; 9330 -6.5; 10263 -7.7; 11289 -1.6; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`B&O PLAY E8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `B&O PLAY E8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 294 Hz  | 1.85 | -3.8 dB |
| Peaking | 3312 Hz | 1.74 | 5.6 dB  |
| Peaking | 5666 Hz | 2.25 | 4.8 dB  |
| Peaking | 6960 Hz | 2.91 | -9.5 dB |
| Peaking | 9935 Hz | 4.67 | -8.0 dB |
| Peaking | 17 Hz   | 0.81 | 3.5 dB  |
| Peaking | 90 Hz   | 1.72 | 3.0 dB  |
| Peaking | 790 Hz  | 3.02 | 2.6 dB  |
| Peaking | 1688 Hz | 1.32 | -3.8 dB |
| Peaking | 2283 Hz | 3.31 | 4.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/B&O%20PLAY%20E8/B&O%20PLAY%20E8.png)