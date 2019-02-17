# Jabra Elite Sport
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -7.8; 25 -7.9; 28 -7.9; 31 -7.8; 34 -7.9; 37 -7.9; 41 -8.0; 45 -8.1; 49 -8.1; 54 -8.3; 60 -8.7; 66 -9.1; 72 -9.3; 79 -9.7; 87 -10.1; 96 -10.5; 106 -10.9; 116 -11.4; 128 -11.8; 141 -12.0; 155 -12.1; 170 -12.0; 187 -11.8; 206 -11.5; 227 -11.1; 249 -10.3; 274 -9.3; 302 -8.2; 332 -7.3; 365 -6.6; 402 -6.3; 442 -6.1; 486 -5.9; 535 -5.6; 588 -5.1; 647 -4.6; 712 -4.1; 783 -3.9; 861 -3.9; 947 -3.9; 1042 -4.2; 1146 -4.2; 1261 -3.8; 1387 -3.3; 1526 -3.1; 1678 -3.7; 1846 -4.6; 2031 -5.4; 2234 -5.0; 2457 -4.3; 2703 -3.7; 2973 -3.0; 3270 -2.5; 3597 -2.1; 3957 -1.8; 4353 -1.9; 4788 -1.1; 5267 -0.6; 5793 -0.5; 6373 -2.0; 7010 -4.6; 7711 -7.4; 8482 -7.5; 9330 -7.5; 10263 -9.7; 11289 -10.8; 12418 -8.9; 13660 -6.0; 15026 -5.6; 16529 -7.4; 18182 -5.1; 20000 -4.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite Sport GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite Sport ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.2  | -3.4 dB |
| Peaking | 126 Hz   | 0.91 | -4.1 dB |
| Peaking | 213 Hz   | 1.12 | -4.5 dB |
| Peaking | 5485 Hz  | 1.35 | 6.0 dB  |
| Peaking | 10156 Hz | 0.78 | -6.5 dB |
| Peaking | 1926 Hz  | 1.3  | 2.5 dB  |
| Peaking | 2068 Hz  | 2.56 | -4.1 dB |
| Peaking | 11651 Hz | 4.11 | -2.6 dB |
| Peaking | 14115 Hz | 1.31 | 2.4 dB  |
| Peaking | 16679 Hz | 2.25 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -7.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | -3.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Elite%20Sport/Jabra%20Elite%20Sport.png)