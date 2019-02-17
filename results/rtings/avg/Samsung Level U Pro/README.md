# Samsung Level U Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.2; 25 -8.2; 28 -8.1; 31 -8.0; 34 -7.9; 37 -7.8; 41 -7.7; 45 -7.6; 49 -7.5; 54 -7.5; 60 -7.6; 66 -7.8; 72 -7.9; 79 -8.1; 87 -8.3; 96 -8.7; 106 -9.1; 116 -9.4; 128 -9.6; 141 -9.7; 155 -9.8; 170 -9.7; 187 -9.5; 206 -9.2; 227 -8.9; 249 -8.5; 274 -7.9; 302 -7.3; 332 -6.7; 365 -6.0; 402 -5.4; 442 -4.7; 486 -3.9; 535 -3.2; 588 -2.5; 647 -1.8; 712 -1.3; 783 -1.1; 861 -1.2; 947 -1.7; 1042 -2.3; 1146 -2.7; 1261 -3.0; 1387 -3.1; 1526 -3.1; 1678 -3.1; 1846 -3.1; 2031 -2.9; 2234 -2.0; 2457 -1.0; 2703 -0.9; 2973 -1.8; 3270 -3.2; 3597 -4.7; 3957 -5.9; 4353 -7.0; 4788 -7.2; 5267 -6.8; 5793 -4.8; 6373 -3.4; 7010 -0.5; 7711 -1.7; 8482 -3.8; 9330 -7.1; 10263 -4.1; 11289 -2.5; 12418 -5.6; 13660 -7.7; 15026 -7.1; 16529 -9.8; 18182 -14.3; 20000 -13.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Level U Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Level U Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 0.92 | -5.7 dB  |
| Peaking | 44 Hz    | 0.26 | -4.7 dB  |
| Peaking | 189 Hz   | 0.78 | -5.6 dB  |
| Peaking | 4623 Hz  | 2.91 | -5.5 dB  |
| Peaking | 19055 Hz | 0.56 | -13.3 dB |
| Peaking | 768 Hz   | 1.4  | 3.4 dB   |
| Peaking | 1293 Hz  | 0.32 | -1.8 dB  |
| Peaking | 2623 Hz  | 2.95 | 3.2 dB   |
| Peaking | 7304 Hz  | 4.16 | 3.3 dB   |
| Peaking | 9211 Hz  | 8.06 | -4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.2 dB  |
| Peaking | 62 Hz    | 1.41 | -3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -6.4 dB  |
| Peaking | 250 Hz   | 1.41 | -5.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 4000 Hz  | 1.41 | -3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -10.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Samsung%20Level%20U%20Pro/Samsung%20Level%20U%20Pro.png)