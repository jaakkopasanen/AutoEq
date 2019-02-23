# Sennheiser HD 201
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -1.0; 106 -1.9; 116 -2.4; 128 -3.2; 141 -3.7; 155 -4.3; 170 -4.6; 187 -5.0; 206 -5.1; 227 -5.4; 249 -6.1; 274 -6.4; 302 -6.9; 332 -7.4; 365 -7.9; 402 -8.4; 442 -8.8; 486 -9.2; 535 -9.1; 588 -8.8; 647 -8.7; 712 -9.1; 783 -9.7; 861 -10.3; 947 -9.9; 1042 -9.2; 1146 -9.6; 1261 -9.3; 1387 -9.5; 1526 -9.2; 1678 -8.8; 1846 -9.4; 2031 -9.0; 2234 -8.2; 2457 -6.8; 2703 -6.1; 2973 -5.8; 3270 -5.3; 3597 -6.7; 3957 -6.4; 4353 -3.1; 4788 -0.5; 5267 -0.5; 5793 -1.1; 6373 -1.0; 7010 -4.0; 7711 -7.0; 8482 -13.1; 9330 -13.4; 10263 -9.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 201 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 201 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 51 Hz   | 0.23 | 6.7 dB   |
| Peaking | 453 Hz  | 0.3  | -3.3 dB  |
| Peaking | 1487 Hz | 0.8  | -1.4 dB  |
| Peaking | 5777 Hz | 1.46 | 7.6 dB   |
| Peaking | 8899 Hz | 3.21 | -10.3 dB |
| Peaking | 87 Hz   | 6.04 | 0.9 dB   |
| Peaking | 3144 Hz | 2.67 | 2.8 dB   |
| Peaking | 3879 Hz | 2.1  | -4.0 dB  |
| Peaking | 4614 Hz | 4.96 | 3.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.3 dB  |
| Peaking | 125 Hz   | 1.41 | 2.9 dB  |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20201/Sennheiser%20HD%20201.png)