# Earsonics ES2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.4; 45 -2.0; 49 -2.5; 54 -3.2; 60 -3.9; 66 -4.7; 72 -5.5; 79 -6.2; 87 -6.8; 96 -7.6; 106 -8.4; 116 -9.1; 128 -9.6; 141 -10.2; 155 -10.6; 170 -10.9; 187 -11.0; 206 -11.2; 227 -11.3; 249 -11.4; 274 -11.5; 302 -11.3; 332 -11.2; 365 -11.0; 402 -10.8; 442 -10.5; 486 -10.2; 535 -9.9; 588 -9.4; 647 -9.1; 712 -8.6; 783 -8.1; 861 -7.7; 947 -7.5; 1042 -7.8; 1146 -8.5; 1261 -9.3; 1387 -9.9; 1526 -10.1; 1678 -10.1; 1846 -9.9; 2031 -8.9; 2234 -6.6; 2457 -2.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.6; 3957 -1.4; 4353 -0.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics ES2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics ES2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.49 | 6.8 dB  |
| Peaking | 217 Hz  | 0.43 | -5.5 dB |
| Peaking | 1873 Hz | 1.5  | -7.3 dB |
| Peaking | 2821 Hz | 1.31 | 8.8 dB  |
| Peaking | 5429 Hz | 2.23 | 5.2 dB  |
| Peaking | 911 Hz  | 2.32 | 2.4 dB  |
| Peaking | 928 Hz  | 1.29 | -1.5 dB |
| Peaking | 4403 Hz | 4.99 | 1.3 dB  |
| Peaking | 6482 Hz | 4.65 | 4.0 dB  |
| Peaking | 6931 Hz | 1.57 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 8.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Earsonics%20ES2/Earsonics%20ES2.png)