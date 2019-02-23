# Stax SR-009 SZ9-1278
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.9; 45 -1.7; 49 -2.4; 54 -2.5; 60 -4.1; 66 -4.6; 72 -4.3; 79 -4.2; 87 -4.3; 96 -4.6; 106 -4.8; 116 -4.9; 128 -5.2; 141 -5.4; 155 -5.6; 170 -5.8; 187 -5.9; 206 -6.0; 227 -6.0; 249 -6.2; 274 -6.1; 302 -6.2; 332 -6.3; 365 -6.3; 402 -6.5; 442 -6.6; 486 -7.0; 535 -7.1; 588 -7.0; 647 -7.2; 712 -7.6; 783 -7.5; 861 -7.7; 947 -8.5; 1042 -9.1; 1146 -9.3; 1261 -9.3; 1387 -9.3; 1526 -9.2; 1678 -9.6; 1846 -7.9; 2031 -6.3; 2234 -6.0; 2457 -5.0; 2703 -5.0; 2973 -5.7; 3270 -5.8; 3597 -5.1; 3957 -6.4; 4353 -7.8; 4788 -9.4; 5267 -6.5; 5793 -0.6; 6373 -3.4; 7010 -6.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-009 SZ9-1278 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-009 SZ9-1278 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.16 | 1.4 dB  |
| Peaking | 28 Hz   | 0.77 | 5.0 dB  |
| Peaking | 1225 Hz | 1.69 | -3.3 dB |
| Peaking | 4897 Hz | 6.42 | -4.5 dB |
| Peaking | 5830 Hz | 5.34 | 7.0 dB  |
| Peaking | 655 Hz  | 1.59 | -0.4 dB |
| Peaking | 1638 Hz | 1.65 | 1.0 dB  |
| Peaking | 1665 Hz | 4.26 | -2.9 dB |
| Peaking | 2572 Hz | 2.12 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.9 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-009%20SZ9-1278/Stax%20SR-009%20SZ9-1278.png)