# Stax SR-207 SB2217
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.3; 25 -1.9; 28 -2.6; 31 -2.9; 34 -3.1; 37 -3.0; 41 -2.9; 45 -2.8; 49 -2.7; 54 -2.6; 60 -2.5; 66 -2.6; 72 -2.8; 79 -3.1; 87 -3.5; 96 -3.7; 106 -4.0; 116 -4.1; 128 -4.4; 141 -4.5; 155 -4.5; 170 -4.6; 187 -4.7; 206 -4.8; 227 -4.7; 249 -4.8; 274 -4.7; 302 -4.8; 332 -4.9; 365 -4.9; 402 -4.9; 442 -4.8; 486 -5.0; 535 -5.1; 588 -4.9; 647 -5.0; 712 -5.4; 783 -5.5; 861 -5.9; 947 -6.4; 1042 -6.8; 1146 -7.4; 1261 -8.1; 1387 -9.0; 1526 -9.8; 1678 -10.2; 1846 -9.3; 2031 -6.9; 2234 -5.0; 2457 -3.7; 2703 -4.6; 2973 -5.0; 3270 -5.6; 3597 -5.1; 3957 -4.2; 4353 -5.3; 4788 -5.8; 5267 -5.1; 5793 -6.7; 6373 -5.1; 7010 -4.3; 7711 -6.4; 8482 -7.9; 9330 -10.1; 10263 -7.6; 11289 -6.7; 12418 -6.7; 13660 -6.7; 15026 -6.7; 16529 -6.7; 18182 -7.6; 20000 -9.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-207 SB2217 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-207 SB2217 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.16 | 4.7 dB  |
| Peaking | 250 Hz  | 0.18 | 1.6 dB  |
| Peaking | 1646 Hz | 1.42 | -9.1 dB |
| Peaking | 2125 Hz | 0.77 | 5.7 dB  |
| Peaking | 9294 Hz | 6.47 | -4.2 dB |
| Peaking | 36 Hz   | 2.72 | -0.9 dB |
| Peaking | 62 Hz   | 3.05 | 0.6 dB  |
| Peaking | 2506 Hz | 5.19 | 2.4 dB  |
| Peaking | 2790 Hz | 2.86 | -1.7 dB |
| Peaking | 6806 Hz | 9.83 | 2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | 1.6 dB  |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-207%20SB2217/Stax%20SR-207%20SB2217.png)