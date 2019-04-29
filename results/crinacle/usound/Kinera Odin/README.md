# Kinera Odin
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -4.0; 25 -4.4; 28 -4.8; 31 -5.2; 34 -5.4; 37 -5.6; 41 -5.9; 45 -6.1; 49 -6.4; 54 -6.6; 60 -6.9; 66 -7.2; 72 -7.6; 79 -7.9; 87 -8.3; 96 -8.6; 106 -9.0; 116 -9.3; 128 -9.5; 141 -9.6; 155 -9.7; 170 -9.7; 187 -9.7; 206 -9.6; 227 -9.4; 249 -9.1; 274 -8.8; 302 -8.5; 332 -8.1; 365 -7.6; 402 -7.3; 442 -6.8; 486 -6.4; 535 -6.0; 588 -5.6; 647 -5.2; 712 -4.9; 783 -4.7; 861 -4.8; 947 -5.3; 1042 -6.5; 1146 -8.3; 1261 -10.1; 1387 -11.3; 1526 -11.4; 1678 -10.5; 1846 -9.2; 2031 -8.0; 2234 -6.8; 2457 -5.3; 2703 -3.3; 2973 -0.9; 3270 -0.5; 3597 -0.7; 3957 -2.5; 4353 -5.1; 4788 -2.3; 5267 -0.5; 5793 -2.1; 6373 -5.2; 7010 -7.3; 7711 -9.2; 8482 -6.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kinera Odin GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kinera Odin ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.99 | 3.1 dB  |
| Peaking | 155 Hz   | 0.88 | -3.6 dB |
| Peaking | 1536 Hz  | 2.85 | -5.8 dB |
| Peaking | 3264 Hz  | 2.73 | 6.8 dB  |
| Peaking | 5320 Hz  | 5.55 | 6.1 dB  |
| Peaking | 806 Hz   | 1.73 | 2.5 dB  |
| Peaking | 1250 Hz  | 5.56 | -2.0 dB |
| Peaking | 2026 Hz  | 5.88 | -1.0 dB |
| Peaking | 7612 Hz  | 7.09 | -3.5 dB |
| Peaking | 18852 Hz | 3.19 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kinera%20Odin/Kinera%20Odin.png)