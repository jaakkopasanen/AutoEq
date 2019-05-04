# Jabra Evolve 65t
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -2.3; 25 -3.3; 28 -4.5; 31 -5.4; 34 -6.1; 37 -6.6; 41 -7.1; 45 -7.4; 49 -7.6; 54 -7.7; 60 -7.9; 66 -8.1; 72 -8.2; 79 -8.4; 87 -8.5; 96 -8.6; 106 -8.6; 116 -8.7; 128 -8.6; 141 -8.6; 155 -8.5; 170 -8.3; 187 -8.0; 206 -7.9; 227 -7.6; 249 -7.4; 274 -7.1; 302 -6.6; 332 -6.2; 365 -5.9; 402 -5.6; 442 -5.1; 486 -4.6; 535 -3.9; 588 -3.3; 647 -2.7; 712 -2.1; 783 -1.7; 861 -1.4; 947 -1.5; 1042 -2.2; 1146 -3.3; 1261 -4.1; 1387 -4.5; 1526 -4.6; 1678 -4.7; 1846 -4.9; 2031 -5.0; 2234 -4.6; 2457 -3.5; 2703 -2.4; 2973 -1.6; 3270 -1.5; 3597 -1.9; 3957 -2.7; 4353 -3.7; 4788 -5.0; 5267 -4.7; 5793 -2.7; 6373 -0.5; 7010 -2.3; 7711 -4.9; 8482 -7.3; 9330 -8.1; 10263 -11.1; 11289 -13.3; 12418 -10.2; 13660 -5.9; 15026 -5.9; 16529 -9.5; 18182 -9.3; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Evolve 65t GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Evolve 65t ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 2.45 | 4.7 dB   |
| Peaking | 118 Hz   | 0.39 | -4.5 dB  |
| Peaking | 4298 Hz  | 0.06 | 2.1 dB   |
| Peaking | 11085 Hz | 2.25 | -10.7 dB |
| Peaking | 17434 Hz | 1.66 | -7.5 dB  |
| Peaking | 870 Hz   | 1.09 | 5.9 dB   |
| Peaking | 1366 Hz  | 0.42 | -4.6 dB  |
| Peaking | 3254 Hz  | 1.57 | 4.7 dB   |
| Peaking | 5711 Hz  | 1.27 | -3.5 dB  |
| Peaking | 6384 Hz  | 3.67 | 7.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -5.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Evolve%2065t/Jabra%20Evolve%2065t.png)