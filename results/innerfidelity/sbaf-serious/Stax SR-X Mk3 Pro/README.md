# Stax SR-X Mk3 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.3; 34 -1.7; 37 -2.1; 41 -2.4; 45 -2.7; 49 -2.8; 54 -3.0; 60 -3.1; 66 -3.3; 72 -3.5; 79 -3.8; 87 -4.1; 96 -4.4; 106 -4.7; 116 -4.8; 128 -5.0; 141 -5.2; 155 -5.4; 170 -5.5; 187 -5.5; 206 -5.7; 227 -5.6; 249 -5.6; 274 -5.6; 302 -5.6; 332 -5.6; 365 -5.5; 402 -5.5; 442 -5.5; 486 -5.7; 535 -6.1; 588 -5.3; 647 -5.6; 712 -5.9; 783 -5.8; 861 -6.1; 947 -6.5; 1042 -6.4; 1146 -6.3; 1261 -6.5; 1387 -5.9; 1526 -5.7; 1678 -5.3; 1846 -4.4; 2031 -4.5; 2234 -5.0; 2457 -6.0; 2703 -7.2; 2973 -8.3; 3270 -8.8; 3597 -9.6; 3957 -10.3; 4353 -9.8; 4788 -7.1; 5267 -5.5; 5793 -6.1; 6373 -7.7; 7010 -8.8; 7711 -8.8; 8482 -9.2; 9330 -8.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.8; 20000 -12.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-X Mk3 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-X Mk3 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.27 | 5.6 dB  |
| Peaking | 54 Hz   | 0.06 | 0.8 dB  |
| Peaking | 1974 Hz | 3.28 | 2.4 dB  |
| Peaking | 3781 Hz | 2.91 | -4.0 dB |
| Peaking | 8136 Hz | 3.35 | -2.9 dB |
| Peaking | 2377 Hz | 5.48 | 0.2 dB  |
| Peaking | 2987 Hz | 5.62 | -1.4 dB |
| Peaking | 4353 Hz | 5.32 | -3.1 dB |
| Peaking | 5160 Hz | 1.59 | 2.9 dB  |
| Peaking | 6663 Hz | 3.49 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-X%20Mk3%20Pro/Stax%20SR-X%20Mk3%20Pro.png)