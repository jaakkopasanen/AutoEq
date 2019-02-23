# Stax SR-X Mk3 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.9; 31 -1.4; 34 -1.9; 37 -2.3; 41 -2.6; 45 -2.8; 49 -3.0; 54 -3.2; 60 -3.3; 66 -3.4; 72 -3.7; 79 -3.9; 87 -4.3; 96 -4.6; 106 -4.9; 116 -5.0; 128 -5.2; 141 -5.4; 155 -5.6; 170 -5.6; 187 -5.7; 206 -5.8; 227 -5.8; 249 -5.8; 274 -5.8; 302 -5.8; 332 -5.8; 365 -5.7; 402 -5.7; 442 -5.7; 486 -5.9; 535 -6.2; 588 -5.4; 647 -5.7; 712 -6.1; 783 -6.0; 861 -6.2; 947 -6.6; 1042 -6.6; 1146 -6.5; 1261 -6.7; 1387 -6.0; 1526 -5.9; 1678 -5.5; 1846 -4.6; 2031 -4.7; 2234 -5.2; 2457 -6.2; 2703 -7.3; 2973 -8.5; 3270 -8.9; 3597 -9.7; 3957 -10.5; 4353 -10.0; 4788 -7.3; 5267 -5.7; 5793 -6.3; 6373 -7.9; 7010 -8.9; 7711 -9.0; 8482 -9.4; 9330 -8.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.9; 20000 -13.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-X Mk3 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-X Mk3 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.44 | 4.9 dB  |
| Peaking | 25 Hz   | 0.09 | 0.8 dB  |
| Peaking | 1986 Hz | 2.97 | 2.2 dB  |
| Peaking | 3755 Hz | 2.72 | -4.1 dB |
| Peaking | 8113 Hz | 3.19 | -3.0 dB |
| Peaking | 13 Hz   | 1.38 | 0.6 dB  |
| Peaking | 500 Hz  | 1.37 | 0.5 dB  |
| Peaking | 4331 Hz | 7.68 | -1.8 dB |
| Peaking | 5295 Hz | 3.57 | 2.1 dB  |
| Peaking | 6707 Hz | 5.6  | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.0 dB |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-X%20Mk3%20Pro/Stax%20SR-X%20Mk3%20Pro.png)