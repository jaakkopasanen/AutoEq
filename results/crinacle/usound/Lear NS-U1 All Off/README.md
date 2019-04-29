# Lear NS-U1 All Off
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.6; 227 -0.9; 249 -1.2; 274 -1.5; 302 -1.8; 332 -2.2; 365 -2.6; 402 -2.9; 442 -3.4; 486 -3.8; 535 -4.3; 588 -4.9; 647 -5.3; 712 -5.7; 783 -6.0; 861 -6.5; 947 -7.1; 1042 -8.0; 1146 -9.4; 1261 -11.2; 1387 -12.6; 1526 -13.6; 1678 -14.3; 1846 -15.0; 2031 -15.9; 2234 -16.4; 2457 -15.9; 2703 -14.8; 2973 -14.0; 3270 -13.7; 3597 -14.9; 3957 -16.3; 4353 -13.9; 4788 -9.1; 5267 -5.9; 5793 -3.6; 6373 -2.3; 7010 -4.0; 7711 -6.2; 8482 -7.9; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -11.6
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

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 64 Hz   | 0.11 | 6.2 dB   |
| Peaking | 2088 Hz | 0.88 | -10.1 dB |
| Peaking | 4039 Hz | 3.37 | -7.5 dB  |
| Peaking | 6191 Hz | 2.06 | 6.9 dB   |
| Peaking | 8703 Hz | 2.78 | -2.0 dB  |
| Peaking | 202 Hz  | 3.97 | 0.5 dB   |
| Peaking | 993 Hz  | 3.81 | 0.8 dB   |
| Peaking | 1359 Hz | 5.72 | -1.0 dB  |
| Peaking | 8261 Hz | 2.69 | -1.1 dB  |
| Peaking | 9638 Hz | 3.21 | 1.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 4.8 dB  |
| Peaking | 250 Hz   | 1.41 | 4.6 dB  |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -9.8 dB |
| Peaking | 4000 Hz  | 1.41 | -5.4 dB |
| Peaking | 8000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Lear%20NS-U1%20All%20Off/Lear%20NS-U1%20All%20Off.png)