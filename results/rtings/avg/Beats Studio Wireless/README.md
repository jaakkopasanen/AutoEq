# Beats Studio Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -4.2; 25 -5.2; 28 -6.3; 31 -7.1; 34 -7.6; 37 -7.9; 41 -8.1; 45 -8.3; 49 -8.4; 54 -8.6; 60 -8.9; 66 -9.3; 72 -9.5; 79 -9.7; 87 -10.0; 96 -10.3; 106 -10.4; 116 -10.4; 128 -10.3; 141 -10.1; 155 -9.9; 170 -9.5; 187 -9.1; 206 -8.4; 227 -7.7; 249 -6.9; 274 -5.9; 302 -4.7; 332 -3.2; 365 -1.2; 402 -0.5; 442 -0.6; 486 -3.5; 535 -6.2; 588 -6.9; 647 -7.1; 712 -7.7; 783 -8.1; 861 -8.1; 947 -7.6; 1042 -7.5; 1146 -8.1; 1261 -8.6; 1387 -8.4; 1526 -7.9; 1678 -8.0; 1846 -7.7; 2031 -6.8; 2234 -5.5; 2457 -4.4; 2703 -3.8; 2973 -4.8; 3270 -6.8; 3597 -7.8; 3957 -8.2; 4353 -6.0; 4788 -2.0; 5267 -3.3; 5793 -4.0; 6373 -3.0; 7010 -4.1; 7711 -6.2; 8482 -7.9; 9330 -9.9; 10263 -11.6; 11289 -12.9; 12418 -12.8; 13660 -10.7; 15026 -8.1; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Studio Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Studio Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 1.73 | 5.6 dB  |
| Peaking | 213 Hz   | 0.2  | -4.4 dB |
| Peaking | 388 Hz   | 1.61 | 10.4 dB |
| Peaking | 6041 Hz  | 1.52 | 4.6 dB  |
| Peaking | 11480 Hz | 1.39 | -7.4 dB |
| Peaking | 1758 Hz  | 1.69 | -1.2 dB |
| Peaking | 2692 Hz  | 2.13 | 4.8 dB  |
| Peaking | 3746 Hz  | 1.8  | -4.0 dB |
| Peaking | 4814 Hz  | 7.71 | 4.3 dB  |
| Peaking | 16693 Hz | 2.51 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 4.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -3.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Studio%20Wireless/Beats%20Studio%20Wireless.png)