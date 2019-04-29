# Shozy & Neo BG sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -4.0; 25 -4.4; 28 -4.9; 31 -5.3; 34 -5.6; 37 -5.8; 41 -6.1; 45 -6.4; 49 -6.7; 54 -7.0; 60 -7.2; 66 -7.5; 72 -7.9; 79 -8.2; 87 -8.6; 96 -8.9; 106 -9.4; 116 -9.6; 128 -9.9; 141 -10.1; 155 -10.1; 170 -10.2; 187 -10.3; 206 -10.2; 227 -10.1; 249 -9.8; 274 -9.6; 302 -9.4; 332 -9.0; 365 -8.7; 402 -8.3; 442 -7.9; 486 -7.4; 535 -7.0; 588 -6.5; 647 -6.0; 712 -5.4; 783 -4.9; 861 -4.5; 947 -4.4; 1042 -4.7; 1146 -5.6; 1261 -6.5; 1387 -7.3; 1526 -7.8; 1678 -8.2; 1846 -8.8; 2031 -8.2; 2234 -5.7; 2457 -2.9; 2703 -1.5; 2973 -2.2; 3270 -4.0; 3597 -4.2; 3957 -1.2; 4353 -0.5; 4788 -0.5; 5267 -2.4; 5793 -5.0; 6373 -7.0; 7010 -5.5; 7711 -7.2; 8482 -7.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.6; 18182 -7.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shozy & Neo BG sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shozy & Neo BG sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.15 | 3.2 dB  |
| Peaking | 168 Hz   | 0.73 | -4.1 dB |
| Peaking | 2743 Hz  | 3.98 | 6.6 dB  |
| Peaking | 3976 Hz  | 0.7  | -3.7 dB |
| Peaking | 4470 Hz  | 2.04 | 10.0 dB |
| Peaking | 348 Hz   | 1.93 | -0.9 dB |
| Peaking | 907 Hz   | 1.69 | 2.9 dB  |
| Peaking | 1868 Hz  | 2.1  | -2.6 dB |
| Peaking | 2375 Hz  | 6    | 2.2 dB  |
| Peaking | 17792 Hz | 4.22 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Shozy%20&%20Neo%20BG%20sample%201/Shozy%20&%20Neo%20BG%20sample%201.png)