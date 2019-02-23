# Fostex TH900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.2; 23 -10.4; 25 -10.6; 28 -10.7; 31 -10.8; 34 -10.8; 37 -10.8; 41 -10.8; 45 -10.7; 49 -10.1; 54 -9.7; 60 -10.8; 66 -11.3; 72 -11.5; 79 -11.5; 87 -11.3; 96 -11.5; 106 -11.5; 116 -11.4; 128 -11.5; 141 -11.5; 155 -11.2; 170 -10.8; 187 -10.7; 206 -10.3; 227 -9.9; 249 -9.5; 274 -9.0; 302 -8.4; 332 -7.7; 365 -6.8; 402 -5.9; 442 -4.7; 486 -3.0; 535 -1.0; 588 -0.5; 647 -2.3; 712 -3.4; 783 -3.4; 861 -4.9; 947 -5.3; 1042 -5.5; 1146 -5.5; 1261 -5.3; 1387 -5.2; 1526 -5.7; 1678 -6.3; 1846 -6.4; 2031 -4.0; 2234 -1.8; 2457 -3.1; 2703 -3.3; 2973 -4.3; 3270 -4.0; 3597 -3.4; 3957 -3.4; 4353 -5.6; 4788 -7.1; 5267 -7.6; 5793 -8.8; 6373 -7.7; 7010 -7.7; 7711 -7.4; 8482 -6.2; 9330 -6.2; 10263 -6.3; 11289 -7.4; 12418 -6.3; 13660 -6.3; 15026 -6.4; 16529 -8.0; 18182 -8.3; 20000 -14.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex TH900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.92 | -3.3 dB |
| Peaking | 122 Hz   | 0.4  | -5.2 dB |
| Peaking | 567 Hz   | 1.84 | 6.8 dB  |
| Peaking | 2350 Hz  | 3.75 | 4.2 dB  |
| Peaking | 3656 Hz  | 5.12 | 3.0 dB  |
| Peaking | 1363 Hz  | 4.78 | 0.7 dB  |
| Peaking | 1768 Hz  | 6.14 | -1.6 dB |
| Peaking | 4760 Hz  | 0.86 | 1.5 dB  |
| Peaking | 5769 Hz  | 1.79 | -3.7 dB |
| Peaking | 20018 Hz | 1.09 | -8.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | 5.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Fostex%20TH900/Fostex%20TH900.png)