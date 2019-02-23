# Sennheiser HD 202
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -2.3; 25 -3.2; 28 -4.4; 31 -5.5; 34 -6.5; 37 -7.3; 41 -8.3; 45 -9.1; 49 -9.6; 54 -10.0; 60 -10.6; 66 -11.3; 72 -11.3; 79 -11.8; 87 -12.0; 96 -12.1; 106 -12.1; 116 -11.9; 128 -11.8; 141 -11.5; 155 -11.1; 170 -10.3; 187 -8.9; 206 -6.2; 227 -5.2; 249 -5.8; 274 -6.0; 302 -6.1; 332 -6.6; 365 -7.3; 402 -7.4; 442 -7.6; 486 -8.2; 535 -8.5; 588 -9.0; 647 -9.3; 712 -9.6; 783 -9.9; 861 -10.0; 947 -10.2; 1042 -10.4; 1146 -10.6; 1261 -10.4; 1387 -10.7; 1526 -11.0; 1678 -10.5; 1846 -9.4; 2031 -7.9; 2234 -6.1; 2457 -4.4; 2703 -2.4; 2973 -2.2; 3270 -1.3; 3597 -0.5; 3957 -0.8; 4353 -9.2; 4788 -8.2; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 202 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 202 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 2.17 | 5.7 dB  |
| Peaking | 91 Hz   | 0.94 | -6.2 dB |
| Peaking | 1322 Hz | 0.74 | -4.9 dB |
| Peaking | 3072 Hz | 2.04 | 7.3 dB  |
| Peaking | 5989 Hz | 4.55 | 6.6 dB  |
| Peaking | 168 Hz  | 2.37 | -3.1 dB |
| Peaking | 223 Hz  | 2.11 | 3.9 dB  |
| Peaking | 3879 Hz | 6.13 | 5.9 dB  |
| Peaking | 4497 Hz | 4.53 | -8.4 dB |
| Peaking | 5185 Hz | 7.37 | 5.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | 2.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | -4.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20202/Sennheiser%20HD%20202.png)