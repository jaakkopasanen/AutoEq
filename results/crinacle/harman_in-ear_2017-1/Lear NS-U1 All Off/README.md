# Lear NS-U1 All Off
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.7; 187 -1.1; 206 -1.7; 227 -2.0; 249 -2.3; 274 -2.6; 302 -2.9; 332 -3.2; 365 -3.4; 402 -3.8; 442 -4.2; 486 -4.6; 535 -5.0; 588 -5.6; 647 -6.0; 712 -6.3; 783 -6.7; 861 -7.2; 947 -7.9; 1042 -8.8; 1146 -10.1; 1261 -11.7; 1387 -12.8; 1526 -13.5; 1678 -14.1; 1846 -14.8; 2031 -15.3; 2234 -15.2; 2457 -14.2; 2703 -12.7; 2973 -11.7; 3270 -11.5; 3597 -12.9; 3957 -14.8; 4353 -12.8; 4788 -8.2; 5267 -5.1; 5793 -2.5; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -7.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.4; 15026 -11.4; 16529 -11.1; 18182 -13.4; 20000 -23.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lear NS-U1 All Off GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lear NS-U1 All Off ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 55 Hz    | 0.13 | 6.2 dB   |
| Peaking | 1938 Hz  | 0.98 | -9.2 dB  |
| Peaking | 4057 Hz  | 4.18 | -6.9 dB  |
| Peaking | 6092 Hz  | 2.86 | 7.1 dB   |
| Peaking | 20033 Hz | 0.73 | -16.2 dB |
| Peaking | 155 Hz   | 4.89 | 0.5 dB   |
| Peaking | 6643 Hz  | 9.19 | 1.1 dB   |
| Peaking | 8714 Hz  | 1.23 | -2.0 dB  |
| Peaking | 13537 Hz | 0.69 | 3.4 dB   |
| Peaking | 15123 Hz | 2.33 | -5.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 5.1 dB  |
| Peaking | 250 Hz   | 1.41 | 3.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -9.0 dB |
| Peaking | 4000 Hz  | 1.41 | -3.6 dB |
| Peaking | 8000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 16000 Hz | 1.41 | -6.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Lear%20NS-U1%20All%20Off/Lear%20NS-U1%20All%20Off.png)