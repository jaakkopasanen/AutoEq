# Elysian Artemis
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.4; 25 -6.8; 28 -7.2; 31 -7.6; 34 -7.9; 37 -8.1; 41 -8.4; 45 -8.7; 49 -9.0; 54 -9.3; 60 -9.6; 66 -9.9; 72 -10.3; 79 -10.6; 87 -11.0; 96 -11.4; 106 -11.9; 116 -12.2; 128 -12.4; 141 -12.7; 155 -12.8; 170 -12.9; 187 -13.0; 206 -12.9; 227 -12.8; 249 -12.6; 274 -12.4; 302 -12.1; 332 -11.6; 365 -11.2; 402 -10.7; 442 -10.3; 486 -9.8; 535 -9.2; 588 -8.6; 647 -7.9; 712 -7.2; 783 -6.5; 861 -5.9; 947 -5.5; 1042 -5.5; 1146 -5.8; 1261 -6.1; 1387 -5.8; 1526 -5.2; 1678 -4.4; 1846 -3.8; 2031 -3.7; 2234 -3.5; 2457 -2.6; 2703 -1.1; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.1; 5267 -2.6; 5793 -3.6; 6373 -5.2; 7010 -6.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -11.8; 16529 -10.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Elysian Artemis GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Elysian Artemis ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 136 Hz   | 0.53 | -5.5 dB |
| Peaking | 308 Hz   | 1    | -2.9 dB |
| Peaking | 3094 Hz  | 1.05 | 5.6 dB  |
| Peaking | 4563 Hz  | 2.97 | 3.0 dB  |
| Peaking | 15660 Hz | 3.11 | -6.9 dB |
| Peaking | 17 Hz    | 2.19 | 1.4 dB  |
| Peaking | 514 Hz   | 3.2  | -0.6 dB |
| Peaking | 908 Hz   | 3.35 | 1.3 dB  |
| Peaking | 7951 Hz  | 2.62 | -0.7 dB |
| Peaking | 13328 Hz | 6.5  | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -4.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Elysian%20Artemis/Elysian%20Artemis.png)