# Sennheiser HD 202 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -5.2; 25 -5.7; 28 -6.5; 31 -7.2; 34 -7.8; 37 -8.4; 41 -9.0; 45 -9.5; 49 -10.1; 54 -10.7; 60 -11.4; 66 -11.9; 72 -12.0; 79 -12.2; 87 -12.4; 96 -12.5; 106 -12.3; 116 -12.0; 128 -11.5; 141 -10.9; 155 -10.3; 170 -9.6; 187 -8.7; 206 -7.7; 227 -6.6; 249 -5.5; 274 -4.5; 302 -4.2; 332 -5.3; 365 -5.4; 402 -5.5; 442 -5.8; 486 -6.6; 535 -7.3; 588 -7.9; 647 -8.1; 712 -8.3; 783 -8.5; 861 -8.7; 947 -9.0; 1042 -9.2; 1146 -9.6; 1261 -10.0; 1387 -10.7; 1526 -10.9; 1678 -10.7; 1846 -10.2; 2031 -9.1; 2234 -8.0; 2457 -7.0; 2703 -5.5; 2973 -4.4; 3270 -2.1; 3597 -0.5; 3957 -0.5; 4353 -2.2; 4788 -4.2; 5267 -3.8; 5793 -1.4; 6373 -1.0; 7010 -4.0; 7711 -7.6; 8482 -7.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -11.8; 13660 -13.6; 15026 -10.8; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 202 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 202 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 70 Hz    | 1.22 | -5.2 dB |
| Peaking | 121 Hz   | 1.84 | -4.0 dB |
| Peaking | 3781 Hz  | 3.86 | 6.9 dB  |
| Peaking | 6122 Hz  | 4.6  | 6.1 dB  |
| Peaking | 13587 Hz | 2.65 | -8.0 dB |
| Peaking | 20 Hz    | 2.72 | 2.3 dB  |
| Peaking | 303 Hz   | 2.42 | 3.1 dB  |
| Peaking | 1762 Hz  | 0.78 | -7.0 dB |
| Peaking | 2648 Hz  | 0.88 | 4.6 dB  |
| Peaking | 7996 Hz  | 9.68 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -5.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | 2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.0 dB |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -4.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20202%20II/Sennheiser%20HD%20202%20II.png)