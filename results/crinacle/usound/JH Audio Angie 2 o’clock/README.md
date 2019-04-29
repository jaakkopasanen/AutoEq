# JH Audio Angie 2 o’clock
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.9; 25 -4.1; 28 -4.3; 31 -4.6; 34 -4.9; 37 -5.1; 41 -5.4; 45 -5.7; 49 -5.9; 54 -6.2; 60 -6.5; 66 -6.9; 72 -7.3; 79 -7.7; 87 -8.0; 96 -8.5; 106 -8.8; 116 -9.1; 128 -9.3; 141 -9.6; 155 -9.8; 170 -9.9; 187 -9.9; 206 -9.9; 227 -9.8; 249 -9.7; 274 -9.6; 302 -9.5; 332 -9.4; 365 -9.3; 402 -9.2; 442 -9.1; 486 -9.0; 535 -8.8; 588 -8.6; 647 -8.4; 712 -8.2; 783 -7.9; 861 -7.9; 947 -8.3; 1042 -9.4; 1146 -10.8; 1261 -11.7; 1387 -12.0; 1526 -11.3; 1678 -9.6; 1846 -7.3; 2031 -5.1; 2234 -3.5; 2457 -2.8; 2703 -3.2; 2973 -3.4; 3270 -1.9; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.4; 8482 -10.2; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -11.3; 20000 -20.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio Angie 2 o’clock GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio Angie 2 o’clock ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.19 | 3.1 dB  |
| Peaking | 183 Hz  | 0.35 | -3.7 dB |
| Peaking | 1373 Hz | 2.45 | -6.3 dB |
| Peaking | 3559 Hz | 1.2  | 5.8 dB  |
| Peaking | 5656 Hz | 3.51 | 4.5 dB  |
| Peaking | 2347 Hz | 3.03 | 3.9 dB  |
| Peaking | 2974 Hz | 1.22 | -3.3 dB |
| Peaking | 3946 Hz | 2.02 | 2.4 dB  |
| Peaking | 6506 Hz | 7.67 | 2.4 dB  |
| Peaking | 8288 Hz | 4.97 | -5.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -3.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/JH%20Audio%20Angie%202%20o%E2%80%99clock/JH%20Audio%20Angie%202%20o%E2%80%99clock.png)