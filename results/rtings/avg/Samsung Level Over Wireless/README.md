# Samsung Level Over Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.3; 25 -2.6; 28 -3.0; 31 -3.3; 34 -3.6; 37 -3.9; 41 -4.2; 45 -4.6; 49 -4.9; 54 -5.3; 60 -5.7; 66 -6.2; 72 -6.5; 79 -7.0; 87 -7.4; 96 -7.9; 106 -8.3; 116 -8.6; 128 -8.8; 141 -8.9; 155 -8.8; 170 -8.6; 187 -8.3; 206 -7.8; 227 -7.5; 249 -8.0; 274 -9.4; 302 -10.1; 332 -9.5; 365 -8.8; 402 -7.9; 442 -7.4; 486 -7.2; 535 -7.1; 588 -7.3; 647 -7.5; 712 -7.1; 783 -6.7; 861 -6.8; 947 -5.4; 1042 -5.3; 1146 -5.4; 1261 -5.4; 1387 -6.1; 1526 -5.9; 1678 -4.9; 1846 -3.8; 2031 -4.3; 2234 -5.5; 2457 -3.0; 2703 -0.5; 2973 -0.5; 3270 -1.9; 3597 -6.1; 3957 -9.1; 4353 -8.6; 4788 -7.1; 5267 -5.8; 5793 -4.8; 6373 -4.9; 7010 -5.8; 7711 -6.2; 8482 -6.5; 9330 -7.5; 10263 -6.7; 11289 -6.8; 12418 -8.3; 13660 -9.1; 15026 -9.5; 16529 -8.1; 18182 -8.0; 20000 -14.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Level Over Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Level Over Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.46 | 4.7 dB  |
| Peaking | 128 Hz   | 1.13 | -2.7 dB |
| Peaking | 315 Hz   | 2.75 | -3.3 dB |
| Peaking | 2806 Hz  | 3.46 | 6.8 dB  |
| Peaking | 20995 Hz | 0.18 | -4.7 dB |
| Peaking | 1841 Hz  | 5.21 | 2.1 dB  |
| Peaking | 4122 Hz  | 5.51 | -4.0 dB |
| Peaking | 6056 Hz  | 3.9  | 2.2 dB  |
| Peaking | 11195 Hz | 6.89 | 0.9 dB  |
| Peaking | 13877 Hz | 3.15 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -3.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Samsung%20Level%20Over%20Wireless/Samsung%20Level%20Over%20Wireless.png)