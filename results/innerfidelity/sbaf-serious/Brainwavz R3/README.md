# Brainwavz R3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -4.0; 25 -4.2; 28 -4.5; 31 -4.7; 34 -4.9; 37 -5.1; 41 -5.4; 45 -5.6; 49 -5.9; 54 -6.2; 60 -6.6; 66 -7.0; 72 -7.5; 79 -7.9; 87 -8.4; 96 -8.8; 106 -9.2; 116 -9.6; 128 -9.9; 141 -10.2; 155 -10.5; 170 -10.7; 187 -10.7; 206 -10.9; 227 -10.8; 249 -10.9; 274 -10.7; 302 -10.6; 332 -10.4; 365 -10.2; 402 -10.0; 442 -9.6; 486 -9.4; 535 -9.1; 588 -8.6; 647 -8.2; 712 -8.1; 783 -7.7; 861 -7.7; 947 -7.8; 1042 -7.9; 1146 -7.9; 1261 -7.5; 1387 -8.5; 1526 -8.9; 1678 -9.5; 1846 -9.9; 2031 -9.9; 2234 -8.8; 2457 -5.7; 2703 -2.2; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.1; 4788 -2.8; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Brainwavz R3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz R3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.23 | 3.0 dB  |
| Peaking | 207 Hz  | 0.43 | -4.6 dB |
| Peaking | 2059 Hz | 1.64 | -7.0 dB |
| Peaking | 3087 Hz | 1.38 | 8.8 dB  |
| Peaking | 5840 Hz | 3.49 | 5.1 dB  |
| Peaking | 6632 Hz | 8.36 | 1.9 dB  |
| Peaking | 7923 Hz | 2.33 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Brainwavz%20R3/Brainwavz%20R3.png)