# Beyerdynamic T50p sample A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.9; 49 -1.5; 54 -2.3; 60 -3.1; 66 -3.9; 72 -4.5; 79 -4.9; 87 -5.3; 96 -5.8; 106 -5.1; 116 -5.1; 128 -4.7; 141 -4.9; 155 -4.3; 170 -4.3; 187 -6.0; 206 -7.9; 227 -8.7; 249 -9.0; 274 -8.9; 302 -9.1; 332 -9.1; 365 -9.1; 402 -9.1; 442 -8.9; 486 -8.9; 535 -8.6; 588 -8.0; 647 -7.9; 712 -7.7; 783 -6.3; 861 -6.3; 947 -6.5; 1042 -6.3; 1146 -6.0; 1261 -5.8; 1387 -5.9; 1526 -6.2; 1678 -6.3; 1846 -5.6; 2031 -4.4; 2234 -2.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T50p sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T50p sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.54 | 6.7 dB  |
| Peaking | 158 Hz  | 1.66 | 5.5 dB  |
| Peaking | 217 Hz  | 0.53 | -4.6 dB |
| Peaking | 3014 Hz | 1.42 | 6.1 dB  |
| Peaking | 5384 Hz | 2.12 | 5.3 dB  |
| Peaking | 1248 Hz | 1.41 | 1.0 dB  |
| Peaking | 1714 Hz | 1.97 | -1.7 dB |
| Peaking | 2385 Hz | 6.92 | 1.9 dB  |
| Peaking | 6502 Hz | 5.89 | 2.7 dB  |
| Peaking | 7716 Hz | 1.99 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | 2.0 dB  |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T50p%20sample%20A/Beyerdynamic%20T50p%20sample%20A.png)