# Sennheiser Amperior
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -2.4; 25 -3.0; 28 -3.7; 31 -4.3; 34 -4.9; 37 -5.3; 41 -5.8; 45 -6.2; 49 -6.6; 54 -7.0; 60 -7.5; 66 -7.6; 72 -7.8; 79 -8.6; 87 -9.3; 96 -9.6; 106 -10.2; 116 -10.4; 128 -10.8; 141 -10.9; 155 -10.7; 170 -10.3; 187 -10.1; 206 -9.4; 227 -8.5; 249 -7.5; 274 -6.6; 302 -5.9; 332 -5.1; 365 -4.4; 402 -3.9; 442 -3.7; 486 -4.0; 535 -4.2; 588 -4.1; 647 -4.4; 712 -4.7; 783 -4.8; 861 -5.2; 947 -5.5; 1042 -5.8; 1146 -6.1; 1261 -6.5; 1387 -7.1; 1526 -7.9; 1678 -8.6; 1846 -8.9; 2031 -8.9; 2234 -8.0; 2457 -6.2; 2703 -4.8; 2973 -3.6; 3270 -3.4; 3597 -3.5; 3957 -3.3; 4353 -2.7; 4788 -2.4; 5267 -1.1; 5793 -0.5; 6373 -0.5; 7010 -3.5; 7711 -6.6; 8482 -11.0; 9330 -10.2; 10263 -6.1; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Amperior GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Amperior ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 1.81 | 4.3 dB   |
| Peaking | 130 Hz  | 1.23 | -5.4 dB  |
| Peaking | 1904 Hz | 2.78 | -4.3 dB  |
| Peaking | 6465 Hz | 0.87 | 7.5 dB   |
| Peaking | 8584 Hz | 2.46 | -10.8 dB |
| Peaking | 208 Hz  | 2.36 | -2.0 dB  |
| Peaking | 448 Hz  | 0.97 | 2.6 dB   |
| Peaking | 1440 Hz | 3.09 | -1.0 dB  |
| Peaking | 3048 Hz | 5.9  | 1.2 dB   |
| Peaking | 4483 Hz | 3.75 | -0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Amperior/Sennheiser%20Amperior.png)