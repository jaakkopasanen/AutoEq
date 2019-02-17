# Sennheiser HD 419
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.4; 23 -11.6; 25 -11.8; 28 -12.1; 31 -12.3; 34 -12.4; 37 -12.6; 41 -12.7; 45 -12.8; 49 -12.8; 54 -12.9; 60 -13.0; 66 -12.9; 72 -13.0; 79 -13.4; 87 -12.6; 96 -11.1; 106 -13.3; 116 -14.7; 128 -15.4; 141 -15.6; 155 -15.7; 170 -15.4; 187 -15.6; 206 -15.5; 227 -15.1; 249 -14.3; 274 -13.4; 302 -12.3; 332 -10.8; 365 -9.7; 402 -9.4; 442 -8.6; 486 -8.5; 535 -9.1; 588 -9.1; 647 -8.3; 712 -7.3; 783 -7.4; 861 -6.7; 947 -6.4; 1042 -6.5; 1146 -6.9; 1261 -6.7; 1387 -7.5; 1526 -8.0; 1678 -8.1; 1846 -7.9; 2031 -6.9; 2234 -5.2; 2457 -4.0; 2703 -4.3; 2973 -3.3; 3270 -3.2; 3597 -2.7; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.0; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 419 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 419 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.64 | -5.2 dB |
| Peaking | 65 Hz   | 1.48 | -2.9 dB |
| Peaking | 128 Hz  | 2.97 | -3.1 dB |
| Peaking | 203 Hz  | 0.89 | -8.4 dB |
| Peaking | 4708 Hz | 1.4  | 6.8 dB  |
| Peaking | 593 Hz  | 5.69 | -1.6 dB |
| Peaking | 1714 Hz | 1.68 | -5.2 dB |
| Peaking | 1952 Hz | 0.74 | 3.3 dB  |
| Peaking | 6294 Hz | 3.36 | 5.9 dB  |
| Peaking | 6484 Hz | 1.26 | -4.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.9 dB |
| Peaking | 250 Hz   | 1.41 | -7.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20419/Sennheiser%20HD%20419.png)