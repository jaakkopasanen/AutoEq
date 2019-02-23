# Stax SR-Lambda Signature
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -1.0; 34 -2.7; 37 -4.5; 41 -6.5; 45 -7.9; 49 -8.6; 54 -8.4; 60 -8.1; 66 -7.1; 72 -6.5; 79 -6.4; 87 -6.3; 96 -6.2; 106 -6.0; 116 -5.8; 128 -5.8; 141 -5.7; 155 -5.7; 170 -5.7; 187 -5.6; 206 -5.6; 227 -5.5; 249 -5.5; 274 -5.4; 302 -5.4; 332 -5.4; 365 -5.5; 402 -5.4; 442 -5.1; 486 -5.1; 535 -5.3; 588 -5.1; 647 -5.4; 712 -5.6; 783 -5.7; 861 -6.1; 947 -6.5; 1042 -7.1; 1146 -7.5; 1261 -8.5; 1387 -9.8; 1526 -10.6; 1678 -11.1; 1846 -11.2; 2031 -9.0; 2234 -5.9; 2457 -2.9; 2703 -4.3; 2973 -5.5; 3270 -6.1; 3597 -6.3; 3957 -6.9; 4353 -7.5; 4788 -6.6; 5267 -4.9; 5793 -4.1; 6373 -6.6; 7010 -7.7; 7711 -6.9; 8482 -9.4; 9330 -10.2; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.6; 20000 -10.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-Lambda Signature GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-Lambda Signature ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 35 Hz   | 0.22 | 26.6 dB  |
| Peaking | 47 Hz   | 0.36 | -26.6 dB |
| Peaking | 1730 Hz | 2.01 | -6.0 dB  |
| Peaking | 2473 Hz | 3.89 | 5.5 dB   |
| Peaking | 9024 Hz | 5.71 | -4.4 dB  |
| Peaking | 71 Hz   | 5.28 | 0.8 dB   |
| Peaking | 618 Hz  | 2.12 | 0.7 dB   |
| Peaking | 4402 Hz | 5.58 | -1.3 dB  |
| Peaking | 5674 Hz | 4.36 | 3.0 dB   |
| Peaking | 6720 Hz | 6.05 | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | 1.2 dB  |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-Lambda%20Signature/Stax%20SR-Lambda%20Signature.png)