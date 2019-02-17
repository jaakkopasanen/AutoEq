# Stax SR-L300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -1.2; 49 -2.2; 54 -3.0; 60 -3.7; 66 -4.3; 72 -4.7; 79 -5.0; 87 -5.4; 96 -5.6; 106 -5.9; 116 -5.6; 128 -5.7; 141 -5.6; 155 -5.5; 170 -5.4; 187 -5.4; 206 -5.3; 227 -5.1; 249 -5.1; 274 -4.9; 302 -4.9; 332 -4.8; 365 -4.8; 402 -4.7; 442 -4.7; 486 -4.9; 535 -5.0; 588 -4.6; 647 -4.8; 712 -5.2; 783 -5.4; 861 -6.0; 947 -6.6; 1042 -6.1; 1146 -6.5; 1261 -7.6; 1387 -7.5; 1526 -6.4; 1678 -4.7; 1846 -3.6; 2031 -3.8; 2234 -4.9; 2457 -5.6; 2703 -5.9; 2973 -4.5; 3270 -3.8; 3597 -3.7; 3957 -4.4; 4353 -5.8; 4788 -6.1; 5267 -4.8; 5793 -5.9; 6373 -6.3; 7010 -6.0; 7711 -6.7; 8482 -9.5; 9330 -9.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.6; 20000 -10.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-L300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-L300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.78 | 6.6 dB  |
| Peaking | 384 Hz  | 0.85 | 1.8 dB  |
| Peaking | 3164 Hz | 1.02 | 2.1 dB  |
| Peaking | 8841 Hz | 1.9  | 1.5 dB  |
| Peaking | 8864 Hz | 4.41 | -5.7 dB |
| Peaking | 636 Hz  | 4.99 | 0.8 dB  |
| Peaking | 1350 Hz | 3.66 | -2.3 dB |
| Peaking | 1910 Hz | 2.55 | 3.6 dB  |
| Peaking | 2644 Hz | 1.34 | -2.5 dB |
| Peaking | 3365 Hz | 3.42 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.0 dB  |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-L300/Stax%20SR-L300.png)