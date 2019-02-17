# Bose QuietComfort 20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -6.0; 25 -7.5; 28 -9.0; 31 -9.9; 34 -10.4; 37 -10.6; 41 -10.7; 45 -10.6; 49 -10.5; 54 -10.4; 60 -10.4; 66 -10.5; 72 -10.6; 79 -10.8; 87 -11.1; 96 -11.4; 106 -11.6; 116 -11.6; 128 -11.4; 141 -11.0; 155 -10.6; 170 -10.4; 187 -10.2; 206 -10.2; 227 -10.1; 249 -10.0; 274 -9.9; 302 -9.9; 332 -9.8; 365 -9.6; 402 -9.2; 442 -8.5; 486 -7.6; 535 -6.4; 588 -5.1; 647 -3.9; 712 -2.7; 783 -1.3; 861 -0.5; 947 -1.4; 1042 -2.5; 1146 -3.5; 1261 -4.6; 1387 -5.6; 1526 -6.9; 1678 -8.6; 1846 -9.8; 2031 -9.9; 2234 -8.8; 2457 -7.4; 2703 -6.7; 2973 -6.9; 3270 -7.7; 3597 -9.7; 3957 -12.1; 4353 -12.5; 4788 -9.0; 5267 -5.5; 5793 -4.9; 6373 -9.1; 7010 -7.8; 7711 -3.9; 8482 -3.0; 9330 -3.5; 10263 -2.1; 11289 -2.1; 12418 -2.1; 13660 -2.1; 15026 -2.1; 16529 -2.1; 18182 -2.1; 20000 -2.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 78 Hz    | 0.31 | -9.4 dB |
| Peaking | 340 Hz   | 1.45 | -4.4 dB |
| Peaking | 1904 Hz  | 2.66 | -7.0 dB |
| Peaking | 4183 Hz  | 1.54 | -9.3 dB |
| Peaking | 22050 Hz | 2.47 | -3.5 dB |
| Peaking | 33 Hz    | 3.66 | -1.5 dB |
| Peaking | 818 Hz   | 0.85 | -2.9 dB |
| Peaking | 840 Hz   | 2.01 | 6.4 dB  |
| Peaking | 5456 Hz  | 5.38 | 3.5 dB  |
| Peaking | 6621 Hz  | 7.12 | -6.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.9 dB |
| Peaking | 62 Hz    | 1.41 | -6.5 dB |
| Peaking | 125 Hz   | 1.41 | -7.2 dB |
| Peaking | 250 Hz   | 1.41 | -6.6 dB |
| Peaking | 500 Hz   | 1.41 | -4.0 dB |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.4 dB |
| Peaking | 4000 Hz  | 1.41 | -7.3 dB |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20QuietComfort%2020/Bose%20QuietComfort%2020.png)