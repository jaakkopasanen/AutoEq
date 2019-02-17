# Sennheiser Momentum True Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.6; 25 -7.7; 28 -7.7; 31 -7.8; 34 -7.8; 37 -7.8; 41 -7.8; 45 -7.9; 49 -7.9; 54 -8.0; 60 -8.2; 66 -8.6; 72 -8.9; 79 -9.2; 87 -9.6; 96 -10.1; 106 -10.6; 116 -11.0; 128 -11.5; 141 -11.8; 155 -12.0; 170 -12.1; 187 -12.1; 206 -12.1; 227 -11.9; 249 -11.6; 274 -11.2; 302 -10.8; 332 -10.5; 365 -10.1; 402 -9.7; 442 -9.3; 486 -8.9; 535 -8.4; 588 -7.8; 647 -7.2; 712 -6.7; 783 -6.3; 861 -6.2; 947 -6.3; 1042 -6.7; 1146 -7.2; 1261 -8.1; 1387 -8.7; 1526 -8.9; 1678 -8.6; 1846 -7.7; 2031 -6.5; 2234 -4.6; 2457 -2.7; 2703 -1.1; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -1.3; 4788 -1.6; 5267 -2.3; 5793 -4.0; 6373 -7.8; 7010 -10.7; 7711 -9.8; 8482 -7.7; 9330 -9.0; 10263 -13.2; 11289 -15.3; 12418 -14.0; 13660 -12.4; 15026 -10.0; 16529 -6.7; 18182 -6.5; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum True Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum True Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 202 Hz   | 0.45 | -5.9 dB  |
| Peaking | 1659 Hz  | 1.14 | -10.1 dB |
| Peaking | 2744 Hz  | 0.37 | 9.6 dB   |
| Peaking | 6951 Hz  | 3.64 | -7.2 dB  |
| Peaking | 11659 Hz | 1.39 | -10.8 dB |
| Peaking | 25 Hz    | 1.67 | -0.8 dB  |
| Peaking | 2155 Hz  | 6.6  | -0.6 dB  |
| Peaking | 2805 Hz  | 5.59 | 0.8 dB   |
| Peaking | 4300 Hz  | 4.77 | -0.4 dB  |
| Peaking | 16987 Hz | 4.35 | 1.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.0 dB |
| Peaking | 16000 Hz | 1.41 | -4.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20Momentum%20True%20Wireless/Sennheiser%20Momentum%20True%20Wireless.png)