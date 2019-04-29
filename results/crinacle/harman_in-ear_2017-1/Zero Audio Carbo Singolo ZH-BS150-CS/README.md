# Zero Audio Carbo Singolo ZH-BS150-CS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.3; 25 -5.4; 28 -5.6; 31 -5.8; 34 -6.0; 37 -6.1; 41 -6.3; 45 -6.5; 49 -6.6; 54 -6.9; 60 -7.2; 66 -7.5; 72 -7.9; 79 -8.3; 87 -8.6; 96 -9.2; 106 -9.6; 116 -9.9; 128 -10.3; 141 -10.6; 155 -10.9; 170 -11.1; 187 -11.2; 206 -11.2; 227 -11.2; 249 -11.1; 274 -11.0; 302 -10.8; 332 -10.4; 365 -10.1; 402 -10.3; 442 -10.0; 486 -9.5; 535 -9.0; 588 -8.4; 647 -7.9; 712 -7.2; 783 -6.5; 861 -6.0; 947 -5.7; 1042 -5.8; 1146 -6.2; 1261 -6.5; 1387 -6.5; 1526 -6.2; 1678 -5.9; 1846 -5.9; 2031 -6.3; 2234 -7.3; 2457 -8.5; 2703 -6.7; 2973 -2.8; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.9; 4788 -7.3; 5267 -5.1; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Zero Audio Carbo Singolo ZH-BS150-CS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Zero Audio Carbo Singolo ZH-BS150-CS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.54 | 1.5 dB  |
| Peaking | 207 Hz  | 0.56 | -5.0 dB |
| Peaking | 3689 Hz | 2.92 | 7.0 dB  |
| Peaking | 4927 Hz | 6.48 | -4.6 dB |
| Peaking | 5988 Hz | 3.92 | 6.4 dB  |
| Peaking | 471 Hz  | 2.4  | -1.0 dB |
| Peaking | 929 Hz  | 1.98 | 1.6 dB  |
| Peaking | 2529 Hz | 5.36 | -3.4 dB |
| Peaking | 3134 Hz | 7.52 | 2.4 dB  |
| Peaking | 8202 Hz | 4.72 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Zero%20Audio%20Carbo%20Singolo%20ZH-BS150-CS/Zero%20Audio%20Carbo%20Singolo%20ZH-BS150-CS.png)