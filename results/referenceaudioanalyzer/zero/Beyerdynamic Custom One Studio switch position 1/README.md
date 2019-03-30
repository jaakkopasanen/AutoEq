# Beyerdynamic Custom One Studio switch position 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -2.4; 25 -3.2; 28 -4.1; 31 -5.0; 34 -5.6; 37 -6.1; 41 -6.7; 45 -7.2; 49 -7.7; 54 -8.0; 60 -8.1; 66 -8.0; 72 -8.1; 79 -8.5; 87 -9.3; 96 -10.2; 106 -10.9; 116 -11.3; 128 -11.6; 141 -11.5; 155 -11.2; 170 -10.9; 187 -10.2; 206 -9.2; 227 -7.8; 249 -6.3; 274 -4.5; 302 -3.0; 332 -1.9; 365 -1.3; 402 -1.3; 442 -1.6; 486 -2.0; 535 -2.2; 588 -2.4; 647 -2.5; 712 -2.2; 783 -1.7; 861 -1.5; 947 -1.3; 1042 -1.2; 1146 -1.2; 1261 -1.2; 1387 -1.2; 1526 -1.2; 1678 -1.2; 1846 -1.6; 2031 -2.3; 2234 -2.5; 2457 -2.5; 2703 -2.5; 2973 -2.8; 3270 -3.1; 3597 -3.2; 3957 -2.4; 4353 -0.7; 4788 -0.5; 5267 -3.7; 5793 -6.7; 6373 -7.4; 7010 -5.5; 7711 -3.7; 8482 -3.9; 9330 -3.9; 10263 -3.9; 11289 -3.9; 12418 -4.5; 13660 -3.9; 15026 -3.9; 16529 -3.9; 18182 -3.9; 20000 -3.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Custom One Studio switch position 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Custom One Studio switch position 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 2.27 | 3.4 dB  |
| Peaking | 79 Hz   | 0.58 | -4.9 dB |
| Peaking | 158 Hz  | 1.22 | -7.4 dB |
| Peaking | 572 Hz  | 0.16 | 3.0 dB  |
| Peaking | 6256 Hz | 5.58 | -4.9 dB |
| Peaking | 228 Hz  | 3.76 | -1.4 dB |
| Peaking | 351 Hz  | 2.16 | 1.9 dB  |
| Peaking | 618 Hz  | 2.96 | -1.2 dB |
| Peaking | 4234 Hz | 1.22 | -1.8 dB |
| Peaking | 4567 Hz | 4.36 | 5.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -8.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20Custom%20One%20Studio%20switch%20position%201/Beyerdynamic%20Custom%20One%20Studio%20switch%20position%201.png)