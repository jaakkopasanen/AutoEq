# ViSang VS-K1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -5.0; 25 -5.4; 28 -5.9; 31 -6.3; 34 -6.6; 37 -6.9; 41 -7.2; 45 -7.5; 49 -7.8; 54 -8.1; 60 -8.5; 66 -8.8; 72 -9.1; 79 -9.5; 87 -9.9; 96 -10.2; 106 -10.4; 116 -10.5; 128 -10.6; 141 -10.7; 155 -10.8; 170 -10.7; 187 -10.6; 206 -10.5; 227 -10.2; 249 -10.0; 274 -9.7; 302 -9.4; 332 -9.1; 365 -8.8; 402 -8.5; 442 -8.1; 486 -8.0; 535 -7.7; 588 -7.3; 647 -7.2; 712 -7.3; 783 -7.2; 861 -7.7; 947 -8.2; 1042 -8.8; 1146 -8.9; 1261 -9.3; 1387 -10.3; 1526 -9.2; 1678 -10.1; 1846 -11.0; 2031 -9.9; 2234 -8.1; 2457 -5.2; 2703 -2.8; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.4; 5267 -1.2; 5793 -0.9; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`ViSang VS-K1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ViSang VS-K1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.24 | 2.5 dB  |
| Peaking | 144 Hz  | 0.52 | -4.4 dB |
| Peaking | 1911 Hz | 1.17 | -7.4 dB |
| Peaking | 3195 Hz | 1.18 | 9.2 dB  |
| Peaking | 5865 Hz | 3.26 | 4.1 dB  |
| Peaking | 690 Hz  | 3.27 | 0.6 dB  |
| Peaking | 1473 Hz | 2.35 | -1.1 dB |
| Peaking | 1566 Hz | 8.35 | 2.6 dB  |
| Peaking | 6566 Hz | 7.99 | 1.8 dB  |
| Peaking | 7986 Hz | 2.39 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/ViSang%20VS-K1/ViSang%20VS-K1.png)