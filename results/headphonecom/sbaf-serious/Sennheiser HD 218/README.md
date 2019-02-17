# Sennheiser HD 218
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.6; 72 -1.2; 79 -1.4; 87 -2.0; 96 -3.2; 106 -4.3; 116 -5.1; 128 -6.0; 141 -6.9; 155 -7.5; 170 -7.1; 187 -7.4; 206 -8.4; 227 -9.0; 249 -9.6; 274 -10.1; 302 -10.3; 332 -10.8; 365 -11.5; 402 -10.3; 442 -9.1; 486 -8.7; 535 -8.7; 588 -7.0; 647 -6.3; 712 -6.1; 783 -6.1; 861 -6.2; 947 -6.4; 1042 -6.5; 1146 -6.5; 1261 -6.1; 1387 -5.5; 1526 -5.1; 1678 -6.0; 1846 -6.0; 2031 -5.4; 2234 -4.3; 2457 -3.2; 2703 -2.7; 2973 -2.8; 3270 -2.2; 3597 -1.1; 3957 -0.5; 4353 -4.2; 4788 -8.9; 5267 -8.4; 5793 -6.9; 6373 -5.0; 7010 -4.1; 7711 -6.2; 8482 -6.9; 9330 -7.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -9.7; 18182 -13.0; 20000 -13.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 218 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 218 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.48 | 6.8 dB  |
| Peaking | 300 Hz   | 1.06 | -4.9 dB |
| Peaking | 3267 Hz  | 1.76 | 5.3 dB  |
| Peaking | 14915 Hz | 1.07 | 4.6 dB  |
| Peaking | 18793 Hz | 0.41 | -8.1 dB |
| Peaking | 143 Hz   | 4.88 | -1.4 dB |
| Peaking | 722 Hz   | 3.2  | 1.3 dB  |
| Peaking | 4078 Hz  | 6.08 | 4.7 dB  |
| Peaking | 4886 Hz  | 3.46 | -4.9 dB |
| Peaking | 6793 Hz  | 6.66 | 3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20218/Sennheiser%20HD%20218.png)