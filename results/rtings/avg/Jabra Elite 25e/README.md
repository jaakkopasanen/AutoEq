# Jabra Elite 25e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.7; 25 -8.9; 28 -9.0; 31 -9.1; 34 -9.1; 37 -9.1; 41 -9.1; 45 -9.0; 49 -9.0; 54 -9.0; 60 -9.2; 66 -9.3; 72 -9.4; 79 -9.5; 87 -9.8; 96 -10.0; 106 -10.3; 116 -10.6; 128 -10.8; 141 -10.9; 155 -10.9; 170 -10.8; 187 -10.6; 206 -10.5; 227 -10.2; 249 -9.7; 274 -9.0; 302 -8.3; 332 -7.6; 365 -6.9; 402 -6.2; 442 -5.4; 486 -4.5; 535 -3.6; 588 -2.7; 647 -1.8; 712 -0.9; 783 -0.5; 861 -0.5; 947 -0.6; 1042 -1.3; 1146 -2.1; 1261 -2.5; 1387 -2.7; 1526 -2.7; 1678 -2.8; 1846 -3.0; 2031 -3.0; 2234 -2.5; 2457 -2.1; 2703 -2.0; 2973 -2.1; 3270 -1.3; 3597 -0.7; 3957 -1.1; 4353 -2.1; 4788 -2.2; 5267 -2.1; 5793 -0.5; 6373 -0.9; 7010 -2.0; 7711 -4.1; 8482 -4.4; 9330 -4.4; 10263 -4.4; 11289 -4.4; 12418 -4.4; 13660 -4.4; 15026 -6.5; 16529 -9.9; 18182 -12.1; 20000 -13.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite 25e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite 25e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.47 | -3.9 dB |
| Peaking | 172 Hz   | 0.5  | -6.3 dB |
| Peaking | 784 Hz   | 1.03 | 5.0 dB  |
| Peaking | 3495 Hz  | 1.52 | 3.2 dB  |
| Peaking | 6140 Hz  | 4.2  | 3.6 dB  |
| Peaking | 2362 Hz  | 6.9  | 0.6 dB  |
| Peaking | 13548 Hz | 1.3  | 3.3 dB  |
| Peaking | 19402 Hz | 0.41 | -9.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -5.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Elite%2025e/Jabra%20Elite%2025e.png)