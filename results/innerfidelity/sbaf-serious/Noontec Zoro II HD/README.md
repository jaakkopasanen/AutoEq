# Noontec Zoro II HD
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.7; 25 -7.8; 28 -7.9; 31 -8.0; 34 -8.0; 37 -8.1; 41 -8.1; 45 -8.1; 49 -8.0; 54 -8.2; 60 -8.4; 66 -8.5; 72 -8.6; 79 -8.8; 87 -8.9; 96 -9.4; 106 -9.7; 116 -9.4; 128 -9.3; 141 -10.0; 155 -10.5; 170 -10.1; 187 -10.5; 206 -10.5; 227 -10.1; 249 -9.8; 274 -9.1; 302 -8.6; 332 -8.6; 365 -8.3; 402 -8.1; 442 -7.9; 486 -7.9; 535 -7.2; 588 -6.8; 647 -6.5; 712 -6.5; 783 -6.2; 861 -6.3; 947 -6.5; 1042 -6.7; 1146 -6.8; 1261 -7.2; 1387 -7.7; 1526 -8.3; 1678 -8.5; 1846 -8.2; 2031 -7.3; 2234 -6.5; 2457 -5.3; 2703 -4.7; 2973 -3.9; 3270 -3.2; 3597 -1.5; 3957 -0.5; 4353 -0.7; 4788 -3.0; 5267 -3.5; 5793 -2.6; 6373 -3.8; 7010 -4.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Zoro II HD GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro II HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 60 Hz   | 0.33 | -1.6 dB |
| Peaking | 193 Hz  | 0.89 | -3.1 dB |
| Peaking | 1692 Hz | 2.89 | -2.6 dB |
| Peaking | 3935 Hz | 2.05 | 6.1 dB  |
| Peaking | 5967 Hz | 4.49 | 2.5 dB  |
| Peaking | 464 Hz  | 4.33 | -0.6 dB |
| Peaking | 739 Hz  | 2.29 | 0.7 dB  |
| Peaking | 7020 Hz | 6.99 | 1.1 dB  |
| Peaking | 7908 Hz | 2.25 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro%20II%20HD/Noontec%20Zoro%20II%20HD.png)