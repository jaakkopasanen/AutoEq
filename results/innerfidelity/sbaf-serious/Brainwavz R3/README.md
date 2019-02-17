# Brainwavz R3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -2.6; 25 -2.8; 28 -3.1; 31 -3.3; 34 -3.5; 37 -3.7; 41 -4.0; 45 -4.2; 49 -4.5; 54 -4.8; 60 -5.2; 66 -5.6; 72 -6.1; 79 -6.5; 87 -7.0; 96 -7.5; 106 -7.8; 116 -8.2; 128 -8.5; 141 -8.9; 155 -9.1; 170 -9.3; 187 -9.3; 206 -9.5; 227 -9.4; 249 -9.5; 274 -9.3; 302 -9.2; 332 -9.1; 365 -8.8; 402 -8.6; 442 -8.2; 486 -8.0; 535 -7.7; 588 -7.2; 647 -6.9; 712 -6.7; 783 -6.3; 861 -6.3; 947 -6.4; 1042 -6.5; 1146 -6.6; 1261 -6.1; 1387 -7.1; 1526 -7.5; 1678 -8.1; 1846 -8.5; 2031 -8.5; 2234 -7.4; 2457 -4.3; 2703 -1.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.1; 4788 -1.4; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Brainwavz R3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz R3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.34 | 4.1 dB  |
| Peaking | 200 Hz  | 0.58 | -3.4 dB |
| Peaking | 2055 Hz | 1.99 | -6.7 dB |
| Peaking | 2994 Hz | 1.13 | 8.1 dB  |
| Peaking | 5722 Hz | 3.13 | 4.6 dB  |
| Peaking | 803 Hz  | 3.09 | 0.6 dB  |
| Peaking | 1504 Hz | 6.74 | -0.5 dB |
| Peaking | 6551 Hz | 8    | 1.9 dB  |
| Peaking | 7710 Hz | 3.56 | -1.4 dB |
| Peaking | 9917 Hz | 1.73 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Brainwavz%20R3/Brainwavz%20R3.png)