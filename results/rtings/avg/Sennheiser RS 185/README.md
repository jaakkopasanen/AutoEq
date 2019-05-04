# Sennheiser RS 185
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.6; 25 -3.0; 28 -3.6; 31 -4.1; 34 -4.5; 37 -4.8; 41 -5.0; 45 -5.1; 49 -5.2; 54 -5.3; 60 -5.5; 66 -5.8; 72 -6.1; 79 -6.5; 87 -6.8; 96 -7.2; 106 -7.5; 116 -7.9; 128 -8.2; 141 -8.4; 155 -8.6; 170 -8.6; 187 -8.6; 206 -8.4; 227 -8.3; 249 -8.2; 274 -8.0; 302 -7.9; 332 -7.8; 365 -7.6; 402 -7.4; 442 -7.3; 486 -7.1; 535 -5.8; 588 -4.7; 647 -4.5; 712 -4.6; 783 -4.2; 861 -2.4; 947 -2.9; 1042 -3.5; 1146 -3.9; 1261 -4.2; 1387 -4.1; 1526 -3.6; 1678 -3.7; 1846 -4.2; 2031 -4.9; 2234 -7.1; 2457 -9.7; 2703 -11.0; 2973 -11.6; 3270 -11.3; 3597 -9.4; 3957 -7.3; 4353 -5.9; 4788 -3.9; 5267 -2.3; 5793 -2.5; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.3; 11289 -7.9; 12418 -6.1; 13660 -6.0; 15026 -6.5; 16529 -6.1; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 185 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 185 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 288 Hz   | 0.37 | -3.8 dB |
| Peaking | 1010 Hz  | 0.46 | 4.5 dB  |
| Peaking | 2956 Hz  | 2    | -8.1 dB |
| Peaking | 5908 Hz  | 2.62 | 5.3 dB  |
| Peaking | 18 Hz    | 0.98 | 4.4 dB  |
| Peaking | 58 Hz    | 1.62 | 0.9 dB  |
| Peaking | 1250 Hz  | 2.92 | -3.2 dB |
| Peaking | 1256 Hz  | 1.52 | 2.1 dB  |
| Peaking | 11105 Hz | 4.4  | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20RS%20185/Sennheiser%20RS%20185.png)