# FLC Technologies FLC8 CCY Voca
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -0.7; 34 -0.9; 37 -1.0; 41 -1.2; 45 -1.5; 49 -1.7; 54 -2.0; 60 -2.5; 66 -2.9; 72 -3.2; 79 -3.8; 87 -4.3; 96 -4.8; 106 -5.2; 116 -5.4; 128 -5.8; 141 -6.2; 155 -6.5; 170 -6.7; 187 -6.8; 206 -7.0; 227 -6.9; 249 -7.0; 274 -6.9; 302 -6.8; 332 -6.7; 365 -6.5; 402 -6.4; 442 -6.1; 486 -6.1; 535 -5.9; 588 -5.4; 647 -5.3; 712 -5.4; 783 -5.2; 861 -5.4; 947 -6.0; 1042 -6.8; 1146 -7.8; 1261 -9.0; 1387 -10.7; 1526 -12.6; 1678 -13.5; 1846 -12.4; 2031 -10.1; 2234 -8.7; 2457 -7.5; 2703 -7.1; 2973 -7.1; 3270 -2.9; 3597 -0.5; 3957 -0.5; 4353 -1.4; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.7; 9330 -7.9; 10263 -9.0; 11289 -8.2; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FLC Technologies FLC8 CCY Voca GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technologies FLC8 CCY Voca ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.79 | 5.9 dB  |
| Peaking | 57 Hz   | 1.3  | 2.5 dB  |
| Peaking | 1722 Hz | 2.23 | -8.1 dB |
| Peaking | 4994 Hz | 1.03 | 7.3 dB  |
| Peaking | 9583 Hz | 1.62 | -3.9 dB |
| Peaking | 227 Hz  | 1.57 | -0.8 dB |
| Peaking | 740 Hz  | 1.81 | 1.8 dB  |
| Peaking | 2995 Hz | 3.95 | -4.4 dB |
| Peaking | 3489 Hz | 3.97 | 4.5 dB  |
| Peaking | 4555 Hz | 5.73 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.6 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technologies%20FLC8%20CCY%20Voca/FLC%20Technologies%20FLC8%20CCY%20Voca.png)