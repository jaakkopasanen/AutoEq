# Sony XBA-H3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.3; 25 -5.5; 28 -5.7; 31 -5.8; 34 -6.0; 37 -6.1; 41 -6.3; 45 -6.4; 49 -6.6; 54 -6.8; 60 -7.1; 66 -7.3; 72 -7.6; 79 -7.9; 87 -8.2; 96 -8.6; 106 -8.8; 116 -9.1; 128 -9.2; 141 -9.3; 155 -9.3; 170 -9.2; 187 -9.0; 206 -8.8; 227 -8.4; 249 -8.1; 274 -7.7; 302 -7.3; 332 -7.0; 365 -6.8; 402 -6.5; 442 -6.2; 486 -6.0; 535 -5.8; 588 -5.6; 647 -5.4; 712 -5.2; 783 -5.2; 861 -5.4; 947 -5.6; 1042 -5.9; 1146 -6.4; 1261 -6.9; 1387 -7.1; 1526 -6.9; 1678 -6.5; 1846 -5.7; 2031 -4.4; 2234 -2.6; 2457 -0.7; 2703 -0.5; 2973 -2.3; 3270 -4.8; 3597 -5.9; 3957 -5.9; 4353 -7.7; 4788 -9.8; 5267 -8.7; 5793 -5.2; 6373 -2.7; 7010 -4.0; 7711 -6.2; 8482 -8.5; 9330 -11.0; 10263 -11.7; 11289 -9.9; 12418 -8.1; 13660 -7.1; 15026 -6.5; 16529 -7.4; 18182 -9.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-H3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-H3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 142 Hz   | 1.05 | -3.1 dB |
| Peaking | 2609 Hz  | 3.04 | 6.7 dB  |
| Peaking | 4974 Hz  | 3.85 | -4.8 dB |
| Peaking | 6492 Hz  | 3    | 5.4 dB  |
| Peaking | 9997 Hz  | 2.12 | -5.8 dB |
| Peaking | 21 Hz    | 1.35 | 1.4 dB  |
| Peaking | 246 Hz   | 1.87 | -0.7 dB |
| Peaking | 917 Hz   | 0.68 | 1.8 dB  |
| Peaking | 1363 Hz  | 1.69 | -2.3 dB |
| Peaking | 18440 Hz | 2.18 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sony%20XBA-H3/Sony%20XBA-H3.png)