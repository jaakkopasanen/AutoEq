# HiFiMan HE-400i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.2; 49 -1.6; 54 -2.1; 60 -2.6; 66 -3.0; 72 -3.3; 79 -3.7; 87 -4.2; 96 -4.6; 106 -4.9; 116 -5.2; 128 -5.5; 141 -5.8; 155 -5.9; 170 -6.0; 187 -6.0; 206 -6.0; 227 -6.2; 249 -6.2; 274 -6.5; 302 -6.7; 332 -6.8; 365 -7.0; 402 -6.9; 442 -6.3; 486 -5.8; 535 -6.0; 588 -6.8; 647 -7.0; 712 -6.7; 783 -6.9; 861 -6.5; 947 -5.8; 1042 -5.6; 1146 -5.2; 1261 -5.2; 1387 -5.3; 1526 -5.6; 1678 -5.5; 1846 -4.9; 2031 -5.2; 2234 -5.3; 2457 -6.5; 2703 -6.8; 2973 -7.4; 3270 -7.2; 3597 -7.6; 3957 -7.2; 4353 -6.6; 4788 -6.4; 5267 -5.0; 5793 -3.8; 6373 -7.0; 7010 -10.9; 7711 -12.1; 8482 -11.6; 9330 -8.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.8; 16529 -9.3; 18182 -10.1; 20000 -9.8
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
| Peaking | 30 Hz    | 0.55 | 6.4 dB  |
| Peaking | 1520 Hz  | 1.62 | 1.4 dB  |
| Peaking | 5747 Hz  | 5.54 | 4.4 dB  |
| Peaking | 7693 Hz  | 2.94 | -6.4 dB |
| Peaking | 18717 Hz | 0.95 | -4.2 dB |
| Peaking | 345 Hz   | 3.16 | -0.7 dB |
| Peaking | 1609 Hz  | 4.76 | -1.5 dB |
| Peaking | 1911 Hz  | 1.62 | 1.4 dB  |
| Peaking | 3072 Hz  | 1.86 | -1.4 dB |
| Peaking | 11320 Hz | 2.41 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | -2.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HiFiMan%20HE-400i/HiFiMan%20HE-400i.png)