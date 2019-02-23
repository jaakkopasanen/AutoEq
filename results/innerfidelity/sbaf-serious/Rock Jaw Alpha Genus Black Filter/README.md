# Rock Jaw Alpha Genus Black Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -3.0; 25 -3.4; 28 -4.0; 31 -4.5; 34 -4.9; 37 -5.2; 41 -5.6; 45 -6.0; 49 -6.3; 54 -6.6; 60 -7.1; 66 -7.4; 72 -7.7; 79 -8.1; 87 -8.5; 96 -9.0; 106 -9.1; 116 -9.2; 128 -9.4; 141 -9.5; 155 -9.6; 170 -9.4; 187 -9.3; 206 -9.2; 227 -8.8; 249 -8.5; 274 -8.1; 302 -7.7; 332 -7.2; 365 -6.7; 402 -6.2; 442 -5.6; 486 -5.2; 535 -4.7; 588 -3.9; 647 -3.4; 712 -3.0; 783 -2.4; 861 -2.3; 947 -2.4; 1042 -2.7; 1146 -3.2; 1261 -3.8; 1387 -4.8; 1526 -6.0; 1678 -7.0; 1846 -7.6; 2031 -8.0; 2234 -8.2; 2457 -8.1; 2703 -7.4; 2973 -5.1; 3270 -2.3; 3597 -0.5; 3957 -1.6; 4353 -4.7; 4788 -7.4; 5267 -11.1; 5793 -10.2; 6373 -4.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rock Jaw Alpha Genus Black Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rock Jaw Alpha Genus Black Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.71 | 4.5 dB  |
| Peaking | 151 Hz  | 0.52 | -3.9 dB |
| Peaking | 899 Hz  | 0.89 | 5.0 dB  |
| Peaking | 2941 Hz | 0.71 | -5.5 dB |
| Peaking | 3553 Hz | 2.92 | 10.8 dB |
| Peaking | 1318 Hz | 3.04 | 1.1 dB  |
| Peaking | 1516 Hz | 1.53 | -0.9 dB |
| Peaking | 5375 Hz | 1.3  | 2.3 dB  |
| Peaking | 5499 Hz | 4.53 | -8.1 dB |
| Peaking | 6680 Hz | 5.55 | 4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Rock%20Jaw%20Alpha%20Genus%20Black%20Filter/Rock%20Jaw%20Alpha%20Genus%20Black%20Filter.png)