# Samsung Level On Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.8; 28 -1.3; 31 -1.8; 34 -2.3; 37 -2.9; 41 -3.6; 45 -4.2; 49 -4.6; 54 -5.0; 60 -5.4; 66 -5.8; 72 -6.2; 79 -6.7; 87 -7.2; 96 -7.8; 106 -8.3; 116 -8.8; 128 -9.3; 141 -9.8; 155 -10.1; 170 -10.3; 187 -10.3; 206 -10.2; 227 -10.0; 249 -9.7; 274 -9.3; 302 -8.7; 332 -8.0; 365 -7.3; 402 -6.8; 442 -6.5; 486 -6.2; 535 -6.2; 588 -6.6; 647 -7.0; 712 -7.3; 783 -7.3; 861 -6.6; 947 -6.3; 1042 -6.4; 1146 -5.9; 1261 -4.8; 1387 -4.1; 1526 -3.8; 1678 -4.0; 1846 -4.5; 2031 -4.9; 2234 -5.2; 2457 -4.9; 2703 -4.9; 2973 -5.1; 3270 -5.4; 3597 -6.1; 3957 -7.7; 4353 -5.8; 4788 -2.7; 5267 -0.7; 5793 -0.5; 6373 -1.2; 7010 -4.3; 7711 -6.2; 8482 -7.1; 9330 -9.5; 10263 -11.0; 11289 -10.4; 12418 -9.8; 13660 -9.9; 15026 -9.2; 16529 -7.1; 18182 -6.5; 20000 -10.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Level On Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Level On Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.72 | 6.1 dB  |
| Peaking | 175 Hz   | 0.93 | -4.2 dB |
| Peaking | 1627 Hz  | 1.77 | 2.7 dB  |
| Peaking | 5880 Hz  | 2.41 | 7.8 dB  |
| Peaking | 11288 Hz | 0.88 | -4.5 dB |
| Peaking | 483 Hz   | 1.73 | 3.4 dB  |
| Peaking | 527 Hz   | 1.03 | -2.4 dB |
| Peaking | 3954 Hz  | 1.68 | 2.3 dB  |
| Peaking | 3972 Hz  | 4.74 | -5.0 dB |
| Peaking | 15355 Hz | 6.25 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -3.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Samsung%20Level%20On%20Wireless/Samsung%20Level%20On%20Wireless.png)