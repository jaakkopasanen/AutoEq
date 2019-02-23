# Shure SRH750DJ
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.9; 45 -1.5; 49 -1.9; 54 -2.3; 60 -2.9; 66 -3.5; 72 -4.2; 79 -4.8; 87 -5.2; 96 -5.2; 106 -4.8; 116 -4.9; 128 -5.6; 141 -6.3; 155 -6.8; 170 -6.4; 187 -6.5; 206 -6.9; 227 -6.8; 249 -8.1; 274 -8.2; 302 -7.8; 332 -7.4; 365 -7.2; 402 -7.3; 442 -7.5; 486 -7.7; 535 -7.7; 588 -7.3; 647 -7.0; 712 -6.5; 783 -5.8; 861 -5.4; 947 -5.2; 1042 -5.8; 1146 -5.9; 1261 -5.7; 1387 -6.4; 1526 -7.6; 1678 -9.1; 1846 -11.1; 2031 -12.9; 2234 -13.5; 2457 -11.6; 2703 -9.5; 2973 -6.4; 3270 -4.7; 3597 -3.3; 3957 -3.7; 4353 -6.8; 4788 -3.9; 5267 -0.7; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -10.2; 9330 -11.3; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH750DJ GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH750DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.71 | 6.6 dB  |
| Peaking | 2189 Hz | 2.89 | -7.9 dB |
| Peaking | 3507 Hz | 4.8  | 3.7 dB  |
| Peaking | 5883 Hz | 2.66 | 6.9 dB  |
| Peaking | 8961 Hz | 4.94 | -6.5 dB |
| Peaking | 57 Hz   | 3.28 | 0.4 dB  |
| Peaking | 267 Hz  | 3.23 | -1.8 dB |
| Peaking | 541 Hz  | 1.45 | -1.7 dB |
| Peaking | 950 Hz  | 1.1  | 1.8 dB  |
| Peaking | 1800 Hz | 5.56 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH750DJ/Shure%20SRH750DJ.png)