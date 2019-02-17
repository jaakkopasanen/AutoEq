# Sennheiser RS 185
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -4.2; 25 -4.6; 28 -5.2; 31 -5.7; 34 -6.0; 37 -6.3; 41 -6.5; 45 -6.6; 49 -6.7; 54 -6.8; 60 -7.1; 66 -7.4; 72 -7.7; 79 -8.1; 87 -8.4; 96 -8.8; 106 -9.2; 116 -9.5; 128 -9.8; 141 -10.0; 155 -10.2; 170 -10.2; 187 -10.1; 206 -9.9; 227 -9.8; 249 -9.6; 274 -9.5; 302 -9.3; 332 -9.2; 365 -9.0; 402 -8.8; 442 -8.7; 486 -8.4; 535 -7.1; 588 -6.0; 647 -5.8; 712 -5.8; 783 -5.5; 861 -3.5; 947 -4.2; 1042 -4.7; 1146 -5.1; 1261 -5.4; 1387 -5.3; 1526 -4.7; 1678 -4.9; 1846 -5.3; 2031 -5.8; 2234 -7.6; 2457 -10.2; 2703 -11.8; 2973 -12.8; 3270 -13.0; 3597 -11.0; 3957 -9.0; 4353 -7.7; 4788 -4.9; 5267 -3.2; 5793 -4.0; 6373 -0.5; 7010 -1.9; 7711 -4.1; 8482 -5.3; 9330 -6.4; 10263 -8.0; 11289 -8.3; 12418 -6.7; 13660 -6.2; 15026 -8.2; 16529 -7.1; 18182 -4.4; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 185 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 185 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 175 Hz   |  0.44 | -5.9 dB |
| Peaking | 3100 Hz  |  2.23 | -9.4 dB |
| Peaking | 6564 Hz  |  3.59 | 5.0 dB  |
| Peaking | 10779 Hz |  2.21 | -3.9 dB |
| Peaking | 15550 Hz |  2.59 | -4.1 dB |
| Peaking | 439 Hz   |  3.72 | -1.3 dB |
| Peaking | 884 Hz   |  4.93 | 2.1 dB  |
| Peaking | 1821 Hz  |  2.57 | 1.1 dB  |
| Peaking | 2487 Hz  |  7.06 | -1.8 dB |
| Peaking | 5117 Hz  | 11.71 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | -5.0 dB |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -4.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20RS%20185/Sennheiser%20RS%20185.png)