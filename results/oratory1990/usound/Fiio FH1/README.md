# Fiio FH1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.4; 23 -11.6; 25 -11.7; 28 -11.8; 31 -11.7; 34 -11.7; 37 -11.6; 41 -11.6; 45 -11.6; 49 -11.7; 54 -11.8; 60 -12.0; 66 -12.2; 72 -12.3; 79 -12.4; 87 -12.4; 96 -12.0; 106 -12.2; 116 -11.9; 128 -11.9; 141 -11.6; 155 -11.3; 170 -11.1; 187 -10.8; 206 -10.5; 227 -10.0; 249 -9.6; 274 -9.1; 302 -8.6; 332 -8.2; 365 -7.7; 402 -7.2; 442 -6.7; 486 -6.3; 535 -5.8; 588 -5.4; 647 -4.9; 712 -4.4; 783 -4.0; 861 -3.8; 947 -3.9; 1042 -4.7; 1146 -5.8; 1261 -6.9; 1387 -7.7; 1526 -8.1; 1678 -8.3; 1846 -8.3; 2031 -8.1; 2234 -7.4; 2457 -6.1; 2703 -4.8; 2973 -4.0; 3270 -3.6; 3597 -2.7; 3957 -0.5; 4353 -0.5; 4788 -2.7; 5267 -1.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.6; 8482 -10.9; 9330 -7.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.0; 20000 -10.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fiio FH1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fiio FH1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.34 | -5.2 dB |
| Peaking | 144 Hz  | 0.89 | -3.2 dB |
| Peaking | 4013 Hz | 2.97 | 5.1 dB  |
| Peaking | 6036 Hz | 2.36 | 6.1 dB  |
| Peaking | 8371 Hz | 4.38 | -6.2 dB |
| Peaking | 151 Hz  | 1.61 | 1.6 dB  |
| Peaking | 193 Hz  | 0.72 | -1.5 dB |
| Peaking | 904 Hz  | 1.04 | 4.4 dB  |
| Peaking | 1586 Hz | 1.02 | -3.9 dB |
| Peaking | 2836 Hz | 3.25 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Fiio%20FH1/Fiio%20FH1.png)