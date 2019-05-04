# Beyerdynamic DTX 350p
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -9.0; 25 -9.1; 28 -9.0; 31 -8.9; 34 -8.6; 37 -8.2; 41 -7.7; 45 -7.7; 49 -8.0; 54 -8.2; 60 -7.8; 66 -7.8; 72 -8.5; 79 -9.5; 87 -10.5; 96 -11.1; 106 -10.9; 116 -10.4; 128 -9.1; 141 -6.7; 155 -4.2; 170 -3.7; 187 -4.7; 206 -4.8; 227 -3.6; 249 -2.8; 274 -1.9; 302 -0.8; 332 -0.5; 365 -0.7; 402 -1.2; 442 -1.8; 486 -2.4; 535 -3.1; 588 -3.7; 647 -4.3; 712 -5.0; 783 -5.4; 861 -5.9; 947 -6.3; 1042 -6.5; 1146 -6.6; 1261 -6.5; 1387 -6.2; 1526 -5.7; 1678 -5.0; 1846 -4.4; 2031 -4.3; 2234 -4.6; 2457 -4.1; 2703 -3.7; 2973 -2.2; 3270 -0.7; 3597 -5.4; 3957 -6.8; 4353 -5.1; 4788 -1.3; 5267 -0.8; 5793 -2.9; 6373 -4.7; 7010 -6.7; 7711 -7.0; 8482 -8.0; 9330 -9.2; 10263 -9.2; 11289 -8.1; 12418 -8.1; 13660 -9.5; 15026 -6.8; 16529 -4.7; 18182 -5.5; 20000 -21.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DTX 350p GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DTX 350p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.48 | -4.3 dB  |
| Peaking | 100 Hz   | 2.07 | -6.3 dB  |
| Peaking | 336 Hz   | 1.69 | 4.7 dB   |
| Peaking | 11043 Hz | 1.33 | -4.6 dB  |
| Peaking | 19983 Hz | 2.51 | -17.1 dB |
| Peaking | 164 Hz   | 8.79 | 2.3 dB   |
| Peaking | 1098 Hz  | 1.94 | -2.3 dB  |
| Peaking | 3247 Hz  | 3.78 | 7.1 dB   |
| Peaking | 3767 Hz  | 2.56 | -5.5 dB  |
| Peaking | 5045 Hz  | 4.17 | 6.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | 3.7 dB  |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.9 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DTX%20350p/Beyerdynamic%20DTX%20350p.png)