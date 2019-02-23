# Samsung Level On Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.0; 28 -1.5; 31 -2.0; 34 -2.5; 37 -3.0; 41 -3.8; 45 -4.3; 49 -4.8; 54 -5.1; 60 -5.6; 66 -6.1; 72 -6.4; 79 -6.9; 87 -7.5; 96 -8.0; 106 -8.6; 116 -9.1; 128 -9.6; 141 -10.0; 155 -10.3; 170 -10.5; 187 -10.5; 206 -10.4; 227 -10.1; 249 -9.7; 274 -9.2; 302 -8.7; 332 -8.0; 365 -7.3; 402 -6.8; 442 -6.5; 486 -6.1; 535 -6.2; 588 -6.5; 647 -6.8; 712 -7.2; 783 -7.2; 861 -6.5; 947 -6.2; 1042 -6.2; 1146 -5.8; 1261 -4.5; 1387 -3.9; 1526 -3.6; 1678 -3.7; 1846 -4.2; 2031 -4.5; 2234 -4.4; 2457 -4.0; 2703 -4.4; 2973 -5.0; 3270 -5.6; 3597 -6.2; 3957 -8.2; 4353 -6.2; 4788 -2.5; 5267 -0.5; 5793 -0.5; 6373 -1.7; 7010 -4.3; 7711 -6.2; 8482 -7.4; 9330 -11.0; 10263 -11.5; 11289 -9.4; 12418 -9.5; 13660 -10.7; 15026 -9.7; 16529 -7.3; 18182 -6.6; 20000 -10.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Level On Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Level On Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.8  | 6.0 dB  |
| Peaking | 171 Hz   | 1.02 | -4.5 dB |
| Peaking | 5729 Hz  | 2.51 | 6.9 dB  |
| Peaking | 9813 Hz  | 3.32 | -5.4 dB |
| Peaking | 13950 Hz | 1.82 | -4.1 dB |
| Peaking | 273 Hz   | 3.68 | -0.7 dB |
| Peaking | 471 Hz   | 3.92 | 1.0 dB  |
| Peaking | 1521 Hz  | 2.7  | 2.7 dB  |
| Peaking | 2445 Hz  | 2.14 | 1.9 dB  |
| Peaking | 4043 Hz  | 7.15 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -3.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Samsung%20Level%20On%20Wireless/Samsung%20Level%20On%20Wireless.png)