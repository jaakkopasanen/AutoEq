# Fostex TH600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.7; 25 -10.0; 28 -10.3; 31 -10.5; 34 -10.7; 37 -10.9; 41 -11.0; 45 -11.1; 49 -11.1; 54 -10.9; 60 -10.6; 66 -10.9; 72 -11.3; 79 -11.6; 87 -11.7; 96 -11.9; 106 -11.8; 116 -11.7; 128 -11.7; 141 -11.6; 155 -11.4; 170 -10.8; 187 -10.6; 206 -10.2; 227 -9.6; 249 -9.1; 274 -8.5; 302 -7.7; 332 -6.9; 365 -5.9; 402 -4.7; 442 -3.2; 486 -2.4; 535 -2.6; 588 -3.0; 647 -4.1; 712 -5.2; 783 -5.0; 861 -5.0; 947 -6.1; 1042 -6.1; 1146 -5.8; 1261 -5.5; 1387 -5.5; 1526 -5.6; 1678 -5.7; 1846 -5.5; 2031 -5.1; 2234 -4.0; 2457 -1.1; 2703 -2.4; 2973 -0.5; 3270 -0.6; 3597 -1.3; 3957 -1.7; 4353 -5.3; 4788 -7.6; 5267 -7.2; 5793 -8.5; 6373 -8.3; 7010 -8.3; 7711 -6.5; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -8.6; 20000 -12.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex TH600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.75 | -3.1 dB |
| Peaking | 125 Hz  | 0.47 | -5.4 dB |
| Peaking | 496 Hz  | 1.68 | 5.2 dB  |
| Peaking | 3067 Hz | 2.38 | 6.3 dB  |
| Peaking | 2476 Hz | 7.69 | 3.8 dB  |
| Peaking | 2659 Hz | 4.39 | -1.8 dB |
| Peaking | 3852 Hz | 6.58 | 3.4 dB  |
| Peaking | 5672 Hz | 1.75 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 4.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20TH600/Fostex%20TH600.png)