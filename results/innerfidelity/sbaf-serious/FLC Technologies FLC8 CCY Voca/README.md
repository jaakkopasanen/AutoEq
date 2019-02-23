# FLC Technologies FLC8 CCY Voca
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.0; 25 -1.2; 28 -1.4; 31 -1.5; 34 -1.7; 37 -1.9; 41 -2.1; 45 -2.3; 49 -2.6; 54 -2.9; 60 -3.3; 66 -3.7; 72 -4.1; 79 -4.6; 87 -5.1; 96 -5.6; 106 -6.0; 116 -6.3; 128 -6.7; 141 -7.0; 155 -7.3; 170 -7.5; 187 -7.6; 206 -7.8; 227 -7.8; 249 -7.9; 274 -7.8; 302 -7.7; 332 -7.6; 365 -7.4; 402 -7.3; 442 -6.9; 486 -6.9; 535 -6.7; 588 -6.3; 647 -6.2; 712 -6.3; 783 -6.1; 861 -6.2; 947 -6.8; 1042 -7.7; 1146 -8.6; 1261 -9.8; 1387 -11.6; 1526 -13.5; 1678 -14.4; 1846 -13.2; 2031 -11.0; 2234 -9.6; 2457 -8.3; 2703 -7.9; 2973 -7.9; 3270 -3.8; 3597 -0.6; 3957 -0.6; 4353 -2.2; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.4; 9330 -8.7; 10263 -9.8; 11289 -9.0; 12418 -6.6; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FLC Technologies FLC8 CCY Voca GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technologies FLC8 CCY Voca ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.06 | 5.5 dB  |
| Peaking | 51 Hz    | 1.69 | 2.8 dB  |
| Peaking | 1692 Hz  | 2.05 | -8.2 dB |
| Peaking | 3770 Hz  | 4.12 | 6.2 dB  |
| Peaking | 5530 Hz  | 2.83 | 6.7 dB  |
| Peaking | 82 Hz    | 2.06 | 0.9 dB  |
| Peaking | 234 Hz   | 0.76 | -1.5 dB |
| Peaking | 809 Hz   | 1.35 | 1.4 dB  |
| Peaking | 1305 Hz  | 2.31 | -0.7 dB |
| Peaking | 10238 Hz | 3.08 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.4 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technologies%20FLC8%20CCY%20Voca/FLC%20Technologies%20FLC8%20CCY%20Voca.png)