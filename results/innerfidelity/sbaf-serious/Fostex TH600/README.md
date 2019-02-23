# Fostex TH600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.8; 25 -10.1; 28 -10.4; 31 -10.7; 34 -10.8; 37 -11.0; 41 -11.1; 45 -11.2; 49 -11.2; 54 -11.0; 60 -10.7; 66 -11.0; 72 -11.4; 79 -11.7; 87 -11.8; 96 -12.0; 106 -11.9; 116 -11.8; 128 -11.8; 141 -11.7; 155 -11.5; 170 -10.9; 187 -10.7; 206 -10.3; 227 -9.7; 249 -9.2; 274 -8.6; 302 -7.8; 332 -7.0; 365 -6.0; 402 -4.8; 442 -3.3; 486 -2.5; 535 -2.7; 588 -3.1; 647 -4.2; 712 -5.3; 783 -5.1; 861 -5.1; 947 -6.2; 1042 -6.2; 1146 -6.0; 1261 -5.6; 1387 -5.6; 1526 -5.7; 1678 -5.8; 1846 -5.6; 2031 -5.2; 2234 -4.1; 2457 -1.2; 2703 -2.5; 2973 -0.5; 3270 -0.7; 3597 -1.4; 3957 -1.8; 4353 -5.4; 4788 -7.7; 5267 -7.3; 5793 -8.6; 6373 -8.4; 7010 -8.4; 7711 -6.6; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -8.7; 20000 -12.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex TH600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.73 | -3.2 dB |
| Peaking | 124 Hz  | 0.47 | -5.4 dB |
| Peaking | 495 Hz  | 1.72 | 5.2 dB  |
| Peaking | 3069 Hz | 2.44 | 6.2 dB  |
| Peaking | 2189 Hz | 3.91 | -0.9 dB |
| Peaking | 2447 Hz | 5.7  | 3.4 dB  |
| Peaking | 2745 Hz | 7.64 | -1.9 dB |
| Peaking | 3861 Hz | 7.07 | 3.3 dB  |
| Peaking | 5693 Hz | 1.77 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 4.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20TH600/Fostex%20TH600.png)