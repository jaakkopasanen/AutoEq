# Oppo PM1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -1.9; 25 -2.4; 28 -2.8; 31 -3.2; 34 -3.5; 37 -3.6; 41 -3.8; 45 -3.9; 49 -3.8; 54 -3.4; 60 -4.2; 66 -4.9; 72 -5.3; 79 -5.8; 87 -6.1; 96 -6.6; 106 -6.9; 116 -7.1; 128 -7.4; 141 -7.8; 155 -8.0; 170 -8.1; 187 -8.2; 206 -8.3; 227 -8.2; 249 -8.4; 274 -8.8; 302 -9.0; 332 -8.8; 365 -7.1; 402 -6.0; 442 -6.6; 486 -7.5; 535 -8.0; 588 -8.0; 647 -8.4; 712 -8.9; 783 -9.0; 861 -9.3; 947 -6.9; 1042 -6.8; 1146 -6.9; 1261 -7.0; 1387 -7.5; 1526 -7.6; 1678 -7.5; 1846 -6.8; 2031 -6.1; 2234 -5.4; 2457 -4.5; 2703 -4.1; 2973 -3.3; 3270 -3.0; 3597 -2.7; 3957 -1.9; 4353 -2.0; 4788 -1.3; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.69 | 5.2 dB  |
| Peaking | 54 Hz   | 2.22 | 2.0 dB  |
| Peaking | 218 Hz  | 0.91 | -2.1 dB |
| Peaking | 768 Hz  | 2.3  | -2.6 dB |
| Peaking | 4856 Hz | 1.3  | 6.1 dB  |
| Peaking | 1001 Hz | 6.74 | 1.1 dB  |
| Peaking | 1604 Hz | 2.69 | -1.6 dB |
| Peaking | 2950 Hz | 1.85 | 1.8 dB  |
| Peaking | 6215 Hz | 2.82 | 6.1 dB  |
| Peaking | 6555 Hz | 1.14 | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM1/Oppo%20PM1.png)