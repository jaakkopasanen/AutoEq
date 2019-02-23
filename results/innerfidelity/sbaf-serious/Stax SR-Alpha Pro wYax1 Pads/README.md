# Stax SR-Alpha Pro wYax1 Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.8; 28 -1.0; 31 -1.2; 34 -1.3; 37 -1.4; 41 -1.4; 45 -1.5; 49 -1.6; 54 -1.7; 60 -2.0; 66 -2.5; 72 -3.2; 79 -4.0; 87 -4.1; 96 -4.6; 106 -5.2; 116 -5.3; 128 -5.4; 141 -5.5; 155 -5.6; 170 -5.8; 187 -5.8; 206 -5.9; 227 -5.9; 249 -6.0; 274 -6.1; 302 -6.1; 332 -6.0; 365 -6.0; 402 -6.0; 442 -6.0; 486 -6.2; 535 -6.2; 588 -6.0; 647 -6.2; 712 -6.4; 783 -6.3; 861 -6.6; 947 -6.8; 1042 -6.9; 1146 -7.4; 1261 -8.0; 1387 -8.7; 1526 -9.6; 1678 -10.4; 1846 -10.9; 2031 -10.6; 2234 -10.3; 2457 -8.5; 2703 -6.8; 2973 -5.4; 3270 -5.1; 3597 -5.1; 3957 -4.0; 4353 -4.4; 4788 -5.0; 5267 -5.8; 5793 -5.6; 6373 -4.7; 7010 -4.4; 7711 -6.2; 8482 -7.1; 9330 -9.3; 10263 -7.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -10.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-Alpha Pro wYax1 Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-Alpha Pro wYax1 Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.92 | 4.9 dB   |
| Peaking | 50 Hz    | 0.82 | 3.9 dB   |
| Peaking | 1938 Hz  | 1.12 | -10.0 dB |
| Peaking | 2454 Hz  | 0.52 | 5.8 dB   |
| Peaking | 9369 Hz  | 4.82 | -3.8 dB  |
| Peaking | 1278 Hz  | 3.95 | -0.2 dB  |
| Peaking | 5416 Hz  | 3.78 | -3.1 dB  |
| Peaking | 5633 Hz  | 1.99 | 2.0 dB   |
| Peaking | 19938 Hz | 2.9  | -4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 3.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-Alpha%20Pro%20wYax1%20Pads/Stax%20SR-Alpha%20Pro%20wYax1%20Pads.png)