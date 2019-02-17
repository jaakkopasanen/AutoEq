# Massdrop x Fostex TH-X00 sn1927
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.2; 25 -6.4; 28 -6.7; 31 -6.7; 34 -6.7; 37 -6.7; 41 -6.7; 45 -6.6; 49 -6.6; 54 -6.5; 60 -6.4; 66 -6.3; 72 -6.4; 79 -6.7; 87 -7.0; 96 -7.2; 106 -7.4; 116 -7.4; 128 -7.6; 141 -7.7; 155 -7.7; 170 -7.5; 187 -7.4; 206 -7.3; 227 -6.9; 249 -6.5; 274 -6.1; 302 -5.8; 332 -5.6; 365 -5.3; 402 -5.1; 442 -4.6; 486 -4.7; 535 -4.7; 588 -4.5; 647 -4.7; 712 -5.3; 783 -4.3; 861 -4.5; 947 -5.2; 1042 -5.3; 1146 -5.2; 1261 -5.2; 1387 -5.6; 1526 -6.1; 1678 -6.2; 1846 -5.8; 2031 -5.2; 2234 -4.5; 2457 -3.4; 2703 -2.5; 2973 -0.7; 3270 -0.5; 3597 -0.7; 3957 -1.2; 4353 -2.2; 4788 -2.4; 5267 -4.0; 5793 -3.4; 6373 -3.2; 7010 -3.0; 7711 -5.0; 8482 -5.2; 9330 -5.2; 10263 -5.7; 11289 -5.3; 12418 -5.3; 13660 -5.5; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Fostex TH-X00 sn1927 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Fostex TH-X00 sn1927 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.54 | -1.3 dB |
| Peaking | 148 Hz  | 1.17 | -2.4 dB |
| Peaking | 1764 Hz | 2.6  | -1.8 dB |
| Peaking | 3395 Hz | 1.58 | 5.1 dB  |
| Peaking | 6663 Hz | 5.63 | 1.8 dB  |
| Peaking | 227 Hz  | 3.14 | -0.5 dB |
| Peaking | 531 Hz  | 1.37 | 0.8 dB  |
| Peaking | 9612 Hz | 2.23 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.4 dB |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20Fostex%20TH-X00%20sn1927/Massdrop%20x%20Fostex%20TH-X00%20sn1927.png)