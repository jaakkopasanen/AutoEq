# Sony XBA-N1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.9; 25 -8.1; 28 -8.4; 31 -8.6; 34 -8.7; 37 -8.8; 41 -8.9; 45 -9.0; 49 -9.1; 54 -9.2; 60 -9.3; 66 -9.3; 72 -9.4; 79 -9.4; 87 -9.4; 96 -9.3; 106 -9.2; 116 -9.6; 128 -10.1; 141 -10.1; 155 -9.8; 170 -9.5; 187 -9.0; 206 -8.6; 227 -8.1; 249 -7.6; 274 -7.0; 302 -6.5; 332 -6.0; 365 -5.4; 402 -4.9; 442 -4.4; 486 -3.9; 535 -3.5; 588 -3.0; 647 -2.6; 712 -2.2; 783 -2.0; 861 -1.9; 947 -2.1; 1042 -2.5; 1146 -2.9; 1261 -3.5; 1387 -4.0; 1526 -4.2; 1678 -4.4; 1846 -3.2; 2031 -1.9; 2234 -2.2; 2457 -2.2; 2703 -2.0; 2973 -1.0; 3270 -0.5; 3597 -1.2; 3957 -1.4; 4353 -1.2; 4788 -1.6; 5267 -0.8; 5793 -0.5; 6373 -2.4; 7010 -4.4; 7711 -5.0; 8482 -4.5; 9330 -4.3; 10263 -4.3; 11289 -4.3; 12418 -4.3; 13660 -4.3; 15026 -6.3; 16529 -7.4; 18182 -4.6; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-N1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-N1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.81 | -2.4 dB |
| Peaking | 57 Hz    | 0.66 | -3.3 dB |
| Peaking | 159 Hz   | 0.8  | -4.5 dB |
| Peaking | 757 Hz   | 1.42 | 2.7 dB  |
| Peaking | 3785 Hz  | 1.03 | 3.6 dB  |
| Peaking | 1690 Hz  | 3.66 | -1.9 dB |
| Peaking | 1970 Hz  | 3.39 | 1.7 dB  |
| Peaking | 5859 Hz  | 3.58 | 4.7 dB  |
| Peaking | 6452 Hz  | 1.65 | -2.9 dB |
| Peaking | 16154 Hz | 2.64 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sony%20XBA-N1/Sony%20XBA-N1.png)