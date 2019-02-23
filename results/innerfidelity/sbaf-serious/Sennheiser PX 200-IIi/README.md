# Sennheiser PX 200-IIi
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.7; 54 -1.3; 60 -2.0; 66 -2.7; 72 -3.1; 79 -3.8; 87 -4.6; 96 -4.5; 106 -4.5; 116 -5.4; 128 -6.1; 141 -6.9; 155 -7.5; 170 -7.7; 187 -7.9; 206 -8.2; 227 -8.5; 249 -8.7; 274 -8.6; 302 -8.9; 332 -8.9; 365 -8.8; 402 -8.1; 442 -8.0; 486 -8.5; 535 -8.4; 588 -7.9; 647 -7.2; 712 -6.9; 783 -6.7; 861 -6.9; 947 -7.9; 1042 -8.4; 1146 -7.3; 1261 -6.6; 1387 -7.6; 1526 -8.8; 1678 -9.7; 1846 -10.2; 2031 -10.0; 2234 -10.0; 2457 -8.7; 2703 -7.5; 2973 -6.3; 3270 -5.3; 3597 -4.4; 3957 -3.1; 4353 -2.3; 4788 -1.5; 5267 -1.5; 5793 -0.7; 6373 -1.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.6; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 200-IIi GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 200-IIi ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.42 | 6.4 dB  |
| Peaking | 185 Hz  | 0.96 | -1.8 dB |
| Peaking | 351 Hz  | 0.89 | -1.9 dB |
| Peaking | 1998 Hz | 1.91 | -4.4 dB |
| Peaking | 5159 Hz | 1.62 | 6.1 dB  |
| Peaking | 536 Hz  | 5.72 | -0.8 dB |
| Peaking | 927 Hz  | 1.45 | 1.0 dB  |
| Peaking | 1001 Hz | 7.08 | -2.5 dB |
| Peaking | 6446 Hz | 5.02 | 3.1 dB  |
| Peaking | 7727 Hz | 1.57 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 3.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.0 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PX%20200-IIi/Sennheiser%20PX%20200-IIi.png)