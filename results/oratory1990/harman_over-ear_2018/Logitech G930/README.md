# Logitech G930
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -6.0; 25 -6.8; 28 -7.7; 31 -8.4; 34 -8.8; 37 -9.2; 41 -9.4; 45 -9.5; 49 -9.5; 54 -9.2; 60 -8.4; 66 -7.3; 72 -6.7; 79 -7.6; 87 -8.9; 96 -9.2; 106 -10.2; 116 -11.5; 128 -12.1; 141 -12.1; 155 -11.7; 170 -10.8; 187 -10.3; 206 -9.0; 227 -7.6; 249 -6.0; 274 -5.1; 302 -5.5; 332 -5.8; 365 -6.3; 402 -6.6; 442 -6.7; 486 -6.7; 535 -6.8; 588 -6.9; 647 -7.0; 712 -7.0; 783 -6.6; 861 -6.5; 947 -6.7; 1042 -6.8; 1146 -7.5; 1261 -8.3; 1387 -8.0; 1526 -7.3; 1678 -7.1; 1846 -6.9; 2031 -5.9; 2234 -5.9; 2457 -6.1; 2703 -4.8; 2973 -2.0; 3270 -0.7; 3597 -0.5; 3957 -0.9; 4353 -9.2; 4788 -9.1; 5267 -8.5; 5793 -11.2; 6373 -10.6; 7010 -4.9; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.7; 13660 -9.8; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G930 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G930 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 43 Hz    | 1.98 | -3.1 dB |
| Peaking | 137 Hz   | 1.84 | -6.1 dB |
| Peaking | 3614 Hz  | 2.62 | 10.4 dB |
| Peaking | 4692 Hz  | 1.67 | -6.4 dB |
| Peaking | 13332 Hz | 6.78 | -4.1 dB |
| Peaking | 193 Hz   | 4.5  | -1.6 dB |
| Peaking | 276 Hz   | 3.17 | 2.3 dB  |
| Peaking | 1324 Hz  | 2.94 | -1.9 dB |
| Peaking | 6232 Hz  | 6.54 | -7.5 dB |
| Peaking | 6443 Hz  | 2.6  | 4.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Logitech%20G930/Logitech%20G930.png)