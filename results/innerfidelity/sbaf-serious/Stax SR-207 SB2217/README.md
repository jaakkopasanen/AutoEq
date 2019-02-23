# Stax SR-207 SB2217
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.3; 25 -1.9; 28 -2.5; 31 -2.9; 34 -3.0; 37 -3.0; 41 -2.8; 45 -2.7; 49 -2.6; 54 -2.5; 60 -2.4; 66 -2.6; 72 -2.8; 79 -3.1; 87 -3.4; 96 -3.7; 106 -3.9; 116 -4.1; 128 -4.3; 141 -4.4; 155 -4.4; 170 -4.5; 187 -4.6; 206 -4.7; 227 -4.7; 249 -4.7; 274 -4.7; 302 -4.7; 332 -4.9; 365 -4.8; 402 -4.9; 442 -4.8; 486 -5.0; 535 -5.0; 588 -4.8; 647 -5.0; 712 -5.3; 783 -5.4; 861 -5.8; 947 -6.3; 1042 -6.8; 1146 -7.4; 1261 -8.0; 1387 -8.9; 1526 -9.7; 1678 -10.1; 1846 -9.2; 2031 -6.8; 2234 -4.9; 2457 -3.6; 2703 -4.5; 2973 -4.9; 3270 -5.5; 3597 -5.0; 3957 -4.1; 4353 -5.2; 4788 -5.8; 5267 -5.0; 5793 -6.7; 6373 -5.0; 7010 -3.4; 7711 -5.3; 8482 -7.7; 9330 -10.1; 10263 -7.4; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -7.4; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-207 SB2217 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-207 SB2217 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 2.19 | 5.0 dB  |
| Peaking | 38 Hz    | 0.23 | 2.6 dB  |
| Peaking | 1701 Hz  | 1.85 | -7.1 dB |
| Peaking | 2236 Hz  | 1.45 | 4.0 dB  |
| Peaking | 9316 Hz  | 6.07 | -5.2 dB |
| Peaking | 61 Hz    | 4.16 | 0.5 dB  |
| Peaking | 556 Hz   | 1.86 | 0.7 dB  |
| Peaking | 1918 Hz  | 5.42 | -0.2 dB |
| Peaking | 6931 Hz  | 8.95 | 2.7 dB  |
| Peaking | 19668 Hz | 1.47 | -3.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-207%20SB2217/Stax%20SR-207%20SB2217.png)