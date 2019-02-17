# Sennheiser MM 450-X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -1.3; 31 -2.6; 34 -4.0; 37 -5.0; 41 -6.0; 45 -6.7; 49 -7.1; 54 -7.6; 60 -7.8; 66 -8.0; 72 -8.4; 79 -8.8; 87 -9.2; 96 -9.7; 106 -10.1; 116 -10.4; 128 -10.6; 141 -10.5; 155 -10.3; 170 -10.0; 187 -9.9; 206 -9.7; 227 -9.4; 249 -9.1; 274 -9.1; 302 -8.8; 332 -8.3; 365 -7.8; 402 -7.4; 442 -7.0; 486 -6.6; 535 -6.3; 588 -6.2; 647 -6.2; 712 -6.2; 783 -6.5; 861 -6.7; 947 -6.5; 1042 -6.5; 1146 -6.8; 1261 -7.3; 1387 -8.0; 1526 -8.7; 1678 -9.6; 1846 -11.1; 2031 -11.6; 2234 -12.7; 2457 -11.8; 2703 -10.1; 2973 -8.8; 3270 -6.7; 3597 -3.5; 3957 -1.6; 4353 -4.3; 4788 -4.3; 5267 -3.8; 5793 -3.9; 6373 -4.5; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MM 450-X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MM 450-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.68 | 6.9 dB  |
| Peaking | 135 Hz  | 0.68 | -4.2 dB |
| Peaking | 2238 Hz | 1.95 | -6.5 dB |
| Peaking | 3867 Hz | 4.91 | 5.7 dB  |
| Peaking | 5752 Hz | 2.19 | 2.8 dB  |
| Peaking | 297 Hz  | 2.99 | -0.8 dB |
| Peaking | 593 Hz  | 1.65 | 1.0 dB  |
| Peaking | 1088 Hz | 3.1  | 0.5 dB  |
| Peaking | 1644 Hz | 3.45 | -0.5 dB |
| Peaking | 8517 Hz | 5.51 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20MM%20450-X/Sennheiser%20MM%20450-X.png)