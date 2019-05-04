# Sennheiser Momentum True Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -10.2; 25 -10.4; 28 -10.7; 31 -10.8; 34 -10.9; 37 -11.0; 41 -11.1; 45 -11.2; 49 -11.3; 54 -11.3; 60 -11.4; 66 -11.5; 72 -11.6; 79 -11.8; 87 -11.9; 96 -12.0; 106 -11.9; 116 -11.9; 128 -12.7; 141 -12.9; 155 -12.7; 170 -12.5; 187 -12.3; 206 -12.0; 227 -11.6; 249 -11.1; 274 -11.0; 302 -10.9; 332 -10.3; 365 -9.8; 402 -9.4; 442 -9.0; 486 -8.6; 535 -8.1; 588 -7.8; 647 -7.4; 712 -7.1; 783 -6.8; 861 -6.8; 947 -7.0; 1042 -7.4; 1146 -7.5; 1261 -7.2; 1387 -7.1; 1526 -6.8; 1678 -6.2; 1846 -5.3; 2031 -3.9; 2234 -2.0; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.1; 6373 -5.0; 7010 -7.7; 7711 -6.6; 8482 -8.0; 9330 -13.1; 10263 -14.9; 11289 -11.0; 12418 -10.7; 13660 -19.8; 15026 -29.9; 16529 -31.1; 18182 -22.4; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum True Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum True Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.51 | -3.4 dB  |
| Peaking | 160 Hz   | 0.43 | -5.5 dB  |
| Peaking | 3885 Hz  | 0.92 | 7.8 dB   |
| Peaking | 15652 Hz | 1.34 | -22.9 dB |
| Peaking | 17481 Hz | 1.68 | -10.0 dB |
| Peaking | 1492 Hz  | 1.83 | -1.7 dB  |
| Peaking | 2416 Hz  | 4.93 | 2.8 dB   |
| Peaking | 5570 Hz  | 7.79 | 2.8 dB   |
| Peaking | 9903 Hz  | 4.61 | -5.6 dB  |
| Peaking | 12108 Hz | 4.9  | 6.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB  |
| Peaking | 62 Hz    | 1.41 | -3.5 dB  |
| Peaking | 125 Hz   | 1.41 | -5.0 dB  |
| Peaking | 250 Hz   | 1.41 | -4.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -29.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sennheiser%20Momentum%20True%20Wireless/Sennheiser%20Momentum%20True%20Wireless.png)