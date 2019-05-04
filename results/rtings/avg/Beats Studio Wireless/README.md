# Beats Studio Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -4.0; 25 -4.9; 28 -6.1; 31 -6.9; 34 -7.4; 37 -7.7; 41 -8.0; 45 -8.1; 49 -8.3; 54 -8.5; 60 -8.7; 66 -9.0; 72 -9.2; 79 -9.5; 87 -9.8; 96 -10.1; 106 -10.2; 116 -10.2; 128 -10.1; 141 -9.9; 155 -9.7; 170 -9.4; 187 -8.9; 206 -8.3; 227 -7.6; 249 -6.8; 274 -5.9; 302 -4.7; 332 -3.2; 365 -1.1; 402 -0.5; 442 -0.6; 486 -3.6; 535 -6.3; 588 -7.1; 647 -7.2; 712 -7.8; 783 -8.2; 861 -8.2; 947 -7.7; 1042 -7.7; 1146 -8.2; 1261 -8.7; 1387 -8.6; 1526 -8.2; 1678 -8.2; 1846 -8.0; 2031 -7.2; 2234 -6.3; 2457 -5.2; 2703 -4.3; 2973 -5.0; 3270 -6.6; 3597 -7.7; 3957 -7.8; 4353 -5.6; 4788 -2.5; 5267 -3.7; 5793 -3.9; 6373 -2.1; 7010 -4.0; 7711 -6.3; 8482 -7.5; 9330 -8.2; 10263 -11.0; 11289 -13.7; 12418 -12.8; 13660 -9.8; 15026 -7.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Studio Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Studio Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 1.7  | 5.7 dB  |
| Peaking | 232 Hz   | 0.19 | -4.2 dB |
| Peaking | 388 Hz   | 1.63 | 10.3 dB |
| Peaking | 6011 Hz  | 1.71 | 4.5 dB  |
| Peaking | 11598 Hz | 1.95 | -8.0 dB |
| Peaking | 997 Hz   | 4.41 | 1.3 dB  |
| Peaking | 1430 Hz  | 0.88 | -1.0 dB |
| Peaking | 2787 Hz  | 2.52 | 3.9 dB  |
| Peaking | 3783 Hz  | 1.93 | -3.0 dB |
| Peaking | 4678 Hz  | 7.23 | 3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 4.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.4 dB |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Studio%20Wireless/Beats%20Studio%20Wireless.png)