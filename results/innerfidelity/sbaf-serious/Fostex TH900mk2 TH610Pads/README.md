# Fostex TH900mk2 TH610Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.6; 25 -7.1; 28 -7.7; 31 -8.1; 34 -8.3; 37 -8.5; 41 -8.7; 45 -8.8; 49 -8.9; 54 -9.0; 60 -9.1; 66 -9.2; 72 -9.3; 79 -9.5; 87 -9.8; 96 -10.1; 106 -10.1; 116 -10.2; 128 -10.5; 141 -10.6; 155 -10.7; 170 -10.3; 187 -10.3; 206 -10.3; 227 -10.1; 249 -9.8; 274 -9.5; 302 -9.1; 332 -8.7; 365 -8.2; 402 -7.8; 442 -7.2; 486 -6.9; 535 -6.5; 588 -6.1; 647 -6.0; 712 -6.1; 783 -4.4; 861 -5.2; 947 -5.4; 1042 -5.2; 1146 -4.8; 1261 -4.7; 1387 -5.0; 1526 -5.4; 1678 -5.5; 1846 -5.1; 2031 -4.2; 2234 -3.7; 2457 -2.2; 2703 -1.3; 2973 -1.7; 3270 -2.6; 3597 -3.0; 3957 -2.4; 4353 -2.2; 4788 -1.9; 5267 -0.5; 5793 -1.4; 6373 -3.5; 7010 -4.0; 7711 -5.5; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex TH900mk2 TH610Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH900mk2 TH610Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 70 Hz   | 0.45 | -3.1 dB |
| Peaking | 192 Hz  | 2.48 | 1.9 dB  |
| Peaking | 197 Hz  | 1.03 | -4.8 dB |
| Peaking | 2828 Hz | 1.6  | 3.9 dB  |
| Peaking | 5326 Hz | 2.79 | 4.7 dB  |
| Peaking | 354 Hz  | 3.57 | -0.5 dB |
| Peaking | 786 Hz  | 9.88 | 1.5 dB  |
| Peaking | 1413 Hz | 1.31 | 1.6 dB  |
| Peaking | 1660 Hz | 2.25 | -2.0 dB |
| Peaking | 8590 Hz | 3.48 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20TH900mk2%20TH610Pads/Fostex%20TH900mk2%20TH610Pads.png)