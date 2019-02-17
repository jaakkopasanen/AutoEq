# Massdrop x Fostex TH-X00 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -5.0; 25 -5.7; 28 -6.5; 31 -7.0; 34 -7.3; 37 -7.5; 41 -7.6; 45 -7.6; 49 -7.7; 54 -7.7; 60 -7.7; 66 -7.8; 72 -8.1; 79 -8.2; 87 -8.5; 96 -8.7; 106 -8.7; 116 -8.7; 128 -8.8; 141 -8.8; 155 -8.7; 170 -8.5; 187 -8.4; 206 -8.0; 227 -7.2; 249 -7.0; 274 -6.7; 302 -6.5; 332 -6.2; 365 -5.8; 402 -5.5; 442 -5.0; 486 -5.1; 535 -5.1; 588 -5.0; 647 -3.8; 712 -4.0; 783 -4.6; 861 -4.9; 947 -5.8; 1042 -6.1; 1146 -6.1; 1261 -6.1; 1387 -6.6; 1526 -7.1; 1678 -7.2; 1846 -7.0; 2031 -6.5; 2234 -5.8; 2457 -4.8; 2703 -4.4; 2973 -4.0; 3270 -2.8; 3597 -0.5; 3957 -2.2; 4353 -3.4; 4788 -3.7; 5267 -5.0; 5793 -5.6; 6373 -4.4; 7010 -4.0; 7711 -5.8; 8482 -6.0; 9330 -6.1; 10263 -7.6; 11289 -7.2; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Fostex TH-X00 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Fostex TH-X00 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 1.65 | 3.6 dB  |
| Peaking | 44 Hz    | 0.45 | -1.7 dB |
| Peaking | 140 Hz   | 1.1  | -2.3 dB |
| Peaking | 656 Hz   | 2.29 | 2.3 dB  |
| Peaking | 3672 Hz  | 2.74 | 5.3 dB  |
| Peaking | 426 Hz   | 4.22 | 0.8 dB  |
| Peaking | 1699 Hz  | 2.27 | -1.5 dB |
| Peaking | 2560 Hz  | 7.17 | 0.9 dB  |
| Peaking | 6804 Hz  | 7.07 | 2.2 dB  |
| Peaking | 10649 Hz | 5.16 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20Fostex%20TH-X00%20sample%201/Massdrop%20x%20Fostex%20TH-X00%20sample%201.png)