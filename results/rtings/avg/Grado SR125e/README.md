# Grado SR125e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -1.1; 54 -1.7; 60 -2.2; 66 -2.7; 72 -3.0; 79 -3.3; 87 -3.6; 96 -3.8; 106 -4.0; 116 -4.2; 128 -4.4; 141 -4.5; 155 -4.6; 170 -4.6; 187 -4.5; 206 -4.3; 227 -4.0; 249 -3.9; 274 -4.0; 302 -4.4; 332 -4.4; 365 -4.3; 402 -4.3; 442 -4.4; 486 -4.5; 535 -4.5; 588 -4.4; 647 -4.3; 712 -4.1; 783 -3.9; 861 -3.7; 947 -3.7; 1042 -3.8; 1146 -3.9; 1261 -4.3; 1387 -4.8; 1526 -5.7; 1678 -7.1; 1846 -11.2; 2031 -13.6; 2234 -13.0; 2457 -11.5; 2703 -9.7; 2973 -8.1; 3270 -7.0; 3597 -8.1; 3957 -10.2; 4353 -7.5; 4788 -4.7; 5267 -7.7; 5793 -8.6; 6373 -8.3; 7010 -11.4; 7711 -12.4; 8482 -13.1; 9330 -12.8; 10263 -10.3; 11289 -7.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR125e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR125e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.47 | 6.3 dB  |
| Peaking | 294 Hz   | 0.67 | 1.8 dB  |
| Peaking | 1307 Hz  | 0.79 | 4.0 dB  |
| Peaking | 2104 Hz  | 2.16 | -9.8 dB |
| Peaking | 8443 Hz  | 2.06 | -7.3 dB |
| Peaking | 751 Hz   | 4.02 | 0.2 dB  |
| Peaking | 3408 Hz  | 3.79 | 3.6 dB  |
| Peaking | 3901 Hz  | 2.49 | -4.9 dB |
| Peaking | 4688 Hz  | 6.1  | 4.9 dB  |
| Peaking | 12380 Hz | 3.99 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | 1.0 dB  |
| Peaking | 250 Hz   | 1.41 | 2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20SR125e/Grado%20SR125e.png)