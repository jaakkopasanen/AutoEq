# Sennheiser HD 424
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -1.8; 106 -3.1; 116 -4.3; 128 -5.7; 141 -6.8; 155 -7.6; 170 -8.0; 187 -8.1; 206 -8.0; 227 -7.8; 249 -7.4; 274 -7.0; 302 -6.6; 332 -6.3; 365 -5.9; 402 -5.7; 442 -5.3; 486 -5.2; 535 -5.2; 588 -5.0; 647 -5.0; 712 -5.3; 783 -5.3; 861 -5.7; 947 -6.1; 1042 -6.5; 1146 -7.0; 1261 -7.6; 1387 -8.9; 1526 -10.1; 1678 -11.2; 1846 -11.8; 2031 -11.4; 2234 -10.3; 2457 -8.7; 2703 -7.6; 2973 -6.9; 3270 -6.8; 3597 -7.3; 3957 -7.2; 4353 -6.6; 4788 -4.3; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.1; 9330 -7.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 424 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 424 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 59 Hz   | 0.27 | 7.3 dB  |
| Peaking | 176 Hz  | 1    | -6.7 dB |
| Peaking | 690 Hz  | 1.02 | 1.5 dB  |
| Peaking | 1827 Hz | 1.78 | -5.8 dB |
| Peaking | 5785 Hz | 3.39 | 7.1 dB  |
| Peaking | 18 Hz   | 1.14 | 1.7 dB  |
| Peaking | 42 Hz   | 0.77 | -0.8 dB |
| Peaking | 86 Hz   | 4.33 | 1.4 dB  |
| Peaking | 4117 Hz | 7.07 | -1.2 dB |
| Peaking | 8700 Hz | 5.77 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 6.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20424/Sennheiser%20HD%20424.png)