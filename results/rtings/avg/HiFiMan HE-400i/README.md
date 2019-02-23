# HiFiMan HE-400i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.8; 45 -1.3; 49 -1.8; 54 -2.3; 60 -2.7; 66 -3.2; 72 -3.6; 79 -4.0; 87 -4.4; 96 -4.8; 106 -5.2; 116 -5.5; 128 -5.7; 141 -5.9; 155 -6.1; 170 -6.2; 187 -6.2; 206 -6.2; 227 -6.2; 249 -6.3; 274 -6.6; 302 -6.7; 332 -6.9; 365 -7.0; 402 -6.9; 442 -6.3; 486 -5.7; 535 -6.0; 588 -6.6; 647 -6.9; 712 -6.5; 783 -6.8; 861 -6.4; 947 -5.7; 1042 -5.5; 1146 -5.1; 1261 -5.0; 1387 -5.1; 1526 -5.4; 1678 -5.3; 1846 -4.5; 2031 -4.8; 2234 -4.4; 2457 -5.6; 2703 -6.1; 2973 -7.4; 3270 -7.4; 3597 -7.8; 3957 -7.6; 4353 -6.9; 4788 -5.9; 5267 -4.7; 5793 -3.8; 6373 -8.2; 7010 -10.8; 7711 -11.4; 8482 -12.0; 9330 -10.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.2; 16529 -9.5; 18182 -10.3; 20000 -9.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan HE-400i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan HE-400i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.59 | 6.4 dB  |
| Peaking | 1709 Hz  | 1.5  | 1.8 dB  |
| Peaking | 5590 Hz  | 6.01 | 4.8 dB  |
| Peaking | 7773 Hz  | 2.24 | -5.9 dB |
| Peaking | 18633 Hz | 0.97 | -4.4 dB |
| Peaking | 341 Hz   | 3.29 | -0.7 dB |
| Peaking | 1151 Hz  | 6.1  | 0.8 dB  |
| Peaking | 2252 Hz  | 6.95 | 1.3 dB  |
| Peaking | 3416 Hz  | 2.9  | -1.5 dB |
| Peaking | 11316 Hz | 3.09 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HiFiMan%20HE-400i/HiFiMan%20HE-400i.png)