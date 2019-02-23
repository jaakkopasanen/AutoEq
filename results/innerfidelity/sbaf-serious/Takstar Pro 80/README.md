# Takstar Pro 80
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.3; 25 -5.7; 28 -6.0; 31 -6.3; 34 -6.5; 37 -6.7; 41 -6.8; 45 -6.8; 49 -7.0; 54 -7.1; 60 -7.2; 66 -7.3; 72 -7.5; 79 -7.7; 87 -8.0; 96 -8.2; 106 -8.2; 116 -8.3; 128 -8.9; 141 -9.4; 155 -9.2; 170 -9.0; 187 -9.3; 206 -9.3; 227 -9.0; 249 -8.8; 274 -8.6; 302 -8.1; 332 -7.7; 365 -7.2; 402 -6.5; 442 -5.9; 486 -5.9; 535 -6.0; 588 -6.1; 647 -6.6; 712 -7.0; 783 -7.0; 861 -6.7; 947 -7.4; 1042 -7.9; 1146 -8.3; 1261 -9.1; 1387 -9.9; 1526 -10.9; 1678 -11.5; 1846 -11.9; 2031 -11.7; 2234 -10.2; 2457 -7.4; 2703 -4.6; 2973 -1.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -5.1; 5267 -3.8; 5793 -1.2; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -10.1; 9330 -12.1; 10263 -10.7; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Takstar Pro 80 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Takstar Pro 80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 164 Hz  |  0.97 | -3.0 dB |
| Peaking | 1930 Hz |  1.5  | -7.7 dB |
| Peaking | 3376 Hz |  1.54 | 8.4 dB  |
| Peaking | 6281 Hz |  4.35 | 5.5 dB  |
| Peaking | 9325 Hz |  3.39 | -6.8 dB |
| Peaking | 20 Hz   |  2.18 | 1.7 dB  |
| Peaking | 281 Hz  |  2.53 | -0.8 dB |
| Peaking | 479 Hz  |  2.13 | 1.4 dB  |
| Peaking | 4363 Hz |  9.17 | 2.2 dB  |
| Peaking | 4903 Hz | 11.29 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -6.2 dB |
| Peaking | 4000 Hz  | 1.41 | 9.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Takstar%20Pro%2080/Takstar%20Pro%2080.png)