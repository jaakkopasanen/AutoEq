# Stax SR-1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -1.0; 96 -3.2; 106 -5.1; 116 -6.0; 128 -6.6; 141 -6.9; 155 -6.9; 170 -7.3; 187 -7.4; 206 -7.0; 227 -6.7; 249 -6.3; 274 -6.0; 302 -5.8; 332 -5.5; 365 -5.4; 402 -5.4; 442 -5.0; 486 -5.1; 535 -5.1; 588 -4.8; 647 -4.8; 712 -4.9; 783 -5.1; 861 -5.6; 947 -5.9; 1042 -6.3; 1146 -5.6; 1261 -4.9; 1387 -5.0; 1526 -6.0; 1678 -6.2; 1846 -5.8; 2031 -5.1; 2234 -4.9; 2457 -4.9; 2703 -4.9; 2973 -4.1; 3270 -2.8; 3597 -1.1; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -10.3; 10263 -8.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.66 | 7.1 dB  |
| Peaking | 616 Hz  | 1.48 | 1.7 dB  |
| Peaking | 4174 Hz | 1.53 | 5.9 dB  |
| Peaking | 6019 Hz | 3.38 | 4.1 dB  |
| Peaking | 9579 Hz | 5.04 | -5.1 dB |
| Peaking | 18 Hz   | 1.32 | 2.9 dB  |
| Peaking | 38 Hz   | 1.76 | -1.7 dB |
| Peaking | 82 Hz   | 2.42 | 3.6 dB  |
| Peaking | 133 Hz  | 1.3  | -2.5 dB |
| Peaking | 1304 Hz | 7.13 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 6.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-1/Stax%20SR-1.png)