# Fostex TH600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.5; 25 -9.0; 28 -9.5; 31 -9.9; 34 -10.2; 37 -10.4; 41 -10.6; 45 -10.6; 49 -10.7; 54 -11.1; 60 -11.5; 66 -11.1; 72 -10.9; 79 -11.6; 87 -11.9; 96 -12.0; 106 -12.0; 116 -11.9; 128 -11.8; 141 -11.7; 155 -11.5; 170 -11.0; 187 -10.8; 206 -10.3; 227 -9.8; 249 -9.2; 274 -8.5; 302 -7.5; 332 -6.4; 365 -5.3; 402 -4.5; 442 -4.0; 486 -3.4; 535 -3.2; 588 -3.7; 647 -4.4; 712 -5.3; 783 -5.8; 861 -5.0; 947 -6.3; 1042 -6.5; 1146 -6.3; 1261 -6.3; 1387 -6.4; 1526 -6.7; 1678 -6.7; 1846 -6.3; 2031 -6.0; 2234 -4.8; 2457 -2.0; 2703 -0.5; 2973 -0.5; 3270 -0.6; 3597 -1.2; 3957 -3.5; 4353 -6.8; 4788 -8.6; 5267 -9.0; 5793 -9.7; 6373 -9.8; 7010 -9.5; 7711 -8.7; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.9; 18182 -10.1; 20000 -11.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex TH600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 1.03 | -1.6 dB |
| Peaking | 122 Hz   | 0.39 | -5.5 dB |
| Peaking | 467 Hz   | 1.31 | 5.1 dB  |
| Peaking | 3146 Hz  | 2.07 | 7.7 dB  |
| Peaking | 5713 Hz  | 1.62 | -4.5 dB |
| Peaking | 1929 Hz  | 1.57 | -1.2 dB |
| Peaking | 2556 Hz  | 8.43 | 2.7 dB  |
| Peaking | 16091 Hz | 0.64 | 1.8 dB  |
| Peaking | 19415 Hz | 0.68 | -6.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 4.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Fostex%20TH600/Fostex%20TH600.png)