# Sennheiser Momentum True Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -6.6; 25 -6.6; 28 -6.7; 31 -6.7; 34 -6.7; 37 -6.8; 41 -6.8; 45 -6.8; 49 -6.9; 54 -7.0; 60 -7.2; 66 -7.5; 72 -7.8; 79 -8.2; 87 -8.6; 96 -9.0; 106 -9.5; 116 -10.0; 128 -10.4; 141 -10.8; 155 -11.0; 170 -11.0; 187 -11.1; 206 -11.0; 227 -10.8; 249 -10.5; 274 -10.2; 302 -9.8; 332 -9.4; 365 -9.0; 402 -8.7; 442 -8.3; 486 -7.8; 535 -7.3; 588 -6.8; 647 -6.2; 712 -5.6; 783 -5.3; 861 -5.1; 947 -5.2; 1042 -5.6; 1146 -6.1; 1261 -7.0; 1387 -7.7; 1526 -7.9; 1678 -7.5; 1846 -6.6; 2031 -5.4; 2234 -3.6; 2457 -1.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.3; 5793 -3.0; 6373 -6.7; 7010 -9.6; 7711 -8.8; 8482 -6.6; 9330 -8.0; 10263 -12.2; 11289 -14.2; 12418 -12.9; 13660 -11.3; 15026 -9.0; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum True Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum True Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 205 Hz   | 0.57 | -4.9 dB  |
| Peaking | 1610 Hz  | 1.4  | -7.6 dB  |
| Peaking | 4039 Hz  | 0.25 | 8.5 dB   |
| Peaking | 6988 Hz  | 3.53 | -7.7 dB  |
| Peaking | 11558 Hz | 1.24 | -12.5 dB |
| Peaking | 51 Hz    | 2.22 | 0.6 dB   |
| Peaking | 2101 Hz  | 6.64 | -0.8 dB  |
| Peaking | 2633 Hz  | 3.84 | 1.1 dB   |
| Peaking | 3733 Hz  | 2.15 | -0.6 dB  |
| Peaking | 5012 Hz  | 5.79 | 0.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.0 dB |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 8.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB |
| Peaking | 16000 Hz | 1.41 | -3.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20Momentum%20True%20Wireless/Sennheiser%20Momentum%20True%20Wireless.png)