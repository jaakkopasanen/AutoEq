# Dunu DN2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.9; 23 -10.8; 25 -10.7; 28 -10.6; 31 -10.4; 34 -10.2; 37 -10.1; 41 -9.9; 45 -9.7; 49 -9.6; 54 -9.5; 60 -9.4; 66 -9.3; 72 -9.3; 79 -9.4; 87 -9.5; 96 -9.7; 106 -9.7; 116 -9.6; 128 -9.7; 141 -9.8; 155 -9.8; 170 -9.8; 187 -9.8; 206 -9.8; 227 -9.6; 249 -9.5; 274 -9.3; 302 -9.2; 332 -9.0; 365 -8.9; 402 -8.7; 442 -8.4; 486 -8.2; 535 -7.9; 588 -7.4; 647 -7.2; 712 -7.1; 783 -6.6; 861 -6.6; 947 -6.6; 1042 -6.5; 1146 -6.4; 1261 -6.3; 1387 -6.4; 1526 -6.3; 1678 -6.1; 1846 -5.2; 2031 -4.2; 2234 -3.4; 2457 -2.6; 2703 -2.5; 2973 -1.2; 3270 -0.5; 3597 -0.5; 3957 -2.2; 4353 -6.6; 4788 -9.0; 5267 -6.0; 5793 -2.9; 6373 -2.4; 7010 -4.0; 7711 -7.6; 8482 -11.9; 9330 -12.7; 10263 -9.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DN2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.29 | -4.5 dB |
| Peaking | 191 Hz  | 0.49 | -3.1 dB |
| Peaking | 3092 Hz | 2.01 | 6.3 dB  |
| Peaking | 6476 Hz | 4.95 | 5.1 dB  |
| Peaking | 8961 Hz | 3.62 | -7.5 dB |
| Peaking | 1613 Hz | 4.97 | -0.3 dB |
| Peaking | 2142 Hz | 5.21 | 1.3 dB  |
| Peaking | 3806 Hz | 6.68 | 3.3 dB  |
| Peaking | 4734 Hz | 3.88 | -4.8 dB |
| Peaking | 5653 Hz | 5.76 | 2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.2 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20DN2000/Dunu%20DN2000.png)