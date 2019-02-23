# Audeze LCD-2 sn5325928
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.6; 25 -3.6; 28 -3.6; 31 -3.6; 34 -3.7; 37 -3.8; 41 -3.9; 45 -4.0; 49 -4.2; 54 -4.4; 60 -4.7; 66 -4.8; 72 -5.1; 79 -5.3; 87 -5.7; 96 -6.0; 106 -6.3; 116 -6.4; 128 -6.7; 141 -7.0; 155 -7.2; 170 -7.3; 187 -7.5; 206 -7.6; 227 -7.5; 249 -7.7; 274 -7.7; 302 -7.6; 332 -7.6; 365 -7.7; 402 -7.8; 442 -7.8; 486 -8.0; 535 -8.0; 588 -8.2; 647 -8.3; 712 -8.2; 783 -8.1; 861 -8.3; 947 -8.2; 1042 -7.8; 1146 -7.9; 1261 -7.9; 1387 -8.4; 1526 -9.0; 1678 -9.2; 1846 -8.2; 2031 -7.7; 2234 -7.1; 2457 -6.0; 2703 -5.3; 2973 -4.5; 3270 -3.2; 3597 -1.8; 3957 -0.5; 4353 -3.1; 4788 -3.9; 5267 -2.6; 5793 -1.7; 6373 -2.6; 7010 -3.7; 7711 -5.9; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.9; 16529 -9.2; 18182 -10.6; 20000 -10.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 sn5325928 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 sn5325928 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.49 | 2.8 dB  |
| Peaking | 918 Hz   | 0.16 | -2.1 dB |
| Peaking | 3728 Hz  | 2.25 | 6.3 dB  |
| Peaking | 6025 Hz  | 2.83 | 4.7 dB  |
| Peaking | 18847 Hz | 0.95 | -5.1 dB |
| Peaking | 1201 Hz  | 2.18 | 0.5 dB  |
| Peaking | 1612 Hz  | 3.53 | -1.5 dB |
| Peaking | 2553 Hz  | 5.77 | 0.9 dB  |
| Peaking | 13713 Hz | 3.11 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20sn5325928/Audeze%20LCD-2%20sn5325928.png)