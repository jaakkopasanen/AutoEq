# Sennheiser IE80 Max
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.9; 23 -10.1; 25 -10.3; 28 -10.5; 31 -10.6; 34 -10.8; 37 -10.8; 41 -11.0; 45 -11.1; 49 -11.2; 54 -11.2; 60 -11.3; 66 -11.5; 72 -11.7; 79 -11.8; 87 -12.0; 96 -12.1; 106 -12.2; 116 -12.3; 128 -12.2; 141 -12.1; 155 -12.0; 170 -11.8; 187 -11.5; 206 -11.1; 227 -10.7; 249 -10.3; 274 -9.8; 302 -9.3; 332 -8.8; 365 -8.3; 402 -7.8; 442 -7.4; 486 -7.0; 535 -6.6; 588 -6.1; 647 -5.7; 712 -5.2; 783 -4.7; 861 -4.3; 947 -3.8; 1042 -3.7; 1146 -4.0; 1261 -4.3; 1387 -4.3; 1526 -3.9; 1678 -3.0; 1846 -2.1; 2031 -1.3; 2234 -0.8; 2457 -0.5; 2703 -0.5; 2973 -0.9; 3270 -1.4; 3597 -2.0; 3957 -2.8; 4353 -4.3; 4788 -7.3; 5267 -10.2; 5793 -6.5; 6373 -1.7; 7010 -3.3; 7711 -5.5; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -7.2; 16529 -5.9; 18182 -6.2; 20000 -10.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE80 Max GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE80 Max ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.34 | -4.7 dB |
| Peaking | 136 Hz   | 0.84 | -3.9 dB |
| Peaking | 259 Hz   | 1.35 | -2.0 dB |
| Peaking | 2423 Hz  | 1.16 | 5.5 dB  |
| Peaking | 15193 Hz | 3.19 | -1.3 dB |
| Peaking | 935 Hz   | 1.55 | 3.0 dB  |
| Peaking | 1085 Hz  | 0.71 | -1.6 dB |
| Peaking | 3843 Hz  | 1.98 | 1.8 dB  |
| Peaking | 5283 Hz  | 4.04 | -6.7 dB |
| Peaking | 6500 Hz  | 5.86 | 5.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sennheiser%20IE80%20Max/Sennheiser%20IE80%20Max.png)