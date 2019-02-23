# Stax SR-L300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.9; 45 -2.1; 49 -3.1; 54 -3.9; 60 -4.7; 66 -5.2; 72 -5.6; 79 -5.9; 87 -6.3; 96 -6.5; 106 -6.8; 116 -6.6; 128 -6.6; 141 -6.5; 155 -6.4; 170 -6.4; 187 -6.3; 206 -6.2; 227 -6.0; 249 -6.0; 274 -5.8; 302 -5.8; 332 -5.7; 365 -5.7; 402 -5.7; 442 -5.6; 486 -5.8; 535 -6.0; 588 -5.6; 647 -5.8; 712 -6.2; 783 -6.3; 861 -6.9; 947 -7.5; 1042 -7.1; 1146 -7.5; 1261 -8.5; 1387 -8.5; 1526 -7.3; 1678 -5.6; 1846 -4.5; 2031 -4.8; 2234 -5.8; 2457 -6.5; 2703 -6.8; 2973 -5.4; 3270 -4.8; 3597 -4.7; 3957 -5.3; 4353 -6.7; 4788 -7.1; 5267 -5.7; 5793 -6.8; 6373 -7.2; 7010 -6.9; 7711 -7.6; 8482 -10.5; 9330 -10.3; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.1; 20000 -11.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-L300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-L300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 1.06 | 6.9 dB  |
| Peaking | 1353 Hz | 0.4  | 2.8 dB  |
| Peaking | 1433 Hz | 0.96 | -5.4 dB |
| Peaking | 1790 Hz | 3.35 | 3.8 dB  |
| Peaking | 8733 Hz | 4.64 | -5.1 dB |
| Peaking | 41 Hz   | 3.88 | 1.2 dB  |
| Peaking | 101 Hz  | 1.72 | -0.8 dB |
| Peaking | 2670 Hz | 6.58 | -1.5 dB |
| Peaking | 3527 Hz | 2.28 | 1.8 dB  |
| Peaking | 4461 Hz | 3.85 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-L300/Stax%20SR-L300.png)