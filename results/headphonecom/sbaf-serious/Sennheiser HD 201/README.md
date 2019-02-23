# Sennheiser HD 201
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.7; 155 -0.8; 170 -1.3; 187 -1.4; 206 -2.1; 227 -1.5; 249 -2.4; 274 -3.1; 302 -3.5; 332 -3.9; 365 -4.3; 402 -4.5; 442 -4.8; 486 -5.3; 535 -5.5; 588 -5.5; 647 -5.5; 712 -6.0; 783 -7.3; 861 -9.4; 947 -11.4; 1042 -13.3; 1146 -13.9; 1261 -14.2; 1387 -13.9; 1526 -13.7; 1678 -8.9; 1846 -11.3; 2031 -11.4; 2234 -11.3; 2457 -11.3; 2703 -10.0; 2973 -8.5; 3270 -8.0; 3597 -8.5; 3957 -8.4; 4353 -3.9; 4788 -0.7; 5267 -13.8; 5793 -8.7; 6373 -9.4; 7010 -5.6; 7711 -6.2; 8482 -6.9; 9330 -12.5; 10263 -12.8; 11289 -9.3; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 201 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 201 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 53 Hz    | 0.15 | 6.2 dB   |
| Peaking | 1214 Hz  | 1.74 | -8.5 dB  |
| Peaking | 2314 Hz  | 2.39 | -4.0 dB  |
| Peaking | 9952 Hz  | 4.23 | -7.6 dB  |
| Peaking | 22050 Hz | 2.19 | -4.0 dB  |
| Peaking | 3190 Hz  | 3.82 | 0.1 dB   |
| Peaking | 3839 Hz  | 5.76 | -2.7 dB  |
| Peaking | 4759 Hz  | 5.54 | 12.9 dB  |
| Peaking | 5179 Hz  | 5.63 | -12.1 dB |
| Peaking | 7511 Hz  | 6.26 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 5.1 dB  |
| Peaking | 250 Hz   | 1.41 | 2.8 dB  |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.7 dB |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20201/Sennheiser%20HD%20201.png)