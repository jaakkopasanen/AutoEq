# Stax SR-L300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -1.6; 60 -3.1; 66 -4.5; 72 -5.7; 79 -6.9; 87 -7.6; 96 -7.8; 106 -7.7; 116 -7.5; 128 -7.3; 141 -7.0; 155 -6.9; 170 -6.7; 187 -6.4; 206 -6.2; 227 -6.0; 249 -5.8; 274 -5.7; 302 -5.9; 332 -6.0; 365 -5.9; 402 -6.0; 442 -6.1; 486 -6.2; 535 -6.5; 588 -6.2; 647 -6.2; 712 -6.2; 783 -6.3; 861 -6.4; 947 -6.5; 1042 -6.4; 1146 -6.7; 1261 -7.3; 1387 -7.8; 1526 -7.4; 1678 -6.1; 1846 -5.2; 2031 -5.4; 2234 -5.3; 2457 -5.7; 2703 -4.9; 2973 -5.3; 3270 -4.2; 3597 -3.9; 3957 -4.6; 4353 -5.3; 4788 -6.0; 5267 -7.1; 5793 -9.0; 6373 -10.2; 7010 -8.1; 7711 -7.2; 8482 -9.3; 9330 -9.7; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.0; 18182 -9.6; 20000 -11.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-L300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-L300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.37 | 9.3 dB  |
| Peaking | 90 Hz   | 0.82 | -8.7 dB |
| Peaking | 3523 Hz | 1.65 | 2.5 dB  |
| Peaking | 6194 Hz | 4.29 | -4.2 dB |
| Peaking | 8977 Hz | 5.8  | -3.8 dB |
| Peaking | 12 Hz   | 1.73 | 0.8 dB  |
| Peaking | 1416 Hz | 4.12 | -1.9 dB |
| Peaking | 1881 Hz | 3.91 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Stax%20SR-L300/Stax%20SR-L300.png)