# Dunu Titan 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.5; 25 -2.6; 28 -2.8; 31 -2.9; 34 -3.0; 37 -3.1; 41 -3.2; 45 -3.3; 49 -3.5; 54 -3.7; 60 -4.0; 66 -4.3; 72 -4.6; 79 -5.0; 87 -5.3; 96 -5.7; 106 -5.9; 116 -6.1; 128 -6.3; 141 -6.5; 155 -6.6; 170 -6.6; 187 -6.5; 206 -6.4; 227 -6.2; 249 -6.0; 274 -5.7; 302 -5.4; 332 -5.1; 365 -4.1; 402 -3.8; 442 -3.6; 486 -3.1; 535 -2.5; 588 -1.6; 647 -1.2; 712 -1.0; 783 -0.6; 861 -0.5; 947 -0.5; 1042 -0.8; 1146 -1.0; 1261 -1.5; 1387 -2.3; 1526 -3.4; 1678 -4.6; 1846 -5.4; 2031 -5.4; 2234 -5.0; 2457 -4.0; 2703 -3.2; 2973 -2.2; 3270 -1.3; 3597 -1.4; 3957 -2.4; 4353 -4.5; 4788 -5.2; 5267 -4.3; 5793 -3.6; 6373 -2.5; 7010 -1.8; 7711 -3.2; 8482 -3.5; 9330 -3.5; 10263 -3.5; 11289 -3.5; 12418 -3.5; 13660 -3.5; 15026 -3.5; 16529 -3.5; 18182 -3.5; 20000 -3.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu Titan 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu Titan 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 184 Hz  | 0.63 | -3.5 dB |
| Peaking | 948 Hz  | 0.74 | 4.0 dB  |
| Peaking | 1983 Hz | 1.43 | -4.7 dB |
| Peaking | 3836 Hz | 1.1  | 4.8 dB  |
| Peaking | 4666 Hz | 2.66 | -5.7 dB |
| Peaking | 21 Hz   | 1.38 | 1.1 dB  |
| Peaking | 37 Hz   | 1.51 | 0.5 dB  |
| Peaking | 6909 Hz | 4.66 | 1.7 dB  |
| Peaking | 7812 Hz | 1.55 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20Titan%201/Dunu%20Titan%201.png)