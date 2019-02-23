# HiFiMAN HE-400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.5; 25 -3.9; 28 -4.3; 31 -4.5; 34 -4.6; 37 -4.7; 41 -4.7; 45 -4.8; 49 -4.8; 54 -4.8; 60 -4.8; 66 -5.0; 72 -5.1; 79 -5.3; 87 -5.6; 96 -6.0; 106 -6.2; 116 -6.3; 128 -6.6; 141 -6.8; 155 -7.0; 170 -7.2; 187 -7.4; 206 -6.9; 227 -6.9; 249 -7.7; 274 -6.4; 302 -6.9; 332 -7.5; 365 -7.5; 402 -7.5; 442 -7.8; 486 -7.7; 535 -6.8; 588 -5.9; 647 -7.1; 712 -8.3; 783 -8.8; 861 -10.6; 947 -11.6; 1042 -10.5; 1146 -9.4; 1261 -9.1; 1387 -7.0; 1526 -6.0; 1678 -6.1; 1846 -5.5; 2031 -6.0; 2234 -5.9; 2457 -3.0; 2703 -0.7; 2973 -0.5; 3270 -1.7; 3597 -1.0; 3957 -2.6; 4353 -5.7; 4788 -6.2; 5267 -1.6; 5793 -0.8; 6373 -5.0; 7010 -6.2; 7711 -7.3; 8482 -11.4; 9330 -12.3; 10263 -8.1; 11289 -6.7; 12418 -10.3; 13660 -12.4; 15026 -8.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 962 Hz   | 2.26 | -5.2 dB |
| Peaking | 3052 Hz  | 2.1  | 6.3 dB  |
| Peaking | 5619 Hz  | 6.6  | 6.3 dB  |
| Peaking | 8933 Hz  | 4.84 | -6.8 dB |
| Peaking | 13619 Hz | 3.49 | -6.5 dB |
| Peaking | 15 Hz    | 0.82 | 4.0 dB  |
| Peaking | 63 Hz    | 1.05 | 1.4 dB  |
| Peaking | 257 Hz   | 0.46 | -0.8 dB |
| Peaking | 593 Hz   | 6.36 | 1.8 dB  |
| Peaking | 16231 Hz | 3.25 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.7 dB |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-400/HiFiMAN%20HE-400.png)