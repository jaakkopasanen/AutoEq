# Google Pixel Buds
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.5; 49 4.2; 54 2.5; 60 0.9; 66 -0.4; 72 -1.4; 79 -2.4; 87 -3.4; 96 -4.3; 106 -5.1; 116 -5.8; 128 -6.3; 141 -6.6; 155 -6.8; 170 -6.8; 187 -6.7; 206 -6.5; 227 -6.2; 249 -5.8; 274 -5.3; 302 -4.7; 332 -4.0; 365 -3.4; 402 -3.1; 442 -3.0; 486 -2.9; 535 -2.8; 588 -2.7; 647 -2.4; 712 -2.0; 783 -1.6; 861 -1.0; 947 -0.4; 1042 0.3; 1146 1.2; 1261 2.2; 1387 3.0; 1526 3.7; 1678 4.2; 1846 4.3; 2031 4.1; 2234 3.6; 2457 2.0; 2703 0.1; 2973 -1.9; 3270 -3.1; 3597 -3.6; 3957 -3.5; 4353 -3.3; 4788 -3.0; 5267 -3.4; 5793 -2.5; 6373 -1.1; 7010 0.1; 7711 -1.6; 8482 -2.8; 9330 -0.6; 10263 0.0; 11289 -0.3; 12418 -3.9; 13660 -5.3; 15026 -5.1; 16529 -4.6; 18182 -4.3; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Google Pixel Buds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Google Pixel Buds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.51 | 11.6 dB  |
| Peaking | 111 Hz   | 0.35 | -10.1 dB |
| Peaking | 1913 Hz  | 1.28 | 6.2 dB   |
| Peaking | 3646 Hz  | 1.3  | -5.1 dB  |
| Peaking | 17627 Hz | 0.61 | -5.4 dB  |
| Peaking | 8382 Hz  | 6.01 | -3.3 dB  |
| Peaking | 9373 Hz  | 1.85 | 2.4 dB   |
| Peaking | 11082 Hz | 4.26 | 2.4 dB   |
| Peaking | 13096 Hz | 2    | -2.9 dB  |
| Peaking | 17556 Hz | 3.39 | 1.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Google%20Pixel%20Buds/Google%20Pixel%20Buds.png)