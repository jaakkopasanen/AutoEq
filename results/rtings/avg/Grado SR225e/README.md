# Grado SR225e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -1.2; 54 -1.8; 60 -2.4; 66 -3.0; 72 -3.4; 79 -3.7; 87 -4.1; 96 -4.3; 106 -4.5; 116 -4.8; 128 -4.9; 141 -5.0; 155 -5.0; 170 -5.0; 187 -4.9; 206 -4.7; 227 -4.4; 249 -4.4; 274 -5.1; 302 -5.0; 332 -4.7; 365 -4.7; 402 -4.7; 442 -4.8; 486 -4.9; 535 -4.8; 588 -4.8; 647 -4.6; 712 -4.4; 783 -4.2; 861 -4.1; 947 -4.1; 1042 -4.1; 1146 -4.3; 1261 -4.5; 1387 -5.1; 1526 -5.8; 1678 -6.7; 1846 -10.2; 2031 -13.2; 2234 -12.8; 2457 -11.1; 2703 -9.3; 2973 -8.2; 3270 -7.7; 3597 -5.9; 3957 -5.2; 4353 -10.5; 4788 -9.5; 5267 -8.7; 5793 -9.5; 6373 -7.0; 7010 -5.6; 7711 -7.8; 8482 -11.2; 9330 -13.9; 10263 -15.0; 11289 -14.5; 12418 -12.7; 13660 -9.1; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.43 | 6.2 dB  |
| Peaking | 903 Hz   | 0.48 | 2.8 dB  |
| Peaking | 2159 Hz  | 2.6  | -8.5 dB |
| Peaking | 9420 Hz  | 3.55 | -4.8 dB |
| Peaking | 11333 Hz | 2.1  | -7.4 dB |
| Peaking | 232 Hz   | 4.07 | 1.0 dB  |
| Peaking | 3897 Hz  | 4.86 | 6.8 dB  |
| Peaking | 4337 Hz  | 2.78 | -6.4 dB |
| Peaking | 7063 Hz  | 7.12 | 3.1 dB  |
| Peaking | 14992 Hz | 4.36 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.3 dB |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.0 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20SR225e/Grado%20SR225e.png)