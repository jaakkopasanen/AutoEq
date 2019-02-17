# Beyerdynamic T51i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.7; 25 -7.2; 28 -7.9; 31 -8.5; 34 -9.0; 37 -9.5; 41 -9.9; 45 -10.3; 49 -10.6; 54 -11.3; 60 -11.8; 66 -12.2; 72 -12.5; 79 -12.8; 87 -13.0; 96 -13.2; 106 -13.7; 116 -14.1; 128 -13.8; 141 -14.1; 155 -14.0; 170 -13.2; 187 -12.9; 206 -12.1; 227 -11.0; 249 -10.3; 274 -9.4; 302 -8.8; 332 -9.0; 365 -9.5; 402 -9.8; 442 -9.5; 486 -9.4; 535 -9.1; 588 -8.5; 647 -8.2; 712 -8.0; 783 -7.0; 861 -6.5; 947 -6.5; 1042 -6.2; 1146 -5.8; 1261 -5.5; 1387 -5.2; 1526 -4.9; 1678 -4.1; 1846 -2.6; 2031 -1.5; 2234 -2.8; 2457 -4.6; 2703 -4.6; 2973 -3.2; 3270 -1.6; 3597 -0.8; 3957 -0.9; 4353 -2.9; 4788 -4.6; 5267 -2.4; 5793 -0.5; 6373 -0.9; 7010 -3.8; 7711 -6.1; 8482 -8.6; 9330 -10.9; 10263 -7.6; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T51i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T51i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 1.62 | -0.7 dB |
| Peaking | 123 Hz  | 0.48 | -7.4 dB |
| Peaking | 1972 Hz | 2.95 | 4.5 dB  |
| Peaking | 3663 Hz | 3    | 5.7 dB  |
| Peaking | 6001 Hz | 4.72 | 6.2 dB  |
| Peaking | 288 Hz  | 2.1  | 2.7 dB  |
| Peaking | 599 Hz  | 0.5  | -2.6 dB |
| Peaking | 953 Hz  | 0.93 | 2.4 dB  |
| Peaking | 6852 Hz | 2.31 | 1.0 dB  |
| Peaking | 9246 Hz | 4.42 | -5.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -7.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T51i/Beyerdynamic%20T51i.png)