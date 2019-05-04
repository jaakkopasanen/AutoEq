# Samsung Level U Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.2; 25 -7.1; 28 -7.1; 31 -7.0; 34 -6.9; 37 -6.9; 41 -6.7; 45 -6.6; 49 -6.5; 54 -6.5; 60 -6.7; 66 -6.8; 72 -6.9; 79 -7.0; 87 -7.3; 96 -7.6; 106 -8.0; 116 -8.3; 128 -8.6; 141 -8.8; 155 -8.8; 170 -8.7; 187 -8.5; 206 -8.3; 227 -8.0; 249 -7.6; 274 -7.1; 302 -6.5; 332 -5.8; 365 -5.2; 402 -4.5; 442 -3.8; 486 -3.2; 535 -2.4; 588 -1.7; 647 -1.1; 712 -0.6; 783 -0.5; 861 -0.5; 947 -1.0; 1042 -1.6; 1146 -2.0; 1261 -2.4; 1387 -2.5; 1526 -2.5; 1678 -2.5; 1846 -2.6; 2031 -2.5; 2234 -2.0; 2457 -1.2; 2703 -0.7; 2973 -1.1; 3270 -2.3; 3597 -3.7; 3957 -4.8; 4353 -5.8; 4788 -6.8; 5267 -6.4; 5793 -4.0; 6373 -1.6; 7010 -1.5; 7711 -3.7; 8482 -4.0; 9330 -4.6; 10263 -4.0; 11289 -4.0; 12418 -4.8; 13660 -5.9; 15026 -5.6; 16529 -8.6; 18182 -13.3; 20000 -12.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Level U Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Level U Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.6  | -2.9 dB  |
| Peaking | 169 Hz   | 0.57 | -4.9 dB  |
| Peaking | 746 Hz   | 0.95 | 4.2 dB   |
| Peaking | 2677 Hz  | 3.57 | 3.4 dB   |
| Peaking | 19002 Hz | 0.95 | -10.9 dB |
| Peaking | 3279 Hz  | 3.37 | 1.4 dB   |
| Peaking | 3755 Hz  | 3.28 | -0.9 dB  |
| Peaking | 4958 Hz  | 3.01 | -3.6 dB  |
| Peaking | 6573 Hz  | 4.14 | 4.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -5.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Samsung%20Level%20U%20Pro/Samsung%20Level%20U%20Pro.png)