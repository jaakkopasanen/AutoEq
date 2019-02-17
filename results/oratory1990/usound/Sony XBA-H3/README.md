# Sony XBA-H3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.6; 25 -5.8; 28 -6.0; 31 -6.1; 34 -6.3; 37 -6.4; 41 -6.5; 45 -6.7; 49 -6.9; 54 -7.1; 60 -7.3; 66 -7.6; 72 -7.9; 79 -8.2; 87 -8.5; 96 -8.8; 106 -9.1; 116 -9.3; 128 -9.5; 141 -9.6; 155 -9.6; 170 -9.5; 187 -9.3; 206 -9.0; 227 -8.7; 249 -8.3; 274 -7.9; 302 -7.5; 332 -7.3; 365 -7.0; 402 -6.7; 442 -6.5; 486 -6.2; 535 -6.0; 588 -5.9; 647 -5.7; 712 -5.5; 783 -5.5; 861 -5.7; 947 -5.9; 1042 -6.2; 1146 -6.7; 1261 -7.2; 1387 -7.3; 1526 -7.2; 1678 -6.8; 1846 -6.0; 2031 -4.7; 2234 -2.9; 2457 -1.0; 2703 -0.5; 2973 -2.5; 3270 -5.1; 3597 -6.3; 3957 -6.2; 4353 -7.9; 4788 -10.1; 5267 -9.1; 5793 -5.4; 6373 -3.1; 7010 -3.6; 7711 -6.1; 8482 -8.7; 9330 -11.2; 10263 -12.0; 11289 -10.2; 12418 -8.4; 13660 -7.4; 15026 -6.3; 16529 -7.7; 18182 -9.9; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-H3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-H3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 142 Hz   | 0.75 | -3.7 dB |
| Peaking | 2612 Hz  | 3.87 | 6.3 dB  |
| Peaking | 4810 Hz  | 6.87 | -4.8 dB |
| Peaking | 10210 Hz | 3.17 | -6.6 dB |
| Peaking | 18321 Hz | 1.57 | -4.1 dB |
| Peaking | 21 Hz    | 1.58 | 0.8 dB  |
| Peaking | 723 Hz   | 1.69 | 0.9 dB  |
| Peaking | 1397 Hz  | 2.92 | -1.7 dB |
| Peaking | 6648 Hz  | 3.44 | 6.6 dB  |
| Peaking | 6819 Hz  | 1.23 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -2.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sony%20XBA-H3/Sony%20XBA-H3.png)