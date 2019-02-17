# Grado SR325e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.0; 37 -1.7; 41 -2.5; 45 -3.2; 49 -3.8; 54 -4.4; 60 -4.9; 66 -5.4; 72 -5.8; 79 -6.1; 87 -6.4; 96 -6.6; 106 -6.9; 116 -7.1; 128 -7.2; 141 -7.3; 155 -7.3; 170 -7.4; 187 -7.3; 206 -6.9; 227 -6.7; 249 -6.8; 274 -7.2; 302 -7.2; 332 -7.1; 365 -6.9; 402 -6.9; 442 -7.1; 486 -7.2; 535 -7.2; 588 -7.0; 647 -6.9; 712 -6.7; 783 -6.6; 861 -6.5; 947 -6.5; 1042 -6.5; 1146 -6.6; 1261 -6.9; 1387 -7.5; 1526 -8.3; 1678 -9.5; 1846 -12.4; 2031 -15.5; 2234 -15.4; 2457 -13.5; 2703 -11.8; 2973 -10.6; 3270 -10.4; 3597 -9.9; 3957 -10.6; 4353 -11.8; 4788 -9.1; 5267 -9.5; 5793 -9.9; 6373 -8.3; 7010 -8.1; 7711 -10.2; 8482 -13.9; 9330 -17.0; 10263 -17.5; 11289 -15.8; 12418 -13.5; 13660 -10.9; 15026 -8.6; 16529 -6.9; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR325e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.69 | 6.5 dB  |
| Peaking | 115 Hz   | 0.57 | -1.3 dB |
| Peaking | 2251 Hz  | 1.93 | -8.7 dB |
| Peaking | 9405 Hz  | 4.12 | -3.7 dB |
| Peaking | 10777 Hz | 1.3  | -9.2 dB |
| Peaking | 1388 Hz  | 1.43 | 1.3 dB  |
| Peaking | 2001 Hz  | 6.62 | -2.4 dB |
| Peaking | 2501 Hz  | 4.79 | 1.0 dB  |
| Peaking | 4255 Hz  | 4.17 | -3.3 dB |
| Peaking | 7027 Hz  | 6.79 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.4 dB |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | -7.2 dB |
| Peaking | 16000 Hz | 1.41 | -3.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20SR325e/Grado%20SR325e.png)