# Meze 99 Classics
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.6; 23 -10.8; 25 -11.1; 28 -11.3; 31 -11.6; 34 -11.7; 37 -11.9; 41 -12.0; 45 -12.1; 49 -12.2; 54 -12.3; 60 -12.5; 66 -12.5; 72 -12.5; 79 -12.5; 87 -12.3; 96 -12.1; 106 -11.9; 116 -12.3; 128 -12.7; 141 -12.5; 155 -13.5; 170 -13.9; 187 -13.8; 206 -13.6; 227 -12.8; 249 -12.0; 274 -10.4; 302 -7.9; 332 -5.4; 365 -3.7; 402 -3.5; 442 -4.2; 486 -5.0; 535 -5.6; 588 -5.8; 647 -5.8; 712 -5.6; 783 -5.1; 861 -4.4; 947 -3.3; 1042 -2.8; 1146 -3.6; 1261 -3.9; 1387 -4.5; 1526 -5.3; 1678 -6.2; 1846 -6.3; 2031 -5.3; 2234 -4.1; 2457 -3.5; 2703 -3.2; 2973 -2.3; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -5.0; 4788 -9.7; 5267 -9.6; 5793 -8.6; 6373 -8.9; 7010 -8.5; 7711 -8.4; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.9; 12418 -13.1; 13660 -12.2; 15026 -7.0; 16529 -6.5; 18182 -7.8; 20000 -8.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze 99 Classics GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 99 Classics ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 51 Hz    | 0.54 | -6.3 dB |
| Peaking | 158 Hz   | 2.12 | -5.0 dB |
| Peaking | 220 Hz   | 3.91 | -4.6 dB |
| Peaking | 3313 Hz  | 2.68 | 6.6 dB  |
| Peaking | 12951 Hz | 3.56 | -8.0 dB |
| Peaking | 20 Hz    | 1.93 | -1.2 dB |
| Peaking | 393 Hz   | 3.77 | 4.2 dB  |
| Peaking | 1046 Hz  | 1.97 | 3.5 dB  |
| Peaking | 5413 Hz  | 2.97 | -4.2 dB |
| Peaking | 10866 Hz | 5.73 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.9 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Meze%2099%20Classics/Meze%2099%20Classics.png)