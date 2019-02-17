# Beats Studio Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -3.3; 25 -4.2; 28 -5.4; 31 -6.2; 34 -6.7; 37 -7.0; 41 -7.2; 45 -7.4; 49 -7.5; 54 -7.7; 60 -8.0; 66 -8.3; 72 -8.6; 79 -8.8; 87 -9.1; 96 -9.3; 106 -9.5; 116 -9.5; 128 -9.4; 141 -9.1; 155 -8.9; 170 -8.6; 187 -8.1; 206 -7.5; 227 -6.7; 249 -6.0; 274 -5.0; 302 -3.8; 332 -2.3; 365 -0.6; 402 -0.5; 442 -0.5; 486 -2.6; 535 -5.3; 588 -5.9; 647 -6.1; 712 -6.7; 783 -7.2; 861 -7.1; 947 -6.6; 1042 -6.6; 1146 -7.2; 1261 -7.7; 1387 -7.5; 1526 -7.0; 1678 -7.0; 1846 -6.8; 2031 -5.9; 2234 -4.5; 2457 -3.4; 2703 -2.8; 2973 -3.9; 3270 -5.9; 3597 -6.9; 3957 -7.3; 4353 -5.1; 4788 -1.1; 5267 -2.4; 5793 -3.1; 6373 -2.1; 7010 -4.0; 7711 -6.2; 8482 -7.0; 9330 -9.0; 10263 -10.6; 11289 -12.0; 12418 -11.9; 13660 -9.8; 15026 -7.2; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Studio Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Studio Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 3.9  | 4.7 dB  |
| Peaking | 399 Hz   | 3.04 | 7.1 dB  |
| Peaking | 4937 Hz  | 6.57 | 5.3 dB  |
| Peaking | 6368 Hz  | 3.21 | 4.8 dB  |
| Peaking | 11627 Hz | 1.76 | -6.2 dB |
| Peaking | 19 Hz    | 2.76 | 2.7 dB  |
| Peaking | 90 Hz    | 1.13 | -2.7 dB |
| Peaking | 150 Hz   | 2.29 | -1.9 dB |
| Peaking | 2403 Hz  | 0.78 | -2.5 dB |
| Peaking | 2576 Hz  | 2.4  | 6.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 4.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Studio%20Wireless/Beats%20Studio%20Wireless.png)