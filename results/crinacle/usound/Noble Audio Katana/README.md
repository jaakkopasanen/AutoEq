# Noble Audio Katana
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.3; 25 -4.5; 28 -4.8; 31 -5.1; 34 -5.4; 37 -5.6; 41 -5.8; 45 -6.0; 49 -6.2; 54 -6.5; 60 -6.8; 66 -7.1; 72 -7.5; 79 -7.8; 87 -8.2; 96 -8.7; 106 -9.0; 116 -9.3; 128 -9.5; 141 -9.8; 155 -10.0; 170 -10.0; 187 -10.1; 206 -10.0; 227 -9.8; 249 -9.7; 274 -9.4; 302 -9.2; 332 -8.9; 365 -8.5; 402 -8.2; 442 -7.9; 486 -7.5; 535 -7.1; 588 -6.7; 647 -6.3; 712 -5.9; 783 -5.4; 861 -5.0; 947 -4.9; 1042 -5.1; 1146 -5.7; 1261 -6.4; 1387 -6.7; 1526 -6.6; 1678 -6.1; 1846 -5.6; 2031 -5.4; 2234 -5.4; 2457 -5.5; 2703 -5.0; 2973 -3.9; 3270 -3.3; 3597 -1.6; 3957 -0.5; 4353 -0.5; 4788 -0.6; 5267 -3.8; 5793 -7.5; 6373 -7.0; 7010 -6.9; 7711 -9.5; 8482 -8.1; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.6; 18182 -8.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noble Audio Katana GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble Audio Katana ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.33 | 3.0 dB  |
| Peaking | 179 Hz   | 0.56 | -3.7 dB |
| Peaking | 862 Hz   | 2.15 | 2.0 dB  |
| Peaking | 4435 Hz  | 1.6  | 9.2 dB  |
| Peaking | 6066 Hz  | 1.25 | -4.8 dB |
| Peaking | 1421 Hz  | 5.86 | -0.9 dB |
| Peaking | 7915 Hz  | 6.2  | -4.4 dB |
| Peaking | 8152 Hz  | 2.26 | 2.1 dB  |
| Peaking | 18248 Hz | 2.47 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Noble%20Audio%20Katana/Noble%20Audio%20Katana.png)