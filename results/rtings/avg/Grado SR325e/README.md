# Grado SR325e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.8; 49 -1.3; 54 -1.9; 60 -2.5; 66 -3.0; 72 -3.3; 79 -3.6; 87 -3.9; 96 -4.1; 106 -4.3; 116 -4.5; 128 -4.7; 141 -4.8; 155 -4.9; 170 -4.9; 187 -4.8; 206 -4.5; 227 -4.3; 249 -4.4; 274 -4.9; 302 -4.9; 332 -4.8; 365 -4.6; 402 -4.6; 442 -4.7; 486 -4.9; 535 -4.9; 588 -4.8; 647 -4.6; 712 -4.5; 783 -4.4; 861 -4.2; 947 -4.2; 1042 -4.3; 1146 -4.4; 1261 -4.8; 1387 -5.3; 1526 -6.1; 1678 -7.2; 1846 -10.6; 2031 -13.7; 2234 -13.9; 2457 -12.2; 2703 -10.1; 2973 -8.5; 3270 -7.8; 3597 -7.3; 3957 -8.1; 4353 -9.0; 4788 -7.2; 5267 -7.5; 5793 -7.5; 6373 -5.1; 7010 -5.9; 7711 -8.7; 8482 -11.3; 9330 -12.9; 10263 -14.7; 11289 -14.6; 12418 -11.5; 13660 -7.8; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR325e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.51 | 6.3 dB  |
| Peaking | 289 Hz   | 0.64 | 1.4 dB  |
| Peaking | 1304 Hz  | 0.76 | 3.3 dB  |
| Peaking | 2157 Hz  | 2.23 | -9.8 dB |
| Peaking | 10601 Hz | 2.13 | -9.3 dB |
| Peaking | 3626 Hz  | 3.56 | 0.7 dB  |
| Peaking | 4266 Hz  | 4.78 | -2.1 dB |
| Peaking | 6717 Hz  | 5.47 | 3.2 dB  |
| Peaking | 8556 Hz  | 4.89 | -1.8 dB |
| Peaking | 14787 Hz | 3.69 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | 1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20SR325e/Grado%20SR325e.png)