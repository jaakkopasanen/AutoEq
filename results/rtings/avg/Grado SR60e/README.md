# Grado SR60e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -1.0; 34 -1.7; 37 -2.5; 41 -3.4; 45 -4.2; 49 -4.8; 54 -5.5; 60 -6.2; 66 -6.8; 72 -7.3; 79 -7.6; 87 -7.9; 96 -8.2; 106 -8.4; 116 -8.6; 128 -8.7; 141 -8.7; 155 -8.6; 170 -8.4; 187 -8.3; 206 -8.0; 227 -7.9; 249 -7.9; 274 -7.8; 302 -7.6; 332 -7.6; 365 -8.3; 402 -8.4; 442 -8.2; 486 -7.9; 535 -7.7; 588 -7.6; 647 -7.3; 712 -7.1; 783 -6.9; 861 -6.7; 947 -6.6; 1042 -6.4; 1146 -6.5; 1261 -6.8; 1387 -7.3; 1526 -8.1; 1678 -9.3; 1846 -13.0; 2031 -15.3; 2234 -14.3; 2457 -12.6; 2703 -11.2; 2973 -10.0; 3270 -9.6; 3597 -11.9; 3957 -13.5; 4353 -9.9; 4788 -7.3; 5267 -9.6; 5793 -10.2; 6373 -12.1; 7010 -13.9; 7711 -15.1; 8482 -17.0; 9330 -17.3; 10263 -14.1; 11289 -10.4; 12418 -7.8; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR60e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR60e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.7  | 7.7 dB  |
| Peaking | 90 Hz    | 0.32 | -2.9 dB |
| Peaking | 2175 Hz  | 2.27 | -8.3 dB |
| Peaking | 7701 Hz  | 1.2  | -6.6 dB |
| Peaking | 9287 Hz  | 3.3  | -6.5 dB |
| Peaking | 448 Hz   | 2.97 | -0.9 dB |
| Peaking | 1212 Hz  | 2    | 1.3 dB  |
| Peaking | 3906 Hz  | 5.94 | -5.7 dB |
| Peaking | 4757 Hz  | 5.21 | 3.0 dB  |
| Peaking | 13634 Hz | 3.03 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.8 dB |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | -9.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20SR60e/Grado%20SR60e.png)