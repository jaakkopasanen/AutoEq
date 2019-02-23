# Phiton PS500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -1.0; 25 -1.6; 28 -2.7; 31 -3.8; 34 -4.6; 37 -5.4; 41 -6.1; 45 -6.7; 49 -7.1; 54 -7.5; 60 -7.9; 66 -8.3; 72 -8.6; 79 -9.3; 87 -9.8; 96 -10.4; 106 -10.8; 116 -11.1; 128 -11.5; 141 -11.7; 155 -11.6; 170 -11.3; 187 -11.2; 206 -10.9; 227 -10.2; 249 -9.6; 274 -8.3; 302 -6.8; 332 -5.9; 365 -5.6; 402 -5.6; 442 -5.5; 486 -5.8; 535 -5.9; 588 -5.7; 647 -6.2; 712 -6.8; 783 -7.1; 861 -6.7; 947 -7.8; 1042 -8.6; 1146 -9.2; 1261 -9.7; 1387 -10.5; 1526 -10.8; 1678 -11.0; 1846 -10.5; 2031 -9.2; 2234 -7.1; 2457 -4.0; 2703 -1.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.0; 4353 -4.1; 4788 -1.4; 5267 -0.8; 5793 -3.1; 6373 -1.3; 7010 -4.0; 7711 -6.2; 8482 -6.8; 9330 -7.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiton PS500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiton PS500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.72 | 6.2 dB  |
| Peaking | 135 Hz  | 1    | -5.6 dB |
| Peaking | 1713 Hz | 1.54 | -6.4 dB |
| Peaking | 3062 Hz | 1.64 | 7.6 dB  |
| Peaking | 5568 Hz | 2.37 | 4.1 dB  |
| Peaking | 235 Hz  | 1.93 | -3.1 dB |
| Peaking | 336 Hz  | 0.92 | 2.7 dB  |
| Peaking | 1128 Hz | 3.56 | -1.1 dB |
| Peaking | 6574 Hz | 9.84 | 2.7 dB  |
| Peaking | 8484 Hz | 2.11 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiton%20PS500/Phiton%20PS500.png)