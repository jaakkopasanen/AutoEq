# Bose QuietComfort 25
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.6; 23 -8.4; 25 -8.2; 28 -8.0; 31 -7.8; 34 -7.8; 37 -7.9; 41 -8.1; 45 -8.3; 49 -8.5; 54 -8.6; 60 -8.7; 66 -8.9; 72 -9.0; 79 -9.0; 87 -9.1; 96 -9.3; 106 -9.5; 116 -9.7; 128 -9.8; 141 -9.9; 155 -9.9; 170 -9.8; 187 -9.6; 206 -9.3; 227 -9.0; 249 -8.7; 274 -8.6; 302 -8.4; 332 -8.2; 365 -7.9; 402 -7.8; 442 -7.8; 486 -7.5; 535 -7.3; 588 -7.1; 647 -6.8; 712 -6.2; 783 -6.0; 861 -5.8; 947 -5.5; 1042 -5.7; 1146 -6.6; 1261 -8.3; 1387 -9.7; 1526 -10.0; 1678 -11.2; 1846 -12.1; 2031 -12.0; 2234 -11.1; 2457 -9.3; 2703 -7.3; 2973 -6.1; 3270 -8.6; 3597 -11.3; 3957 -10.7; 4353 -7.5; 4788 -3.0; 5267 -0.5; 5793 -7.6; 6373 -14.5; 7010 -8.0; 7711 -5.3; 8482 -5.5; 9330 -5.5; 10263 -5.5; 11289 -6.8; 12418 -9.2; 13660 -8.8; 15026 -10.5; 16529 -12.5; 18182 -12.7; 20000 -14.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 25 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 25 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 112 Hz   | 0.31 | -4.1 dB  |
| Peaking | 1880 Hz  | 2.13 | -6.8 dB  |
| Peaking | 3781 Hz  | 4.56 | -5.6 dB  |
| Peaking | 5087 Hz  | 8.92 | 7.0 dB   |
| Peaking | 19144 Hz | 0.38 | -8.1 dB  |
| Peaking | 20 Hz    | 2.42 | -1.7 dB  |
| Peaking | 943 Hz   | 4.4  | 1.5 dB   |
| Peaking | 5513 Hz  | 8.75 | 4.0 dB   |
| Peaking | 6393 Hz  | 4.5  | -12.9 dB |
| Peaking | 7184 Hz  | 1.55 | 4.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.3 dB |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -8.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20QuietComfort%2025/Bose%20QuietComfort%2025.png)