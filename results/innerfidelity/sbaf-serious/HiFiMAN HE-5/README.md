# HiFiMAN HE-5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.0; 28 -1.5; 31 -2.0; 34 -2.3; 37 -2.5; 41 -2.8; 45 -3.0; 49 -3.1; 54 -2.9; 60 -3.1; 66 -3.7; 72 -4.0; 79 -4.2; 87 -4.5; 96 -4.8; 106 -5.0; 116 -5.2; 128 -5.5; 141 -5.8; 155 -6.1; 170 -6.2; 187 -6.3; 206 -6.6; 227 -6.7; 249 -6.9; 274 -6.8; 302 -6.8; 332 -6.7; 365 -6.8; 402 -7.2; 442 -6.8; 486 -6.6; 535 -7.0; 588 -6.8; 647 -6.7; 712 -6.4; 783 -5.8; 861 -6.2; 947 -6.3; 1042 -5.7; 1146 -4.6; 1261 -4.3; 1387 -4.2; 1526 -4.6; 1678 -3.7; 1846 -1.8; 2031 -2.2; 2234 -3.1; 2457 -2.6; 2703 -3.7; 2973 -5.4; 3270 -6.3; 3597 -6.6; 3957 -7.1; 4353 -9.6; 4788 -8.3; 5267 -5.5; 5793 -7.1; 6373 -9.9; 7010 -10.3; 7711 -10.3; 8482 -13.4; 9330 -15.3; 10263 -11.5; 11289 -8.4; 12418 -10.5; 13660 -12.7; 15026 -10.9; 16529 -6.9; 18182 -6.5; 20000 -11.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.8  | 5.7 dB  |
| Peaking | 61 Hz    | 1.09 | 2.2 dB  |
| Peaking | 2054 Hz  | 1.44 | 4.8 dB  |
| Peaking | 9919 Hz  | 0.73 | -6.0 dB |
| Peaking | 19954 Hz | 2.77 | -4.2 dB |
| Peaking | 4444 Hz  | 6.94 | -2.6 dB |
| Peaking | 5435 Hz  | 7.8  | 4.1 dB  |
| Peaking | 9343 Hz  | 4.57 | -5.1 dB |
| Peaking | 11171 Hz | 2.29 | 4.8 dB  |
| Peaking | 13809 Hz | 2.99 | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB |
| Peaking | 8000 Hz  | 1.41 | -6.3 dB |
| Peaking | 16000 Hz | 1.41 | -3.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-5/HiFiMAN%20HE-5.png)