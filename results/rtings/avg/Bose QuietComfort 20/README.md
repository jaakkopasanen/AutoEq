# Bose QuietComfort 20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -5.0; 25 -6.4; 28 -8.0; 31 -8.9; 34 -9.4; 37 -9.6; 41 -9.7; 45 -9.6; 49 -9.5; 54 -9.4; 60 -9.3; 66 -9.4; 72 -9.6; 79 -9.8; 87 -10.1; 96 -10.4; 106 -10.6; 116 -10.5; 128 -10.3; 141 -9.9; 155 -9.6; 170 -9.3; 187 -9.2; 206 -9.1; 227 -9.1; 249 -9.0; 274 -8.9; 302 -8.8; 332 -8.8; 365 -8.5; 402 -8.1; 442 -7.5; 486 -6.6; 535 -5.4; 588 -4.1; 647 -2.9; 712 -1.6; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -1.5; 1146 -2.5; 1261 -3.6; 1387 -4.6; 1526 -5.9; 1678 -7.6; 1846 -8.7; 2031 -8.8; 2234 -7.8; 2457 -6.3; 2703 -5.7; 2973 -5.9; 3270 -6.7; 3597 -8.7; 3957 -11.1; 4353 -11.5; 4788 -7.9; 5267 -4.4; 5793 -3.8; 6373 -8.1; 7010 -6.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.56 | 7.2 dB  |
| Peaking | 31 Hz   | 1.76 | -1.9 dB |
| Peaking | 284 Hz  | 0.09 | -3.9 dB |
| Peaking | 879 Hz  | 0.97 | 10.0 dB |
| Peaking | 1850 Hz | 4.76 | -2.6 dB |
| Peaking | 62 Hz   | 4.03 | 0.4 dB  |
| Peaking | 404 Hz  | 4.86 | -0.7 dB |
| Peaking | 2900 Hz | 3.6  | 2.6 dB  |
| Peaking | 4198 Hz | 3.89 | -5.3 dB |
| Peaking | 5438 Hz | 5.67 | 4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20QuietComfort%2020/Bose%20QuietComfort%2020.png)