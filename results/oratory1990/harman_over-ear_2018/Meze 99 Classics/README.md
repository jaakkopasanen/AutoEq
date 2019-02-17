# Meze 99 Classics
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.0; 23 -14.3; 25 -14.5; 28 -14.8; 31 -15.0; 34 -15.2; 37 -15.3; 41 -15.4; 45 -15.6; 49 -15.6; 54 -15.8; 60 -15.9; 66 -16.0; 72 -16.0; 79 -15.9; 87 -15.7; 96 -15.6; 106 -15.4; 116 -15.7; 128 -16.3; 141 -15.9; 155 -16.9; 170 -17.4; 187 -17.2; 206 -17.1; 227 -16.2; 249 -15.4; 274 -13.8; 302 -11.4; 332 -8.9; 365 -7.1; 402 -6.9; 442 -7.7; 486 -8.4; 535 -9.0; 588 -9.2; 647 -9.2; 712 -9.0; 783 -8.5; 861 -7.8; 947 -6.7; 1042 -6.2; 1146 -7.1; 1261 -7.3; 1387 -7.9; 1526 -8.8; 1678 -9.6; 1846 -9.7; 2031 -8.8; 2234 -7.5; 2457 -7.0; 2703 -6.7; 2973 -5.7; 3270 -3.6; 3597 -0.5; 3957 -0.6; 4353 -8.6; 4788 -13.3; 5267 -13.0; 5793 -12.0; 6373 -12.4; 7010 -12.0; 7711 -11.8; 8482 -9.1; 9330 -6.1; 10263 -6.1; 11289 -9.2; 12418 -16.5; 13660 -15.7; 15026 -10.2; 16529 -9.3; 18182 -11.2; 20000 -11.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze 99 Classics GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 99 Classics ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.46 | -5.0 dB  |
| Peaking | 86 Hz    | 0.36 | -8.1 dB  |
| Peaking | 200 Hz   | 1.76 | -5.9 dB  |
| Peaking | 6060 Hz  | 2.31 | -7.1 dB  |
| Peaking | 13217 Hz | 2.62 | -11.6 dB |
| Peaking | 374 Hz   | 5.95 | 3.3 dB   |
| Peaking | 1781 Hz  | 2.01 | -3.5 dB  |
| Peaking | 3800 Hz  | 3.69 | 9.3 dB   |
| Peaking | 4697 Hz  | 4.75 | -6.7 dB  |
| Peaking | 10253 Hz | 5.71 | 3.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.8 dB |
| Peaking | 62 Hz    | 1.41 | -6.8 dB |
| Peaking | 125 Hz   | 1.41 | -8.3 dB |
| Peaking | 250 Hz   | 1.41 | -7.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.9 dB |
| Peaking | 16000 Hz | 1.41 | -7.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Meze%2099%20Classics/Meze%2099%20Classics.png)