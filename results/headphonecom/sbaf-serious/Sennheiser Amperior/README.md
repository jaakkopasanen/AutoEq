# Sennheiser Amperior
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.2; 28 -1.9; 31 -2.6; 34 -3.2; 37 -3.8; 41 -4.6; 45 -5.3; 49 -5.8; 54 -6.3; 60 -6.3; 66 -5.6; 72 -6.5; 79 -8.5; 87 -9.4; 96 -9.7; 106 -10.1; 116 -10.8; 128 -11.0; 141 -11.2; 155 -11.1; 170 -10.7; 187 -10.6; 206 -10.5; 227 -10.0; 249 -8.4; 274 -7.2; 302 -7.1; 332 -6.0; 365 -4.7; 402 -3.8; 442 -3.7; 486 -3.7; 535 -3.9; 588 -3.9; 647 -4.1; 712 -4.3; 783 -4.5; 861 -4.7; 947 -5.0; 1042 -5.6; 1146 -6.1; 1261 -6.5; 1387 -7.2; 1526 -8.0; 1678 -9.3; 1846 -9.5; 2031 -9.6; 2234 -9.0; 2457 -7.7; 2703 -5.9; 2973 -4.8; 3270 -4.4; 3597 -4.5; 3957 -5.0; 4353 -4.5; 4788 -5.4; 5267 -5.6; 5793 -2.0; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -10.5; 9330 -8.7; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Amperior GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Amperior ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.38 | 7.3 dB  |
| Peaking | 176 Hz  | 0.58 | -7.0 dB |
| Peaking | 415 Hz  | 0.65 | 5.5 dB  |
| Peaking | 1831 Hz | 2.8  | -4.2 dB |
| Peaking | 6187 Hz | 5.21 | 6.4 dB  |
| Peaking | 45 Hz   | 3.8  | -0.8 dB |
| Peaking | 91 Hz   | 5.98 | -0.8 dB |
| Peaking | 2288 Hz | 4.38 | -1.9 dB |
| Peaking | 3269 Hz | 1.9  | 2.3 dB  |
| Peaking | 8726 Hz | 6.71 | -5.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 3.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20Amperior/Sennheiser%20Amperior.png)