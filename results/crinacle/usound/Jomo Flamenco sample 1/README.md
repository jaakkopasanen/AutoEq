# Jomo Flamenco sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.3; 28 -1.7; 31 -2.1; 34 -2.4; 37 -2.7; 41 -3.0; 45 -3.3; 49 -3.6; 54 -3.9; 60 -4.3; 66 -4.6; 72 -5.0; 79 -5.4; 87 -5.9; 96 -6.4; 106 -6.8; 116 -7.2; 128 -7.5; 141 -7.9; 155 -8.2; 170 -8.3; 187 -8.4; 206 -8.5; 227 -8.5; 249 -8.4; 274 -8.3; 302 -8.1; 332 -7.9; 365 -7.6; 402 -7.3; 442 -7.0; 486 -6.5; 535 -6.0; 588 -5.4; 647 -4.7; 712 -3.9; 783 -3.1; 861 -2.3; 947 -1.9; 1042 -1.9; 1146 -2.5; 1261 -3.3; 1387 -3.9; 1526 -4.1; 1678 -4.2; 1846 -4.6; 2031 -5.5; 2234 -6.5; 2457 -6.5; 2703 -5.7; 2973 -5.3; 3270 -5.9; 3597 -6.4; 3957 -3.9; 4353 -0.8; 4788 -1.7; 5267 -6.4; 5793 -6.1; 6373 -6.7; 7010 -7.9; 7711 -6.9; 8482 -5.6; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -9.0; 16529 -11.1; 18182 -8.6; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Flamenco sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Flamenco sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 10 Hz    | 0.22 | 5.5 dB  |
| Peaking | 208 Hz   | 0.51 | -3.3 dB |
| Peaking | 956 Hz   | 1.52 | 4.5 dB  |
| Peaking | 4472 Hz  | 7.71 | 5.9 dB  |
| Peaking | 16689 Hz | 1.82 | -6.0 dB |
| Peaking | 1796 Hz  | 2.79 | 1.3 dB  |
| Peaking | 2027 Hz  | 1.69 | -0.6 dB |
| Peaking | 2288 Hz  | 4.23 | -1.3 dB |
| Peaking | 6977 Hz  | 5.01 | -2.5 dB |
| Peaking | 13060 Hz | 2.76 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -4.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Jomo%20Flamenco%20sample%201/Jomo%20Flamenco%20sample%201.png)