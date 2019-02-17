# Sennheiser PX 200-IIi
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.7; 79 -1.4; 87 -2.1; 96 -2.1; 106 -2.1; 116 -3.0; 128 -3.7; 141 -4.5; 155 -5.1; 170 -5.3; 187 -5.5; 206 -5.8; 227 -6.1; 249 -6.3; 274 -6.2; 302 -6.4; 332 -6.4; 365 -6.4; 402 -5.7; 442 -5.6; 486 -6.0; 535 -6.0; 588 -5.5; 647 -4.8; 712 -4.4; 783 -4.3; 861 -4.5; 947 -5.5; 1042 -6.0; 1146 -4.9; 1261 -4.2; 1387 -5.1; 1526 -6.4; 1678 -7.3; 1846 -7.8; 2031 -7.6; 2234 -7.6; 2457 -6.3; 2703 -5.1; 2973 -3.9; 3270 -2.9; 3597 -2.0; 3957 -0.7; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 200-IIi GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 200-IIi ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.43 | 6.7 dB  |
| Peaking | 751 Hz  | 2.96 | 2.2 dB  |
| Peaking | 1271 Hz | 4.32 | 2.2 dB  |
| Peaking | 1990 Hz | 2.16 | -2.6 dB |
| Peaking | 4628 Hz | 1.29 | 6.9 dB  |
| Peaking | 43 Hz   | 2.04 | -0.8 dB |
| Peaking | 74 Hz   | 2.05 | 0.7 dB  |
| Peaking | 4765 Hz | 6.12 | -1.1 dB |
| Peaking | 6355 Hz | 2.75 | 4.0 dB  |
| Peaking | 7602 Hz | 1.92 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 5.1 dB  |
| Peaking | 125 Hz   | 1.41 | 2.1 dB  |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PX%20200-IIi/Sennheiser%20PX%20200-IIi.png)