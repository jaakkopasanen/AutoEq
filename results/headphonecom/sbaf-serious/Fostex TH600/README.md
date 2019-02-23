# Fostex TH600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.7; 25 -9.1; 28 -9.6; 31 -10.0; 34 -10.3; 37 -10.5; 41 -10.7; 45 -10.7; 49 -10.8; 54 -11.2; 60 -11.6; 66 -11.2; 72 -11.1; 79 -11.7; 87 -12.1; 96 -12.1; 106 -12.1; 116 -12.0; 128 -12.0; 141 -11.9; 155 -11.7; 170 -11.2; 187 -10.9; 206 -10.4; 227 -9.9; 249 -9.3; 274 -8.7; 302 -7.7; 332 -6.5; 365 -5.4; 402 -4.7; 442 -4.1; 486 -3.6; 535 -3.4; 588 -3.8; 647 -4.5; 712 -5.5; 783 -5.9; 861 -5.1; 947 -6.4; 1042 -6.6; 1146 -6.5; 1261 -6.5; 1387 -6.5; 1526 -6.9; 1678 -6.8; 1846 -6.4; 2031 -6.1; 2234 -4.9; 2457 -2.2; 2703 -0.5; 2973 -0.5; 3270 -0.6; 3597 -1.3; 3957 -3.6; 4353 -6.9; 4788 -8.7; 5267 -9.2; 5793 -9.9; 6373 -9.9; 7010 -9.7; 7711 -8.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.0; 18182 -10.3; 20000 -12.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex TH600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 1.15 | -1.5 dB |
| Peaking | 278 Hz  | 0.19 | -8.1 dB |
| Peaking | 494 Hz  | 0.66 | 10.4 dB |
| Peaking | 3112 Hz | 1.67 | 8.5 dB  |
| Peaking | 5597 Hz | 1.54 | -4.9 dB |
| Peaking | 1264 Hz | 3.28 | 0.7 dB  |
| Peaking | 2316 Hz | 2.03 | -1.2 dB |
| Peaking | 2543 Hz | 7.84 | 2.7 dB  |
| Peaking | 7385 Hz | 4.68 | -2.7 dB |
| Peaking | 8159 Hz | 2.29 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 4.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Fostex%20TH600/Fostex%20TH600.png)