# Sennheiser PX 200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.9; 128 -1.6; 141 -1.7; 155 -1.2; 170 -1.7; 187 -1.0; 206 -1.0; 227 -1.7; 249 -2.5; 274 -3.2; 302 -3.6; 332 -3.8; 365 -3.8; 402 -3.9; 442 -4.2; 486 -5.7; 535 -6.8; 588 -7.1; 647 -7.5; 712 -7.2; 783 -7.0; 861 -6.7; 947 -6.5; 1042 -6.5; 1146 -6.4; 1261 -6.5; 1387 -7.0; 1526 -7.6; 1678 -8.1; 1846 -8.2; 2031 -7.5; 2234 -6.5; 2457 -5.5; 2703 -4.0; 2973 -1.8; 3270 -0.5; 3597 -2.0; 3957 -4.7; 4353 -4.5; 4788 -3.0; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.2  | 6.1 dB  |
| Peaking | 238 Hz  | 0.7  | 3.0 dB  |
| Peaking | 1392 Hz | 0.12 | -1.5 dB |
| Peaking | 3205 Hz | 3.28 | 7.0 dB  |
| Peaking | 5754 Hz | 2.5  | 7.5 dB  |
| Peaking | 433 Hz  | 3.39 | 2.2 dB  |
| Peaking | 579 Hz  | 0.99 | -3.0 dB |
| Peaking | 983 Hz  | 0.58 | 2.3 dB  |
| Peaking | 1765 Hz | 2.57 | -2.2 dB |
| Peaking | 4123 Hz | 8.61 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.6 dB  |
| Peaking | 125 Hz   | 1.41 | 4.2 dB  |
| Peaking | 250 Hz   | 1.41 | 3.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PX%20200/Sennheiser%20PX%20200.png)