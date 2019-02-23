# Samsung Level U Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -7.8; 25 -7.7; 28 -7.7; 31 -7.6; 34 -7.5; 37 -7.4; 41 -7.3; 45 -7.2; 49 -7.1; 54 -7.1; 60 -7.2; 66 -7.4; 72 -7.5; 79 -7.7; 87 -7.9; 96 -8.2; 106 -8.6; 116 -9.0; 128 -9.2; 141 -9.3; 155 -9.4; 170 -9.2; 187 -9.0; 206 -8.8; 227 -8.5; 249 -8.1; 274 -7.5; 302 -6.9; 332 -6.3; 365 -5.6; 402 -4.9; 442 -4.2; 486 -3.5; 535 -2.8; 588 -2.1; 647 -1.4; 712 -0.9; 783 -0.7; 861 -0.8; 947 -1.3; 1042 -1.9; 1146 -2.3; 1261 -2.6; 1387 -2.7; 1526 -2.7; 1678 -2.7; 1846 -2.7; 2031 -2.5; 2234 -1.6; 2457 -0.6; 2703 -0.5; 2973 -1.4; 3270 -2.8; 3597 -4.3; 3957 -5.4; 4353 -6.6; 4788 -6.8; 5267 -6.4; 5793 -4.4; 6373 -2.9; 7010 -2.0; 7711 -4.1; 8482 -4.4; 9330 -6.6; 10263 -4.5; 11289 -4.4; 12418 -5.3; 13660 -7.2; 15026 -6.7; 16529 -9.4; 18182 -13.9; 20000 -13.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Level U Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Level U Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 23 Hz    |  0.63 | -3.1 dB  |
| Peaking | 166 Hz   |  0.55 | -5.1 dB  |
| Peaking | 746 Hz   |  0.96 | 4.3 dB   |
| Peaking | 2576 Hz  |  3.39 | 4.0 dB   |
| Peaking | 19021 Hz |  0.81 | -10.8 dB |
| Peaking | 3038 Hz  |  4.57 | 1.2 dB   |
| Peaking | 4725 Hz  |  2.39 | -3.2 dB  |
| Peaking | 6731 Hz  |  3.79 | 3.4 dB   |
| Peaking | 9277 Hz  | 11.79 | -2.1 dB  |
| Peaking | 17560 Hz |  6.5  | -1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -6.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Samsung%20Level%20U%20Pro/Samsung%20Level%20U%20Pro.png)