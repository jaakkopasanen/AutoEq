# Sennheiser HD 419
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -10.6; 25 -10.8; 28 -11.0; 31 -11.2; 34 -11.4; 37 -11.5; 41 -11.6; 45 -11.7; 49 -11.8; 54 -11.9; 60 -12.0; 66 -11.9; 72 -12.0; 79 -12.4; 87 -11.5; 96 -10.1; 106 -12.3; 116 -13.7; 128 -14.3; 141 -14.6; 155 -14.6; 170 -14.3; 187 -14.6; 206 -14.5; 227 -14.1; 249 -13.3; 274 -12.4; 302 -11.2; 332 -9.8; 365 -8.7; 402 -8.3; 442 -7.5; 486 -7.5; 535 -8.1; 588 -8.1; 647 -7.3; 712 -6.3; 783 -6.3; 861 -5.7; 947 -5.3; 1042 -5.4; 1146 -5.9; 1261 -5.6; 1387 -6.4; 1526 -6.9; 1678 -7.0; 1846 -6.9; 2031 -5.8; 2234 -4.1; 2457 -3.0; 2703 -3.3; 2973 -2.3; 3270 -2.1; 3597 -1.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 419 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 419 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.61 | -4.6 dB |
| Peaking | 68 Hz   | 1.92 | -2.3 dB |
| Peaking | 135 Hz  | 1.95 | -5.0 dB |
| Peaking | 219 Hz  | 1.36 | -6.6 dB |
| Peaking | 4437 Hz | 1.13 | 6.7 dB  |
| Peaking | 979 Hz  | 2.94 | 1.4 dB  |
| Peaking | 1855 Hz | 2.28 | -2.4 dB |
| Peaking | 2349 Hz | 2.47 | 2.4 dB  |
| Peaking | 6269 Hz | 3.13 | 5.1 dB  |
| Peaking | 7009 Hz | 1.3  | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -6.1 dB |
| Peaking | 250 Hz   | 1.41 | -6.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20419/Sennheiser%20HD%20419.png)