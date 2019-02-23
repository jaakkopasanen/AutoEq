# Sennheiser Game One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.1; 49 -1.5; 54 -2.0; 60 -2.6; 66 -3.2; 72 -3.7; 79 -4.2; 87 -4.8; 96 -5.4; 106 -6.0; 116 -6.4; 128 -6.9; 141 -7.2; 155 -7.4; 170 -7.5; 187 -7.5; 206 -7.4; 227 -7.2; 249 -7.2; 274 -7.2; 302 -7.2; 332 -7.2; 365 -7.1; 402 -7.1; 442 -7.2; 486 -7.2; 535 -7.1; 588 -6.9; 647 -6.7; 712 -6.2; 783 -6.1; 861 -6.0; 947 -6.1; 1042 -6.1; 1146 -6.0; 1261 -6.4; 1387 -6.4; 1526 -6.0; 1678 -6.3; 1846 -6.6; 2031 -7.4; 2234 -7.7; 2457 -7.2; 2703 -6.8; 2973 -6.5; 3270 -6.0; 3597 -5.2; 3957 -3.6; 4353 -4.8; 4788 -6.2; 5267 -4.6; 5793 -4.5; 6373 -6.0; 7010 -6.5; 7711 -6.6; 8482 -7.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.9; 20000 -10.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Game One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Game One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.35 | 6.5 dB  |
| Peaking | 134 Hz  | 0.62 | -2.7 dB |
| Peaking | 3998 Hz | 3.9  | 4.5 dB  |
| Peaking | 4676 Hz | 1.09 | -2.1 dB |
| Peaking | 5594 Hz | 3.82 | 3.6 dB  |
| Peaking | 502 Hz  | 1.6  | -1.0 dB |
| Peaking | 844 Hz  | 0.59 | 0.8 dB  |
| Peaking | 2174 Hz | 5.42 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20Game%20One/Sennheiser%20Game%20One.png)