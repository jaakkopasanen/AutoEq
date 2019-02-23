# Jabra Elite Sport
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -7.8; 25 -7.9; 28 -7.9; 31 -7.8; 34 -7.9; 37 -7.9; 41 -8.0; 45 -8.1; 49 -8.1; 54 -8.3; 60 -8.7; 66 -9.1; 72 -9.3; 79 -9.7; 87 -10.1; 96 -10.5; 106 -10.9; 116 -11.4; 128 -11.8; 141 -12.0; 155 -12.1; 170 -12.0; 187 -11.8; 206 -11.5; 227 -11.1; 249 -10.3; 274 -9.3; 302 -8.2; 332 -7.3; 365 -6.6; 402 -6.3; 442 -6.1; 486 -5.9; 535 -5.6; 588 -5.1; 647 -4.6; 712 -4.1; 783 -3.9; 861 -3.9; 947 -3.9; 1042 -4.2; 1146 -4.2; 1261 -3.8; 1387 -3.3; 1526 -3.1; 1678 -3.7; 1846 -4.6; 2031 -5.4; 2234 -5.0; 2457 -4.3; 2703 -3.7; 2973 -3.0; 3270 -2.5; 3597 -2.1; 3957 -1.8; 4353 -1.9; 4788 -1.1; 5267 -0.6; 5793 -0.5; 6373 -2.0; 7010 -4.6; 7711 -7.4; 8482 -7.5; 9330 -7.5; 10263 -9.7; 11289 -10.8; 12418 -8.9; 13660 -6.1; 15026 -5.9; 16529 -7.4; 18182 -6.1; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite Sport GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite Sport ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.15 | -1.5 dB |
| Peaking | 168 Hz   | 0.72 | -6.0 dB |
| Peaking | 821 Hz   | 0.45 | 2.4 dB  |
| Peaking | 5152 Hz  | 1.24 | 5.8 dB  |
| Peaking | 10493 Hz | 1.34 | -5.1 dB |
| Peaking | 1532 Hz  | 4.72 | 1.2 dB  |
| Peaking | 2073 Hz  | 3.32 | -1.4 dB |
| Peaking | 3098 Hz  | 3.59 | 1.0 dB  |
| Peaking | 7698 Hz  | 9.54 | -2.1 dB |
| Peaking | 13962 Hz | 5.41 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Elite%20Sport/Jabra%20Elite%20Sport.png)