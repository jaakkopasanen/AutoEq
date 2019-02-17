# Jabra Elite 65t
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.4; 31 -2.3; 34 -3.0; 37 -3.6; 41 -4.2; 45 -4.6; 49 -4.9; 54 -5.2; 60 -5.8; 66 -6.3; 72 -6.8; 79 -7.3; 87 -7.8; 96 -8.2; 106 -8.9; 116 -9.4; 128 -10.0; 141 -10.4; 155 -10.7; 170 -10.9; 187 -11.0; 206 -11.1; 227 -11.1; 249 -10.8; 274 -10.5; 302 -10.2; 332 -10.0; 365 -9.7; 402 -9.3; 442 -8.8; 486 -8.3; 535 -7.8; 588 -7.2; 647 -6.4; 712 -5.8; 783 -5.5; 861 -5.7; 947 -6.1; 1042 -6.9; 1146 -7.6; 1261 -8.2; 1387 -8.7; 1526 -8.9; 1678 -9.2; 1846 -9.5; 2031 -9.8; 2234 -9.3; 2457 -8.4; 2703 -7.7; 2973 -7.3; 3270 -7.1; 3597 -7.4; 3957 -8.0; 4353 -9.1; 4788 -9.6; 5267 -9.2; 5793 -7.5; 6373 -6.1; 7010 -5.0; 7711 -7.2; 8482 -11.1; 9330 -15.0; 10263 -17.8; 11289 -17.1; 12418 -13.0; 13660 -9.0; 15026 -7.3; 16529 -8.3; 18182 -8.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite 65t GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite 65t ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.76 | 6.3 dB   |
| Peaking | 195 Hz   | 0.73 | -5.0 dB  |
| Peaking | 1462 Hz  | 3.69 | -1.3 dB  |
| Peaking | 2033 Hz  | 2.28 | -3.0 dB  |
| Peaking | 10701 Hz | 2.26 | -12.6 dB |
| Peaking | 786 Hz   | 3.44 | 2.0 dB   |
| Peaking | 4882 Hz  | 3.08 | -3.0 dB  |
| Peaking | 7043 Hz  | 3.12 | 4.1 dB   |
| Peaking | 9050 Hz  | 4.8  | -2.4 dB  |
| Peaking | 17421 Hz | 3.25 | -2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.9 dB |
| Peaking | 16000 Hz | 1.41 | -3.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Elite%2065t/Jabra%20Elite%2065t.png)