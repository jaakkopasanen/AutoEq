# Sennheiser HD 202
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -3.0; 25 -3.7; 28 -4.8; 31 -5.7; 34 -6.6; 37 -7.3; 41 -8.0; 45 -8.6; 49 -9.3; 54 -10.0; 60 -10.6; 66 -11.1; 72 -11.5; 79 -11.5; 87 -11.2; 96 -11.1; 106 -11.6; 116 -11.7; 128 -11.7; 141 -11.6; 155 -11.4; 170 -10.7; 187 -10.5; 206 -9.7; 227 -7.9; 249 -6.6; 274 -6.8; 302 -6.8; 332 -6.5; 365 -5.8; 402 -5.8; 442 -6.5; 486 -7.0; 535 -7.5; 588 -7.7; 647 -8.2; 712 -8.7; 783 -8.8; 861 -9.1; 947 -9.4; 1042 -9.8; 1146 -10.1; 1261 -10.3; 1387 -10.8; 1526 -11.3; 1678 -11.4; 1846 -10.4; 2031 -8.8; 2234 -7.5; 2457 -5.2; 2703 -3.3; 2973 -0.9; 3270 -0.9; 3597 -0.5; 3957 -0.5; 4353 -5.6; 4788 -7.6; 5267 -3.6; 5793 -0.7; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 202 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 202 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.81 | 5.0 dB  |
| Peaking | 95 Hz   | 0.72 | -5.7 dB |
| Peaking | 1550 Hz | 1.01 | -5.5 dB |
| Peaking | 3206 Hz | 2.04 | 8.0 dB  |
| Peaking | 6112 Hz | 5.08 | 6.2 dB  |
| Peaking | 98 Hz   | 2.05 | 2.5 dB  |
| Peaking | 235 Hz  | 0.45 | -4.2 dB |
| Peaking | 305 Hz  | 0.91 | 5.5 dB  |
| Peaking | 3992 Hz | 8.15 | 3.3 dB  |
| Peaking | 4579 Hz | 8.7  | -4.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.9 dB |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20202/Sennheiser%20HD%20202.png)