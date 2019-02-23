# Audeze LCD-XC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.1; 25 -3.0; 28 -2.8; 31 -2.8; 34 -3.0; 37 -3.3; 41 -3.5; 45 -3.5; 49 -3.6; 54 -4.0; 60 -5.1; 66 -5.9; 72 -6.2; 79 -6.5; 87 -6.7; 96 -6.9; 106 -7.0; 116 -7.2; 128 -7.3; 141 -7.4; 155 -7.3; 170 -7.5; 187 -7.5; 206 -7.4; 227 -7.0; 249 -6.7; 274 -6.3; 302 -6.1; 332 -5.9; 365 -5.6; 402 -5.5; 442 -5.4; 486 -5.8; 535 -5.7; 588 -5.4; 647 -5.4; 712 -5.9; 783 -6.3; 861 -6.9; 947 -7.4; 1042 -8.0; 1146 -8.6; 1261 -9.4; 1387 -10.4; 1526 -11.4; 1678 -11.9; 1846 -11.6; 2031 -10.5; 2234 -8.9; 2457 -7.1; 2703 -5.8; 2973 -4.9; 3270 -4.5; 3597 -5.2; 3957 -6.9; 4353 -7.5; 4788 -7.1; 5267 -3.4; 5793 -0.5; 6373 -1.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.5; 15026 -9.1; 16529 -9.2; 18182 -11.2; 20000 -11.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-XC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-XC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 1.14 | 4.2 dB  |
| Peaking | 1694 Hz  | 1.92 | -5.9 dB |
| Peaking | 3033 Hz  | 3.77 | 2.9 dB  |
| Peaking | 6005 Hz  | 4.16 | 6.8 dB  |
| Peaking | 19256 Hz | 0.57 | -5.5 dB |
| Peaking | 51 Hz    | 3.42 | 1.6 dB  |
| Peaking | 388 Hz   | 0.28 | -2.9 dB |
| Peaking | 474 Hz   | 0.61 | 4.1 dB  |
| Peaking | 4401 Hz  | 1.34 | 2.2 dB  |
| Peaking | 4432 Hz  | 3.24 | -4.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -4.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-XC/Audeze%20LCD-XC.png)