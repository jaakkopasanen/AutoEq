# Samsung Level On Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -0.9; 25 -1.3; 28 -1.8; 31 -2.3; 34 -2.8; 37 -3.4; 41 -4.1; 45 -4.7; 49 -5.1; 54 -5.5; 60 -5.9; 66 -6.4; 72 -6.7; 79 -7.2; 87 -7.8; 96 -8.3; 106 -8.9; 116 -9.4; 128 -9.9; 141 -10.3; 155 -10.6; 170 -10.8; 187 -10.8; 206 -10.7; 227 -10.4; 249 -10.0; 274 -9.6; 302 -9.0; 332 -8.3; 365 -7.7; 402 -7.1; 442 -6.8; 486 -6.4; 535 -6.5; 588 -6.8; 647 -7.1; 712 -7.5; 783 -7.5; 861 -6.8; 947 -6.5; 1042 -6.5; 1146 -6.2; 1261 -4.8; 1387 -4.3; 1526 -3.9; 1678 -4.0; 1846 -4.5; 2031 -4.8; 2234 -4.7; 2457 -4.3; 2703 -4.7; 2973 -5.3; 3270 -5.9; 3597 -6.5; 3957 -8.5; 4353 -6.5; 4788 -2.8; 5267 -0.6; 5793 -0.5; 6373 -2.0; 7010 -4.5; 7711 -6.2; 8482 -7.7; 9330 -11.3; 10263 -11.8; 11289 -9.7; 12418 -9.8; 13660 -11.0; 15026 -10.0; 16529 -7.7; 18182 -6.6; 20000 -10.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Level On Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Level On Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.8  | 5.8 dB  |
| Peaking | 171 Hz   | 0.92 | -4.8 dB |
| Peaking | 5731 Hz  | 2.85 | 7.0 dB  |
| Peaking | 9818 Hz  | 3.5  | -5.6 dB |
| Peaking | 13958 Hz | 1.64 | -4.4 dB |
| Peaking | 489 Hz   | 1.78 | 2.4 dB  |
| Peaking | 614 Hz   | 0.76 | -1.9 dB |
| Peaking | 1469 Hz  | 2.64 | 1.9 dB  |
| Peaking | 2187 Hz  | 0.76 | 1.7 dB  |
| Peaking | 4018 Hz  | 5.82 | -4.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -4.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Samsung%20Level%20On%20Wireless/Samsung%20Level%20On%20Wireless.png)