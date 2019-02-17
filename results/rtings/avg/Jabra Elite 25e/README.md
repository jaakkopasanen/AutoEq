# Jabra Elite 25e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.7; 25 -8.9; 28 -9.0; 31 -9.1; 34 -9.1; 37 -9.1; 41 -9.1; 45 -9.0; 49 -9.0; 54 -9.0; 60 -9.2; 66 -9.3; 72 -9.4; 79 -9.5; 87 -9.8; 96 -10.0; 106 -10.3; 116 -10.6; 128 -10.8; 141 -10.9; 155 -10.9; 170 -10.8; 187 -10.6; 206 -10.5; 227 -10.2; 249 -9.7; 274 -9.0; 302 -8.3; 332 -7.6; 365 -6.9; 402 -6.2; 442 -5.4; 486 -4.5; 535 -3.6; 588 -2.7; 647 -1.8; 712 -0.9; 783 -0.5; 861 -0.5; 947 -0.6; 1042 -1.3; 1146 -2.1; 1261 -2.5; 1387 -2.7; 1526 -2.7; 1678 -2.8; 1846 -3.0; 2031 -3.0; 2234 -2.5; 2457 -2.1; 2703 -2.0; 2973 -2.1; 3270 -1.3; 3597 -0.7; 3957 -1.1; 4353 -2.1; 4788 -2.2; 5267 -2.1; 5793 -0.5; 6373 -0.9; 7010 -1.4; 7711 -3.7; 8482 -4.1; 9330 -1.1; 10263 -1.0; 11289 -1.0; 12418 -1.0; 13660 -1.1; 15026 -6.5; 16529 -9.9; 18182 -12.1; 20000 -13.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite 25e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite 25e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.19 | -7.7 dB  |
| Peaking | 207 Hz   | 0.75 | -6.2 dB  |
| Peaking | 1886 Hz  | 2.28 | -2.0 dB  |
| Peaking | 4730 Hz  | 6.03 | -1.1 dB  |
| Peaking | 18999 Hz | 0.74 | -13.5 dB |
| Peaking | 787 Hz   | 3.44 | 2.1 dB   |
| Peaking | 8211 Hz  | 4.28 | -5.3 dB  |
| Peaking | 8710 Hz  | 1.4  | 2.2 dB   |
| Peaking | 13563 Hz | 2.18 | 3.5 dB   |
| Peaking | 15829 Hz | 2.02 | -3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.1 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -7.9 dB |
| Peaking | 250 Hz   | 1.41 | -7.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -9.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Elite%2025e/Jabra%20Elite%2025e.png)