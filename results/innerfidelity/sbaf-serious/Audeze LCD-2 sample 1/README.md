# Audeze LCD-2 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.7; 25 -4.0; 28 -4.3; 31 -4.4; 34 -4.4; 37 -4.4; 41 -4.5; 45 -4.5; 49 -4.7; 54 -5.0; 60 -5.4; 66 -6.1; 72 -6.5; 79 -6.6; 87 -6.9; 96 -7.1; 106 -7.3; 116 -7.5; 128 -7.7; 141 -7.9; 155 -8.1; 170 -8.2; 187 -8.4; 206 -8.5; 227 -8.5; 249 -8.7; 274 -8.8; 302 -8.8; 332 -9.0; 365 -9.1; 402 -9.1; 442 -9.2; 486 -9.2; 535 -8.9; 588 -8.9; 647 -9.4; 712 -9.7; 783 -9.9; 861 -10.1; 947 -10.1; 1042 -8.9; 1146 -6.5; 1261 -5.8; 1387 -5.8; 1526 -6.2; 1678 -4.9; 1846 -3.3; 2031 -3.1; 2234 -4.8; 2457 -4.8; 2703 -4.9; 2973 -3.9; 3270 -3.2; 3597 -1.6; 3957 -0.5; 4353 -0.5; 4788 -2.1; 5267 -2.1; 5793 -0.7; 6373 -1.5; 7010 -5.1; 7711 -6.2; 8482 -8.4; 9330 -7.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.2; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.58 | 2.8 dB  |
| Peaking | 1275 Hz  | 4.48 | 3.0 dB  |
| Peaking | 1590 Hz  | 0.11 | -3.6 dB |
| Peaking | 1904 Hz  | 3.1  | 4.8 dB  |
| Peaking | 4476 Hz  | 0.94 | 9.2 dB  |
| Peaking | 910 Hz   | 6.03 | -1.3 dB |
| Peaking | 5093 Hz  | 4.55 | -4.1 dB |
| Peaking | 5682 Hz  | 2.41 | 3.5 dB  |
| Peaking | 8480 Hz  | 4.54 | -2.9 dB |
| Peaking | 18913 Hz | 2.74 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20sample%201/Audeze%20LCD-2%20sample%201.png)