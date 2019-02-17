# Sennheiser PX 100-IIi
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.4; 45 -2.1; 49 -2.8; 54 -3.7; 60 -4.5; 66 -5.2; 72 -5.9; 79 -6.5; 87 -7.2; 96 -7.8; 106 -8.1; 116 -8.2; 128 -8.6; 141 -8.9; 155 -9.1; 170 -9.3; 187 -9.3; 206 -9.3; 227 -9.0; 249 -8.9; 274 -8.8; 302 -8.5; 332 -8.2; 365 -8.0; 402 -7.7; 442 -7.2; 486 -7.2; 535 -6.9; 588 -6.6; 647 -6.5; 712 -6.3; 783 -6.1; 861 -6.3; 947 -6.4; 1042 -6.6; 1146 -6.7; 1261 -7.1; 1387 -7.9; 1526 -8.9; 1678 -9.6; 1846 -9.8; 2031 -8.8; 2234 -6.6; 2457 -3.8; 2703 -2.5; 2973 -1.7; 3270 -3.1; 3597 -4.1; 3957 -2.7; 4353 -7.4; 4788 -6.5; 5267 -2.3; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 100-IIi GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 100-IIi ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.67 | 6.7 dB  |
| Peaking | 155 Hz  | 0.63 | -3.3 dB |
| Peaking | 1830 Hz | 2.64 | -4.5 dB |
| Peaking | 2854 Hz | 2.45 | 5.5 dB  |
| Peaking | 5991 Hz | 4.22 | 6.6 dB  |
| Peaking | 773 Hz  | 2.6  | 0.8 dB  |
| Peaking | 4377 Hz | 2.99 | 3.2 dB  |
| Peaking | 4518 Hz | 7.5  | -6.7 dB |
| Peaking | 8226 Hz | 4.32 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PX%20100-IIi/Sennheiser%20PX%20100-IIi.png)