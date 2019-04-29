# Zero Audio Carbo Tenore
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -7.9; 25 -7.9; 28 -7.9; 31 -7.9; 34 -7.8; 37 -7.8; 41 -7.8; 45 -7.7; 49 -7.6; 54 -7.5; 60 -7.4; 66 -7.4; 72 -7.4; 79 -7.4; 87 -7.4; 96 -7.4; 106 -7.4; 116 -7.3; 128 -7.2; 141 -7.0; 155 -6.9; 170 -6.7; 187 -6.4; 206 -6.0; 227 -5.7; 249 -5.4; 274 -5.4; 302 -5.2; 332 -4.8; 365 -4.5; 402 -4.2; 442 -3.9; 486 -3.7; 535 -3.5; 588 -3.3; 647 -3.0; 712 -2.8; 783 -2.6; 861 -2.5; 947 -2.8; 1042 -3.5; 1146 -4.6; 1261 -5.6; 1387 -5.8; 1526 -6.0; 1678 -6.3; 1846 -6.8; 2031 -7.7; 2234 -8.8; 2457 -9.2; 2703 -7.7; 2973 -5.5; 3270 -3.2; 3597 -1.7; 3957 -0.9; 4353 -0.5; 4788 -0.9; 5267 -2.5; 5793 -6.4; 6373 -9.6; 7010 -7.6; 7711 -6.2; 8482 -7.5; 9330 -7.2; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -8.2; 15026 -13.7; 16529 -12.0; 18182 -11.0; 20000 -18.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Zero Audio Carbo Tenore GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Zero Audio Carbo Tenore ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 762 Hz   | 1.5  | 2.9 dB   |
| Peaking | 2443 Hz  | 1.43 | -7.5 dB  |
| Peaking | 4575 Hz  | 0.8  | 9.3 dB   |
| Peaking | 6382 Hz  | 2.22 | -9.4 dB  |
| Peaking | 20501 Hz | 0.2  | -10.4 dB |
| Peaking | 30 Hz    | 0.41 | -2.7 dB  |
| Peaking | 123 Hz   | 1.27 | -1.4 dB  |
| Peaking | 12817 Hz | 2.48 | 5.3 dB   |
| Peaking | 14899 Hz | 1.86 | -5.4 dB  |
| Peaking | 17878 Hz | 2.14 | 3.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | -8.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Zero%20Audio%20Carbo%20Tenore/Zero%20Audio%20Carbo%20Tenore.png)