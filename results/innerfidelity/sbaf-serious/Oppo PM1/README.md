# Oppo PM1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.6; 25 -3.0; 28 -3.5; 31 -3.8; 34 -4.1; 37 -4.3; 41 -4.4; 45 -4.5; 49 -4.4; 54 -4.1; 60 -4.8; 66 -5.5; 72 -6.0; 79 -6.4; 87 -6.7; 96 -7.3; 106 -7.5; 116 -7.7; 128 -8.0; 141 -8.4; 155 -8.6; 170 -8.7; 187 -8.8; 206 -9.0; 227 -8.8; 249 -9.1; 274 -9.4; 302 -9.6; 332 -9.5; 365 -7.8; 402 -6.6; 442 -7.3; 486 -8.2; 535 -8.6; 588 -8.6; 647 -9.1; 712 -9.6; 783 -9.7; 861 -10.0; 947 -7.5; 1042 -7.4; 1146 -7.5; 1261 -7.6; 1387 -8.2; 1526 -8.3; 1678 -8.2; 1846 -7.4; 2031 -6.7; 2234 -6.1; 2457 -5.1; 2703 -4.8; 2973 -3.9; 3270 -3.6; 3597 -3.4; 3957 -2.5; 4353 -2.7; 4788 -2.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.8; 9330 -7.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.22 | 4.3 dB  |
| Peaking | 202 Hz  | 0.66 | -2.9 dB |
| Peaking | 763 Hz  | 2.48 | -3.1 dB |
| Peaking | 1567 Hz | 3.48 | -2.1 dB |
| Peaking | 5064 Hz | 1.43 | 5.9 dB  |
| Peaking | 319 Hz  | 4.75 | -1.3 dB |
| Peaking | 399 Hz  | 6.68 | 1.9 dB  |
| Peaking | 3138 Hz | 2.35 | 1.7 dB  |
| Peaking | 6281 Hz | 2.78 | 6.2 dB  |
| Peaking | 6635 Hz | 1.14 | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM1/Oppo%20PM1.png)