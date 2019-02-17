# Stax SR-Alpha Pro wYax1 Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -0.7; 34 -0.9; 37 -0.9; 41 -1.0; 45 -1.1; 49 -1.1; 54 -1.3; 60 -1.6; 66 -2.0; 72 -2.8; 79 -3.6; 87 -3.7; 96 -4.2; 106 -4.7; 116 -4.8; 128 -5.0; 141 -5.1; 155 -5.2; 170 -5.3; 187 -5.4; 206 -5.5; 227 -5.5; 249 -5.6; 274 -5.6; 302 -5.6; 332 -5.5; 365 -5.6; 402 -5.6; 442 -5.6; 486 -5.7; 535 -5.7; 588 -5.6; 647 -5.7; 712 -5.9; 783 -5.9; 861 -6.1; 947 -6.4; 1042 -6.4; 1146 -7.0; 1261 -7.5; 1387 -8.3; 1526 -9.1; 1678 -9.9; 1846 -10.4; 2031 -10.1; 2234 -9.9; 2457 -8.1; 2703 -6.4; 2973 -5.0; 3270 -4.7; 3597 -4.7; 3957 -3.6; 4353 -3.9; 4788 -4.5; 5267 -5.4; 5793 -5.2; 6373 -4.3; 7010 -4.3; 7711 -6.2; 8482 -6.8; 9330 -8.9; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -10.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-Alpha Pro wYax1 Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-Alpha Pro wYax1 Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.7  | 5.3 dB  |
| Peaking | 54 Hz    | 0.99 | 3.4 dB  |
| Peaking | 578 Hz   | 0.28 | 1.0 dB  |
| Peaking | 1951 Hz  | 1.41 | -5.9 dB |
| Peaking | 3570 Hz  | 1.06 | 3.5 dB  |
| Peaking | 6743 Hz  | 6.86 | 2.2 dB  |
| Peaking | 9468 Hz  | 4.16 | -3.1 dB |
| Peaking | 10429 Hz | 5.13 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 3.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-Alpha%20Pro%20wYax1%20Pads/Stax%20SR-Alpha%20Pro%20wYax1%20Pads.png)