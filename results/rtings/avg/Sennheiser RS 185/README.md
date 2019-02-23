# Sennheiser RS 185
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.7; 25 -3.2; 28 -3.8; 31 -4.2; 34 -4.6; 37 -4.8; 41 -5.1; 45 -5.2; 49 -5.2; 54 -5.3; 60 -5.6; 66 -5.9; 72 -6.3; 79 -6.6; 87 -7.0; 96 -7.3; 106 -7.7; 116 -8.0; 128 -8.3; 141 -8.6; 155 -8.7; 170 -8.7; 187 -8.7; 206 -8.5; 227 -8.3; 249 -8.2; 274 -8.0; 302 -7.9; 332 -7.7; 365 -7.5; 402 -7.4; 442 -7.2; 486 -6.9; 535 -5.7; 588 -4.6; 647 -4.3; 712 -4.4; 783 -4.1; 861 -2.1; 947 -2.7; 1042 -3.3; 1146 -3.6; 1261 -3.9; 1387 -3.8; 1526 -3.3; 1678 -3.4; 1846 -3.8; 2031 -4.4; 2234 -6.2; 2457 -8.8; 2703 -10.4; 2973 -11.4; 3270 -11.5; 3597 -9.6; 3957 -7.5; 4353 -6.2; 4788 -3.4; 5267 -1.7; 5793 -2.6; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -6.5; 11289 -6.9; 12418 -5.9; 13660 -5.9; 15026 -6.8; 16529 -6.1; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 185 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 185 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 277 Hz   | 0.37 | -3.9 dB |
| Peaking | 1030 Hz  | 0.44 | 4.7 dB  |
| Peaking | 3062 Hz  | 1.93 | -8.3 dB |
| Peaking | 5708 Hz  | 2.3  | 5.2 dB  |
| Peaking | 18 Hz    | 0.99 | 4.2 dB  |
| Peaking | 58 Hz    | 1.74 | 0.9 dB  |
| Peaking | 1268 Hz  | 2.78 | -3.1 dB |
| Peaking | 1271 Hz  | 1.42 | 2.0 dB  |
| Peaking | 10640 Hz | 2.08 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | -2.2 dB |
| Peaking | 8000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20RS%20185/Sennheiser%20RS%20185.png)