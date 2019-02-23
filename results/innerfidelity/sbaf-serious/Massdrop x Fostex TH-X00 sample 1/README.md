# Massdrop x Fostex TH-X00 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -5.4; 25 -6.1; 28 -6.9; 31 -7.4; 34 -7.7; 37 -7.8; 41 -7.9; 45 -8.0; 49 -8.0; 54 -8.0; 60 -8.1; 66 -8.2; 72 -8.4; 79 -8.6; 87 -8.8; 96 -9.0; 106 -9.1; 116 -9.1; 128 -9.1; 141 -9.2; 155 -9.1; 170 -8.9; 187 -8.8; 206 -8.4; 227 -7.5; 249 -7.3; 274 -7.1; 302 -6.8; 332 -6.5; 365 -6.2; 402 -5.9; 442 -5.4; 486 -5.4; 535 -5.5; 588 -5.4; 647 -4.2; 712 -4.3; 783 -4.9; 861 -5.3; 947 -6.1; 1042 -6.5; 1146 -6.5; 1261 -6.5; 1387 -6.9; 1526 -7.5; 1678 -7.6; 1846 -7.3; 2031 -6.8; 2234 -6.2; 2457 -5.2; 2703 -4.7; 2973 -4.4; 3270 -3.2; 3597 -0.5; 3957 -2.6; 4353 -3.7; 4788 -4.1; 5267 -5.4; 5793 -6.0; 6373 -4.8; 7010 -4.2; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -8.0; 11289 -7.5; 12418 -6.1; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Fostex TH-X00 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Fostex TH-X00 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.69 | 3.6 dB  |
| Peaking | 43 Hz    | 0.39 | -2.1 dB |
| Peaking | 143 Hz   | 1.01 | -2.5 dB |
| Peaking | 671 Hz   | 3.82 | 2.1 dB  |
| Peaking | 3628 Hz  | 3.72 | 5.4 dB  |
| Peaking | 446 Hz   | 4.15 | 0.8 dB  |
| Peaking | 1692 Hz  | 1.98 | -1.8 dB |
| Peaking | 2596 Hz  | 5.42 | 0.9 dB  |
| Peaking | 6821 Hz  | 6.64 | 2.0 dB  |
| Peaking | 10613 Hz | 4.82 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20Fostex%20TH-X00%20sample%201/Massdrop%20x%20Fostex%20TH-X00%20sample%201.png)