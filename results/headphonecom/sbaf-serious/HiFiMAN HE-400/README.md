# HiFiMAN HE-400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.4; 25 -5.4; 28 -5.4; 31 -5.4; 34 -5.4; 37 -5.5; 41 -5.5; 45 -5.4; 49 -5.4; 54 -5.5; 60 -5.7; 66 -5.8; 72 -5.9; 79 -6.2; 87 -6.4; 96 -6.9; 106 -7.1; 116 -7.3; 128 -7.5; 141 -7.7; 155 -8.2; 170 -8.4; 187 -6.8; 206 -6.8; 227 -7.5; 249 -7.9; 274 -8.1; 302 -7.9; 332 -8.1; 365 -9.0; 402 -8.8; 442 -5.5; 486 -5.8; 535 -6.5; 588 -7.6; 647 -8.1; 712 -9.2; 783 -10.1; 861 -10.4; 947 -10.5; 1042 -11.1; 1146 -9.6; 1261 -9.0; 1387 -7.2; 1526 -6.2; 1678 -5.0; 1846 -4.0; 2031 -1.4; 2234 -3.5; 2457 -0.8; 2703 -0.5; 2973 -0.9; 3270 -0.5; 3597 -0.6; 3957 -1.6; 4353 -1.5; 4788 -5.3; 5267 -2.2; 5793 -0.8; 6373 -4.8; 7010 -8.2; 7711 -9.3; 8482 -12.5; 9330 -14.1; 10263 -9.8; 11289 -6.5; 12418 -8.6; 13660 -10.3; 15026 -9.0; 16529 -7.9; 18182 -6.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 1061 Hz  | 0.96 | -7.6 dB  |
| Peaking | 2794 Hz  | 0.44 | 7.3 dB   |
| Peaking | 9115 Hz  | 2.1  | -10.7 dB |
| Peaking | 11086 Hz | 2.38 | 6.0 dB   |
| Peaking | 13337 Hz | 1.38 | -4.9 dB  |
| Peaking | 154 Hz   | 3.29 | -1.6 dB  |
| Peaking | 405 Hz   | 2    | -4.6 dB  |
| Peaking | 465 Hz   | 2.95 | 5.7 dB   |
| Peaking | 4814 Hz  | 8.96 | -3.8 dB  |
| Peaking | 5638 Hz  | 8.29 | 4.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.8 dB |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.1 dB |
| Peaking | 16000 Hz | 1.41 | -2.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE-400/HiFiMAN%20HE-400.png)