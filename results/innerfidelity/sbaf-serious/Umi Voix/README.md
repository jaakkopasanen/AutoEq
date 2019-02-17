# Umi Voix
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.1; 23 -10.2; 25 -10.2; 28 -10.3; 31 -10.4; 34 -10.4; 37 -10.5; 41 -10.5; 45 -10.6; 49 -10.7; 54 -10.8; 60 -10.8; 66 -11.0; 72 -11.2; 79 -11.4; 87 -11.6; 96 -11.7; 106 -11.8; 116 -11.7; 128 -11.7; 141 -11.6; 155 -11.5; 170 -11.3; 187 -10.9; 206 -10.6; 227 -10.0; 249 -9.5; 274 -8.8; 302 -8.0; 332 -7.3; 365 -6.4; 402 -5.6; 442 -4.5; 486 -4.0; 535 -3.8; 588 -3.2; 647 -3.4; 712 -3.8; 783 -4.2; 861 -5.0; 947 -5.9; 1042 -6.9; 1146 -7.6; 1261 -8.3; 1387 -9.0; 1526 -9.2; 1678 -8.7; 1846 -7.2; 2031 -5.2; 2234 -3.0; 2457 -0.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.2; 4353 -3.8; 4788 -1.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Umi Voix GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Umi Voix ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.5  | -3.9 dB |
| Peaking | 108 Hz  | 1.26 | -3.8 dB |
| Peaking | 188 Hz  | 2.15 | -3.1 dB |
| Peaking | 3044 Hz | 2.14 | 6.6 dB  |
| Peaking | 5601 Hz | 2.59 | 6.0 dB  |
| Peaking | 280 Hz  | 2.18 | -1.6 dB |
| Peaking | 604 Hz  | 1.08 | 3.9 dB  |
| Peaking | 1479 Hz | 1.56 | -4.2 dB |
| Peaking | 2362 Hz | 4.45 | 3.1 dB  |
| Peaking | 8268 Hz | 4.7  | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 4.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Umi%20Voix/Umi%20Voix.png)