# AUKEY Latitude
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -6.9; 25 -6.8; 28 -6.7; 31 -6.7; 34 -6.7; 37 -6.7; 41 -6.7; 45 -6.8; 49 -6.8; 54 -6.9; 60 -7.0; 66 -7.2; 72 -7.4; 79 -7.6; 87 -7.8; 96 -8.0; 106 -8.2; 116 -8.3; 128 -8.4; 141 -8.4; 155 -8.3; 170 -8.1; 187 -7.8; 206 -7.8; 227 -7.7; 249 -7.5; 274 -7.1; 302 -6.7; 332 -6.2; 365 -5.7; 402 -5.3; 442 -4.8; 486 -4.3; 535 -3.6; 588 -2.9; 647 -2.2; 712 -1.6; 783 -1.2; 861 -1.2; 947 -1.4; 1042 -2.0; 1146 -2.7; 1261 -2.6; 1387 -2.6; 1526 -2.4; 1678 -2.2; 1846 -2.1; 2031 -1.8; 2234 -1.2; 2457 -0.5; 2703 -0.7; 2973 -2.4; 3270 -4.9; 3597 -6.2; 3957 -6.0; 4353 -5.8; 4788 -6.2; 5267 -6.4; 5793 -6.2; 6373 -5.9; 7010 -6.3; 7711 -4.6; 8482 -4.7; 9330 -5.7; 10263 -10.5; 11289 -9.0; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -6.5; 18182 -7.6; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AUKEY Latitude GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AUKEY Latitude ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 175 Hz   | 0.23 | -3.9 dB |
| Peaking | 787 Hz   | 0.7  | 5.5 dB  |
| Peaking | 2455 Hz  | 2.2  | 5.2 dB  |
| Peaking | 5547 Hz  | 0.3  | -2.1 dB |
| Peaking | 17784 Hz | 2.99 | -3.5 dB |
| Peaking | 20 Hz    | 2.13 | -1.5 dB |
| Peaking | 3570 Hz  | 7.27 | -1.4 dB |
| Peaking | 8803 Hz  | 2.76 | 3.4 dB  |
| Peaking | 10611 Hz | 3.1  | -7.9 dB |
| Peaking | 12244 Hz | 1.71 | 3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.4 dB |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AUKEY%20Latitude/AUKEY%20Latitude.png)