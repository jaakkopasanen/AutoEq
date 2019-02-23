# Denon AH-C560R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.8; 25 -6.1; 28 -6.4; 31 -6.7; 34 -6.9; 37 -7.1; 41 -7.3; 45 -7.6; 49 -7.8; 54 -8.0; 60 -8.3; 66 -8.5; 72 -8.8; 79 -9.1; 87 -9.5; 96 -9.7; 106 -9.9; 116 -9.9; 128 -10.0; 141 -10.0; 155 -9.9; 170 -9.8; 187 -9.6; 206 -9.3; 227 -8.8; 249 -8.5; 274 -7.9; 302 -7.4; 332 -6.8; 365 -6.2; 402 -5.6; 442 -4.8; 486 -4.3; 535 -3.7; 588 -2.8; 647 -2.2; 712 -2.1; 783 -1.3; 861 -0.9; 947 -0.6; 1042 -0.5; 1146 -0.6; 1261 -1.0; 1387 -1.5; 1526 -2.0; 1678 -2.3; 1846 -2.3; 2031 -2.3; 2234 -2.5; 2457 -2.8; 2703 -3.7; 2973 -4.4; 3270 -4.1; 3597 -3.3; 3957 -3.6; 4353 -6.0; 4788 -8.0; 5267 -9.4; 5793 -8.5; 6373 -5.8; 7010 -4.2; 7711 -5.0; 8482 -7.2; 9330 -6.3; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C560R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C560R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 86 Hz   | 0.42 | -1.5 dB |
| Peaking | 168 Hz  | 0.44 | -4.0 dB |
| Peaking | 959 Hz  | 0.57 | 5.2 dB  |
| Peaking | 3793 Hz | 5.06 | 1.8 dB  |
| Peaking | 5260 Hz | 3.41 | -5.1 dB |
| Peaking | 1580 Hz | 4.76 | -0.5 dB |
| Peaking | 2253 Hz | 5.45 | 0.7 dB  |
| Peaking | 6022 Hz | 4.03 | -1.1 dB |
| Peaking | 6949 Hz | 3.53 | 2.2 dB  |
| Peaking | 8683 Hz | 6.37 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-C560R/Denon%20AH-C560R.png)