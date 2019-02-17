# HiFiMan HE-400i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.7; 37 -1.1; 41 -1.7; 45 -2.2; 49 -2.7; 54 -3.2; 60 -3.6; 66 -4.1; 72 -4.5; 79 -4.9; 87 -5.3; 96 -5.7; 106 -6.1; 116 -6.3; 128 -6.6; 141 -6.8; 155 -7.0; 170 -7.1; 187 -7.1; 206 -7.1; 227 -7.1; 249 -7.2; 274 -7.5; 302 -7.6; 332 -7.8; 365 -7.9; 402 -7.8; 442 -7.2; 486 -6.6; 535 -6.9; 588 -7.5; 647 -7.8; 712 -7.4; 783 -7.7; 861 -7.3; 947 -6.6; 1042 -6.4; 1146 -6.0; 1261 -5.9; 1387 -6.0; 1526 -6.3; 1678 -6.2; 1846 -5.4; 2031 -5.7; 2234 -5.2; 2457 -6.5; 2703 -7.0; 2973 -8.3; 3270 -8.3; 3597 -8.7; 3957 -8.5; 4353 -7.8; 4788 -6.8; 5267 -5.6; 5793 -4.7; 6373 -9.1; 7010 -11.7; 7711 -12.3; 8482 -12.9; 9330 -11.2; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -7.0; 15026 -9.1; 16529 -10.4; 18182 -11.2; 20000 -10.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan HE-400i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan HE-400i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.57 | 6.3 dB  |
| Peaking | 249 Hz   | 0.51 | -1.2 dB |
| Peaking | 3509 Hz  | 4.39 | -2.3 dB |
| Peaking | 8087 Hz  | 3.16 | -7.0 dB |
| Peaking | 18581 Hz | 0.87 | -5.4 dB |
| Peaking | 750 Hz   | 3.12 | -1.0 dB |
| Peaking | 1889 Hz  | 0.91 | 1.3 dB  |
| Peaking | 5583 Hz  | 5.36 | 4.7 dB  |
| Peaking | 9413 Hz  | 0.4  | -2.5 dB |
| Peaking | 11499 Hz | 1.29 | 3.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | -4.3 dB |
| Peaking | 16000 Hz | 1.41 | -3.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HiFiMan%20HE-400i/HiFiMan%20HE-400i.png)