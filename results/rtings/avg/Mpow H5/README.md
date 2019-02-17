# Mpow H5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.0; 23 -1.7; 25 -2.3; 28 -3.1; 31 -3.7; 34 -4.2; 37 -4.6; 41 -5.0; 45 -5.4; 49 -5.7; 54 -6.1; 60 -6.7; 66 -7.2; 72 -7.8; 79 -8.3; 87 -8.9; 96 -9.4; 106 -9.9; 116 -10.3; 128 -10.7; 141 -10.9; 155 -11.1; 170 -11.1; 187 -11.1; 206 -10.9; 227 -10.7; 249 -10.5; 274 -10.2; 302 -10.1; 332 -10.3; 365 -10.1; 402 -9.6; 442 -8.5; 486 -7.2; 535 -5.7; 588 -4.5; 647 -3.5; 712 -2.7; 783 -1.9; 861 -0.9; 947 -0.5; 1042 -0.5; 1146 -2.3; 1261 -4.1; 1387 -5.9; 1526 -6.6; 1678 -6.6; 1846 -6.5; 2031 -6.6; 2234 -5.9; 2457 -5.0; 2703 -5.3; 2973 -6.7; 3270 -8.2; 3597 -9.4; 3957 -8.1; 4353 -5.5; 4788 -4.0; 5267 -4.0; 5793 -1.5; 6373 -2.8; 7010 -6.3; 7711 -7.9; 8482 -11.0; 9330 -13.5; 10263 -12.4; 11289 -9.3; 12418 -6.4; 13660 -6.0; 15026 -8.4; 16529 -9.2; 18182 -8.4; 20000 -9.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mpow H5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mpow H5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--1.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 91 Hz    | 0.47 | -7.1 dB |
| Peaking | 200 Hz   | 0.88 | -6.1 dB |
| Peaking | 386 Hz   | 1.82 | -5.9 dB |
| Peaking | 2172 Hz  | 0.93 | -5.1 dB |
| Peaking | 16242 Hz | 0.17 | -9.1 dB |
| Peaking | 963 Hz   | 4.91 | 2.9 dB  |
| Peaking | 3634 Hz  | 5.8  | -4.3 dB |
| Peaking | 5979 Hz  | 3.52 | 6.0 dB  |
| Peaking | 9516 Hz  | 2.47 | -6.6 dB |
| Peaking | 13039 Hz | 2.44 | 4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -5.1 dB  |
| Peaking | 125 Hz   | 1.41 | -8.6 dB  |
| Peaking | 250 Hz   | 1.41 | -9.2 dB  |
| Peaking | 500 Hz   | 1.41 | -5.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.5 dB  |
| Peaking | 16000 Hz | 1.41 | -12.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Mpow%20H5/Mpow%20H5.png)